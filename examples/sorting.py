my_list = [3, 1, 4, 1, 5, 9, 2]
sorted_list = sorted(my_list)
print(sorted_list)  # Output: [1, 1, 2, 3, 4, 5, 9]

sorted_list_desc = sorted(my_list, reverse=True)
print(sorted_list_desc)  # Output: [9, 5, 4, 3, 2, 1, 1]

my_list.sort()
print(my_list)  # Output: [1, 1, 2, 3, 4, 5, 9]

my_list.sort(reverse=True)
print(my_list)  # Output: [9, 5, 4, 3, 2, 1, 1]

my_object = {'1': 'apple', '3': 'carrot', '2': 'banana'}
sorted_people = sorted(my_object, key=lambda my_object: my_object[0])
print(sorted_people)

my_object2 = [{'name': 'apple', 'color': 'red'}, {'name': 'carrot', 'color': 'orange'}, {'name': 'banana', 'color': 'yellow'}]
sorted_people2 = sorted(my_object2, key=lambda my_object2: my_object2['color'])
print(sorted_people2)