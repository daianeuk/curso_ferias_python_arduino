import serial

arduino = serial.Serial('COM3', 9600)

while True:

    print("The distance of object is: ")
    x = arduino.readline()
    print(str(x.decode().strip()))
