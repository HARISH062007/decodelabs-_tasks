print("🤖 AI Chatbot Started!")
print("Type 'exit' to end the conversation.\n")

responses = {
    "hello": "Hi there!",
    "hi": "Hello!",
    "hey": "Hey! How can I help you?",
    "what is ai": "AI stands for Artificial Intelligence.",
    "your name": "I am a Rule-Based AI Chatbot."
}

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["exit", "bye", "quit"]:
        print("Bot: Goodbye! Have a great day.")
        break
    
    elif user_input == "help":
        print("Bot: Try saying hello, hi, hey, or ask about AI.")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day.")
        
    elif "how are you" in user_input:
        print("Bot: I am functioning perfectly. Thanks for asking!")
        
    elif "weather" in user_input:
        print("Bot: It's already a nice weather now.")
        
    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"Bot: Current time is {current_time}")
        
    else:
        # Uses .get() for response lookup
        reply = responses.get(
            user_input,
            "I do not understand that command."
        )
        print("Bot:", reply)