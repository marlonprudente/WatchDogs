from multiprocessing import Process
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
        sql = con.cursor()
	
  	if bool(re.search(r'\b(LIGAR|\sLIGAR\s.*alarme)\b', text, re.IGNORECASE)):
		mic.say('Alarmes Ligados')
                #Process(target=Ativar).start()
		#os.system(cmd)#+" switch on")
                sql.execute('UPDATE sensors SET status=1')
		#con.commit()	
   	elif bool(re.search(r'\b(DESLIGAR?|\sOFF?\s.*desligar)\b', text, re.IGNORECASE)):
    		mic.say('Alarmes Desligados')
       		#os.system(cmd+"exit(0)")#+" switch off")
                sql.execute('UPDATE sensors SET status=0')
		#con.commit()
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
