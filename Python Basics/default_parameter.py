#default argument
def greet(name, msg="Hello"):
    print(msg + ", " + name + "!")   
    
#if we don't pass the second argument, it will use the default value
greet("Alice")


greet("Bob", "Good morning")


def greeting():
    pass