#! /usr/bin/env python

import RPi.GPIO as GPIO ## Import GPIO Library
import time ## Import 'time' library.  Allows us to use 'sleep'
import sys, getopt

buzz_pin=7
pir_pin=14
door_pin=17
button_pin=18

#GPIO.cleanup()
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_pin, GPIO.IN)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(door_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buzz_pin,GPIO.OUT)

## Define function named Blink()
def Blink(numTimes, speed):
    for i in range(0,numTimes): ## Run loop numTimes
        print "Iteration " + str(i+1) ##Print current loop
        GPIO.output(buzz_pin, True) ## Turn on GPIO pin 7
        time.sleep(speed) ## Wait
        GPIO.output(buzz_pin, False) ## Switch off GPIO pin 7
        time.sleep(speed) ## Wait
    print "Done" ## When loop is complete, print "Done"
    GPIO.cleanup()


## ON OFF Function
def Switch(power):
   if power:
	try:
		while True:
		if GPIO.input(pir_pin):
			GPIO.output(buzz_pin, GPIO.HIGH)

		if GPIO.input(door_pin):
			GPIO.output(buzz_pin, GPIO.HIGH)
		if not GPIO.input(button_pin):
			GPIO.output(buzz_pin, GPIO.LOW)
	except KeyboardInterrupt:
		print "voce usou Ctrl+C!"
	finally:
		GPIO.cleanup()
		print 'Alarme Ligado'

	else:
		GPIO.output(buzz_pin, False)
		GPIO.cleanup()
		print 'Alarme Desligado'

def main(argv):
   GPIO.cleanup()
   GPIO.setmode(GPIO.BOARD) ## Use BOARD pin numbering
   GPIO.setup(buzz_pin, GPIO.OUT) ## Setup GPIO pin 7 to OUT
   type = ''
   try:
      opts, args = getopt.getopt(argv,"i:p:h",['input=', 'params=', 'help'])
   except getopt.GetoptError:
      print 'Wrong command'
      sys.exit(2)
   print opts,args

   for opt, arg in opts:
      if opt == '-h':
         print 'Sensores.py -i switch <on/off> or Sensores.py -i blink <no>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         input = arg

         if input == 'switch' :
		#print opts,args[0]
		if args[0] == 'on':
			Switch(True)
		elif args[0] == 'off':
			Switch(False)
		else:
			print 'Please choose on or off'
	 elif input == 'blink':
		## Prompt user for input
		if len(args)==2 :
			iterations = args[0]
			speed = args[1]
		else:
			iterations = raw_input("Enter the total number of times to blink: ")
			speed = raw_input("Enter the length of each blink in seconds: ")
		## Start Blink() function. Convert user input from strings to numeric data types and pass to Blink() as parameters
		Blink(int(iterations),float(speed))
		## Start Blink() function. Convert user input from strings to numeric data types and pass to Blink() as parameters

      

#if __name__ == "__main__":
try:
	main(sys.argv[1:])
except:
	GPIO.cleanup()
	print 'error in main block'


