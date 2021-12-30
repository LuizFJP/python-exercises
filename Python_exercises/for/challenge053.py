'''Make a program that reads a any phrase and
say if it's a palindrome, disregarding the spaces'''

phrase = input().replace(' ','')
reversePhrase = ''

for n in range(len(phrase) - 1,-1, -1):
  reversePhrase += phrase[n]

if(phrase == reversePhrase):
  print('It\'s a palindrome')
else:
  print('It\'s not palindrome')
