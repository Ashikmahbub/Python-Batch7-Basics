#error is compile time errors,syntax errors
#exception is runtime errors,index error,value error,zero division error,file not found error
#try,except,finally,raise,assert



try: #code that may raise an exception
    with open("sample.txt","r") as file:
        content = file.read()
        print(content)
        
except FileNotFoundError: #handling specific exception
    print("File not found. Please check the file path.")    
    