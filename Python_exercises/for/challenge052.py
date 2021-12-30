'''Make a program that read a itenger number and
say if it is or not a cousin number'''

number = int(input())
count = 0
for n in range(number, 0, -1):
  if(number % n == 0):
    count += 1

if(count == 2):
  print('It\'s cousin')
else:
  print('It is not a cousin')