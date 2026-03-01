import os
import re
import json
import datetime

def read_file(filepath):
    f = open(filepath, "r")
    content = f.read()
    f.close()
    return content

def format_name(first, last):
    return "%s %s" % (first, last)

def calculate_discount(price, discount):
    return price - price * discount / 100

temp = None
