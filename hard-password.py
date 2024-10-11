# Time limit	1 second
# Memory limit	64.0 MB
# Input	stdin or input.txt
# Output	stdout or output.txt
# Vasya and Petya are trying to strengthen computer protection in the accounting department of the shark.olymp service.
# They come up with a new complex password for the computer.
# Guys consider a password complex if it contains at least one capital letter, at least one lowercase letter,
# and at least one number. However, accountant Zinaida Markovna cannot remember the password if it contains
# more than 3 digits or is longer than 10 characters.

# To optimize the search, the guys asked you to write a program that checks whether the password is strong
# and whether Zinaida Markovna can remember it.

# Input format
# Given a file input.txt, which contains one line consisting of Latin letters and numbers, no more than 30 in length.
# There is no line feed at the end.

# Output format
# Output two lines to the output.txt file. In the first, type YES if the password is considered complex,
# and NO otherwise. In the second, type YES if Zinaida Markovna can remember the password, and NO otherwise.

# Sample 1
# Input
# Pa55word12
# Output
# YES
# NO

# Sample 2
# Input
# nailpolish
# Output
# NO
# YES


with open("input.txt", "r") as f:
    password = f.readline()


number_of_digits = sum(digit.isdigit() for digit in password)
number_of_capital = sum(capital.isupper() for capital in password)
number_of_lower = sum(lower.islower() for lower in password)
if number_of_capital == 0 or number_of_digits == 0 or number_of_lower == 0:
    complex_password = "NO"
else:
    complex_password = "YES"
if number_of_digits > 3 or len(password) > 10:
    readable_password = "NO"
else:
    readable_password = "YES"

with open("output.txt", "w") as f:
    f.write(complex_password + "\n")
    f.write(readable_password)
