import os
import hashlib
import json

def verify_user(username: str, password: str) -> bool:
    """
    Verify username/password against users stored in environment variable
    BASIC_AUTH_USERS format: {"username": "sha256_hash", ...}
    """
    users_json = os.environ.get("BASIC_AUTH_USERS", "{}")

    try:
        users = json.loads(users_json)
    except json.JSONDecodeError:
        return False

    if username not in users:
        return False

    stored_hash = users[username]
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    return stored_hash == password_hash
