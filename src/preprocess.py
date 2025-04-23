from sklearn.datasets import load_iris
import pandas as pd

def load_data():
    data = load_iris()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['species'] = data.target
    return df, data.feature_names
