#3 Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.



def string(s):
    d = {'uppercase':0,'lowercase':0}
    for char in s:
        if char.isupper():
            d['uppercase'] +=1
        elif char.islower():
             d['lowercase'] +=1
        else:
            pass

    print("number of uppercase letters",d['uppercase'])
    print("number of lowercase letters",d['lowercase'])

string(input("enter the string"))