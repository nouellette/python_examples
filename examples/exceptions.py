try:
    raise ValueError('This is a value error')
except ValueError as e:
    print(f"Caught an exception: {e}")

class MyCustomError(Exception):
    pass

try:
    raise MyCustomError('This is a custom error')
except MyCustomError as e:
    print(f"Caught an exception: {e}")


raise ValueError('Halt')

print('Should not be called')