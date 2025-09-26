#A region where variables are accessible is called scope


a=10  #global variable
def func1():
    b=20  #local variable
    print(a)
    print(b)        

func1()
print(a)