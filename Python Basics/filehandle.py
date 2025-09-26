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
