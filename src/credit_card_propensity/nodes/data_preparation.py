def prepare_data(raw_data):
    """
    Data preparation node using Spark DataFrame.
    Args:
        raw_data (pyspark.sql.DataFrame): Raw input Spark DataFrame.
    Returns:
        pyspark.sql.DataFrame: Cleaned and feature-engineered Spark DataFrame.
    """
    # Drop missing values and select features using Spark
    data = raw_data.dropna()
    features = data.select('age', 'income', 'credit_score')
    return features
