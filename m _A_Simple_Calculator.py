# [S.O.F.T]lab 
#>> https://www.facebook.com/groups/soft.lab/ <<

# 02 July 2017
# Python 3.6.1

# A Simple Calculator of asking users Two values to do basic Math.

def summ(x,y):
  return x+y

def dec (x,y):
  return x-y
  
def mul (x,y):
  return x*y
  
def div (x,y):
  return x/y  

ask = input('''What do you want to do :

  Summation       [1]
  Deduction       [2]
  Multiplication  [3]
  Division        [4]
  
  << Enter a correspond number >> : ''')
  
if ask =='1' or ask=='2' or ask=='3' or ask=='4':
  print()  
  x = int(input('Enter a value (x) and press ENTER : '))  
  y = int(input('Enter another value (y) and press ENTER : '))
  print()
  
  
  if ask =='1':
    print('(x+y) =', summ( x, y))
    
  elif ask =='2':
    print('(x-y) =', dec( x,y))
    
  elif ask =='3':
    print('(x*y) =', mul( x,y))
    
  else:
    print('(x/y) =', div( x,y))
  
  print('Done!')

else:
    print()
    print ('''
    Enter a correspond number [1/2/3/4]
    Please, RUN again!''')



