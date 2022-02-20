string = input("Input text: ")
string = string.replace(" ", "")
while string.isalpha() == False:
        print("Input must only contain letters.")
        string = input("Input text: ")
        
string = string.lower()
a = len(string) // 2

string2 = string[a:]
mylst = list(string2)
mylst = list(reversed(mylst))
string2 = ''.join(mylst)

if len(string) % 2 == 0:
    if string[:a] == string2:
        print("It's a palindrome!")
    else:
        print("It's not a palindrome!")
else:
    if string[:a] == string2[:-1]:
        print("It's a palindrome!")
    else:
        print("It's not a palindrome!")