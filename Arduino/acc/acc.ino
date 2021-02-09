#include <Wire.h>

int addressAcc = 0x53 ;
int accpower = 0x2d;
int acc_bw_rate = 0x2c;
int accxl = 0x32;
int accxh = 0x33;
int accyl = 0x34;
int accyh = 0x35;
int acczl = 0x36;
int acczh = 0x37;
float accX,accY,accZ;

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
  Wire.begin(addressAcc);

  writeReg(addressAcc,accpower,0x08);
  writeReg(addressAcc,acc_bw_rate,0x0b);
}

void loop() {
  // put your main code here, to run repeatedly:
  accX = readReg(addressAcc,accxh)*256+ readReg(addressAcc,accxl);
  if (accX > 32767){
    accX -= 65536;
  }
  accX *= 0.004*9.8;
  accY = readReg(addressAcc,accyh)*256+ readReg(addressAcc,accyl);
  if (accY > 32767){
    accY -= 65536;
  }
  accY *= 0.004*9.8;
  accZ = readReg(addressAcc,acczh)*256+ readReg(addressAcc,acczl);
  if (accZ > 32767){
    accZ -= 65536;
  }
  accZ *= 0.004*9.8;
  
  Serial.print("X = ");
  Serial.println(accX);
  Serial.print("Y = ");
  Serial.println(accY);
  Serial.print("Z = ");
  Serial.println(accZ);
  Serial.print("\n");
  delay(1000);
  
}
