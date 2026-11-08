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
 / Logits distillation loss

Logits distillation loss
========================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distillation/distillation_loss.py#L260)

### `LogitsDistillation` class

Copied!

`keras.distillation.LogitsDistillation(temperature=3.0, loss="kl_divergence")`

Distillation loss that transfers knowledge from final model outputs.

This distillation loss applies temperature scaling to the teacher's logits before computing the loss between teacher and student predictions. It's the most common approach for knowledge distillation.

**Arguments**

*   **temperature**: Temperature for softmax scaling. Higher values produce softer probability distributions that are easier for the student to learn. Typical values range from 3-5. Defaults to 3.0.
*   **loss**: Loss function to use for distillation. Can be:
    *   String identifier (e.g., 'kl\_divergence', 'categorical\_crossentropy')
    *   Keras loss instance
    *   Nested structure of losses matching the model output structure
    *   `None` to skip distillation for that output (useful for multi-output models where you only want to distill some outputs) At least one loss must be non-`None`. Defaults to 'kl\_divergence'.

Examlpe(s):

Copied!

`# Basic logits distillation with KL divergence distillation_loss = LogitsDistillation(temperature=3.0)  # With categorical crossentropy loss distillation_loss = LogitsDistillation(     temperature=4.0,     loss="categorical_crossentropy" )  # With custom loss instance distillation_loss = LogitsDistillation(     temperature=4.0,     loss=keras.losses.CategoricalCrossentropy(from_logits=True) )  # For multi-output models distillation_loss = LogitsDistillation(     temperature=3.0,     loss=["kl_divergence", "categorical_crossentropy"] )  # For multi-output models, only distill some outputs distillation_loss = LogitsDistillation(     temperature=3.0,     loss=["kl_divergence", None]  # Skip second output )`

* * *

[Logits distillation loss](https://keras.io/api/models/distillation/logits_distillation/#logits-distillation-loss)

[`LogitsDistillation` class](https://keras.io/api/models/distillation/logits_distillation/#logitsdistillation-class)