import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client with Nebius configuration
client = OpenAI(
    base_url="https://api.studio.nebius.ai/v1/",
    api_key=os.environ.get("NEBIUS_API_KEY"),
)

def get_bot_response(user_input):
    try:
        completion = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3.1-70B-Instruct",
            messages=[
                {"role": "user", "content": user_input}
            ],
            temperature=0.6,
            max_tokens=512,
            top_p=0.9
        )
        return completion.choices[0].message.content
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
