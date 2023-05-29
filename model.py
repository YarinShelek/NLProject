from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from bert_sklearn import BertClassifier
from bert_sklearn import load_model


def build_model(X_train, y_train):
    model = BertClassifier(max_seq_length=64, train_batch_size=16, random_state=42, use_cuda=True)
    #model.fit(X_train, y_train)
    savefile = 'mymodel.bin'
    #model.save(savefile)
    model = load_model(savefile)
    """ model = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('svm', SVC())
    ])"""

    """ model = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('rf', RandomForestClassifier())
    ])"""
    """model = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('nb', MultinomialNB())
    ])"""

    return model


def predict(model, data_to_predict):
    predictions = model.predict(data_to_predict)
    return predictions


def split_data(X, y):
    return train_test_split(X, y, test_size=0.33, random_state=42)
