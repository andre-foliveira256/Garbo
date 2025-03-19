import serial
import time

# Configure the serial ports
OPENMV_PORT = 'COM10'  # Port for OpenMV Cam
ARDUINO_PORT = 'COM12'  # Port for Arduino
BAUD_RATE = 115200  # Match the baud rate with OpenMV and Arduino

# Initialize counters for labels
label_counts = {"plastic": 0, "paper": 0}
TARGET_COUNT = 10  # Number of detections required to trigger sending data to Arduino

def forward_data():
    try:
        # Open serial connections
        openmv_serial = serial.Serial(OPENMV_PORT, BAUD_RATE, timeout=1)
        arduino_serial = serial.Serial(ARDUINO_PORT, BAUD_RATE, timeout=1)
        print(f"Connected to OpenMV Cam on {OPENMV_PORT} and Arduino on {ARDUINO_PORT} at {BAUD_RATE} baud.")

        while True:
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
                                #Make the camera light up to Green
                                openmv_serial.write("ready\n".encode('utf-8'))
                                print(f"Sent to OpenMV: ready")

                                # Reset the counter for the label
                                label_counts[label] = 0

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