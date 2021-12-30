''' Make a number table, the user can choose a number'''

number = int(input())

for n in range(1, 11):
  print(f'{ number } X { n } = { number * n }')