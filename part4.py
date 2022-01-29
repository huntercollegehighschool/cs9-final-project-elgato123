import time
import os
import sys
os.system("printf '\033c'")
print("You decide to go to the center of worship")
time.sleep(5)
os.system("printf '\033c'")

def type(text):
  words = text
  for char in words:
    time.sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()
type(" you and Max reach the stairs and begin to ascend. As you reach the top you feel yourself feeling uneasy. You come into view of the entrance at the top and before entering, you and Max look in. You see an old relic, a jaguar, in the middle of the room that almost feels like it is staring at you. Max \nproposes that you can steal the relic together with him but you \nfeel uncertain. You wonder if entering the tomb would be a \nbetter option. Type C to charge in and snatch the relic. Type T \nto return to the summit and enter the tomb. Type S to walk in \nslowly and with caution to evaluate whether stealing the relic \nwould be the best idea. ")
program=input("")
if program == 't':
  import part3

if program == 'T':
  import part3

elif program == 'c':
  import part9

elif program == 'C':
  import part9

elif program == 's':
  import part91

elif program == 'S':
  import part91