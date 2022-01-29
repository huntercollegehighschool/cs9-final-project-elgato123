import time
import os
import sys
os.system("printf '\033c'")
print("your greed overcomes your friendship with Max")
time.sleep(5)
os.system("printf '\033c'")

def type(text):
  words = text
  for char in words:
    time.sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()
type("you run to the gold selfishly. \nMax knocks on the stone coffin and slowly, you \nhear the sound of the top being pulled back. \nMax turns white and exclaims in fear before \ntwo mummified arms grab him and wrench him into the coffin. \nYou cry out but you manage to stuff your pockets with gold. \nAs you sprint out of the tomb, \nyou hear a pitter patter of steps behind you. \nYou practically hurl yourself out of the hole \nand run screaming into the jungle. \nYou live richly for the rest of your life but you never \ntruly escape the horror of almost dying in that tomb. \nEvery so often, you hear the footsteps in your house. ")