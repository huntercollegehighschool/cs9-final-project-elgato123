import time
import os
import sys
os.system("printf '\033c'")
print("Your fear takes over and you go back")
time.sleep(5)
os.system("printf '\033c'")

def type(text):
  words = text
  for char in words:
    time.sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()
type("You begin to walk down the mountains but you hear the bellows of \na large animal in the distance. You begin to sprint down the \nmountain with Max but you hear loud footsteps nearby. The yeti \nemerges from behind a rock, and Max panics. You tell him to calm down \nand sacrifice the sherpa. The sherpa yells but you shove him and \nsprint down the mountain. You successfully make it to the base and \npay your respects to him. ")