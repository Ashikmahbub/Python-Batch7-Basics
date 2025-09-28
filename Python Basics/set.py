a = [1,2,2,3,4,4,5,6,7,7,8,9,9]
s = set(a)
print(s)
s.add(10)
b=[3,3,4,5,6,7,8,9,10]

c = set(b)
d = s.union(c)
print(d)
print(s.intersection(c))