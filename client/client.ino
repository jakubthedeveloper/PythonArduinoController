String incoming;
int meterPin = 11;
int meterMax = 16;

void setup() {
  Serial.begin(9600);
  pinMode(meterPin, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    incoming = Serial.readString();
    Serial.print("received: ");
    Serial.println(incoming);
    
    int analogValue = incoming.toFloat() * meterMax;
    analogWrite(meterPin, analogValue);
  }

}
