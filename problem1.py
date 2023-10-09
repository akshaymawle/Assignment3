#1) write python function to  sum all the numbers in list.

def sum(numbers):
    total = 0
    for i in  numbers:
        total += i
    return total

list1 = [8, 2, 3, 0, 7]
print(sum(list1))