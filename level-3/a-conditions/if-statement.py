user_age = 17
month = "June"

if (user_age >= 18):
    print("You're an adult")
else:
    print("You're not an adult yet")

if month in ["December", "January", "February"]:
    print("Summer time")

elif month in ["March", "April", "May"]:
    print("Autumn time")

elif month in ["June", "July", "August"]:
    print("Winter time")

else:
    print("Spring time")

print("End of program")
