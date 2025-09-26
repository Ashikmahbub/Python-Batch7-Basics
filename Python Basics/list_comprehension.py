a= [1,2,3,4,5,6,7,8]

result = []

for i in a :
    if i %2 ==0:

        result.append(i)




print(result)



new_result =[ i for i in a if i  % 2 == 0]

print(new_result)

square_list =[i**2 for i in a if i % 2 == 0]


print(square_list)