import sys

digit_string = sys.argv[1]
sum_of_digit = 0
for char in digit_string:
    sum_of_digit += int(char)
print(sum_of_digit)
