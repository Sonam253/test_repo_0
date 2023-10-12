def string_to_base10(s):
    base = 26
    result = 0

    for char in s:
        result = result * base +(ord(char)-ord('a') + 1)

    return result

def compare_strings(str1, str2):
    if len(str1) == len(str2):
        return str1 == str2
    else:
        return False

#Example usage:
input_string1 = "abcd"
input_string2 = "abcde"

result1 = string_to_base10(input_string1)
result2 = string_to_base10(input_string2)

print(f"The base 10 equivalent of '{input_string1}' is: {result1}")
print(f"The base 10 equivalent of '{input_string2}' is: {result2}")

#Compare strings
if compare_strings(input_string1, input_string2):
    print("Strings are equal.")
else:
    print("Strings are not equal.")
