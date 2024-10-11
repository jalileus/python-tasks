# Time limit: 1 second
# Memory limit: 64.0 MB
# Input: stdin or input.txt
# Output: stdout or output.txt

# The school decided to create three new math classes. Since their math classes
# take place at the same time, it was decided to allocate a room for each class
# and buy new desks for them. No more than two students can sit at each desk.
# The number of students in each of the three classes is known. How many desks
# do you need to buy so that there are enough for all the students?

# Input format:
# The input is three numbers on a new line:
# a, b, c - the number of students in each of the three classes.

# Output format:
# Print the required number of desks.

# Sample:
# Input:
# 20
# 21
# 22
# Output:
# 32

a = int(input())
b = int(input())
c = int(input())
if a % 2 == 0:
    res1 = a / 2
else:
    res1 = (a + 1) / 2
if b % 2 == 0:
    res2 = b / 2
else:
    res2 = (b + 1) / 2
if c % 2 == 0:
    res3 = c / 2
else:
    res3 = (c + 1) / 2
print(int(res1 + res2 + res3))
