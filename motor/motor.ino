
const int motorPin1 = 2;  // Motor control pin 1
const int motorPin2 = 3;  // Motor control pin 2
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
                turnMotorClockwisePlastic();
            } else if (received == "paper") {
                turnMotorClockwisePaper();
            } else {
                stopMotor();
            }
        }
    }
}

void turnMotorClockwisePlastic() {
    digitalWrite(motorPin1, LOW);
    digitalWrite(motorPin2, HIGH);
    analogWrite(motorEnable, 250);  // Adjust speed if needed
    Serial.println("Motor turning clockwise 6 seconds (plastic detected)");
    delay(6000); // Run for 6 seconds
    stopMotor();
}

void turnMotorClockwisePaper() {
    digitalWrite(motorPin1, LOW);
    digitalWrite(motorPin2, HIGH);
    analogWrite(motorEnable, 250);  // Adjust speed if needed
    Serial.println("Motor turning clockwise 4 (paper detected)");
    delay(4000); // Run for 4 seconds
    stopMotor();
}




void stopMotor() {
    analogWrite(motorEnable, 0);
    Serial.println("Motor stopped");
}
