from machine import Pin, SPI
from ili9341 import Display, color565
from time import sleep

def test():
    spi = SPI(1, baudrate=10000000, sck=Pin(14), mosi=Pin(15))
    display = Display(spi, dc=Pin(6), cs=Pin(17), rst=Pin(7))
    
    display.clear(color565(255, 0, 0))
    
    current_r = 0
    
    while True:
        sleep(0.02)
        display.clear(color565(current_r, 0, 0))
        
        if(current_r is 255): continue
        
        current_r += 1
        print(current_r)
        
                  
test()