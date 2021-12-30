'''Make a program that read a birth year of seven
people. In the end, show how much people aren't still achieve the majority and how much are already legal age'''

from datetime import date

year = date.today().year
majorityCount = 0

for n in range(0, 7):
  birthYear = int(input())
  if((year - birthYear) >= 18):
    majorityCount += 1

print(f'There are { majorityCount } that didn\'t achieve the majority and { 7 - majorityCount } are in majority.')
