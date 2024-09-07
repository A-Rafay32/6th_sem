import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Predefined responses
responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! What can I do for you?",
    "how are you": "I'm just a bunch of code, but I'm here to assist you!",
    "bye": "Goodbye! Have a great day!",
}

# Function to preprocess user input
def preprocess_input(user_input):
    # Tokenize the input
    tokens = word_tokenize(user_input.lower())
    # Remove stopwords
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    # Lemmatize the tokens
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return tokens

# Function to get a response from the chatbot
def get_response(user_input):
    tokens = preprocess_input(user_input)
    for token in tokens:
        if token in responses:
            return responses[token]
    return "I'm sorry, I don't understand that."

# Chatbot loop
def chatbot():
    print("Hi! I'm a simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

# Start the chatbot
chatbot()
