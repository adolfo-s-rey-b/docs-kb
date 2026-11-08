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
 / Distiller model

Distiller model
===============

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distillation/distiller.py#L9)

### `Distiller` class

Copied!

`keras.distillation.Distiller(     teacher,     student,     distillation_losses,     distillation_loss_weights=None,     student_loss_weight=0.5,     name="distiller",     **kwargs )`

Distillation model for transferring knowledge from teacher to student.

Knowledge distillation transfers knowledge from a large, complex model (teacher) to a smaller, simpler model (student). The student learns from both ground truth labels and the teacher's predictions, often achieving better performance than training on labels alone.

**Arguments**

*   **teacher**: A trained [`keras.Model`](https://keras.io/api/models/model#model-class)
     that serves as the knowledge source. The teacher model is frozen during distillation.
*   **student**: A [`keras.Model`](https://keras.io/api/models/model#model-class)
     to be trained through distillation.
*   **distillation\_losses**: List of distillation losses to apply. Can be a single distillation loss or a list of distillation losses like [`keras.distillation.LogitsDistillation`](https://keras.io/api/models/distillation/logits_distillation#logitsdistillation-class)
    , [`keras.distillation.FeatureDistillation`](https://keras.io/api/models/distillation/feature_distillation#featuredistillation-class)
    , or custom distillation losses.
*   **distillation\_loss\_weights**: List of weights for each distillation loss. Must have the same length as `distillation_losses`. If `None`, equal weights are used.
*   **student\_loss\_weight**: Weight for the student's supervised loss component. Must be between 0 and 1. Defaults to 0.5.
*   **name**: Name for the distiller model. Defaults to `"distiller"`.
*   **\*\*kwargs**: Additional keyword arguments passed to the parent `Model` class.

**Attributes**

*   **student**: The student model being trained. Access this to get the trained student model for independent use after distillation training.
*   **teacher**: The teacher model providing knowledge. This model is frozen during training.

**Examples**

Copied!

`# Basic distillation with KerasHub models import keras_hub as hub  teacher = hub.models.CausalLM.from_preset("gemma_2b_en") student = hub.models.CausalLM.from_preset(     "gemma_1.1_2b_en", load_weights=False )  # Single distillation loss distiller = Distiller(     teacher=teacher,     student=student,     distillation_losses=LogitsDistillation(temperature=3.0), )  # Compile the distiller (like any Keras model) distiller.compile(     optimizer='adam',     loss='sparse_categorical_crossentropy',     metrics=['accuracy'] )  # Train the distiller distiller.fit(x_train, y_train, epochs=10)  # Access the trained student model trained_student = distiller.student  # Multiple distillation losses distiller = Distiller(     teacher=teacher,     student=student,     distillation_losses=[         LogitsDistillation(temperature=3.0),         FeatureDistillation(             teacher_layer_name="dense_1",             student_layer_name="dense_1"         )     ],     distillation_loss_weights=[1.0, 0.5], )  # Compile with custom settings distiller.compile(     optimizer='adam',     loss='sparse_categorical_crossentropy',     metrics=['accuracy'] )`

* * *

[Distiller model](https://keras.io/api/models/distillation/distiller/#distiller-model)

[`Distiller` class](https://keras.io/api/models/distillation/distiller/#distiller-class)