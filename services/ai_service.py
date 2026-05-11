# # import requests

# # OLLAMA_URL = "http://localhost:11434/api/generate"


# # def ask_llm(prompt: str):

# #     payload = {
# #         "model": "llama3",
# #         "prompt": prompt,
# #         "stream": False
# #     }

# #     response = requests.post(OLLAMA_URL, json=payload)

# #     data = response.json()

# #     return data["response"]


# import requests

# OLLAMA_URL = "http://localhost:11434/api/generate"


# def ask_llm(prompt: str):

#     try:
#         response = requests.post(
#             OLLAMA_URL,
#             json={
#                 "model": "llama3",
#                 "prompt": prompt,
#                 "stream": False
#             }
#         )

#         data = response.json()

#         return data.get("response", "")

#     except Exception as e:
#         return f"AI ERROR: {str(e)}"

# import os
# import google.generativeai as genai
# from dotenv import load_dotenv

# load_dotenv()

# genai.configure(
#     api_key=os.getenv("GEMINI_API_KEY")
# )

# # model = genai.GenerativeModel("gemini-1.5-flash")
# model = genai.GenerativeModel("gemini-2.0-flash")

# def ask_llm(prompt: str):

#     try:

#         response = model.generate_content(prompt)

#         return response.text

#     except Exception as e:

#         return f"AI ERROR: {str(e)}"


import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def ask_llm(prompt: str):

    try:

        chat_completion = client.chat.completions.create(

            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],

            model="llama-3.1-8b-instant",

            temperature=0.4,

            max_tokens=2000
        )

        return (
            chat_completion
            .choices[0]
            .message
            .content
        )

    except Exception as e:

        return f"AI ERROR: {str(e)}"