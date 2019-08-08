'''

                            Online Python Compiler.
                Online Compiler Link: https://www.onlinegdb.com/online_python_compiler

'''

x, p = [int(x) for x in input("Enter Price of Coffee and Discount Rate: ").split()]
c=0

y=0

while x>=1:
  y=y+x
  
  dif=(x*(p/100))
  
  x=x-dif
  c=c+1
  
  
  
print('Total Amount neccessary to order Free Coffee:')
print(round(y))  
  

