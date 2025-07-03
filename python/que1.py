# Predefined list
my_list = [10, 20, 30, 40, 50]

try:
    # Ask the user for an index
    user_input = input("Please enter an index (0-4): ")
    
    try:
        # Attempt to convert input to an integer
        index = int(user_input)
        
        # Access the list at the given index
        print(f"The value at index {index} is {my_list[index]}")
        
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
    except IndexError:
        print("Index out of range! Please enter an index between 0 and 4.")

finally:
    print("End of program")
3