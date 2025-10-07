from machine import Pin
from machine import UART

sw5 = Pin(22, Pin.IN, Pin.PULL_DOWN)
uart = UART(1, baudrate=9600, rx=Pin(9))
# uart.init(bits=8, parity=None, stop=1) 

while True:
    
    data= uart.read()
    if data:
        print(data)
        print(data.decode())

    
    if sw5.value():
        uart.write("hello")
        print("sent")
        while sw5.value():
            pass  # Wait until button is released
        
    

