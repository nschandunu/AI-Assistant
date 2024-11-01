import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_bot_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    print("AI Chatbot (type 'quit' to exit)")
    print("-" * 50)
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['quit', 'exit']:
            print("Goodbye!")
            break
            
        response = get_bot_response(user_input)
        print(f"Bot: {response}")
        print("-" * 50)

if __name__ == "__main__":
    main()
