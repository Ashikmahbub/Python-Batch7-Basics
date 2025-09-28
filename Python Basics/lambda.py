#lambda funtion is anonymous function


square = lambda x: x * x
print(square(5))

sum = lambda a, b: a + b
print(sum(3, 4))


print((lambda x, y: x * y)(5, 6))


students = [("John", 25), ("Alice", 22), ("Bob", 23)]

sorted_students =sorted(students,key=lambda x:x[1])
print(sorted_students)


