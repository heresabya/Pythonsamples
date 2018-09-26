import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
ledpin=11
GPIO.setup(ledpin, GPIO.OUT, initial=GPIO.LOW) 

while True: 
 GPIO.output(ledpin, GPIO.HIGH) # Turn on
 sleep(5) # Sleep for 5 second
 GPIO.cleanup()
 sleep(1) # Sleep for 1 second
