# Time limit: 1 second
# Memory limit: 64.0 MB
# Input: stdin or input.txt
# Output: stdout or output.txt

# Vasya and Petya set up a common mailbox and agreed that the password for it
# would be the number a mod b. The password was approved by Petya, who used
# the C++ language for calculations. He forgot that if a is negative and b is
# positive, then the remainder of the division will be equal to:
#
# -( |a| mod b ),
#
# that is, it will be negative, contrary to the definition (C++ is so mysterious).
# Help Vasya, who is a Python developer, recover the password.

# Input format:
# Given two integers,
# -10^18 ≤ a ≤ 10^18 ,
# 0 < b < 10^18.
#
# Output format:
# Print one integer — the password for the mailbox.
#
# Sample 1:
# Input: 7 2
# Output: 1
#
# Sample 2:
# Input: -7 2
# Output: -1
#
# Sample 3:
# Input: 1000000000000000000 1
# Output: 0


a, b = map(int, input().split())
if a < 0:
    password = abs(a) % b
    password = password * (-1)
    print(password)
else:
    password = a % b
    print(password)
