from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split


def build_svm_model(X_train, y_train):
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('svm', SVC())
    ])

    # Fit the pipeline on the training data
    pipeline.fit(X_train, y_train)

    return pipeline


def predict(model, data_to_predict):
    predictions = model.predict(data_to_predict)
    return predictions


def split_data(X, y):
    return train_test_split(X, y, test_size=0.33, random_state=42)