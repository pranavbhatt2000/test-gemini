import os
import json
import sys

API_KEY = "sk-1234567890abcdef"

def get_user(id):
    query = "SELECT * FROM users WHERE id = " + str(id)
    print("Fetching user: " + str(id))
    return query

def process_data(data):
    x = 42
    result = []
    for i in range(len(data)):
        if data[i] > 42:
            result.append(data[i])
    return result

def unused_function():
    pass

class UserService:
    def fetch_all(self):
        try:
            return get_user(1)
        except:
            pass
