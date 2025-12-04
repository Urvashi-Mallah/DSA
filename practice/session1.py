# Create a function that tells me if I am allowed to drink legally


def is_legal(age):
    if age >= 18:
        return True
    else:
        return False

age = int(input("type your age "))

# is_legal -> return: 
# 1. "you are allowed to drink"
# 2. "you are not allowed to drink" 


# A non empty string is always true

if is_legal(age):
    print("True will be returned when equal or more than 18")
else:
    print("False when less than 18")

# If user is under age -> A completely different ui  

# Can you use this in a production code? 
# Do you think the return value is usable? 
# What could have been the correct return type? string, integer, boolean, float, None ..... 
# Whenever there is check that needs to happen in a function, what is the best return type? 


# What if age given to the function was a string? 