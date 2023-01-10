#!/usr/bin/python3
""" Advance task module """


def append_after(filename="", search_string="", new_string=""):
    """ search and write a new line """
    text = ""

    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, 'w') as f:
        f.write(text)
