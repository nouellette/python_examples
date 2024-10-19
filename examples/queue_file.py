from collections import deque

# Creating a queue
queue = deque()

# Enqueue: Adding elements to the end of the queue
queue.append('item1')  # Queue is now ['item1']
queue.append('item2')  # Queue is now ['item1', 'item2']
queue.append('item3')  # Queue is now ['item1', 'item2', 'item3']

# Dequeue: Removing elements from the front of the queue
first_item = queue.popleft()  # first_item is 'item1', queue is now ['item2', 'item3']

# Checking if queue is empty
is_empty = not queue  # is_empty is False

# Size of the queue
size = len(queue)  # size is 2

print('Is stack empty?', is_empty)
print('What is top element?', first_item)
print('Size of stack?', size)