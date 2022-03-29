#check if a string is a palindrome or not
def checkString(string):
    newstr = string[::-1]
    if newstr.lower() == string.lower():
        print("The string is palindrome")
    else:
        print("The string is not palindrome")

checkString(input("Enter string: "))
