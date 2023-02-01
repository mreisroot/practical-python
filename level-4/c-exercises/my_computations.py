def max_value(number_list):
    maxval = 0
    for number in number_list:
        if number > maxval:
            maxval = number
    return maxval
