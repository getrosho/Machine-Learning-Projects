import pandas as pd

def load_mental_health_data():
    path = "../data/raw/Student Mental Health Analysis During Online Learning.csv"
    df = pd.read_csv(path)
    return df