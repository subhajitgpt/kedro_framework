from kedro.pipeline import Pipeline, node
from credit_card_propensity.nodes.data_preparation import (
    prepare_data, create_target_variable, feature_selection, standard_scaler, scoring, lead_generation
)
from credit_card_propensity.nodes.ml_model import train_model, accuracy_metrics, model_inference

credit_card_propensity_pipeline = Pipeline([
    node(
        func=prepare_data,
        inputs="raw_data",
        outputs="prepared_data",
        name="data_preparation_node"
    ),
    node(
        func=create_target_variable,
        inputs="prepared_data",
        outputs="data_with_target",
        name="create_target_variable_node"
    ),
    node(
        func=feature_selection,
        inputs="data_with_target",
        outputs="selected_features",
        name="feature_selection_node"
    ),
    node(
        func=standard_scaler,
        inputs="selected_features",
        outputs="scaled_features",
        name="standard_scaler_node"
    ),
    node(
        func=train_model,
        inputs="scaled_features",
        outputs="trained_model",
        name="ml_model_node"
    ),
    node(
        func=accuracy_metrics,
        inputs=dict(model="trained_model", X="scaled_features", y="selected_features.target"),
        outputs="metrics",
        name="accuracy_metrics_node"
    ),
    node(
        func=model_inference,
        inputs=dict(model="trained_model", X="scaled_features"),
        outputs="predictions",
        name="model_inference_node"
    ),
    node(
        func=scoring,
        inputs=["scaled_features", "trained_model"],
        outputs="scored_data",
        name="scoring_node"
    ),
    node(
        func=lead_generation,
        inputs="scored_data",
        outputs="leads",
        name="lead_generation_node"
    )
])
