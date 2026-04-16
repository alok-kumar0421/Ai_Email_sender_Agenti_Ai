from agno.agent import Agent
from agno.tools.email import EmailTools
from dotenv import load_dotenv
import os
from agno.models.google import Gemini

load_dotenv()

def send_email(receiver_email, user_name, purpose, extra_details=""):
    sender_passkey = os.getenv("SENDER_PASSKEY")
    google_api_key = os.getenv("GOOGLE_API_KEY")
    sender_email = os.getenv("SENDER_EMAIL")

    agent = Agent(
        model=Gemini(
            id="gemini-3-flash-preview",
            api_key=google_api_key
        ),
        tools=[
            EmailTools(
                receiver_email=receiver_email,
                sender_email=sender_email,
                sender_name=user_name,
                sender_passkey=sender_passkey,
            )
        ],
        instructions="""
You are a professional email assistant.

You MUST send emails using the email tool.

Rules:
- No placeholders like [Name]
- Write clear subject and body
- Keep tone professional
- Adapt email based on purpose
"""
    )

    prompt = f"""
Send a professional email.

Purpose: {purpose}
Sender Name: {user_name}
Additional Details: {extra_details}

Generate a proper subject and body and send the email.
"""

    return agent.run(prompt)