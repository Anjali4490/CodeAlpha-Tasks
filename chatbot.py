# ─────────────────────────────────────────
#  Basic Chatbot — CodeAlpha Internship
#  Task 4: Rule-based chatbot
#  Key Concepts: if-elif, functions, loops, input/output
# ─────────────────────────────────────────


# ─────────────────────────────────────────
#  Response logic — the brain of the bot
# ─────────────────────────────────────────
def get_response(user_input):

    # ── Greetings ──
    if user_input in ["hello", "hi", "hey", "hii", "helo"]:
        return "Hi there! How can I help you today?"

    elif user_input in ["good morning", "morning"]:
        return "Good morning! Hope you have a wonderful day!"

    elif user_input in ["good evening", "evening"]:
        return "Good evening! How's your day been?"

    elif user_input in ["good night", "goodnight"]:
        return "Good night! Sweet dreams!"

    # ── How are you ──
    elif user_input in ["how are you", "how are you?", "how r u", "how do you do"]:
        return "I'm doing great, thanks for asking! What about you?"

    elif user_input in ["i am fine", "i'm fine", "i am good", "i'm good", "doing well"]:
        return "That's wonderful to hear!"

    elif user_input in ["not good", "i am sad", "i'm sad", "not well", "i am bad"]:
        return "Oh no, I'm sorry to hear that. I hope things get better soon!"

    # ── Bot identity ──
    elif user_input in ["what is your name", "what's your name", "your name", "who are you"]:
        return "I'm ByteBot, your friendly chatbot! Nice to meet you."

    elif user_input in ["how old are you", "what is your age", "your age"]:
        return "I was just born when this code was written, so pretty young!"

    elif user_input in ["who made you", "who created you", "who built you"]:
        return "I was built by a CodeAlpha intern using Python. Pretty cool, right?"

    elif user_input in ["are you human", "are you a robot", "are you a bot", "are you real"]:
        return "I'm a bot — but I'm here to help just like a human would!"

    # ── Compliments ──
    elif user_input in ["you are great", "you're great", "you are awesome", "you're awesome", "good bot"]:
        return "Aww, thank you! You're pretty awesome yourself!"

    elif user_input in ["i love you", "i like you"]:
        return "That's so kind! I like you too, friend."

    # ── Help ──
    elif user_input in ["help", "help me", "what can you do", "what do you do"]:
        return (
            "I can chat with you! Try saying:\n"
            "  - hello / hi\n"
            "  - how are you\n"
            "  - what is your name\n"
            "  - tell me a joke\n"
            "  - what time is it\n"
            "  - bye"
        )

    # ── Fun ──
    elif user_input in ["tell me a joke", "joke", "say something funny", "make me laugh"]:
        return "Why do programmers prefer dark mode? Because light attracts bugs! 😄"

    elif user_input in ["tell me a fact", "fun fact", "fact"]:
        return "Fun fact: Python was named after Monty Python, not the snake!"

    elif user_input in ["favourite color", "favorite color", "your colour", "your color"]:
        return "I'd say Python blue — #306998 to be exact!"

    # ── Time & Date ──
    elif user_input in ["what time is it", "current time", "time"]:
        import datetime
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {now}."

    elif user_input in ["what is today", "today's date", "what date is it", "date"]:
        import datetime
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {today}."

    # ── Thanks ──
    elif user_input in ["thank you", "thanks", "thank you so much", "thanks a lot"]:
        return "You're very welcome! Happy to help."

    # ── Default fallback ──
    else:
        return "Hmm, I didn't quite understand that. Type 'help' to see what I can do!"


# ─────────────────────────────────────────
#  Main chatbot loop
# ─────────────────────────────────────────
def run_chatbot():
    print("\n" + "=" * 45)
    print("        Welcome to ByteBot!")
    print("   Your simple rule-based chatbot")
    print("=" * 45)
    print("  Type 'bye' or 'exit' to quit.\n")

    while True:
        # Get user input and clean it
        user_input = input("You: ").strip().lower()

        # Skip empty input
        if not user_input:
            print("ByteBot: Please type something!\n")
            continue

        # Exit condition
        if user_input in ["bye", "exit", "quit", "goodbye", "see you"]:
            print("ByteBot: Goodbye! It was nice talking to you. Take care!")
            print("=" * 45 + "\n")
            break

        # Get and print bot response
        response = get_response(user_input)
        print(f"ByteBot: {response}\n")


# ─────────────────────────────────────────
#  Entry point
# ─────────────────────────────────────────
if __name__ == "__main__":
    run_chatbot()
