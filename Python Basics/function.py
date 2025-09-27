def makesum(n):
    
    sum = 0
    i = 0
    while i <= n1
        sum = sum + i
        i = i + 1
    
    return sum
    
n = int(input("Enter a number: "))
print("The sum is:", makesum(n))



def add_two_number(a,b):
    return a+b
print(add_two_number(2,3))




#multiple arguments
def add_multiple_number(*args):
    sum = 0
    print(args)
    for i in args:
        sum = sum + i
    return sum
print(add_multiple_number(2,3,4,5,6))
