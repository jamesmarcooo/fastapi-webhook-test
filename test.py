import requests

webhook_url = "https://argental-jadishly-eula.ngrok-free.dev/webhook"

payload = {
    "event": "user.signup",
    "data": {
        "user_id": 123,
        "email": "test@example.com"
    }
}

response = requests.post(webhook_url, json=payload)
print(response.status_code, response.json())