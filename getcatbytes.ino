#include <SPI.h>
#include <RF24.h>

RF24 radio(2, 3);  // CE, CSN

const byte address[6] = "00001";

void setup()
{
  radio.begin();
  Serial.begin(115200);
  radio.setDataRate(1); // 2mbps
  radio.openReadingPipe(0, address);
  radio.startListening();
}

void loop() {
  // if getting cat bytes from nrf
  if(radio.available()){
    byte catbyte;
    radio.read(&catbyte, sizeof(byte));
    Serial.println(catbyte);
  }

}
