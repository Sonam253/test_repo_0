def string_to_base10(s):
    base = 26
    result = 0
    for char in s:
        result = result * base + (ord(char) - ord('a') + 1)
    return result
#Example usage:
input_string = "abcd"
result = string_to_base10(input_string)
print(f"The base 10 equivalent of '{input_string}' is: {result}")