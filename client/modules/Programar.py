import random
import re
import os
import time

WORDS = ["DELAY", "SOCORRO"]
#PRIORITY = 19

def handle(text, mic, profile):
   try:	

	print(text)	        

	cmd = 'sudo python /home/pi/Sensores.py'
	
	if bool(re.search(r'\b(DELAY?|\sDELAY?\s.*delay)\b', text, re.IGNORECASE)):
		mic.say('Alarmes Ligados em 10 min')
		time.sleep(10)
		os.system(cmd+" switch on")
		
	elif bool(re.search(r'\b(SOCORRO?|\sHELP?\s.*socorro)\b', text, re.IGNORECASE)):
		mic.say('light now is blinking 5 times')
		os.system(cmd+" blink 5 1")
    	mic.say('DONE... ')
   
   except:
	print "Lighting Error"
   	mic.say('Sorry... something wrong on lighting configuration')
  

def isValid(text):
    """
        Returns True if the input is related to the meaning of life.
        Arguments:
        text -- user-input, typically transcribed speech
    """

    if bool(re.search(r'\b(delay|socorro?|\sdelei?\s.*socorro|\sdelay\s.*delay)\b', text, re.IGNORECASE)):
    	return True
    return False
