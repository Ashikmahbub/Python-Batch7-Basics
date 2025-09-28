


try: 
    # with open("non_existent_file.txt", "r") as file:
    #     content = file.read()
    #     print(content)
    a= [1, 2, 3]
    print(10 / 10)
    x = int("2")  # This will raise a ValueError
    print(a[100])  # This will raise an IndexError
    
    x = abc  # This will raise a NameError
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except FileNotFoundError:
    print("Error: The specified file was not found.")
except ValueError:
    print("Error: Invalid value provided.")
#handling any other exception 
except Exception as e:
    print(f"An unexpected error occurred: {e}")