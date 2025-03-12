from dotenv import load_dotenv
load_dotenv()

import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Create the model with modified settings
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 300,  # Reduced to make responses shorter
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

def generate_response(prompt):
    response = model.generate_content([
    "You are a teaching chatbot with an understanding of all subjects. Your goal is to help students learn concepts clearly. Keep your answers brief and focused.\nYou:\n\nExplain topics concisely but accurately.\nUse simple language and short examples.\nKeep explanations under 3 sentences when possible.\nFocus only on the most important points.",
    "input: who are you",
    "output: I'm a teaching assistant designed to help you learn. I can explain concepts from various subjects in a simple, straightforward way.",
    f'input: {prompt}',
    "output: ",
    ])
    return (response.text)


while True:
    string= str(input("Enter your question: "))
    print("bot : ", generate_response(string))
