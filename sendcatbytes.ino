#include <SPI.h>
#include <RF24.h>

RF24 radio(2, 3);  // CE, CSN

const byte address[6] = "00001";

void setup()
{
  radio.begin();
  Serial.begin(115200);
  radio.setDataRate(1); // 2mbps
  radio.openWritingPipe(address);
  radio.stopListening();
}

void loop() {
  // if getting cat bytes from pyserial
  if(Serial.available()){
    byte catbyte = Serial.read();
    radio.write(&catbyte, sizeof(byte)); //send cat byte thru rf
  }

}
