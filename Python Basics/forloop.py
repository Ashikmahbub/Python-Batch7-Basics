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

#eliminate negative numbers from list

a = [-10,-20,-30,40,50]

i =  0
while i < len(a):
    if a[i] < 0:
        i = i + 1
        continue
    print(a[i])
    i = i + 1