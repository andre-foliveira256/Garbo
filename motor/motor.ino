
const int motorPin1 = 5;  // Motor control pin 1
const int motorPin2 = 6;  // Motor control pin 2
const int motorEnable = 9; // Motor speed control (PWM)

String lastCommand = "";  // Store last received command

void setup() {
    Serial.begin(115200);  // Match baud rate with Python script
    pinMode(motorPin1, OUTPUT);
    pinMode(motorPin2, OUTPUT);
    pinMode(motorEnable, OUTPUT);
    
    // Ensure motor is stopped initially
    digitalWrite(motorPin1, LOW);
    digitalWrite(motorPin2, LOW);
    analogWrite(motorEnable, 0);
}

void loop() {
    if (Serial.available() > 0) {
        String received = Serial.readStringUntil('\n');
        received.trim(); // Remove any unwanted newline characters
        Serial.print("Received: ");
        Serial.println(received);
        
        if (received != lastCommand) {  // Only execute if command is different
            lastCommand = received;
            
            if (received == "plastic") {
                turnMotorClockwise2();
            } else if (received == "paper") {
                turnMotorClockwise();
            } else {
                stopMotor();
            }
        }
    }
}

void turnMotorClockwise() {
    digitalWrite(motorPin1, LOW);
    digitalWrite(motorPin2, HIGH);
    analogWrite(motorEnable, 250);  // Adjust speed if needed
    Serial.println("Motor turning clockwise (plastic detected)");
    delay(4000); // Run for 2 seconds
    stopMotor();
}

void turnMotorClockwise2() {
    digitalWrite(motorPin1, LOW);
    digitalWrite(motorPin2, HIGH);
    analogWrite(motorEnable, 250);  // Adjust speed if needed
    Serial.println("Motor turning clockwise (plastic detected)");
    delay(2000); // Run for 2 seconds
    stopMotor();
}




void stopMotor() {
    analogWrite(motorEnable, 0);
    Serial.println("Motor stopped");
}
