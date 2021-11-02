# Author: ATN 10/29/21

palindrome = str(input("Please enter a palindrome: "))

if(palindrome[::-1] == palindrome):
    print("Yes, this word is a palindrome.")
else:
    print("No, this word is not a palindrome.")
