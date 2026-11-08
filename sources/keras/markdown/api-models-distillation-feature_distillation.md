None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [The Model class](https://keras.io/api/models/model/)
 [The Sequential class](https://keras.io/api/models/sequential/)
 [Model training APIs](https://keras.io/api/models/model_training_apis/)
 [Saving & serialization](https://keras.io/api/models/model_saving_apis/)
 [Knowledge distillation](https://keras.io/api/models/distillation/)
 [Layers API](https://keras.io/api/layers/)
 [Callbacks API](https://keras.io/api/callbacks/)
 [Ops API](https://keras.io/api/ops/)
 [Optimizers](https://keras.io/api/optimizers/)
 [Metrics](https://keras.io/api/metrics/)
 [Losses](https://keras.io/api/losses/)
 [Data loading](https://keras.io/api/data_loading/)
 [Tree API](https://keras.io/api/tree/)
 [Built-in small datasets](https://keras.io/api/datasets/)
 [Keras Applications](https://keras.io/api/applications/)
 [Mixed precision](https://keras.io/api/mixed_precision/)
 [Multi-device distribution](https://keras.io/api/distribution/)
 [RNG API](https://keras.io/api/random/)
 [Quantizers](https://keras.io/api/quantizers/)
 [Scope](https://keras.io/api/scope/)
 [Rematerialization](https://keras.io/api/rematerialization/)
 [Utilities](https://keras.io/api/utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

► [Keras 3 API documentation](https://keras.io/api/)
 / [Models API](https://keras.io/api/models/)
 / [Knowledge distillation](https://keras.io/api/models/distillation/)
 / Feature distillation loss

Feature distillation loss
=========================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distillation/distillation_loss.py#L86)

### `FeatureDistillation` class

Copied!

`keras.distillation.FeatureDistillation(     loss="mse", teacher_layer_name=None, student_layer_name=None )`

Feature distillation loss.

Feature distillation transfers knowledge from intermediate layers of the teacher model to corresponding layers of the student model. This approach helps the student learn better internal representations and often leads to better performance compared to logits-only distillation.

**Arguments**

*   **loss**: Loss function to use for feature distillation. Can be:
    *   String identifier (e.g., 'mse', 'cosine\_similarity', 'mae')
    *   Keras loss instance
    *   Nested structure of losses matching the layer output structure
    *   `None` to skip distillation for that output (useful for multi-output models where you only want to distill some outputs) At least one loss must be non-`None`. Defaults to 'mse'.
*   **teacher\_layer\_name**: Name of the teacher layer to extract features from. If `None`, uses the final output. Defaults to `None`.
*   **student\_layer\_name**: Name of the student layer to extract features from. If `None`, uses the final output. Defaults to `None`.

Examlpe(s):

Copied!

`# Basic feature distillation from final outputs distillation_loss = FeatureDistillation(loss="mse")  # Distill from specific intermediate layers distillation_loss = FeatureDistillation(     loss="mse",     teacher_layer_name="dense_1",     student_layer_name="dense_1" )  # Use cosine similarity for different feature sizes distillation_loss = FeatureDistillation(     loss="cosine_similarity",     teacher_layer_name="conv2d_2",     student_layer_name="conv2d_1" )  # With custom loss instance distillation_loss = FeatureDistillation(     loss=keras.losses.MeanAbsoluteError() )  # For multi-output models distillation_loss = FeatureDistillation(     loss=["mse", "cosine_similarity"] )  # For multi-output models, only distill some outputs distillation_loss = FeatureDistillation(     loss=["mse", None, "cosine_similarity"]  # Skip middle output )`

* * *

[Feature distillation loss](https://keras.io/api/models/distillation/feature_distillation/#feature-distillation-loss)

[`FeatureDistillation` class](https://keras.io/api/models/distillation/feature_distillation/#featuredistillation-class)