# # f=open('hwe.txt','r')
# # read_text=f.readlines()
# # print(read_text,"\n")
# # f.close()

# # Open the file in read mode
# with open("C:/Users/ASUS/OneDrive/Desktop/geeks.txt", 'r') as file:
#     content = file.read()  # Read the content if needed

# # Open the file in write mode to write new content
# with open("C:/Users/ASUS/OneDrive/Desktop/geeks.txt", "w") as file:
#     file.write("Hello, World!")  # Write new content

# with open("C:/Users/ASUS/OneDrive/Desktop/geeks.txt", 'a') as file:
#     name=input("enter name: ")
#     file.write(name + '\n')



# try:
#     file=open("C:/Users/ASUS/OneDrive/Desktop/geeks.txt", 'a') as file:")





with open('user_input.txt', 'w') as user_file:
    for _ in range(3):
        line = input("Enter a line: ")
        user_file.write(line + '\n')

with open('user_input.txt', 'r') as user_file:
    content = user_file.read()
    print("Content of user_input.txt:")
    print(content)

with open('log.txt', 'a') as log_file:
    log_file.write(content)




