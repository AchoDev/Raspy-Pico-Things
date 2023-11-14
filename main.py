from machine import Pin 
import time

class Button:
    def __init__(self, _pin_number):
        self.pin = Pin(_pin_number, Pin.IN, Pin.PULL_UP)
        self.pressed = False
    
    def check(self):
        if(not self.pin.value() and not self.pressed):
            self.pressed = True
        
            return True
        
        elif(self.pin.value()):
            self.pressed = False
            


board_led = Pin(25, Pin.OUT)

board_led.toggle()

left_button = Button(14)
right_button = Button(13)

print("runninng")

while True:
    if(left_button.check()):
        print("LEFT")
        print("-------------")
    if(right_button.check()):  
        board_led.toggle()
        print("RIGHT")
        print("-------------")
        
        
        
        
        
        
        