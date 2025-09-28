file = open ("sample.txt", "r")
content = file.read()   
print(content)
file.close()    

file = open ("sample.txt", "a")
file.write("\nThis is new line")        
file.close()        

file = open ("sample.txt", "r")
content = file.read()   
print(content)
file.close()
#FILE Modifucation
file = open ("sample.txt", "w")
file.write("\nThis is new line")        

file.close()    
import os
os.remove("sample.txt")  #file deletion
os.rename("sample.txt","newfile.txt")  #file rename
#file handling      
#file open

#file read  

os.path.exists("sample.txt")  #file existence check
os.path.isfile("sample.txt")  #file type check
os.path.isdir("sample.txt")   #directory type check 
os.path.getsize("sample.txt")  #file size check
os.path.abspath("sample.txt")  #file path check
os.getcwd()  #current working directory 
os.listdir()  #list of files and directories in current working directory
os.mkdir("newdir")  #directory creation
os.rmdir("newdir")  #directory deletion 
os.chdir("newdir")  #change directory   

os.path.join("newdir","sample.txt")  #path join means to join two paths forexample directory and file name      