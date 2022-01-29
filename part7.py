import time
import os
import sys
os.system("printf '\033c'")
print("you decide to stop Max")
time.sleep(5)
os.system("printf '\033c'")

def type(text):
  words = text
  for char in words:
    time.sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()
type("you are a good friend. You don't know it, \nbut you have just saved Max from certain doom. \nYou yell STOP and Max freezes, looks around wildly, \nthen looks at you strangly. \nHe says 'I thought we were in danger. What is it?' \nYou simply tell him you would feel \nmore comfortable if he left the coffin in peace. \nHe laughs and tells you to lighten up. \nThe both of you take off out of the tomb with enough gold to last you a lifetime \nand with the pride of being the only people to have walked \nin that temple for at least another century. \nLittle did you know that many people have visited it before \nbut that none of them had been able to leave ")