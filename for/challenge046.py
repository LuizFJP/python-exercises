''' Do a program who shows a screen with a countdown
to blow fireworks up, starting 10 to 0, with a pause about 1 seconds between them'''

from time import sleep

for n in range(10, -1, -1):
  print(n)
  sleep(1)
print("Buuumm!!!")