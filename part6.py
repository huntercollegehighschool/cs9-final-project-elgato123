import time
import os
import sys
os.system("printf '\033c'")
print("You blindly choose to go up the shorter path, taking into consideration only the fact that the shorter path seems more feasible")
time.sleep(5)
os.system("printf '\033c'")

def type(text):
  words = text
  for char in words:
    time.sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()
type("You ignore the cries of the llama and pull the along up the \nshorter path. This trek takes around just 3 minutes and on the \nfinal turn you feel a weird sense of fear, you take the final turn \nand as you turn left you see a sight you can't unsee. You see a \ngiant yeti gobbling on the llama and just as he's done, he eyes you \nand Max. You turn to max and say what do we do? He says we either \nrun or stand completely still, your choice. Type R for run Type S \nfor stand still")
program=input("")
if program == 'S':
  import staystill

if program == 's':
  import staystill

elif program == 'R':
  import run

elif program == 'r':
  import run