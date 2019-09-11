const int pot = 15;
int potval = 0;
void setup() {
   Serial.begin(115200);
   delay(1000);
}

void loop() {
  potval = analogRead(pot);
  Serial.println(potval);
  delay(500);

}
