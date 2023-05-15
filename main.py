import pandas as pd

from pre_proccessing import pre_process_text
from model import build_svm_model, predict, split_data
from evaluate import evaluate_model
import utils as util


def main_flow():
    dataset = util.get_data_set()
    for index, row in dataset.iterrows():
        dataset.at[index, 'text'] = pre_process_text(row['text'])
    X_train, X_test, y_train, y_test = split_data(dataset["text"], dataset["is_offensive"])

    model = build_svm_model(X_train, y_train)
    predictions = predict(model, X_test)
    evaluate_model(y_test, predictions)


def gui_main_flow():
    dataset = util.get_data_set()
    for index, row in dataset.iterrows():
        dataset.at[index, 'text'] = pre_process_text(row['text'])
    X_train, X_test, y_train, y_test = split_data(dataset["text"], dataset["is_offensive"])

    model = build_svm_model(X_train, y_train)
    return model


if __name__ == "__main__":
    main_flow()
