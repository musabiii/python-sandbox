

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage
numbers = [5, 2, 8, 12, 1]
bubble_sort(numbers)
print(numbers)  # Output: [1, 2, 5, 8, 12]

