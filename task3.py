# Simple rule-based chatbot

def get_reply(user_message):
    # Convert message to lowercase so comparisons are easier
    user_message = user_message.lower()

    # Basic rules using if/elif
    if user_message == "hello":
        return "Hi!"
    elif user_message == "how are you":
        return "I'm fine, thanks!"
    elif user_message == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."


def main():
    print("Simple Chatbot")
    print("Type 'bye' to exit")
    print("-----------------")

    while True:
        user_input = input("You: ")

        # Get bot response
        bot_reply = get_reply(user_input)
        print("Bot:", bot_reply)

        # Exit if user says bye
        if user_input.lower() == "bye":
            break


# Run the program
main()
