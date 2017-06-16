import random
import re
import os
import time
import MySQLdb

WORDS = ["LIGAR", "DESLIGAR"]
#PRIORITY = 20
con = MySQLdb.connect('127.0.0.1','root','watchdogs')


def handle(text, mic, profile):
   try:		        
        con.select_db('wdp')
	cmd = 'sudo python /home/pi/teste.py'
        sql = con.cursor()
	
  	if bool(re.search(r'\b(LIGAR|\sLIGAR\s.*alarme)\b', text, re.IGNORECASE)):
		mic.say('Alarmes Ligados')
		#os.system(cmd)#+" switch on")
                sql.execute('UPDATE sensors SET status=1 WHERE status=-1')

   	elif bool(re.search(r'\b(DESLIGAR?|\sOFF?\s.*desligar)\b', text, re.IGNORECASE)):
    		mic.say('Alarmes Desligados')
       		#os.system(cmd+"exit(0)")#+" switch off")
                sql.execute('UPDATE sensors SET status=-1')
		
    	mic.say('DONE... ')
        con.commit()
   
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
