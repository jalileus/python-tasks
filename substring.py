# Time limit: 1 second
# Memory limit: 64.0 MB

# You are given a string and a positive integer N. Compile a dictionary with the frequencies of occurrence
# of all substrings of length N of the original string. As an answer to the problem, print a lexicographically
# sorted list of substrings that appear 2 or more times in the original substring.

# Input format:
# - String and positive integer via standard input. They can be read by calling the input() function twice.

# Output format:
# - A list of strings sorted in lexicographic order that satisfies the condition of the problem.

# Sample
# Input:
# abbccc
# 1
#
# Output:
# ['b', 'c']


s = input()
n = int(input())
empty_string = ""
temp_list = list(s)
substrings_list = []

length = len(s)
i = j = 0
for i in range(length):
    while j < n:
        if i >= length:
            break
        empty_string += temp_list[i]
        i += 1
        j += 1
    if i < length:
        substrings_list.append(empty_string)
        empty_string = ""
        j = 0


i = 0
j = 1
temp_set = set()
new_length = len(substrings_list)
while i < (new_length):
    while j < (new_length):
        if substrings_list[i] == substrings_list[j]:
            temp_set.add(substrings_list[i])
        j += 1
    i += 1
    j = i + 1

res_list = list(temp_set)
print(sorted(res_list))
