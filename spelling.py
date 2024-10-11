# Time limit    1 second
# Memory limit  64.0 MB
# Input         stdin or input.txt
# Output        stdout or output.txt
#
# System administrator Pakhom is not good with spelling and constantly forgets the rule
# “Жи-Ши write with И.” Vasya and Petya decided to help him and write a program that draws
# a large rectangle from the letters И. They plan to build it into a text editor to remind
# Pakhom about spelling. Help them!
#
# Input format
# Given two integers separated by a line break.
# 1 ≤ a ≤ 15
# 1 ≤ b ≤ 15.
#
# Output format
# Print a rectangle of size a rows and b columns, made up of the letters И, as in the example.
# There must be exactly one space between letters in a line.
# Between lines, exactly one line of spaces must be printed, the same length as the rest of the lines.
#
# Sample
# Input
# 2
# 2
#
# Output
# *   * *   *
# *  ** *  **
# * * * * * *
# **  * **  *
# *   * *   *
#
# *   * *   *
# *  ** *  **
# * * * * * *
# **  * **  *
# *   * *   *


def draw_colums(b):
    print("*   * " * b)
    print("*  ** " * b)
    print("* * * " * b)
    print("**  * " * b)
    print("*   * " * b)


def draw_rows(a, b):
    for i in range(a):
        draw_colums(b)
        print()


a = int(input())
b = int(input())
draw_rows(a, b)
