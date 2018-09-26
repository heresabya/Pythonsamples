from gpiozero import LED
from time import sleep

led = LED(17)
led1 = LED(18)


while True:
	led.on()
	sleep(1)
	led.off()
	sleep(1)
	led1.on()
	sleep(1)
	led1.off()
	sleep(1)

        
