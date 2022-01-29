
import time
import os
import sys

def type(text):
  words = text
  for char in words:
    time.sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()
type("You and your roommate Max decide to go on a trip far away,\nto celebrate your recent graduation from college and Max has\npitched 2 ideas to you. The first of which is a hike up a mountain in the \nHimalayas, the second being a temple in Oaxaca Mexico.\nWhich one do you want to go to? type H for Himalayas and M \nfor mexico ")
program=input("")
if program == 'm':
  import part1
   
elif program == 'M':
  import part1

elif program == 'h':
  import part2

elif program == 'H':
  import part2