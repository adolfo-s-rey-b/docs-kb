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
 / Ftrl

Ftrl
====

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/optimizers/ftrl.py#L26)

### `Ftrl` class

Copied!

`tf_keras.optimizers.Ftrl(     learning_rate=0.001,     learning_rate_power=-0.5,     initial_accumulator_value=0.1,     l1_regularization_strength=0.0,     l2_regularization_strength=0.0,     l2_shrinkage_regularization_strength=0.0,     beta=0.0,     weight_decay=None,     clipnorm=None,     clipvalue=None,     global_clipnorm=None,     use_ema=False,     ema_momentum=0.99,     ema_overwrite_frequency=None,     jit_compile=True,     name="Ftrl",     **kwargs )`

Optimizer that implements the FTRL algorithm.

"Follow The Regularized Leader" (FTRL) is an optimization algorithm developed at Google for click-through rate prediction in the early 2010s. It is most suitable for shallow models with large and sparse feature spaces. The algorithm is described by [McMahan et al., 2013](https://research.google.com/pubs/archive/41159.pdf)
. The TF-Keras version has support for both online L2 regularization (the L2 regularization described in the paper above) and shrinkage-type L2 regularization (which is the addition of an L2 penalty to the loss function).

Initialization:

Copied!

`n = 0 sigma = 0 z = 0`

Update rule for one variable `w`:

Copied!

`prev_n = n n = n + g ** 2 sigma = (n ** -lr_power - prev_n ** -lr_power) / lr z = z + g - sigma * w if abs(z) < lambda_1:   w = 0 else:   w = (sgn(z) * lambda_1 - z) / ((beta + sqrt(n)) / alpha + lambda_2)`

Notation:

*   `lr` is the learning rate
*   `g` is the gradient for the variable
*   `lambda_1` is the L1 regularization strength
*   `lambda_2` is the L2 regularization strength
*   `lr_power` is the power to scale n.

Check the documentation for the `l2_shrinkage_regularization_strength` parameter for more details when shrinkage is enabled, in which case gradient is replaced with a gradient with shrinkage.

**Arguments**

*   **learning\_rate**: A `Tensor`, floating point value, a schedule that is a [`tf.keras.optimizers.schedules.LearningRateSchedule`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/LearningRateSchedule)
    , or a callable that takes no arguments and returns the actual value to use. The learning rate. Defaults to `0.001`. learning\_rate\_power: A float value, must be less or equal to zero. Controls how the learning rate decreases during training. Use zero for a fixed learning rate. initial\_accumulator\_value: The starting value for accumulators. Only zero or positive values are allowed. l1\_regularization\_strength: A float value, must be greater than or equal to zero. Defaults to `0.0`. l2\_regularization\_strength: A float value, must be greater than or equal to zero. Defaults to `0.0`. l2\_shrinkage\_regularization\_strength: A float value, must be greater than or equal to zero. This differs from L2 above in that the L2 above is a stabilization penalty, whereas this L2 shrinkage is a magnitude penalty. When input is sparse shrinkage will only happen on the active weights. beta: A float value, representing the beta value from the paper. Defaults to 0.0. name: String. The name to use for momentum accumulator weights created by the optimizer.
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

* * *

[Ftrl](https://keras.io/2/api/optimizers/ftrl/#ftrl)

[`Ftrl` class](https://keras.io/2/api/optimizers/ftrl/#ftrl-class)