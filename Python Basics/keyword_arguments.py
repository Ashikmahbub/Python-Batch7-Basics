def my_function(f_name, l_name,age):
    print("Hello " + f_name + " " + l_name)
    print("Your age is: " + str(age))
    
    
my_function(l_name="Smith", f_name="John", age=30)
my_function("Alice", "Johnson", age=25)


def my_function2(**kwargs):
    for key, value in kwargs.items():
        print(key + ": " + str(value))
        
my_function2(name="John", age=30, city="New York")
my_function2(country="USA", profession="Engineer")


