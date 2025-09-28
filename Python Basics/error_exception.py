#errors and expceptions
try:
    a = 5 / 0   
    print(a)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.") 
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Execution completed.")


#file handling