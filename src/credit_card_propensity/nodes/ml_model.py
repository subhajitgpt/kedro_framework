def train_model(prepared_data):
    """
    Sample machine learning node: trains a simple classifier.
    Args:
        prepared_data (pandas.DataFrame): Feature-engineered data.
    Returns:
        object: Trained model (dummy for example).
    """
    from sklearn.linear_model import LogisticRegression
    import numpy as np
    # Dummy target for illustration
    y = np.random.randint(0, 2, size=len(prepared_data))
    model = LogisticRegression()
    model.fit(prepared_data, y)
    return model
