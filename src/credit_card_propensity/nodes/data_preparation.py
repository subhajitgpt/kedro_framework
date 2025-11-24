
def prepare_data(raw_data):
    """
    Data preparation node using Spark DataFrame.
    """
    data = raw_data.dropna()
    features = data.select('age', 'income', 'credit_score')
    return features

def create_target_variable(data):
    """
    Create target variable (e.g., propensity to buy).
    """
    from pyspark.sql.functions import when
    # Example: create binary target based on credit_score
    data = data.withColumn('target', when(data['credit_score'] > 700, 1).otherwise(0))
    return data

def feature_selection(data):
    """
    Feature selection based on feature importance (dummy example).
    """
    # For illustration, select top features
    selected = data.select('age', 'income', 'credit_score', 'target')
    return selected

def standard_scaler(data):
    """
    Standard scaling of features.
    """
    from pyspark.ml.feature import VectorAssembler, StandardScaler
    assembler = VectorAssembler(inputCols=['age', 'income', 'credit_score'], outputCol='features_vec')
    assembled = assembler.transform(data)
    scaler = StandardScaler(inputCol='features_vec', outputCol='scaled_features', withMean=True, withStd=True)
    scaled = scaler.fit(assembled).transform(assembled)
    return scaled

def scoring(data, model):
    """
    Score data using trained model (dummy for illustration).
    """
    # In real case, use model.transform(data)
    # Here, just add a dummy score column
    from pyspark.sql.functions import rand
    scored = data.withColumn('score', rand())
    return scored

def lead_generation(scored_data):
    """
    Generate leads based on score threshold.
    """
    leads = scored_data.filter(scored_data['score'] > 0.8)
    return leads
