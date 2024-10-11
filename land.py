# Time limit: 1 second
# Memory limit: 64.0 MB
# Input: stdin or input.txt
# Output: stdout or output.txt

# Yasha was swimming in a pool sized N×M meters and started feeling tired.
# At this moment, he discovered that he was at a distance of x meters from
# one of the long sides (not necessarily from the nearest one) and y meters
# from one of the short sides. What is the minimum distance Yasha must swim
# to get out of the pool onto the side?

# Input format:
# The program receives the numbers N, M, x, y as input.

# Output format:
# The program should print the number of meters that Yasha needs to swim to the side.

# Sample 1:
# Input:
# 23
# 52
# 8
# 43
# Output:
# 8

# Sample 2:
# Input:
# 18
# 90
# 3
# 63
# Output:
# 3

# Sample 3:
# Input:
# 96
# 1
# 0
# 83
# Output:
# 0


N = int(input())
M = int(input())
x = int(input())
y = int(input())
if N > M:
    temp = M
    M = N
    N = temp

dist1 = N - x
dist2 = M - y
print(min(dist1, dist2, x, y))
