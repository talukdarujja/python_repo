# # print("hello world")
# # print("ujjal")
# # name=input("enter your name")
# # print("your name:",name)
# # n=int(input("enter integer:"))
# # print(n)
# # a=int(input("enter a:"))
# # b=int(input("enter b:"))
# # print(a+b)

# # n=10
# # i=0
# # while(i<10):
# #     i+=1
# #     print(i)

# # a=int(input("enter the numbers:"))
# # b=int(input("enter the numbers:"))

# # if(a>b):
# #     print(a)
# # else:
# #     print(b)

# # a=int(input("enter the numbers:"))
# # b=int(input("enter the numbers:"))
# # c=int(input("enter the number:"))
# # if(a>b and a>c):
# #     print(a)
# # elif(b>a and b>c):
# #     print(b)
# # else:
# #     print(c)

# num=8
# if(num>0):
#     print("pos")
# elif(num==0):
#     print("netral")
# else:
#     print("neg")

# num=9
# if(num%2==0):
#     print("even")
# else:
#     print("even")

# age=-23
# if(age>=18):
#     print("vote")
# else:
#     print("non vote")
n=-121
original=n
rn=0
sign=-1 if n<0 else 1
while(n!=0):
    r=n%10
    rn=rn*10+r
    n=n//10
    rn*=sign
print(rn)
if original==rn:
    print("True")
else:
    print("False")
