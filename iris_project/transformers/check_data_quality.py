if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer, test

@transformer
def check_data_quality(df, *args, **kwargs):
    assert df.isnull().sum().sum() == 0, 'Dataset contains missing values'
    assert df['target'].nunique() == 3, 'Expected exactly 3 classes'

    print('Data quality check passed!')
    return df

@test
def test_data_quality(output, *args):
    assert output.isnull().sum().sum() == 0
    assert output['target'].nunique() == 3
