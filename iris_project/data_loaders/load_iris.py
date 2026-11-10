from sklearn.datasets import load_iris as sklearn_load_iris

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader, test

@data_loader
def load_data(*args, **kwargs):
    iris = sklearn_load_iris(as_frame=True)
    return iris.frame

@test
def test_output(output, *args):
    assert len(output) == 150
    assert 'target' in output.columns
