def compute_list_avg(number_list):
    return sum(number_list) / len(number_list)

number_list = []

for i in range(5):
    number_list.append(float(input("Type " + str(i + 1) + "° number: ")))

print("\nThe average of these numbers is " + str(compute_list_avg(number_list)))
