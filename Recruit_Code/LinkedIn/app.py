import os, json, requests
from flask import Flask, redirect, request, render_template
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
SCOPE = os.getenv("SCOPE")
STATE = "xyz_secure_state"

# Load users from JSON
with open("users.json") as f:
    USERS = json.load(f)

TOKENS = {}

@app.route("/connect/<user_id>")
def connect(user_id):
    if user_id not in USERS:
        return "User not found", 404

    auth_url = (
        f"https://www.linkedin.com/oauth/v2/authorization"
        f"?response_type=code"
        f"&client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        f"&scope={SCOPE}"
        f"&state={user_id}"
    )
    return render_template("connect.html", auth_url=auth_url)

@app.route("/callback")
def callback():
    code = request.args.get("code")
    user_id = request.args.get("state")  # passed earlier

    if not code or not user_id:
        return "Invalid request", 400

    token_url = "https://www.linkedin.com/oauth/v2/accessToken"
    token_data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }

    token_response = requests.post(token_url, data=token_data)
    access_token = token_response.json().get("access_token")

    if not access_token:
        return "Failed to get access token", 400

    # Step 2: Request authorization ID
    headers = {
        "Authorization": f"Bearer {access_token}",
        "LinkedIn-Version": "202312",
        "Content-Type": "application/json"
    }

    authz_payload = {
        "clientApplicationId": CLIENT_ID,
        "memberConsent": {
            "purpose": "To import your LinkedIn profile"
        }
    }

    authz_response = requests.post("https://api.linkedin.com/rest/memberAuthorizations",
                                   json=authz_payload, headers=headers)
    authz_data = authz_response.json()
    authorization_id = authz_data.get("authorizationId")

    if not authorization_id:
        return f"Authorization failed: {authz_data}", 400

    # Step 3: Retrieve profile snapshot
    snapshot_url = f"https://api.linkedin.com/rest/memberSnapshotData?q=criteria&authorizationId={authorization_id}"
    snapshot_response = requests.get(snapshot_url, headers=headers)

    if snapshot_response.status_code != 200:
        return f"Snapshot error: {snapshot_response.text}", 400

    profile_data = snapshot_response.json()

    # Store for terminal display
    TOKENS[user_id] = profile_data
    terminal_display(user_id)

    return f"✅ Profile for {user_id} imported. Check terminal!"

def terminal_display(user_id):
    print("\n\n========== LINKEDIN PROFILE ==========")
    profile = TOKENS.get(user_id, {})
    
    # You can customize the fields here:
    for section in ["experience", "education", "skills", "certifications"]:
        print(f"\n>> {section.upper()}")
        for item in profile.get(section, []):
            print(f"  - {item}")

if __name__ == "__main__":
    app.run(debug=True)
