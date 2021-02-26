#include <Wire.h>

void setup(){
  Wire.begin();
  Serial.begin(9600);
}

void loop(){
  byte error, address;
  Serial.println("Scanning...");

  address = 30;
  Wire.beginTransmission(address);
  error = Wire.endTransmission();
  Serial.print("0x");
  if (address < 16){
        Serial.print("0");
  }
  Serial.println(address, HEX);
  Serial.println(error);

/*  for (address = 1; address < 127; address++ ){
    Wire.beginTransmission(address);
    error = Wire.endTransmission();
    if (error == 0){
      Serial.print("I2C device found at address 0x");   
      if (address < 16){
        Serial.print("0");
      }
      Serial.print(address, HEX);
      Serial.println(" !");
      Serial.println(error);
      Serial.println(address);
    }
  }
*/
  delay(5000);
}
