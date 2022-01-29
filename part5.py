import time
import os
import sys
os.system("printf '\033c'")
print("You take the longer path to be careful")
time.sleep(5)
os.system("printf '\033c'")

def type(text):
  words = text
  for char in words:
    time.sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()
type("you feel wary of the warning and decide to go up the longer \npath. As you and Max reach closer to the end of this path you \nbegin to notice how difficult this trek is and begin to lose speed, \nbefore you know it Max is panting very loudly and he insists on \nleaving stating 'This is not for me I can't do this' he begins to \nclimb down the mountain and asks if you want to leave with him. \ntype L if you want to leave S if you want to stay")
program=input("")
if program == 'S':
  import keepgoing

if program == 's':
  import keepgoing

elif program == 'L':
  import goback

elif program == 'l':
  import goback