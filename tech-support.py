# Time limit: 1 second
# Memory limit: 64.0 MB

# Accountant Zinaida Markovna is trying to send a complaint to the technical support of the 2DKontora program
# about the incorrect operation of the program, which is preventing her from drawing up a quarterly report.
# The window for a message on the technical support site has a width of 'a', that is, no more than 'a' characters
# can be placed in one line (not counting the line feed character, that is, place a line of length a+1, in which
# the last character is a line feed, perhaps).
#
# Also, in order for a message to be accepted, it must be formatted correctly, namely:
# - One line is allowed to contain no more than 'b' words,
# - Adjacent words in a line are separated by exactly one space.
# - Each line must end with exactly one newline.
# - The first character of a line, as well as the character before the line break, cannot be spaces.
# - If the next word can be added to the current line so that all the previous points are fulfilled
#   and the line does not overflow, then it must be added to it. If these criteria are not met, the line
#   is not accepted.
#
# Zinaida Markovna's complaint contains no more than a thousand words. Since the site crashes quite often,
# she typed it in the text editor “miv”, which saves only one word per line. Help Zinaida Markovna format
# the text.
#
# Input format:
# - The first line contains the integer 'a' — the width of the window (1 ≤ a ≤ 100).
# - The second line contains an integer 'b' — the maximum number of words in a line (1 ≤ b ≤ 60).
# - What follows is the text typed by Zinaida Markovna - no more than 1000 words, consisting of lowercase
#   Latin letters, one word per line. It is guaranteed that the length of the word does not exceed 'a'.
# - The end of the input ends with the word “0” (single zero), which is not included in the message.
#
# Output format:
# Print a formatted message. Please note that in this problem, the comparison of the answer with the
# correct one is done byte by byte (that is, taking into account spaces and line breaks).
#
# Sample
# Input:
# 10
# 2
# contora
# is
# doing
# well
# 0
#
# Output:
# contora is
# doing well


a = int(input())
if a > 100:
    a = 100
elif a < 1:
    a = 1
b = int(input())
if b > 60:
    b = 60
elif b < 1:
    b = 1
count = 0
l = []
while count <= 1000:
    word = input()
    l.append(word)
    if l[count] == "0":
        break
    count += 1
l.remove("0")
j = 0
i = 0
space = 0
s = ""
while i < count:
    for j in range(b):
        if i >= count:
            break
        else:
            s += l[i]
            if len(s) > a - space:
                break
            else:
                print(l[i], end=" ")
                i += 1
                space += 1
    print()
    s = ""
    space = 0
