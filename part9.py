import time
import os
import sys
os.system("printf '\033c'")
print("You decide to run for the relic")
time.sleep(5)
os.system("printf '\033c'")

def type(text):
  words = text
  for char in words:
    time.sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()
type("You charge in and attempt to grab the relic. What you do not realize is that you unknowingly triggered a trap. As you run out, the doors shut and the \nroom begins to shroud in a deep fog. You fall asleep, never to wake up again. Max learns not to tamper with untouched monuments such as the pyramid. He \nreturns home and decides not to go on any wild adventures again. ")