from kedro.pipeline import Pipeline, node
from credit_card_propensity.nodes.data_preparation import prepare_data
from credit_card_propensity.nodes.ml_model import train_model

credit_card_propensity_pipeline = Pipeline([
    node(
        func=prepare_data,
        inputs="raw_data",
        outputs="prepared_data",
        name="data_preparation_node"
    ),
    node(
        func=train_model,
        inputs="prepared_data",
        outputs="trained_model",
        name="ml_model_node"
    )
])
