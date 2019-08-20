/*
   Touch Sensor Pin Layout
   T0 = GPIO4
   T1 = GPIO0
   T2 = GPIO2
   T3 = GPIO15
   T4 = GPIO13
   T5 = GPIO12
   T6 = GPIO14
   T7 = GPIO27
   T8 = GPIO33
   T9 = GPIO32 */

uint8_t led = 18;

void setup() {
  ledcAttachPin(led, 1);    //Configure variable led, pin 18 to channel 1
  ledcSetup(1, 12000, 8);   // 12 kHz PWM and 8 bit resolution
  ledcWrite(1, 100);        // Write a test value of 100 to channel 1
  Serial.begin(115200);
  Serial.println("Testing ledc 12 channel 1");
}
void loop()
{
  int touch_data = touchRead(T0);
  int led_data = 0;
  Serial.print("Touch sensor value:");
  Serial.println(touch_data);
  led_data = 1.6 * touch_data;
  ledcWrite(1, (led_data));
  delay(100);
}
