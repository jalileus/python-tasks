# Time limit: 1 second
# Memory limit: 64.0 MB

# System administrator Pakhom is trying to clean up the server room. He found a huge box with wires.
# He numbered each wire with a unique natural number. There are several types of connectors in the
# server room. For each connector, Pakhom listed which wires were suitable for it. Since he was
# distracted by accountant Zinaida Markovna during the inventory, the same wire may appear in the
# connector list several times. Vasya and Petya tested all the wires, found some of them to be
# non-working, and threw them away. Now they want to leave only k wires. To do this, they decided to
# count for each wire the number of connectors to which it fits, order them in descending order, and
# select the first k. Help them!

# Input format:
# - First, two numbers n and k are given - the number of connectors and the number of wires that
#   Vasya and Petya want to select.
# - The next n lines list the numbers of wires that fit into this connector, separated by spaces.
# - The last line contains wires separated by a space, which were rejected by Vasya and Petya.

# Output format:
# - For k wires that fit into the largest number of connectors, write down the number of connectors
#   they fit into. Sort these quantities in ascending order and print one per line.

# Sample
# Input:
# 4
# 1
# 1 3 2 4
# 3 3 1 2
# 3 3 3 2
# 2 4
#
# Output:
# 4


number_connectors = int(input())
number_select = int(input())

list_wires = []
for i in range(number_connectors):
    string = input()
    l = string.split()
    list_wires.append(l)

input_string = input()

rej_wires = set(input_string.split())

set_of_wires = []
count = 0
for l in list_wires:
    new_set = set(l) - rej_wires
    keys = frozenset(new_set)
    set_of_wires.append(keys)

d = {}

for s in set_of_wires:
    for items in s:
        d[items] = 0

for s in set_of_wires:
    for items in s:
        d[items] += 1

l = []
for values in d.values():
    l.append(values)

l.sort()


for i in range(len(l) - number_select, len(l)):
    print(l[i])
