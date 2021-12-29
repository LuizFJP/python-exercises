''' Make a program that calculates a sum between
all of odd numbers that are multiple of three and
that meet in the interval from one to five hundread '''
sumOddNumbers = 0

for n in range(1, 500):
  if(n % 2 == 1 and n % 3 == 0):
    sumOddNumbers+= n

print(sumOddNumbers)