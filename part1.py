import time
import os
import sys
os.system("printf '\033c'")
print("flying to Mexico")
time.sleep(5)
os.system("printf '\033c'")

def type(text):
  words = text
  for char in words:
    time.sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()
type("You and Max arrive to Mexico and decide to head to town from the \nairport. After asking the locals from Oaxaca, you are told to not\nventure up into the mountains to the temple or risk disturbing an \nold Mayan king. After consulting with Max, you decide that \nvisiting  the crypt would be a great adventure and you set off. \nUpon reaching the temple, you are faced with 1 of 2 choices. You   may enter the tomb through the entrance at the summit or walk up \nthe pyramid to the center of worship. Which do you want to go to?\nType T to enter the tomb and  W to climb up the pyramid.  ")
program=input("")
if program == 't':
  import part3

if program == 'T':
  import part3

elif program == 'w':
  import part4

elif program == 'W':
  import part4