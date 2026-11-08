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
 / Adamax

Adamax
======

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/optimizers/adamax.py#L26)

### `Adamax` class

Copied!

`tf_keras.optimizers.Adamax(     learning_rate=0.001,     beta_1=0.9,     beta_2=0.999,     epsilon=1e-07,     weight_decay=None,     clipnorm=None,     clipvalue=None,     global_clipnorm=None,     use_ema=False,     ema_momentum=0.99,     ema_overwrite_frequency=None,     jit_compile=True,     name="Adamax",     **kwargs )`

Optimizer that implements the Adamax algorithm.

Adamax, a variant of Adam based on the infinity norm, is a first-order gradient-based optimization method. Due to its capability of adjusting the learning rate based on data characteristics, it is suited to learn time-variant process, e.g., speech data with dynamically changed noise conditions. Default parameters follow those provided in the paper (see references below).

Initialization:

Copied!

`m = 0  # Initialize initial 1st moment vector u = 0  # Initialize the exponentially weighted infinity norm t = 0  # Initialize timestep`

The update rule for parameter `w` with gradient `g` is described at the end of section 7.1 of the paper (see the referenece section):

Copied!

`t += 1 m = beta1 * m + (1 - beta) * g u = max(beta2 * u, abs(g)) current_lr = learning_rate / (1 - beta1 ** t) w = w - current_lr * m / (u + epsilon)`

**Arguments**

*   **learning\_rate**: A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
    , floating point value, a schedule that is a [`tf.keras.optimizers.schedules.LearningRateSchedule`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/LearningRateSchedule)
    , or a callable that takes no arguments and returns the actual value to use. The learning rate. Defaults to `0.001`. beta\_1: A float value or a constant float tensor. The exponential decay rate for the 1st moment estimates. beta\_2: A float value or a constant float tensor. The exponential decay rate for the exponentially weighted infinity norm. epsilon: A small constant for numerical stability. name: String. The name to use for momentum accumulator weights created by the optimizer.
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

*   [Kingma et al., 2014](http://arxiv.org/abs/1412.6980)
    

* * *

[Adamax](https://keras.io/2/api/optimizers/adamax/#adamax)

[`Adamax` class](https://keras.io/2/api/optimizers/adamax/#adamax-class)