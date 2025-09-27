


import functools

nums = [1,2,3,4]


sq_nums =list( map(lambda num : num*num ,nums))
print(sq_nums)

#map modifies each eliment of a iterable



even = list(filter(lambda x: x%2 ==0,nums))
print(even)

#Reduce
sum = functools.reduce(lambda x,y :x+y,nums)
print(sum)