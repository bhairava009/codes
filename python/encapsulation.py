# class Students:
#     def __init__(self,name,age,marks):
#         self.name=name #public
#         self._age=age    #protrcted
#         self.__marks=marks #private use getter and setter to use privte func

#      #public method
#     def display_info(self):
#         print(f"Name of the student is:{self.name}")
#         print(f"age of the student is:{self.age}")
        
#      #access privte method

#     def get_marks(self):
#         print(f"Marks of the student is: {self.marks}")

#     #setter method for private attributes modifires
#     def set_marks(self,new_marks):
#         if 0<=new_marks <=100:
#             self.__marks = new_marks
#             print("New marks has been Assigned")
#         else:
#             print("invalid")



# s1 = Students("Ravi", 23, 50)

# # Print Public Attribute Data
# print("public info",s1.name)

# # Display Protected
# s1.display_info()
# try :
#     print("Private : ", s1.__marks)
# except AttributeError :
#     print("Private Attibute can not be accessed ")

# # Method call for a get method
# s1.get_marks()

# # Method call for set method
# s1.set_marks(55)

# s1.get_marks()               
class Students:
    def __init__(self, name, age,  marks):
        self.name = name  #public 
        self._age = age    #protected
        self.__marks = marks #private

    # public methods
    def display_info(self):
        print(f"Name of the Student is : {self.name}")
        print(f"Age of the Student is : {self._age}")

    # Getter Method for private Attribute Access
    def get_marks(self):
        print(f"Marks of Student is : {self.__marks}")

    # Setter Method for Private Attribute Modification
    def set_marks(self,new_marks):
        if 0<= new_marks <= 100:
            self.__marks = new_marks
            print("New Marks has been Assigned")
        else :
            print("Invalid Input")

s1 = Students("Ravi", 23, 50)

# Print Public Attribute Data
print("public info",s1.name)

# Display Protected
s1.display_info()

try :
    print("Private : ", s1.__marks)
except AttributeError :
    print("Private Attibute can not be accessed ")

# Method call for a get method
s1.get_marks()

# Method call for set method
s1.set_marks(55)

s1.get_marks()