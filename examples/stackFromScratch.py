# Creating a stack
stack = []

# Pushing elements onto the stack
stack.append(1)  # Stack is now [1]
stack.append(2)  # Stack is now [1, 2]
stack.append(3)  # Stack is now [1, 2, 3]

# Popping elements from the stack
top_element = stack.pop()  # top_element is 3, stack is now [1, 2]

# Viewing the top element without removing it
if stack:
    top_element = stack[-1]  # top_element is 2

# Checking if stack is empty
is_empty = not stack  # is_empty is False

# Size of the stack
size = len(stack)  # size is 2

print('Is stack empty?', is_empty)
print('What is top element?', top_element)
print('Size of stack?', size)