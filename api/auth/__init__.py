import azure.functions as func
import json
import base64
import hashlib
import time
from .user_store import verify_user

def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    Basic Auth endpoint
    POST /api/auth with JSON body: {"username": "...", "password": "..."}
    """

    try:
        req_body = req.get_json()
        username = req_body.get('username', '').strip()
        password = req_body.get('password', '')
    except:
        return func.HttpResponse(
            json.dumps({"success": False, "error": "Invalid request"}),
            status_code=400,
            headers={"Content-Type": "application/json"}
        )

    if not username or not password:
        return func.HttpResponse(
            json.dumps({"success": False, "error": "Username and password required"}),
            status_code=400,
            headers={"Content-Type": "application/json"}
        )

    # Verify credentials
    if verify_user(username, password):
        # Create a simple session token
        session_data = f"{username}:{int(time.time())}"
        session_token = base64.b64encode(session_data.encode()).decode()

        return func.HttpResponse(
            json.dumps({"success": True, "username": username}),
            status_code=200,
            headers={
                "Content-Type": "application/json",
                "Set-Cookie": f"NextPM-Auth={session_token}; Path=/; HttpOnly; Secure; SameSite=Strict; Max-Age=28800"
            }
        )
    else:
        return func.HttpResponse(
            json.dumps({"success": False, "error": "Invalid username or password"}),
            status_code=401,
            headers={"Content-Type": "application/json"}
        )
