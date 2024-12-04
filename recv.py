import serial

ser = serial.Serial('COM3', 115200, timeout=1)

with open('received_cat.webp', 'wb') as cat:
    while True:
        byte = ser.readline()
        if byte != b'':
            byte = int(byte.strip()).to_bytes(1, byteorder='big')
            print(byte)
            cat.write(byte)

