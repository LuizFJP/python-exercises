'''Develop a program that read six itenger 
numbers and show the sum only those that are even. If the value typed to be even disregard it'''

sumOfOdds = 0

for n in range(1, 7):
  number = int(input())
  if(number % 2 == 0):
    sumOfOdds += number

print(sumOfOdds)