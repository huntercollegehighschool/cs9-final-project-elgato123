import time
import os
import sys
os.system("printf '\033c'")
print("flying to Himalayas")
time.sleep(5)
os.system("printf '\033c'")

def type(text):
  words = text
  for char in words:
    time.sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()
type("You begin your flight and learn from Max \nthat you are not headed to Nepal. \nRather, he tells you, you are headed to Bhutan to traverse \nthe largest unclimbed peak in the Himalayan mountain range,  \nGangkhar. You arrive in Thimpu and leave on a smaller flight to \nthe town of Naspe at the base of the mountain. \nUnbelievably, you hear of a Sherpa that \nfound strange tracks descending from the mountain. \nYou dismiss it but Max seems all too excited \nto prove or disprove the rumor. \nYou excitedly contact a sherpa and begin \nto approach the Mountain. \nAs you finally reach the snow, you see two trails, \none that looks long and treacherous and the other that \nappears short and pleasant. \nYou and Max decide to take the easy \ntrail but as you approach, you hear Llamas begin to cry out. \nWhich way shall you go? \nType L to go along the longer path. \nType S to go along the shorter path  ")
program=input("")
if program == 'l':
  import part5

if program == 'L':
  import part5

elif program == 's':
  import part6

elif program == 'S':
  import part6

