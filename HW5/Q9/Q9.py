def isPalRecur(string):
    string = string.lower()
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return isPalRecur(string[1:-1])
 
# test the output
print(isPalRecur("kayak")) # True
print(isPalRecur("hello")) # False

# Edge cases
print(isPalRecur("helleh")) # True
print(isPalRecur("abcdefghgfedcba")) # True
