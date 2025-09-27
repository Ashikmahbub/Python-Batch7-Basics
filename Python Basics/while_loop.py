a = [1,2,3,5,6]

result  = 0

n =  len(a)
i =0
while i < n:
    result = result+a[i]
    i = i+1

print(result)


#eliminate negative numbers from list

a = [-10,-20,-30,40,50]

i =  0
while i < len(a):
    if a[i] < 0:
        i = i + 1
        continue
    print(a[i])
    i = i + 1