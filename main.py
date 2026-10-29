import os
import requests

# WhatsApp Credentials - GitHub Secrets lo nundi vastundi
WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")
RECIPIENT_NUMBER = os.getenv("RECIPIENT_NUMBER") # Nee number with country code: 919876543210

def send_whatsapp_message():
    if not WHATSAPP_TOKEN or not PHONE_NUMBER_ID or not RECIPIENT_NUMBER:
        print("ERROR: Secrets missing! Check WHATSAPP_TOKEN, PHONE_NUMBER_ID, RECIPIENT_NUMBER")
        return

    url = f"https://graph.facebook.com/v20.0/{PHONE_NUMBER_ID}/messages"
    
    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }

    message_body = """🔥 *ANANTAPUR STUDY BUDDY* 🔥

📚 *Today's Current Affairs - TEST SUCCESS!*

KING! WhatsApp Bot 100% Working! ✅

From Tomorrow Daily 6 AM Auto Message Vastundi!

Share with Friends!

#Anantapur #APPSC #StudyBuddy"""

    data = {
        "messaging_product": "whatsapp",
        "to": RECIPIENT_NUMBER,
        "type": "text",
        "text": {"body": message_body}
    }

    response = requests.post(url, headers=headers, json=data)
    print(response.json())
    
    if response.status_code == 200:
        print("SUCCESS KING! WhatsApp Message Sent!")
    else:
        print(f"FAILED: {response.text}")

if __name__ == "__main__":
    send_whatsapp_message()
