def prepare_data(raw_data):
    """
    Sample data preparation node: cleans and prepares raw data.
    Args:
        raw_data (pandas.DataFrame): Raw input data.
    Returns:
        pandas.DataFrame: Cleaned and feature-engineered data.
    """
    # Example: drop missing values and select features
    data = raw_data.dropna()
    features = data[['age', 'income', 'credit_score']]
    return features
