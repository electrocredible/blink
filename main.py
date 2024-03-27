from machine import Pin, Timer

led_pin = Pin("LED", Pin.OUT)
tim = Timer()
def tick(timer):
    global led_pin
    led_pin.toggle()

tim.init(freq=3, mode=Timer.PERIODIC, callback=tick)
