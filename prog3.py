def split_array(arr):
    if not arr:
        return[]
    else:
        return [[arr[0]]] + split_array(arr[1:])
    
# Example usage:
input_array = [3, 5, 6, 1, 2, 9, 15]

subarray = split_array(input_array)

print("original array:", input_array)
print("subarray:", subarray)