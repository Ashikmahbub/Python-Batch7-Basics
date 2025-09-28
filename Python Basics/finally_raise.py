# try:
#     f = open("data.txt", "r")
#     content = f.read()
# except Exception as e:
#     print("Something went wrong:", e)
# finally:  
#     print("File has been closed.")
#     f.close()  # MUST close file no matter what
# # OR better way to ensure file is closed    

    
    
f = None
try:
    f = open("data.txt", "r")
    content = f.read()
except Exception as e:
    print("Something went wrong:", e)
finally:
    if f:  # only close if file was opened
        f.close()
