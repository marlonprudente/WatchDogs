import random
import re
import os
import time
import MySQLdb
from multiprocessing import Process

WORDS = ["DELAY", "SOCORRO"]
#PRIORITY = 19
con = MySQLdb.connect('127.0.0.1', 'root', 'watchdogs')
con.select_db('wdp')

def delay():
	#sleep(10)
	sql = con.cursor()
	sql.execute('UPDATE sensors SET status=3')
	con.commit()
#	print "Ligado depois de 10 min"

def handle(text, mic, profile):
   try:	

	print(text)	        

	#cmd = 'sudo python /home/pi/Sensores.py'
	sql = con.cursor()
	
	
	if bool(re.search(r'\b(DELAY?|\sDELAY?\s.*delay)\b', text, re.IGNORECASE)):
		mic.say('Alarmes Ligados em 10 min')
		#time.sleep(10)
		#os.system(cmd+" switch on")
		#Process(target=delay).start()
                delay()
		
	elif bool(re.search(r'\b(SOCORRO?|\sHELP?\s.*socorro)\b', text, re.IGNORECASE)):
		mic.say('light now is blinking 5 times')
		#os.system(cmd+" blink 5 1")
		sql.execute('UPDATE sensors SET status=2')
		con.commit()
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
