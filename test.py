#check if a string is a palindrome or not
def checkString(string):
    string.lower()
    newstr = string[::-1]
    if newstr == string:
        print("The string is palindrome")
    else:
        print("The string is not palindrome")

checkString(input("Enter string: "))
