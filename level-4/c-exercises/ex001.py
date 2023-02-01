from my_computations import max_value

number_list = []

# Reading the numbers file and returning the maximum value
with open("numbers", "r") as f:
    for line in f:
        number_list.append(int(line.rstrip("\n")))

print(number_list)
print("The maximum value of the list is " + str(max_value(number_list)))
