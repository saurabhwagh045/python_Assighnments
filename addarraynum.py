def two_sum(arr,targ):
    look_for = {}
    for n,x in enumerate(arr,0):
        try:
            return look_for[x], n
        except KeyError:
            look_for.setdefault(targ - x,n)

a = (2,7,11,15)
t = 9
print(two_sum(a,t))  

a = (3,2,4)
t = 6
print(two_sum(a,t)) 

a = (3,3)
t = 6
print(two_sum(a,t))



"""
PS C:\Users\Saurabh\Desktop\saurabhpy> & "C:/Program Files/Python311/python.exe" c:/Users/Saurabh/Desktop/saurabhpy/.vscode/addarraynum.py
(0, 1)
(1, 2)
(0, 1)
           """