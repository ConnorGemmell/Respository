#Traffic Light


from gpiozero import LED
from time import sleep

led1 = LED(26)

led1.on()
sleep(5)
led1.off()

led2 = LED(5)

led2.on()
sleep(5)
led2.off()

led3 = LED(4)

led3.on()
sleep(5)
led3.off