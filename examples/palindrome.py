import time

def is_palindrome_efficient(s):
    start_time = time.perf_counter()
    # Convert to lowercase and filter out non-alphanumeric characters
    cleaned = [char.lower() for char in s if char.isalnum()]

    # Compare characters from start and end moving towards the middle
    left = 0
    right = len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            duration = (time.perf_counter() - start_time) * 1000
            print(f'Took {duration} ms')
            return False
        left += 1
        right -= 1
    duration = (time.perf_counter() - start_time) * 1000
    print(f'Took {duration} ms')
    return True

def is_palindrome(s):
    start_time = time.time()
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    isPalindrome = cleaned == cleaned[::-1]
    duration = (time.time() - start_time) * 1000
    print(f'Took {duration} ms')
    return isPalindrome

def main():
    while(True):
        input_string = input('Enter a string to check if it\'s a palindrome: ')
        if is_palindrome(input_string):
            print('IS a palindrome.')
        else:
            print('NOT a palindrome.')

if __name__ == '__main__':
    main()