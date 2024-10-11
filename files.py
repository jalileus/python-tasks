# Time limit	1 second
# Memory limit	64.0 MB
# Input	stdin or input.txt
# Output	stdout or output.txt
# Zinaida Markovna's accounting program has recently started to work poorly.
# She called system administrator Pakhom for help, and the first thing he decided to do was read the program logs.
# Logs are written to a file in the following format:

# hh:mm:ss DD/MM/YYYY 127.0.0.1 message
# The message can only contain Latin letters, numbers, periods and spaces.
# If a period comes at the end of a word, it is considered a punctuation mark.
# If there are two dots at the end of a word, the first one is considered part of the word.
# To determine in which file the breakdown occurred, Pakhom needs to analyze all messages from the logs.
# But he's lazy! He wants to write down all the file names that are mentioned in the messages and put them into a file.
# Help him!

# The files Pakhom is interested in have names consisting of lowercase Latin letters, numbers and periods,
# and have extensions .hlm or .brhl.
# For example, the files abacaba123.hlm and 123.brhl are of interest to him,
# but a.brhl.py and hlm.cpp are not.
# Pakhom is also not interested in names that begin with a period.

# Input format
# Given a file input.txt with no more than 1000 lines of the specified format.

# Output format
# In the file output.txt write down all the files mentioned in the logs, one per line
# in the order in which they were encountered. There is no need to remove duplicates.

# Sample
# Input
# 12:21:10 12/01/2022 127.0.0.1 error abc.hlm is broken.
# Output
# abc.hlm


def is_valid_file_name(name):
    return not (
        name.startswith(".")
        or any(c not in "0123456789abcdefghijklmnopqrstuvwxyz." for c in name)
    )


def write_valid_file_names(logs):
    valid_extensions = {".hlm", ".brhl", ".hlm.", ".brhl."}

    with open("output.txt", "w") as output_file:
        for log in logs:
            words = log.split()
            for word in words:
                if is_valid_file_name(word) and word.endswith(tuple(valid_extensions)):
                    output_file.write(word.rstrip(".") + "\n")


with open("input.txt", "r") as input_file:
    input_data = input_file.read().splitlines()

write_valid_file_names(input_data)
