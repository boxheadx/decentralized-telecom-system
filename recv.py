import serial

ser = serial.Serial('COM3', 115200, timeout=1)

with open('received_cat.webp', 'wb') as cat:
    while True:
        byte = ser.readline()
        if byte != b'':
            byte = int(byte.strip()).to_bytes(1, byteorder='big')
            print(byte)
            cat.write(byte)

# Open a new file to save the received image
# with open('received_cat.webp', 'wb') as img_file:

#     while True:
#         # Read one byte at a time
#         byte = ser.read(1)
#         print(byte)
        
#         # If no byte is received, the end of the transmission might be reached
#         if not byte:
#             break
        
#         # Write the byte to the file (reconstruct the image)
#         img_file.write(byte)

# Close the serial port connection
ser.close()

# print("Image received and saved as 'received_cat.webp'")
