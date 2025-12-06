# Design a function that will tell the user when the user provides input of numbers from 
# 1 - 7, and the output should be the name of the day in a week accordingly

def day_of_week(number):
    day_in_week = {

        1 : "monday",
        2 : "tuesday",
        3 : "wednesday",
        4 : "thursday",    
        5 : "friday",
        6 : "saturday",
        7 : "sunday"
    }
    print(day_in_week[number])

number = int(input("type the number  "))    
day_of_week(number) 

# Make a dictionary
# this_dict = {

#     "brand" : "tata",
#     "color" : "blue",
# }
# print(this_dict["brand"])

# another = { 
#     1: "Something",
#     2: "Nothing"
# }
# print(another)
