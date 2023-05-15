import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def pre_process_text(text):
    # Remove special characters and punctuation
    text = re.sub(r'[^\w\s]', '', text)

    # Convert text to lowercase
    text = text.lower()

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    filtered_text = [word for word in tokens if word not in stop_words]

    # Join the words back into a single string
    preprocessed_text = ' '.join(filtered_text)

    return preprocessed_text
