import time
import os
import sys
os.system("printf '\033c'")
print("Stay still")
time.sleep(5)
os.system("printf '\033c'")

def type(text):
  words = text
  for char in words:
    time.sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()
type("You decide to stand still, Max is trembling in his boots and \nthe yeti slowly makes its way towards you and reaches his hand out \nto you and Max. Max exclaims maybe he is trying to be friends with \nyou and then Max reaches his hand out to the yeti.  Before you know \nit the yeti picks up Max and swallows him whole.  You try to run but \ncan't. You're frozen out of fear. Maybe next time take heed of the \nwarnings")