import os
import google.generativeai as genai

# load API Key.
API_KEY = os.getenv("GENAI_API_KEY")
if not API_KEY:
    raise SystemExit(
        "GENAI_API_KEY not set."
    )

genai.configure(api_key=API_KEY)

# choose your model to work with.
model = genai.GenerativeModel("gemini-2.0-flash")

chat = model.start_chat()

print("Chat with Vidya! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Exiting chat. Goodbye!")
        break

    response = chat.send_message(user_input)
    print("Vidya: ", response.text)