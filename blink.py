from machine import Pin
from machine import UART

sw5 = Pin(22, Pin.IN, Pin.PULL_DOWN)
uart = UART(1, baudrate=9600,tx=Pin(8), rx=Pin(9))
uart.init(bits=8, parity=None, stop=1) 




while True:
    
    if sw5.value(): #if button is pressed
        msg = input("enter your message: ")
        uart.write(msg) #write
        while sw5.value(): #make it so one press sends once
            pass  
    if uart.any():
        data = uart.read()
        print(data)
    

