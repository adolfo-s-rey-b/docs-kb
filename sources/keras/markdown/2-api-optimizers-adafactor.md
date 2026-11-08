None

[Keras 3 API documentation](https://keras.io/api/)
 [Keras 2 API documentation](https://keras.io/2/api/)

[Models API](https://keras.io/2/api/models/)
 [Layers API](https://keras.io/2/api/layers/)
 [Callbacks API](https://keras.io/2/api/callbacks/)
 [Optimizers](https://keras.io/2/api/optimizers/)
 [SGD](https://keras.io/2/api/optimizers/sgd/)
 [RMSprop](https://keras.io/2/api/optimizers/rmsprop/)
 [Adam](https://keras.io/2/api/optimizers/adam/)
 [AdamW](https://keras.io/2/api/optimizers/adamw/)
 [Adadelta](https://keras.io/2/api/optimizers/adadelta/)
 [Adagrad](https://keras.io/2/api/optimizers/adagrad/)
 [Adamax](https://keras.io/2/api/optimizers/adamax/)
 [Adafactor](https://keras.io/2/api/optimizers/adafactor/)
 [Nadam](https://keras.io/2/api/optimizers/Nadam/)
 [Ftrl](https://keras.io/2/api/optimizers/ftrl/)
 [Learning rate schedules API](https://keras.io/2/api/optimizers/learning_rate_schedules/)
 [Metrics](https://keras.io/2/api/metrics/)
 [Losses](https://keras.io/2/api/losses/)
 [Data loading](https://keras.io/2/api/data_loading/)
 [Built-in small datasets](https://keras.io/2/api/datasets/)
 [Keras Applications](https://keras.io/2/api/applications/)
 [Mixed precision](https://keras.io/2/api/mixed_precision/)
 [Utilities](https://keras.io/2/api/utils/)

► [Keras 2 API documentation](https://keras.io/2/api/)
 / [Optimizers](https://keras.io/2/api/optimizers/)
 / Adafactor

Adafactor
=========

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/optimizers/adafactor.py#L27)

### `Adafactor` class

Copied!

`tf_keras.optimizers.Adafactor(     learning_rate=0.001,     beta_2_decay=-0.8,     epsilon_1=1e-30,     epsilon_2=0.001,     clip_threshold=1.0,     relative_step=True,     weight_decay=None,     clipnorm=None,     clipvalue=None,     global_clipnorm=None,     use_ema=False,     ema_momentum=0.99,     ema_overwrite_frequency=None,     jit_compile=True,     name="Adafactor",     **kwargs )`

Optimizer that implements the Adafactor algorithm.

Adafactor is commonly used in NLP tasks, and has the advantage of taking less memory because it only saves partial information of previous gradients.

The default argument setup is based on the original paper (see reference). When gradients are of dimension > 2, Adafactor optimizer will delete the last 2 dimensions separately in its accumulator variables.

**Arguments**

*   **learning\_rate**: Initial value for the learning rate: either a floating point value, or a [`tf.keras.optimizers.schedules.LearningRateSchedule`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/LearningRateSchedule)
     instance. Defaults to 0.001. beta\_2\_decay: float, defaults to -0.8. The decay rate of `beta_2`. epsilon\_1: float, defaults to 1e-30. A small offset to keep denominator away from 0. epsilon\_2: float, defaults to 1e-3. A small offset to avoid learning rate becoming too small by time. clip\_threshold: float, defaults to 1.0. Clipping threshold. This is a part of Adafactor algorithm, independent from `clipnorm`, `clipvalue` and `global_clipnorm`. relative\_step: bool, defaults to True. If `learning_rate` is a constant and `relative_step=True`, learning rate will be adjusted based on current iterations. This is a default learning rate decay in Adafactor.
*   **name**: String. The name to use for momentum accumulator weights created by the optimizer.
*   **weight\_decay**: Float, defaults to None. If set, weight decay is applied.
*   **clipnorm**: Float. If set, the gradient of each weight is individually clipped so that its norm is no higher than this value.
*   **clipvalue**: Float. If set, the gradient of each weight is clipped to be no higher than this value.
*   **global\_clipnorm**: Float. If set, the gradient of all weights is clipped so that their global norm is no higher than this value.
*   **use\_ema**: Boolean, defaults to False. If True, exponential moving average (EMA) is applied. EMA consists of computing an exponential moving average of the weights of the model (as the weight values change after each training batch), and periodically overwriting the weights with their moving average.
*   **ema\_momentum**: Float, defaults to 0.99. Only used if `use_ema=True`. This is the momentum to use when computing the EMA of the model's weights: `new_average = ema_momentum * old_average + (1 - ema_momentum) * current_variable_value`.
*   **ema\_overwrite\_frequency**: Int or None, defaults to None. Only used if `use_ema=True`. Every `ema_overwrite_frequency` steps of iterations, we overwrite the model variable by its moving average. If None, the optimizer does not overwrite model variables in the middle of training, and you need to explicitly overwrite the variables at the end of training by calling `optimizer.finalize_variable_values()` (which updates the model variables in-place). When using the built-in `fit()` training loop, this happens automatically after the last epoch, and you don't need to do anything.
*   **jit\_compile**: Boolean, defaults to True. If True, the optimizer will use XLA compilation. If no GPU device is found, this flag will be ignored.
*   **mesh**: optional [`tf.experimental.dtensor.Mesh`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh)
     instance. When provided, the optimizer will be run in DTensor mode, e.g. state tracking variable will be a DVariable, and aggregation/reduction will happen in the global DTensor context.
*   **\*\*kwargs**: keyword arguments only used for backward compatibility.

**Reference**

*   [Shazeer, Noam et al., 2018](https://arxiv.org/abs/1804.04235)
    .

* * *

[Adafactor](https://keras.io/2/api/optimizers/adafactor/#adafactor)

[`Adafactor` class](https://keras.io/2/api/optimizers/adafactor/#adafactor-class)