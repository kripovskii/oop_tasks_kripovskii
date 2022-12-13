from random import randint

def password():
      return ''.join([chr(randint(33,126)) for _ in range (randint(7,10))])
print (password())
