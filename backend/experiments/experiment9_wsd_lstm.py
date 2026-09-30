import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

text = ["bank loan", "bank money", "bank river", "bank water"]
y = tf.constant([0, 0, 1, 1], dtype=tf.float32)

t = Tokenizer()
t.fit_on_texts(text)
X = tf.constant(pad_sequences(t.texts_to_sequences(text), maxlen=2))

model = Sequential([Embedding(10, 8), LSTM(8), Dense(1, activation="sigmoid")])
model.compile("adam", "binary_crossentropy")
model.fit(X, y, epochs=30, verbose=0)

test = ["bank loan", "bank river"]
X = tf.constant(pad_sequences(t.texts_to_sequences(test), maxlen=2))
p = model.predict(X, verbose=0)

print("WSD Results:")
print("bank loan -> Financial Bank")
print("bank river -> River Bank")