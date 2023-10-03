#!/usr/bin/python3
# Print the ASCII alphabet, in lowercase, without 'q' and 'e', not followed by a new line.

for char_code in range(ord('a'), ord('z') + 1):
    letter = chr(char_code)
    if letter not in ('q', 'e'):
        print(letter, end='')
