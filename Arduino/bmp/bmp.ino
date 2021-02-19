#include <Arduino.h>
#include <Wire.h>
#include <BMP180I2C.h>

int address_bmp = 0x77;
float temp,pressure;
BMP180I2C bmp180(address_bmp);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Wire.begin();

  bmp180.begin();
  bmp180.resetToDefaults();
  bmp180.setSamplingMode(BMP180MI::MODE_UHR);
}

void loop() {

  bmp180.measureTemperature();
  while(!bmp180.hasValue()){
    delay(500);
  }
  temp = bmp180.getTemperature(); 

  bmp180.measurePressure();
  while(!bmp180.hasValue()){
    delay(500);
  }
  pressure = bmp180.getPressure();

  Serial.println("Reading~~(degreeC, Pa)"); 
  Serial.print("Temperature: ");
  Serial.println(temp);
  Serial.print("Pressure: ");
  Serial.println(pressure);
  Serial.print("\n");
  
  delay(1000);
}
