'''Make a program that read the weigth of 5 people.
In the end, show which was the bigger and the 
smallest read weigth'''
from sys import maxsize

bigger = 0
smallest = 9999999

for n in range(0, 5):
  weigth = float(input())
  if(weigth > bigger):
    bigger = weigth
  elif(weigth < smallest):
    smallest = weigth
  else:
    pass

print(f'the biggest weight is { bigger } the smalles weight is { smallest }')