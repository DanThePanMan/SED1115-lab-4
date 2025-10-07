from machine import Pin
from machine import UART

sw5 = Pin(22, Pin.IN, Pin.PULL_DOWN)
uart = UART(1, baudrate=9600,tx=Pin(8), rx=Pin(9))
print("initializing UART...")
uart.init(bits=8, parity=None, stop=1)
print("UART initialized successfully")

while True:
    # data= uart.read()
    # if data:
    #     print(data)
    #     print(data.decode())
    try:
        if sw5.value(): #if button is pressed
            print("button pressed") #print send
            data_to_write = "hello"
            print(f"Preparing to write data: '{data_to_write}'")
            bytes_written = uart.write(data_to_write)
            print(f"Data '{data_to_write}' written to UART.")
            print(f"Number of bytes written: {bytes_written}")
            print("write successful")
        while sw5.value(): #make it so one press sends once
            pass
    except Exception as Error:
        print(Error)
        print("bwoken")
        
        
    
    

