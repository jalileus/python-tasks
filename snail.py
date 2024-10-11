# Time limit: 1 second
# Memory limit: 64.0 MB
# Input: stdin or input.txt
# Output: stdout or output.txt

# A snail crawls along a vertical pole h meters high, rising a meters during
# the day, and descending b meters during the night. On what day will the
# snail crawl to the top of the pole?

# Input format:
# The program receives as input natural numbers h, a, b.

# Output format:
# The program must print one natural number. It is guaranteed that a > b.

# Sample 1:
# Input:
# 10
# 3
# 2
# Output:
# 8

# Sample 2:
# Input:
# 20
# 7
# 3
# Output:
# 5

h = int(input())
a = int(input())
b = int(input())
count_day = 0
current_hight = 0
while h > 0:
    current_hight += a
    count_day += 1
    if current_hight >= h:
        break
    current_hight -= b
print(count_day)
