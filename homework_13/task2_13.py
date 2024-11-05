def funct(x):
   def funct_1(y):
      return x ** y
   return funct_1

numb = funct(1)
print(numb(5))