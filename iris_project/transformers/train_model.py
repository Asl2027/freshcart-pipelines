import pickle
from sklearn.tree import DecisionTreeClassifier

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer, test

@transformer
def train_model(df, *args, **kwargs):
    train_df = df[df['split'] == 'train'].copy()
    test_df = df[df['split'] == 'test'].copy()

    feature_cols = [
        'sepal length (cm)',
        'sepal width (cm)',
        'petal length (cm)',
        'petal width (cm)'
    ]

    X_train = train_df[feature_cols]
    y_train = train_df['target']

    X_test = test_df[feature_cols]

    max_depth = kwargs.get('max_depth', 3)

    model = DecisionTreeClassifier(
        max_depth=max_depth,
        random_state=42
    )

    model.fit(X_train, y_train)

    test_df['predicted'] = model.predict(X_test)

    with open('iris_model.pkl', 'wb') as f:
        pickle.dump(model, f)

    print(f"Train rows: {len(train_df)} | Test rows: {len(test_df)}")
    print(f"max_depth = {max_depth}")

    return test_df

@test
def test_output(output, *args):
    assert len(output) == 30
    assert 'predicted' in output.columns
