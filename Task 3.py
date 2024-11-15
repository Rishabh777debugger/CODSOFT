import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Input, Embedding, LSTM, Dense, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt
import cv2
import os

# Load pre-trained ResNet model
def extract_features(filename):
    model = ResNet50(weights='imagenet', include_top=False, pooling='avg')
    image = load_img(filename, target_size=(224, 224))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = tf.keras.applications.resnet50.preprocess_input(image)
    feature = model.predict(image)
    return feature

# Load the dataset
def load_dataset(directory):
    features = {}
    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            filepath = os.path.join(directory, filename)
            feature = extract_features(filepath)
            features[filename] = feature
    return features

# Define the captioning model
def create_captioning_model(vocab_size, max_length):
    # Image feature input
    inputs1 = Input(shape=(2048,))
    fe1 = Dropout(0.5)(inputs1)
    fe2 = Dense(256, activation='relu')(fe1)

    # Caption input
    inputs2 = Input(shape=(max_length,))
    se1 = Embedding(vocab_size, 256, mask_zero=True)(inputs2)
    se2 = LSTM(256)(se1)

    # Merging the two inputs
    decoder1 = tf.keras.layers.add([fe2, se2])
    decoder2 = Dense(256, activation='relu')(decoder1)
    outputs = Dense(vocab_size, activation='softmax')(decoder2)

    # Create the model
    model = Model(inputs=[inputs1, inputs2], outputs=outputs)
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    return model

# Function to generate captions for an image
def generate_caption(model, photo, tokenizer, max_length):
    in_text = '<start>'
    for _ in range(max_length):
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        sequence = pad_sequences([sequence], maxlen=max_length)
        yhat = model.predict([photo, sequence], verbose=0)
        yhat = np.argmax(yhat)
        word = tokenizer.index_word[yhat]
        if word == '<end>':
            break
        in_text += ' ' + word
    return in_text

# Load dataset
features = load_dataset('path/to/images')  # Change to your image folder
# Assuming you have a tokenizer and caption data already prepared

# Create the model
vocab_size = len(tokenizer.word_index) + 1
max_length = 34  # Example max length of captions
model = create_captioning_model(vocab_size, max_length)

# Train the model
# Assume X1, X2, y are prepared datasets for training
# model.fit([X1, X2], y, epochs=20, verbose=2)

# Generate caption for a new image
filename = 'path/to/new_image.jpg'
photo = extract_features(filename)
caption = generate_caption(model, photo, tokenizer, max_length)
print("Generated Caption:", caption)

# Display the image
img = cv2.imread(filename)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title(caption)
plt.axis('off')
plt.show()
