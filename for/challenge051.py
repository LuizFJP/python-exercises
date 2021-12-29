'''Develop a program that read the first term and the reason of a PA. In the end, show the progression's first ten terms'''

reason = int(input())
firstElement = int(input())
aux = 0

for n in range(1, 11):
  aux = firstElement + reason
  print(f'{ firstElement }',end= ' ')
  firstElement = aux