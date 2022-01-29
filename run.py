import time
import os
import sys
os.system("printf '\033c'")
print("You take care to not trigger any traps")
time.sleep(5)
os.system("printf '\033c'")

def type(text):
  words = text
  for char in words:
    time.sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()
type("You begin to run furiously but you hear the yeti follow you. \nLuckily, you are able to run quickly enough to not be overtaken \nimmediately. Max screams and begins to sprint past you. As the yeti \ncatches up, you realize your only choice may be to outrun Max to \nsurvive. You trip Max and run without looking back until you reach \nthe bottom. You still don't know what happened to Max, only that a \nfew days after you reached the bottom, snow stained with blood was \nfound on the mountain.")