import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from joblib import dump

def retrain_model():
    # Load your data for retraining
    data = pd.read_csv("new_training_data.csv")
    X = data.drop('target', axis=1)
    y = data['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Retrain model
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    # Save the updated model
    dump(model, 'finalized_model.pkl')
    print("Model retrained and saved successfully.")
