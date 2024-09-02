from pycaret.classification import setup, compare_models, tune_model, finalize_model
import pandas as pd

def train_model(features, labels):
    data = pd.concat([features, labels], axis=1)

    clf_setup = setup(data, target='match_outcome', silent=True, verbose=False)

    best_model = compare_models()
    tuned_model = tune_model(best_model)
    finalized_model = finalize_model(tuned_model)

    return finalized_model
