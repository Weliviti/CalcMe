#
from sklearn.linear_model import LogisticRegression

def train_model(df):
    if df.empty:
        return None  # No data to train yet
    X = df[["num1","num2"]]       # Features: the two numbers
    y = df["correct"]             # Label: 0 or 1
    model = LogisticRegression()
    model.fit(X, y)
    return model
