#custom error handling


def checkfile_extension(filename):
    if not filename.endswith('.txt'):
        raise ValueError("Invalid file extension. Only .txt files are allowed.")
    return True

try:
    filename = "data.csv"
    checkfile_extension(filename)   
    
  
except Exception as e:
    print(f"An unexpected error occurred: {e}")