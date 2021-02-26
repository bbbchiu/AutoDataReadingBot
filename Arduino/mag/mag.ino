#include <Wire.h>

int addressMag = 0x30;

int magxl = 0x04;
int magxh = 0x03;
int magyl = 0x06;
int magyh = 0x05;
int magzl = 0x08;
int magzh = 0x07;
float magX,magY,magZ;

void writeReg(int address,int reg,int data){
  Wire.beginTransmission(address);
  Wire.write(reg);
  Wire.write(data);
  Wire.endTransmission();
}

int readReg(int address,int reg){
  Wire.beginTransmission(address);
  Wire.write(reg);
  Wire.endTransmission();

  Wire.requestFrom(address,1);

  if(Wire.available()<=1){
    return Wire.read();
  }
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Wire.begin(addressMag);

}

void loop() {
  // put your main code here, to run repeatedly:
  magX = readReg(addressMag,magxh)*256+ readReg(addressMag,magxl);
  if (magX > 32767){
    magX -= 65536;
  }
  magX *= 0.92;

  magY = readReg(addressMag,magyh)*256+ readReg(addressMag,magyl);
  if (magY > 32767){
    magY -= 65536;
  }
  magY *= 0.92;
  
  magZ = readReg(addressMag,magzh)*256+ readReg(addressMag,magzl);
  if (magZ > 32767){
    magZ -= 65536;
  }
  magZ *= 0.92;
  
  Serial.print("X = ");
  Serial.println(magX);
  Serial.print("Y = ");
  Serial.println(magY);
  Serial.print("Z = ");
  Serial.println(magZ);
  Serial.print("\n");
  delay(1000);
  
}
