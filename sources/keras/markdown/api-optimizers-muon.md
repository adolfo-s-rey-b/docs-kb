None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [Layers API](https://keras.io/api/layers/)
 [Callbacks API](https://keras.io/api/callbacks/)
 [Ops API](https://keras.io/api/ops/)
 [Optimizers](https://keras.io/api/optimizers/)
 [SGD](https://keras.io/api/optimizers/sgd/)
 [RMSprop](https://keras.io/api/optimizers/rmsprop/)
 [Adam](https://keras.io/api/optimizers/adam/)
 [AdamW](https://keras.io/api/optimizers/adamw/)
 [Adadelta](https://keras.io/api/optimizers/adadelta/)
 [Adagrad](https://keras.io/api/optimizers/adagrad/)
 [Adamax](https://keras.io/api/optimizers/adamax/)
 [Adafactor](https://keras.io/api/optimizers/adafactor/)
 [Nadam](https://keras.io/api/optimizers/Nadam/)
 [Ftrl](https://keras.io/api/optimizers/ftrl/)
 [Lion](https://keras.io/api/optimizers/lion/)
 [Lamb](https://keras.io/api/optimizers/lamb/)
 [Loss Scale Optimizer](https://keras.io/api/optimizers/loss_scale_optimizer/)
 [MultiOptimizer](https://keras.io/api/optimizers/multi_optimizer/)
 [OptimizerMap](https://keras.io/api/optimizers/optimizer_map/)
 [Learning rate schedules API](https://keras.io/api/optimizers/learning_rate_schedules/)
 [Muon](https://keras.io/api/optimizers/muon/)
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
 / [Optimizers](https://keras.io/api/optimizers/)
 / Muon

Muon
====

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/muon.py#L8)

### `Muon` class

Copied!

`keras.optimizers.Muon(     learning_rate=0.001,     adam_beta_1=0.9,     adam_beta_2=0.999,     adam_weight_decay=0.004,     epsilon=1e-07,     weight_decay=0.004,     clipnorm=None,     clipvalue=None,     global_clipnorm=None,     use_ema=False,     ema_momentum=0.99,     ema_overwrite_frequency=None,     loss_scale_factor=None,     gradient_accumulation_steps=None,     name=None,     exclude_layers=None,     exclude_embeddings=True,     muon_a=3.4445,     muon_b=-4.775,     muon_c=2.0315,     adam_lr_ratio=1,     momentum=0.95,     ns_steps=5,     nesterov=True,     rms_rate=0.2,     **kwargs )`

Optimizer that implements the Muon algorithm.

Note that this optimizer should not be used in the following layers:

1.  Embedding layer
2.  Final output fully connected layer
3.  Any {0,1}-D variables

These should all be optimized using AdamW.

The Muon optimizer can use both the Muon update step or the AdamW update step based on the following:

*   For any variable that isn't 2D, the AdamW step will be used. This is not configurable.
*   If the argument `exclude_embeddings` (defaults to `True`) is set to `True`, the AdamW step will be used.
*   For any variablewith a name that matches an expression listed in the argument `exclude_layers` (a list), the AdamW step will be used.
*   Any other variable uses the Muon step.

Typically, you only need to pass the name of your densely-connected output layer to `exclude_layers`, e.g. `exclude_layers=["output_dense"]`.

**References**

*   [Original implementation](https://github.com/KellerJordan/Muon)
     - [Liu et al, 2025](https://arxiv.org/abs/2502.16982)
    

**Arguments**

*   **learning\_rate**: A float, [`keras.optimizers.schedules.LearningRateSchedule`](https://keras.io/api/optimizers/learning_rate_schedules/learning_rate_schedule#learningrateschedule-class)
     instance, or a callable that takes no arguments and returns the actual value to use. The learning rate. Defaults to `0.001`.
*   **adam\_beta\_1**: A float value or a constant float tensor, or a callable that takes no arguments and returns the actual value to use. The exponential decay rate for the 1st moment estimates. Defaults to `0.9`.
*   **adam\_beta\_2**: A float value or a constant float tensor, or a callable that takes no arguments and returns the actual value to use. The exponential decay rate for the 2nd moment estimates. Defaults to `0.999`.
*   **adam\_weight\_decay**: Float. If set, weight decay is applied when using the Adam optimizer.
*   **epsilon**: A small constant for numerical stability. This is "epsilon hat" in the Kingma and Ba paper (in the formula just before Section 2.1), not the epsilon in Algorithm 1 of the paper. It be used at Adamw.Defaults to `1e-7`.
*   **exclude\_layers**: List of strings, keywords of layer names to exclude. All layers with keywords in their path will use adamw.
*   **exclude\_embeddings**: Boolean value If True, embedding layers will use adamw.
*   **muon\_a**: Float, parameter a of the muon algorithm. It is recommended to use the default value
*   **muon\_b**: Float, parameter b of the muon algorithm. It is recommended to use the default value
*   **muon\_c**: Float, parameter c of the muon algorithm. It is recommended to use the default value
*   **adam\_lr\_ratio**: Float, the ratio of the learning rate when using Adam to the main learning rate. It is recommended to set it to 1
*   **momentum**: Float, momentum used by internal SGD.
*   **ns\_steps**: Integer, number of Newton-Schulz iterations to run.
*   **nesterov**: Boolean, whether to use Nesterov-style momentum {{base\_optimizer\_keyword\_args}}
*   **rms\_rate**: Float. A parameter from https://arxiv.org/abs/2502.16982 that can enhance the stability of Muon, allowing it to use the same learning rate and weight decay as Adam. Defaults to `0.2`. Set to `None` to disable this feature.

* * *

[Muon](https://keras.io/api/optimizers/muon/#muon)

[`Muon` class](https://keras.io/api/optimizers/muon/#muon-class)