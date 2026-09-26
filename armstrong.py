n=153
original=n
count=0
sum=0
for i in range(len(str(abs(n)))):
    count+=1
while(n>0):
    digits=n%10
    sum+=digits**count
    n//=10

print(sum)

if(sum==original):
    print("armstrong no.")
else:
    print("not arms")

