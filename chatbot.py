import nltk
import spacy
import random
from nltk.chat.util import Chat, reflections

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Define chatbot responses
pairs = [
    [r"hi|hello|hey", ["Hello! How can I assist you today?", "Hi there! How can I help you?"]],
    [r"(.*) your name(.*)", ["I'm an AI chatbot created by CodTech.", "You can call me CodTech Bot!"]],
    [r"how are you", ["I'm just a bot, but I'm here to help!", "I'm doing great! How about you?"]],
    [r"(.*) help (.*)", ["Sure! What do you need help with?", "I'm here to assist you. Please provide more details."]],
    [r"bye|goodbye", ["Goodbye! Have a great day!", "See you later!"]],
    [r"(.*)", ["I'm not sure about that. Can you rephrase your question?", "Could you clarify your query?"]]
]

# Initialize chatbot
chatbot = Chat(pairs, reflections)

def chatbot_response(user_input):
    """Process user input with NLP and generate a response."""
    doc = nlp(user_input)
    response = chatbot.respond(user_input)
    return response if response else "I'm not sure how to answer that."

# Main chat loop
def chat():
    print("CodTech Chatbot: Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("CodTech Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print(f"CodTech Chatbot: {response}")

if name == "main":
    chat()
