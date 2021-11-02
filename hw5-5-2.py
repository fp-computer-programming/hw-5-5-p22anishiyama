# Author: ATN 10/29/21

six_letter_word = str(input("Please enter any 6 letter word: "))

odd = six_letter_word[0] + "-" + six_letter_word[2] + "-" + six_letter_word[4]
even = six_letter_word[1] + "-" + six_letter_word[3] + "-" + six_letter_word[5]

print(odd)
print(even)
