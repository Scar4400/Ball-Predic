from boruta import BorutaPy
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

def extract_features(data):
    data['odds_diff'] = data['home_odds'] - data['away_odds']
    data['goal_diff'] = data['home_goals'] - data['away_goals']
    data['win_probability'] = 1 / data['home_odds']
    data['recent_form'] = (data['home_goals'] + data['away_goals']) / data['total_goals']

    return data

def feature_selection(X, y):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    feat_selector = BorutaPy(model, n_estimators='auto', random_state=42)
    feat_selector.fit(X.values, y)

    selected_features = X.columns[feat_selector.support_].tolist()
    return selected_features
