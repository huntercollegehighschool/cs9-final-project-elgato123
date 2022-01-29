import time
import os
import sys
os.system("printf '\033c'")
print("you are far too adventurous to give up now")
time.sleep(5)
os.system("printf '\033c'")

def type(text):
  words = text
  for char in words:
    time.sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()
type("You continue in spite of Max giving up. You continue climbing. \nAfter walking for an hour, you see a small cabin up on the peak, one \nthat Max mentioned earlier, and you decide to ask to stay the night, \nas opposed to returning in the dark and encountering whatever made \nthose tracks. You spend the night in the cabin and walk back down to \nthe summit safely, where you finally can rest. Max never showed up \nhowever, and you can only speculate what happened to him as he tried \nto walk back down. ")