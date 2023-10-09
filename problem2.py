#2 Write a Python program to reverse a string.

def reverse(s):
    reverse_string = ''
    index  = len(s)
    while index >0:
        reverse_string += s[index-1]
        index = index-1
    return reverse_string

print(reverse(input("enter a string")))

