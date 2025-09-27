n =100
sum = 0
for i in range (1,n+1):
    sum =sum +i


print(sum)



mylist = ["ass","monkey"]

for item in mylist:
    print(item,end="*")


for j in range (10):
    print("*",end="")

a = [1,2,3,4,"A",6,7,8]
for i in a:
    if type(i) is str:
        print("the variable is string")
        break
    print(i)

