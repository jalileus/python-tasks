# Time limit	1 second
# Memory limit	64.0 MB
# Input	stdin or input.txt
# Output	stdout or output.txt
# You are given a string with characters. Print whether a string contains duplicate characters.
# We consider a string to contain duplicate characters if there is at least one character in the string
# that appears anywhere in the string two or more times.

# Input format
# String via standard input. It is guaranteed that it can be read by the input() operator.

# Output format
# True if the string contains duplicate characters, and False otherwise.

# Sample
# Input:
# qwerty
# Output:
# False


def Find_duplicate(s):
    i = 0
    while i < len(s):
        j = i + 1
        while j < len(s):
            if s[i] == s[j]:
                return True
            j += 1
        i += 1
    return False


input_string = input()
print(Find_duplicate(input_string))
