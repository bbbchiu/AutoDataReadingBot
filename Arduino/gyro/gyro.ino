#include <Wire.h>

int addressGyro = 0x69 ;
int ctrl_reg1 = 0x20;
int ctrl_reg4 = 0x23;
int gyroxl = 0x28;
int gyroxh = 0x29;
int gyroyl = 0x2a;
int gyroyh = 0x2b;
int gyrozl = 0x2c;
int gyrozh = 0x2d;
float gyroX,gyroY,gyroZ;

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
  Wire.begin(addressGyro);

  writeReg(addressGyro,ctrl_reg1,0x0F);
  writeReg(addressGyro,ctrl_reg4,0x30);
}

void loop() {
  // put your main code here, to run repeatedly:
  gyroX = readReg(addressGyro,gyroxh)*256+ readReg(addressGyro,gyroxl);
  if (gyroX > 32767){
    gyroX -= 65536;
  }

  gyroY = readReg(addressGyro,gyroyh)*256+ readReg(addressGyro,gyroyl);
  if (gyroY > 32767){
    gyroY -= 65536;
  }

  gyroZ = readReg(addressGyro,gyrozh)*256+ readReg(addressGyro,gyrozl);
  if (gyroZ > 32767){
    gyroZ -= 65536;
  }
  
  Serial.print("X = ");
  Serial.println(gyroX);
  Serial.print("Y = ");
  Serial.println(gyroY);
  Serial.print("Z = ");
  Serial.println(gyroZ);
  Serial.print("\n");
  delay(1000);
  
}
