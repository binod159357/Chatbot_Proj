from nlp1 import clean_text

def get_response(user_input):
    words = clean_text(user_input)
    user_input = user_input.lower()

    # RULE-BASED LOGIC
    if any(w in words for w in ["hello", "hi", "hey"]):
        return "Hello! How can I assist you today?"
    elif "how are you" in words:
        return "I’m doing great, thanks for asking!"
    elif "weather" in words:
        return "I can’t check live weather, but it’s always sunny in my code 😄"
    elif "name" in words:
        return "I’m your friendly Python chatbot!"
    elif "bye" in words:
        return "Goodbye! Have a nice day!"
    else:
        return "Hmm... I’m not sure I understand that yet."


    # if "hello" in user_input or "hi" in user_input or "hey" in user_input or "Good Morning" in user_input or "Good afternoon" in user_input or "good evening" in user_input:
    #     return "Hello there! How can I help you today?"

    # elif "how are you" in user_input:
    #     return "I'm just a bunch of code, but I'm doing great! How about you?"

    # elif "your name" in user_input:
    #     return "I'm ChatPy, your friendly Python chatbot!"

    # elif "weather" in user_input:
    #     return "I can't check the weather right now, but you can look outside 😉"

    # elif "bye" in user_input or "exit" in user_input:
    #     return "Goodbye! Have a great day!"

    # else:
    #     return "I'm not sure I understand. Can you rephrase that?"