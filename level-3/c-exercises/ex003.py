def compute_list_avg(number_list):
    return sum(number_list) / len(number_list)

number_list = []

ask_user_for_numbers = True

while ask_user_for_numbers:
    num = float(input("Type a number (0 to stop): "))
    if num == 0:
        ask_user_for_numbers = False
    else:
        number_list.append(num)

print("\nThe average these numbers is: " + str(compute_list_avg(number_list)))
