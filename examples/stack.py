from collections import deque

# Creating a stack
stack = deque()

# Pushing elements onto the stack
# stack.append(1)  # Stack is now [1]
# stack.append(2)  # Stack is now [1, 2]
# stack.append(3)  # Stack is now [1, 2, 3]

top_element = None

# Popping elements from the stack
if stack:
    top_element = stack.pop()  # top_element is 3, stack is now [1, 2]

# Checking if stack is empty
is_empty = not stack  # is_empty is False

# Size of the stack
size = len(stack)  # size is 2

print('Is stack empty?', is_empty)
print('What is top element?', top_element)
print('Size of stack?', size)