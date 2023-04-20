i=int(input("Enter a number :")) 
columns=12
for j in range(1,columns+1):
   c=i*j
   print("{:2d} ".format(c),end='')
#here no need to nested for loop only for loop is enoghf
   """
Enter a number :8
 8 16 24 32 40 48 56 64 72 80 88 96 
 """