#!/usr/bin/python3
"""
text_indentation
this function put 2 \n before found delimiter[".", "?", ":"]
text formatted
"""


def text_indentation(text):
    """
    :param text: text without format
    :return: text with format
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    aux = 0
    for letter in text:
        if aux == 1 and letter == ' ':
            aux = 0
            pass
        else:
            print(letter, end="")
            aux = 0
            if letter in [".", "?", ":"]:
                print("\n")
                aux = 1
