# Function that prints user name and age
def hello_user(user_name, user_age):
    print("Hello " + user_name + ", you are " + str(user_age))

# Asking the user name
usr_name = input("What is your name? ")

# Asking the user age
usr_age = input("How old are you? ")

# Calling the defined function
hello_user(usr_name, usr_age)
