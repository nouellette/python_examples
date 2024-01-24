def modify_dictionary(d):
    d['new_key'] = 'new_value'
    if 'existing_key' in d:
        d['existing_key'] = 'modified_value'

def modify_list(lst):
    lst.append(3)

def modify_string(s):
    s += ' world'

my_dict = {'existing_key': 'original_value'}
print('Before modification:', my_dict)
modify_dictionary(my_dict)
print('After modification:', my_dict)

my_list = [1, 2]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3]

my_string = 'hello'
modify_string(my_string)
print(my_string)  # Output: 'hello'