import serial
import time
arduino = serial.Serial('COM3', 9600)



def Measure():
    distance = arduino.readline()
    var = float(distance)
    time.sleep(1)
    print(var)
    return var


while True:
    output = Measure()
    if output > 5:
        break
