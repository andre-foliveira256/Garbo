//Constantes Sensor
const int trigPin = 12;
const int echoPin = 13;

float duration, distance;
float max_distance = 20;
//Constantes Motor
const int controlPin1 = 2;
const int controlPin2 = 3;
const int enablePin = 9;
int motorSpeed = 50;

void setup() {
  pinMode(controlPin1, OUTPUT);
  pinMode(controlPin2, OUTPUT);
  pinMode(enablePin, OUTPUT);
  digitalWrite(enablePin, LOW);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  digitalWrite(controlPin1, HIGH);
  digitalWrite(controlPin2, LOW);
}

void loop() {
  //distance = detectObject();
  //if (distance <= max_distance){
  startMotor();
  //}
  delay(5000);
}

float detectObject(){
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = (duration*.0343)/2;
  Serial.print("Distance: ");
  Serial.println(distance);
  return distance;
}

void startMotor(){
  analogWrite(enablePin, motorSpeed);
  delay(2000);
  analogWrite(enablePin, 0);
}
