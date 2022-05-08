def swap(values_list):
    last_el = values_list.pop()
    first_el = values_list.pop(0)
    values_list.insert(0, last_el)
    values_list.append(first_el)

values_list = input().split(',')  # Program receives comma-separated values like 5,4,12,19
swap(values_list)

print(values_list)