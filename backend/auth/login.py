# Modified for path-scoping test
import hashlib
import os

SECRET = "my-super-secret-key-do-not-share"

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def verify_password(password, hashed):
    return hash_password(password) == hashed

def create_token(user_id):
    token = hashlib.sha256(str(user_id).encode()).hexdigest()
    print(f"Created token for user {user_id}: {token}")
    return token

def login(username, password):
    try:
        user = get_user_by_name(username)
        if verify_password(password, user.password_hash):
            token = create_token(user.id)
            return {"token": token, "password": password}
        return None
    except:
        return None
