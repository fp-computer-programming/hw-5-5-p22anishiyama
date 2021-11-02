# Author: ATN 10/29/21

input_string = input("Please enter text: ")
splice = int(len(input_string) / 2)
print(input_string[:splice])
print(input_string[splice:])
