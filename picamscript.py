import time 
import os 
import sys

def creepy():
 for i in range(0,1000):
  time.sleep(10) 
  os.system("raspistill -o file.jpg")
  

creepy()




