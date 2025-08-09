from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key= os.getenv("GOOGLE_API_KEY")
base_url = "https://generativelanguage.googleapis.com/v1beta/openai"
client =OpenAI(base_url=base_url, api_key=api_key)
ai_teacher = "You are an AI teacher"

def ai_chatbot(usermessage, history):
    messages = [{"role": "system", "content": ai_teacher}]
    messages.extend(history)
    messages.append({"role": "user", "content": usermessage})
    response = client.chat.completions.create(model="gemini-2.5-flash", messages=messages)
    return response.choices[0].message.content

if __name__ == "__main__":
    print(ai_chatbot("Hello", []))  
