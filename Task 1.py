import re

def get_response(user_input):
    user_input = user_input.lower() 

    if re.search(r'\b(hello|hi|hey|greetings)\b', user_input):
        return "Hello! How can I assist you today?"
    
    elif re.search(r'\b(how are you|how it going|how do you do)\b', user_input):
        return "I'm just a program, but I'm here to help! How are you doing?"

    elif re.search(r'\b(help|support|assistance)\b', user_input):
        return "Sure! What do you need help with?"

    elif re.search(r'\b(who are you|what are you|tell me about yourself)\b', user_input):
        return "I m a simple chatbot created to assist you. What would you like to know?"

    elif re.search(r'\b(weather|forecast)\b', user_input):
        return "I can't check the weather right now, but you can use a weather app!"

    elif re.search(r'\b(you are great|you are awesome|you are amazing)\b', user_input):
        return "Thank you! I appreciate the compliment!"

    elif re.search(r'\b(confused|don\'t understand|what)\b', user_input):
        return "I understand! Can you rephrase that?"

    elif re.search(r'\b(bye|goodbye|see you|take care)\b', user_input):
        return "Goodbye! Have a wonderful day!"

    elif re.search(r'\b(tell me|give me)\b', user_input):
        return "I can provide information. What topic are you interested in?"

    elif re.search(r'\b(fact|tell me a fact)\b', user_input):
        return "Did you know? Honey never spoils! Archaeologists have found pots of honey in ancient tombs that are over 3000 years old and still perfectly edible."

    elif re.search(r'\b(what do you like|what are your hobbies)\b', user_input):
        return "I dont have personal interests, but I love helping people with their questions!"

    elif re.search(r'\b(recommend|suggest)\b', user_input):
        return "How about discussing books, movies, or hobbies?"

    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

def chat():
    print("Chatbot: Hello! I'm your friendly chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Chatbot:", response)
        if re.search(r'\b(bye|goodbye|see you|take care)\b', user_input):
            break

if __name__ == "__main__":
    chat()
