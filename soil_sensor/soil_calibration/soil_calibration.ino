int sensorVal;
#define SENSOR_IN 0

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
analogReference(EXTERNAL);
}

void loop() {
  // put your main code here, to run repeatedly:
sensorVal = analogRead(SENSOR_IN);
Serial.println(sensorVal);
delay(100);
}
