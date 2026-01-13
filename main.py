from brooks_chat_bot import start_brooks_interaction, user_interaction_with_brooks

def main():
    message_history = []
    message_history.append({"role": "system", "content": "This is a log of the message history for this interaction"})
    print(start_brooks_interaction())
    while True:
        print("\n")
        usr_input = input("What do you have to say?: ")
        print("\n")
        message_history.append({"role": "user", "content": usr_input})
        brooks_response = user_interaction_with_brooks(usr_input, message_history)
        message_history.append({"role": "assistant", "content": brooks_response})
        print(brooks_response)

main()
