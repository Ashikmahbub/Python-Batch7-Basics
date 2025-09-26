mylist = ["ashik","labonno"]
mytring = "I love bangladesh"
print(mytring.split())

mylist.append("Rayean")
print(mylist)
print(mylist.count('ashik'))

print(mylist.reverse())
print(mylist)


# tuple immutable

t = (1,2,3)
c = (1,)

print(tuple(reversed(t)))