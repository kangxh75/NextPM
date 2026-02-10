#!/usr/bin/env python3
"""Add users to Basic Auth configuration"""
import hashlib
import json
import sys

def add_user(username, password, users_file="users.json"):
    """Add user to Basic Auth users file"""
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    try:
        with open(users_file, 'r') as f:
            users = json.load(f)
    except FileNotFoundError:
        users = {}

    users[username] = password_hash

    with open(users_file, 'w') as f:
        json.dump(users, f, indent=2)

    print(f"User '{username}' added successfully")
    print(f"\nCopy this JSON to Azure Static Web App Configuration")
    print(f"Setting name: BASIC_AUTH_USERS")
    print(f"Value:\n{json.dumps(users)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python add_user.py <username> <password>")
        sys.exit(1)

    add_user(sys.argv[1], sys.argv[2])
