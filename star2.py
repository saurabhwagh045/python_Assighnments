rows =  5
for i in range(rows):
    for j in range (i+1):
        print(' ',end=' ')
    for j in range (i,rows):
        print('*',end=' ')
print()


"""
OUTPUT:
star1.py

* * * * *
  * * * *
    * * *
      * *
        *

"""