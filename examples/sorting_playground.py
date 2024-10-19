my_arr = [1, 3, 5, 2, 9, 7, 8, 0]
my_arr.sort()
print(my_arr)
my_arr.sort(reverse=True)
print(my_arr)

my_arr2 = [{'color': 'black'}, {'color': 'red'}, {'color': 'blue'}]
print(sorted(my_arr2, key=lambda i: i['color'], reverse=True))
print(my_arr2)

my_arr3 = {'2': 'black', '6': 'red', '1': 'blue'}
sorted(my_arr3.items(), key=lambda i: i[1])
print(my_arr3)