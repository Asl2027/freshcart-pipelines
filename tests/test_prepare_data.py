import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from sklearn.datasets import load_iris
from iris_project.transformers.prepare_data import transform


def test_prepare_data_split():
    df = load_iris(as_frame=True).frame
    result = transform(df)

    assert len(result) == 150
    assert (result['split'] == 'train').sum() == 120
    assert (result['split'] == 'test').sum() == 30
    assert result['split'].notna().all()
