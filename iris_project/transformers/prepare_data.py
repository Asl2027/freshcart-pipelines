import pandas as pd
from sklearn.model_selection import train_test_split

try:
    from mage_ai.data_preparation.decorators import transformer, test
except ImportError:
    def transformer(func):
        return func

    def test(func):
        return func


@transformer
def transform(df, *args, **kwargs):
    train_df, test_df = train_test_split(
        df,
        test_size=0.3,
        random_state=42,
        stratify=df['target']
    )

    train_df = train_df.copy()
    test_df = test_df.copy()

    train_df['split'] = 'train'
    test_df['split'] = 'test'

    return pd.concat([train_df, test_df]).sort_index()


@test
def test_output(output, *args):
    assert (output['split'] == 'train').sum() == 120
    assert (output['split'] == 'test').sum() == 30
