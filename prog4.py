def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):

        for j in range(0, n -i-1):
            
            if arr[j]>arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example :
input_array = [3, 5, 6, 1, 2, 9, 15]

print("original array:", input_array)
bubble_sort(input_array)
print("Sorted array:", input_array)