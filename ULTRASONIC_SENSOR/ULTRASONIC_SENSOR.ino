//Código sensor ultrassonico
const int trigPin = 11;
const int echoPin = 10;

float duration, distance;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = (duration*.0343)/2;
  Serial.print("Distance: ");
  Serial.println(distance);
  delay(5000);
}



//Código para infravermelho
/*
void loop (){ 
  digitalWrite( enablePin, HIGH);     // Enable the internal 38kHz signal.
  delay( 210);                   // Wait 210µs (8 pulses of 38kHz).
  if( digitalRead( outputPin))        // If detector Output is HIGH,
    {
        objectDetect = false;           // then no object was detected;
    }
  else                                // but if the Output is LOW,
    {
        delay( 395);               // wait for another 15 pulses.
        if( digitalRead( outputPin))    // If the Output is now HIGH,
        {                               // then first Read was noise
            objectDetect = false;       // and no object was detected;
        }
        else                            // but if the Output is still LOW,
        {
            objectDetect = true;        // then an object was truly detected.
        }
    }
  Serial.println(objectDetect);
  digitalWrite( enablePin, LOW);
  delay(300);
} */ 