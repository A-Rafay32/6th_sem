# https://www.kaggle.com/models/dilshananurada/spam_detection?select=spam_model.h5

import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model



# Load your dataset
data = pd.read_csv('/content/Spam-Classification.csv')
messages = data['SMS']
classes = data['CLASS']

# Tokenize and pad the messages
tokenizer = Tokenizer(num_words=10000)
tokenizer.fit_on_texts(messages)
sequences = tokenizer.texts_to_sequences(messages)


# Check the maximum length of sequences
max_len = max(len(seq) for seq in sequences)
print("Maximum sequence length in dataset:", max_len) 



# Pad sequences to the fixed length required by the model (4566)
padded_sequences = pad_sequences(sequences, maxlen=4566)

# Load the pre-trained model
model = load_model('spam_model.h5')

# Check model's input shape
print("Model input shape:", model.input_shape)

# Test the model
sample_message = ["(Bank of Granite issues Strong-Buy) EXPLOSIVE PICK FOR OUR MEMBERS *****UP OVER 300% *********** Nasdaq Symbol CDGT That is a $5.00 per."]
sample_sequence = tokenizer.texts_to_sequences(sample_message)
padded_sample_sequence = pad_sequences(sample_sequence, maxlen=4566)

# Check the shape of the sample sequence
print("Sample sequence shape:", padded_sample_sequence.shape)

# Predict using the model
prediction = model.predict(padded_sample_sequence)
print('Spam Probability:' , prediction[0][1] )

