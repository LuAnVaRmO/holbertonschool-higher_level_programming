#!/usr/bin/python3
def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    current = -1
    for letter in range(0, len(text)):
        if text[letter] in [".", "?", ":"]:
            print(text[current + 1: letter + 1])
            print()
            current = letter + 1
