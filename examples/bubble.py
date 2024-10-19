def bubble_sort(arr):
    print(arr)
    n = len(arr)
    for i in range(n):
        print(i)
        # Flag to check if any swap happens
        swapped = False
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                print(arr)
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break
    return arr

# Example usage:
example_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(example_list)
print("Sorted array:", sorted_list)