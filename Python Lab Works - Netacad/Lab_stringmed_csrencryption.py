line = input("Enter a line of text to encode: ")
n = int(input("Enter a number: "))
newstring = ''
for ch in line:
    # check if character is alphabetic
    if ch.isalpha() != True:
        newstring += ch
        continue
    # check if character is lowercase
    if ch.islower() == True:
        if (ord(ch) + n) > ord('z'):
            newch = chr(ord(ch) + n - 26)
        else:
            newch = chr(ord(ch) + n)
    # check if character is uppercase
    else:
        if (ord(ch) + n) > ord('Z'):
            newch = chr(ord(ch) + n - 26)
        else:
            newch = chr(ord(ch) + n)
    newstring += newch
print(newstring)