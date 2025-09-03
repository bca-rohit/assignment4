content=input("Enter the content for write in a file: ")
file=open("output.txt","w")
file.write(content)
print("data has successfully been written")
file.close()
# append the additional data

additional=input("Enter the additional content for append in a file: ")
file=open("output.txt","a")
file.write(additional)
print("data has successfully appended ")
file.close()
#read and display the data

file=open("output.txt","r")
final_content=file.read()
print("final content is:",final_content)
file.close()
