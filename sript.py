import serial
import time
import requests  # Needed for sending Gotify notifications
import socket

# Configure the serial ports
OPENMV_PORT = '/dev/ttyACM0'  # Port for OpenMV Cam
ARDUINO_PORT = '/dev/ttyACM1'  # Port for Arduino
BAUD_RATE = 115200  # Match the baud rate with OpenMV and Arduino



# Gotify Configuration (Replace with actual details)
GOTIFY_TOKEN = "AwDGy-7W-EjtwFD"
GOTIFY_URL = f"http://192.168.144.219/message?token={GOTIFY_TOKEN}"

# Initialize counters for labels
label_counts = {"plastic": 0, "paper": 0}
TARGET_COUNT = 4  # Number of detections required to trigger sending data to Arduino

# Separate actual garbage counters
actual_garbage = {"plastic": 0, "paper": 0}
GARBAGE_CAPACITY = {"plastic": 3, "paper": 3}  # Max capacity for each type

def send_gotify_notification(material):
    """Send a notification to Gotify when a specific bin is full."""
    try:
        message = f"The {material} garbage bin is full! Please empty it."
        response = requests.post(
            GOTIFY_URL,
            json={"message": message, "priority": 5, "title": f"{material.capitalize()} Bin Full"}
        )
        if response.status_code == 200:
            print(f"Gotify notification sent successfully for {material} bin!")
        else:
            print(f"Failed to send Gotify notification for {material}: {response.status_code}")
    except Exception as e:
        print(f"Error sending Gotify notification for {material}: {e}")

def forward_data():
    global actual_garbage

    try:
        # Open serial connections
        openmv_serial = serial.Serial(OPENMV_PORT, BAUD_RATE, timeout=1)
        arduino_serial = serial.Serial(ARDUINO_PORT, BAUD_RATE, timeout=1)
        print(f"Connected to OpenMV Cam on {OPENMV_PORT} and Arduino on {ARDUINO_PORT} at {BAUD_RATE} baud.")

        while True:
            # Check if any garbage bin is full
            for material, count in actual_garbage.items():
                if count >= GARBAGE_CAPACITY[material]:
                    print(f"{material.capitalize()} garbage bin is full! Sending notification...")
                    send_gotify_notification(material)
                    actual_garbage[material] = 0  # Reset garbage count after notifying

            if openmv_serial.in_waiting > 0:  # Check if data is available from OpenMV
                # Read a line of data from OpenMV
                line = openmv_serial.readline().decode('utf-8').strip()
                if line:  # If the line is not empty
                    print(f"Received from OpenMV: {line}")

                    # Process the data (e.g., split into components)
                    try:
                        label, x, y, score = line.split(',')
                        print(f"Label: {label}, X: {x}, Y: {y}, Score: {score}")

                        # Update the counter for the detected label
                        if label in label_counts:
                            label_counts[label] += 1
                            print(f"Updated {label} count: {label_counts[label]}")

                            # Check if the count has reached the target
                            if label_counts[label] >= TARGET_COUNT:
                                print(f"{label} count reached {TARGET_COUNT}. Sending to Arduino...")
                                arduino_serial.write(f"{label}\n".encode('utf-8'))
                                print(f"Sent to Arduino: {label}")

                                # Make the camera light up to Green
                                openmv_serial.write("ready\n".encode('utf-8'))
                                print(f"Sent to OpenMV: ready")

                                # Reset the counter for the label
                                label_counts["plastic"] = 0
                                label_counts["paper"] = 0
                                actual_garbage[label] += 1  # Increase garbage count for specific material

                    except ValueError:
                        print("Invalid data format received.")

            # Small delay to avoid hogging the CPU
            time.sleep(0.01)

    except serial.SerialException as e:
        print(f"Failed to open serial port: {e}")
    except KeyboardInterrupt:
        print("Program terminated by user.")
    finally:
        # Close serial connections
        if 'openmv_serial' in locals() and openmv_serial.is_open:
            openmv_serial.close()
            print("OpenMV serial port closed.")
        if 'arduino_serial' in locals() and arduino_serial.is_open:
            arduino_serial.close()
            print("Arduino serial port closed.")

if __name__ == "__main__":
    forward_data()