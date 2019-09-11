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

const int analogPin = 15 ;
int val = 0;
int prev_val = 400 ;

void setup() {
  Serial.begin(115200);
  Serial.println("Testing ledc 12 channel 1");
}
void loop()
{
  int touch_data_power = touchRead(T8); //on/off

  //Serial.println(touch_data_power); 
  
  int touch_data_p1 = touchRead(T9); // mute

  int touch_data_p2 = touchRead(T5); //backward/arrow left key
  int touch_data_p3 = touchRead(T6); // space /pause/play
  int touch_data_p4 = touchRead(T7); //arrow right key / forward


  

  //volume
  val = analogRead(analogPin);
  int dif = val- prev_val;
  
  if(dif >= 250 ){

    Serial.println(val);
    delay(100);
    }
   if(dif <= -250){
    Serial.println((-1)*val);
    delay(100);
    }



  if(touch_data_power<15){
      delay(50);
    if(touch_data_power<15 && touch_data_power>0){
      Serial.println("a");
      delay(1000);
      }
    }
  
    if(touch_data_p1<15){
    delay(50);
    if(touch_data_p1<15 && touch_data_p1>0){
      Serial.println("b");
      delay(1000);
      }
    }
    
   if(touch_data_p2<15 && touch_data_p2>0){
    delay(50);
    if(touch_data_p2<15){
      Serial.println("c");
      delay(1000);
      }
    }
    
   if(touch_data_p3<15 && touch_data_p3>0){
    delay(50);
    if(touch_data_p3<15 ){
      Serial.println("d");
      delay(1000);
      }
    }

    if(touch_data_p4<15 && touch_data_p4>0){
    delay(50);
    if(touch_data_p4<15){
      Serial.println("e");
      delay(1000);
      }
    }
    
  delay(100);
}
