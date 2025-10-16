from fastapi import FastAPI, Request
from pydantic import BaseModel
import logging

app = FastAPI()

# Optional: Setup basic logging
logging.basicConfig(level=logging.INFO)

class WebhookPayload(BaseModel):
    event: str
    data: dict

@app.post("/webhook")
async def webhook_listener(payload: WebhookPayload, request: Request):
    headers = dict(request.headers)
    logging.info("Received webhook with headers: %s", headers)
    logging.info("Received webhook data: %s", payload.model_dump())
    # Do something with the payload (save to DB, trigger a process, etc)
    return {"status": "received"}
