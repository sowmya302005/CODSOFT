# -----------------------------------------
# CODSOFT - Task 1 : Rule-Based Chatbot
# Created by: Shetty Sowmya
# -----------------------------------------

print("🤖 Hello! I'm ChatBot. Type 'bye' to end the chat.")
print("--------------------------------------------------")

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["hi", "hello", "hey"]:
        print("Bot: Hello there! How can I assist you today?")

    elif "how are you" in user_input:
        print("Bot: I'm doing great! Thanks for asking. What about you?")

    elif "your name" in user_input:
        print("Bot: I'm ChatBot — your friendly virtual assistant 🤖")

    elif "weather" in user_input:
        print("Bot: I can’t check live weather yet, but I hope it’s sunny where you are! ☀️")

    elif "time" in user_input:
        from datetime import datetime
        now = datetime.now()
        print(f"Bot: The current time is {now.strftime('%I:%M %p')}")

    elif "date" in user_input:
        from datetime import date
        today = date.today()
        print(f"Bot: Today’s date is {today.strftime('%B %d, %Y')}")

    elif "joke" in user_input:
        print("Bot: Why did the computer catch a cold? Because it had too many windows open! 😂")

    elif "bye" in user_input or "exit" in user_input:
        print("Bot: Goodbye! Have a great day ahead! 👋")
        break

    else:
        print("Bot: I'm not sure I understand. Can you rephrase that?")
