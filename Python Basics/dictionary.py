mydict = { "Name": "John", "Age": 30, "City": "New York" }

d = mydict.keys()
print(d)


for key in mydict:
    print(key)
    
for value in mydict.values():
    print(value)
    
    
for key, value in mydict.items():
    print(key, value)
    
if "Name" in mydict:
    print("Yes, 'Name' is one of the keys in the mydict dictionar       y")
a = [1,2,3,4,5]
b = ["mango","banana","orange"]
c=dict(zip(a,b))
print(c[1])