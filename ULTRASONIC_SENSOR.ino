#define TRIGPIN 11
#define ECHOPIN 12

float duration, distance;


void setup() {
  Serial.begin(115200);

  pinMode(ECHOPIN, INPUT);
  pinMode(TRIGPIN, OUTPUT);

}

void loop() {
  digitalWrite(TRIGPIN, LOW);
  delayMicroseconds(2);

  digitalWrite(TRIGPIN, HIGH);
  delayMicroseconds(20);

  digitalWrite(TRIGPIN, LOW);
  
  duration = pulseIn(ECHOPIN, HIGH);
  distance = (duration/2) * 0.343;

  Serial.print("distance:");
  Serial.print(distance);
  Serial.print("mm");

  delay(100);
}
