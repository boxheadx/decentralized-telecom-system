import serial
import time

ser = serial.Serial('COM7', 115200, timeout=1) 

time.sleep(2)

with open('cat.webp', 'rb') as file:
    chunk_size = 64 
    while chunk := file.read(chunk_size):
        for byte in chunk:
            ser.write(byte.to_bytes(1, byteorder='little'))
            print(f"sending: {byte.to_bytes(1, byteorder='little')}")
            time.sleep(0.001);


ser.close()
