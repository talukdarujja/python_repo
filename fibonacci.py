#fibonacci series
n=int(input("enter the required no to print the series:"))
a=0
b=1
print(a)
print(b)
for i in range(2,n):
    c=a+b  #c=1,c=2...
    a=b     #a=1,a=1,a=2...
    b=c     #b=1,b=2,b=3....
    print(c)
