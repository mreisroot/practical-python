def max_value(number_list):
    maxval = 0

    for number in number_list:
        if number > maxval:
            maxval = number

    return maxval

number_list = [3, 2, -3, 9, 4]
maxval = max_value(number_list)

print("The maximum value of the list is: " + str(maxval))
