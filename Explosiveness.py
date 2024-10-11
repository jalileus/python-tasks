# Time limit: 1 second
# Memory limit: 64.0 MB

# When processing radioactive materials, three types of waste are generated - highly hazardous (type A),
# conditionally non-hazardous (type B), and not at all dangerous (type C). The same containers are used to
# store them. After placing the waste in containers, the latter are stacked vertically. A stack is
# considered explosive if it contains more than one type A container in a row. For a given number of
# containers N, we need to determine the number of possible safe stacks.

# Input format:
# - The first line contains one integer N (1 ≤ N ≤ 20).

# Output format:
# - You need to print one number—the number of safe options for forming a stack of N containers.

# Sample
# Input:
# 4
#
# Output:
# 60


def GetSafeContainers(n):
    A = 3
    B = 8
    C = 22
    for i in range(n - 1):
        C = (2 * B) + (2 * A)
        A = B
        B = C
    return A


n = int(input())
print(GetSafeContainers(n))
