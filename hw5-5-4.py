# Author: ATN 10/29/21

word_one = str(input("Please enter a word: "))
word_two = str(input("Please enter another word: "))
word_three = str(input("Please enter another word: "))

a = word_one.lower()
b = word_two.lower()
c = word_three.lower()

if(a < b and a < c):
    if(b < c):
        print(a, b, c)
    else:
        print(a, c, b)
elif(b < a and b < c):
    if(a < c):
        print(b, a, c)
    else:
        print(b, c, a)
elif(c < a and c < b):
    if(a < b):
        print(c, a, b)
    else:
        print(c, b, a)

# words = (word_one, word_two, word_three)
# sorted_words = sorted(words)
# print(sorted_words)
