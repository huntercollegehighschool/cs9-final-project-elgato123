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
type("You walk in cautiously. As you examine the room, you see a series of \ntripwires and panels across the floor. You sigh in relief that \nyou didn't charge in like you had planned. You walk carefully \naround any potential traps and as you arrive at the relic, you \nlift it carefully off its pedestal. You and Max decide to go home with \nthe relic as a souvenir. You don't realize, however, that the statue has a curse. \nYou never make it home. Nothing good ever comes from angering the ancient \nMayan gods.")