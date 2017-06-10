import random
import re
import os
import time

WORDS = ["LIGAR", "DESLIGAR", "DELAY", "SOCORRO"]
PRIORITY = 20

def handle(text, mic, profile):
   try:		        

	cmd = 'sudo python /home/py/Sensores.py'
	
  	if bool(re.search(r'\b(LIGAR|\sLIGAR\s.*alarme)\b', text, re.IGNORECASE)):
		mic.say('Alarmes Ligados')
		os.system(cmd+"switch on")

    elif bool(re.search(r'\b(DESLIGAR?|\sOFF?\s.*desligar)\b', text, re.IGNORECASE)):
    	 mic.say('Alarmes Desligados')
       	os.system(cmd+"switch off")

	elif bool(re.search(r'\b(DELAY?|\sDELAY?\s.*delay)\b', text, re.IGNORECASE)):
		time.sleep(600)
		mic.say('Alarmes Ligados')
		os.system(cmd+"switch on")
		
    else:
		mic.say('light now is blinking 5 times')
		os.system(cmd+"blink 5 1")
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

    if bool(re.search(r'\b(ligar|desligar?|\soff?\s.*light|\son\s.*light|blinking|light blinking|blinking\s.*light)\b', text, re.IGNORECASE)):
    	return True
    
return False