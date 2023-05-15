import pandas as pd


def get_data_set():
    dataset = pd.read_csv("data.csv")
    dataset = factorize_data(dataset)
    return dataset


def factorize_data(dataset):
    dataset['is_offensive'] = dataset['is_offensive'].replace({'OFF': 1, 'NOT': 0})
    return dataset
