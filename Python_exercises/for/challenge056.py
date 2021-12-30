''' Develop a program that read the name, age and sex of 4 people. In the end of program, show:
The group's age average
Which is the oldest man name
How much women have less than 20 years old'''

sumOfAges = 0
oldestManName = ''
oldestManAge = 0
countYoungWomen = 0

for n in range(0, 4):
  name = input()
  age = int(input())
  sex = input()

  sumOfAges += age
  if(sex == 'm' and age > oldestManAge):
    oldestManAge = age
    oldestManName = name
  if(sex == 'f' and age < 20):
    countYoungWomen += 1

print(f'The group\'s average age is { sumOfAges/4 } years old.')
print(f'The oldest man name is { oldestManName }')
print(f'There\'re { countYoungWomen } women are less than 20 years old')