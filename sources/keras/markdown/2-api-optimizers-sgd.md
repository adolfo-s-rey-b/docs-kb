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
 / SGD

SGD
===

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/optimizers/sgd.py#L26)

### `SGD` class

Copied!

`tf_keras.optimizers.SGD(     learning_rate=0.01,     momentum=0.0,     nesterov=False,     weight_decay=None,     clipnorm=None,     clipvalue=None,     global_clipnorm=None,     use_ema=False,     ema_momentum=0.99,     ema_overwrite_frequency=None,     jit_compile=True,     name="SGD",     **kwargs )`

Gradient descent (with momentum) optimizer.

Update rule for parameter `w` with gradient `g` when `momentum` is 0:

Copied!

`w = w - learning_rate * g`

Update rule when `momentum` is larger than 0:

Copied!

`velocity = momentum * velocity - learning_rate * g w = w + velocity`

When `nesterov=True`, this rule becomes:

Copied!

`velocity = momentum * velocity - learning_rate * g w = w + momentum * velocity - learning_rate * g`

**Arguments**

*   **learning\_rate**: A `Tensor`, floating point value, or a schedule that is a [`keras.optimizers.schedules.LearningRateSchedule`](https://keras.io/api/optimizers/learning_rate_schedules/learning_rate_schedule#learningrateschedule-class)
    , or a callable that takes no arguments and returns the actual value to use. The learning rate. Defaults to 0.001. momentum: float hyperparameter >= 0 that accelerates gradient descent in the relevant direction and dampens oscillations. Defaults to 0, i.e., vanilla gradient descent. nesterov: boolean. Whether to apply Nesterov momentum. Defaults to `False`.
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

Usage:

Copied!

``>>> opt = tf.keras.optimizers.SGD(learning_rate=0.1) >>> var = tf.Variable(1.0) >>> loss = lambda: (var ** 2)/2.0         # d(loss)/d(var1) = var1 >>> opt.minimize(loss, [var]) >>> # Step is `- learning_rate * grad` >>> var.numpy() 0.9``

Copied!

``>>> opt = tf.keras.optimizers.SGD(0.1, momentum=0.9) >>> var = tf.Variable(1.0) >>> val0 = var.value() >>> loss = lambda: (var ** 2)/2.0         # d(loss)/d(var1) = var1 >>> # First step is `- learning_rate * grad` >>> opt.minimize(loss, [var]) >>> val1 = var.value() >>> (val0 - val1).numpy() 0.1 >>> # On later steps, step-size increases because of momentum >>> opt.minimize(loss, [var]) >>> val2 = var.value() >>> (val1 - val2).numpy() 0.18``

**Reference**

*   For `nesterov=True`, See [Sutskever et al., 2013](http://proceedings.mlr.press/v28/sutskever13.pdf)
    .

* * *

[SGD](https://keras.io/2/api/optimizers/sgd/#sgd)

[`SGD` class](https://keras.io/2/api/optimizers/sgd/#sgd-class)