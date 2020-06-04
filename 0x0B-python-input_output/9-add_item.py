#!/usr/bin/python3
""" Adds arguments to a Python list """
import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file

filename = "add_item.json"

try:
    my_list = load_from_json_file(filename)
except:
    my_list = []
for items in sys.argv[1:]:
    my_list.append(items)
save_to_json_file(my_list, filename)
