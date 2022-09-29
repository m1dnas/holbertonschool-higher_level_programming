#!/usr/bin/python3
"""
Task 7 module: Load, add, save
"""
import json
import sys
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
args = sys.argv[1:]
new_list = []

if os.path.exists(filename):
    new_list = load_from_json_file(filename)

for item in args:
    new_list.append(item)
save_to_json_file(new_list, filename)
