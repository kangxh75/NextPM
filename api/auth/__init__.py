import azure.functions as func
import json
import base64
from .user_store import verify_user

def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    Basic Auth endpoint
    POST /api/auth with Authorization: Basic <credentials>
    """

    # Get credentials from Authorization header
    auth_header = req.headers.get('Authorization', '')

    if not auth_header.startswith('Basic '):
        return func.HttpResponse(
            json.dumps({"error": "Basic Auth required"}),
            status_code=401,
            headers={
                "WWW-Authenticate": "Basic realm='NextPM'",
                "Content-Type": "application/json"
            }
        )

    # Decode credentials
    try:
        credentials = base64.b64decode(auth_header[6:]).decode('utf-8')
        username, password = credentials.split(':', 1)
    except Exception as e:
        return func.HttpResponse(
            json.dumps({"error": "Invalid credentials format"}),
            status_code=401,
            headers={"Content-Type": "application/json"}
        )

    # Verify credentials
    if verify_user(username, password):
        # Azure Static Web Apps expects specific response format
        return func.HttpResponse(
            json.dumps({
                "userId": username,
                "userRoles": ["authenticated"],
                "claims": []
            }),
            status_code=200,
            headers={
                "Content-Type": "application/json",
                "X-MS-CLIENT-PRINCIPAL": base64.b64encode(
                    json.dumps({
                        "userId": username,
                        "userRoles": ["authenticated"]
                    }).encode()
                ).decode()
            }
        )
    else:
        return func.HttpResponse(
            json.dumps({"error": "Invalid username or password"}),
            status_code=401,
            headers={"Content-Type": "application/json"}
        )
