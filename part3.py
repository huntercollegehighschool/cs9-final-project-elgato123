import time
import os
import sys
os.system("printf '\033c'")
print("you and max lower yourselves into the tomb")
time.sleep(5)
os.system("printf '\033c'")

def type(text):
  words = text
  for char in words:
    time.sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()
type("You and Max clamber down into the tomb, \nwaving away vines and overgrown vegetation as you lower yourself into the crypt. \nYou walk along a dimly lit corridor, the only lights comes from the hole \nthrough which you have just entered. \nA cold wind brushes past you and Max shivers. \nOddly, as you approach the end of the tunnel, you see a light. \nYou finally enter the tomb. \nThere, you see a lit torch above a closed coffin. \nYou turn scared to max. \nHowever, as you turn, you see Max with his eyes wide open. \nOn the other side of the room, there are open chests filled to the brim with Mayan gold. \nYou and Max parade around the room. \nHowever, you can't celebrate just yet. \nYou still wonder how the torch was still lit. \nSomething mysterious seems to happening, \nand the coffin is at the center of it all. \nMax, still overjoyed, walks up to rap his knuckles on \nthe coffin jokingly. \nWhat will you do? \nType S to stop him, G to ignore him and \nrun to the gold ")
program=input("")
if program == 'S':
  import part7

if program == 's':
  import part7

elif program == 'G':
  import part8

elif program == 'g':
  import part8
