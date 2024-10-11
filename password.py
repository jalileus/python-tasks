# Time limit	1 second
# Memory limit	64.0 MB
# Input	stdin or input.txt
# Output	stdout or output.txt
# Accountant Zinaida Markovna is very afraid that her quarterly report will be ruined by hackers.
# She asked system administrator Pakhom to protect the file with a password.
# Pakhom loves the number 3 very much, so he generated a positive integer number with exactly three digits 3 as a password.
# Unfortunately, Zinaida Markovna lost the piece of paper with the password,
# and Pakhom only remembers that he was the ith number with exactly three triples.
# Help them open the file.

# Input format
# Given a positive integer i not exceeding 10000.

# Output format
# Print one integer — the password to the file.

# Sample
# Input	Output
# 1
# 333


def generate_password(i):
    count = 0
    num = 330
    while count < i:
        num += 1
        if str(num).count("3") == 3:
            count += 1
    return num


i = int(input())
password = generate_password(i)
print(password)
