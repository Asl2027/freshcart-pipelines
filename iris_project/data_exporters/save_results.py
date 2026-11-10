if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

@data_exporter
def export_data(df, *args, **kwargs):
    output_file = 'iris_predictions.csv'

    df.to_csv(output_file, index=False)

    print(f"Saved {len(df)} predictions to {output_file}")
