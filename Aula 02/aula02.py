from pyfirmata import Arduino, util
import time

placa = Arduino('COM3')

it = util.Iterator(placa)
it.start()


v1 = placa.get_pin('d:11:i')
v2 = placa.get_pin('d:12:i')
v3 = placa.get_pin('d:13:i')


bt1Ant = True
bt2Ant = True
bt3Ant = True

contador = 0

while True:

    time.sleep(0.15)

    estadoBt1 = v1.read()
    estadoBt2 = v2.read()
    estadoBt3 = v3.read()

    if estadoBt1 == False and bt1Ant:
        contador += 1
        print(contador)

    if estadoBt2 == False and bt2Ant:
        contador -= 1
        print(contador)

    if estadoBt3 == False and bt3Ant:
        contador = 0
        print(contador)

    if contador >= 5:
        placa.digital[5].write(1)
    else:
        placa.digital[5].write(0)

    if contador >= 10 :                         
        placa.digital[6].write(1)                 
    else:                                       
        placa.digital[6].write(0)

    if contador >= 15 :                         
        placa.digital[7].write(1)                 
    else:                                       
        placa.digital[7].write(0)

    bt1Ant = estadoBt1
    bt2Ant = estadoBt2
    bt3Ant = estadoBt3

    

    
    
