# A shoe factory is about to start producing an elite model of boots.
# The lacing holes will be arranged in two rows.
# The distance between the rows will be 'a', and the distance between the holes in the row will be 'b'.
# The number of holes in each row is 'N'. Lacing should occur in an elite way
# "up, horizontally in another row, up, horizontally, etc."
# The length of the free end of the lace must be 'l'.

# Input format:
# The program receives four natural numbers a, b, l, and N as input.

# Output format:
# The program should output one number - the required length of the lace.

# Sample 1:
# Input:
# 2
# 1
# 3
# 4
# Output:
# 26

# Sample 2:
# Input:
# 1
# 1
# 1
# 1
# Output:
# 3

# Explanation:
# The total length of the lace will be calculated by considering the vertical and horizontal lengths of the lace.
# Each "up" move between holes adds the distance between the rows (2 * a).
# Each horizontal move between two rows adds the distance between holes (b).
# The length of the free ends of the lace is 'l' for both ends.
# Total length = 2 * l (for both ends) + (N-1) * b (for horizontal) + 2 * (N-1) * a (for vertical)


a = int(input())
b = int(input())
l = int(input())
N = int(input())
vertical_move = (2 * b * (N - 1)) + (2 * l)
horizontal_move = a + a * (N - 1) * 2
length_lace = vertical_move + horizontal_move
print(length_lace)
