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
 / Adam

Adam
====

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/optimizers/adam.py#L26)

### `Adam` class

Copied!

`tf_keras.optimizers.Adam(     learning_rate=0.001,     beta_1=0.9,     beta_2=0.999,     epsilon=1e-07,     adaptive_epsilon=False,     amsgrad=False,     weight_decay=None,     clipnorm=None,     clipvalue=None,     global_clipnorm=None,     use_ema=False,     ema_momentum=0.99,     ema_overwrite_frequency=None,     jit_compile=True,     name="Adam",     **kwargs )`

Optimizer that implements the Adam algorithm.

Adam optimization is a stochastic gradient descent method that is based on adaptive estimation of first-order and second-order moments.

According to [Kingma et al., 2014](http://arxiv.org/abs/1412.6980)
, the method is "_computationally efficient, has little memory requirement, invariant to diagonal rescaling of gradients, and is well suited for problems that are large in terms of data/parameters_".

**Arguments**

*   **learning\_rate**: A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
    , floating point value, a schedule that is a [`tf.keras.optimizers.schedules.LearningRateSchedule`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/LearningRateSchedule)
    , or a callable that takes no arguments and returns the actual value to use. The learning rate. Defaults to `0.001`. beta\_1: A float value or a constant float tensor, or a callable that takes no arguments and returns the actual value to use. The exponential decay rate for the 1st moment estimates. Defaults to `0.9`. beta\_2: A float value or a constant float tensor, or a callable that takes no arguments and returns the actual value to use. The exponential decay rate for the 2nd moment estimates. Defaults to `0.999`. epsilon: A small constant for numerical stability. This epsilon is "epsilon hat" in the Kingma and Ba paper (in the formula just before Section 2.1) if `adaptive_epsilon` is `False`, not the epsilon in Algorithm 1 of the paper. Defaults to `1e-7`. adaptive\_epsilon: If `True` the epsilon hat is computed adaptively from the given epsilon (Algorithm 1 on the paper). If `False`, the epsilon given will be "epsilon hat". Default to `False`. amsgrad: Boolean. Whether to apply AMSGrad variant of this algorithm from the paper "On the Convergence of Adam and beyond". Defaults to `False`. name: String. The name to use for momentum accumulator weights created by the optimizer.
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
     - [Reddi et al., 2018](https://openreview.net/pdf?id=ryQu7f-RZ)
     for `amsgrad`.

Notes:

The default value of 1e-7 for epsilon might not be a good default in general. For example, when training an Inception network on ImageNet a current good choice is 1.0 or 0.1. Note that since Adam uses the formulation just before Section 2.1 of the Kingma and Ba paper rather than the formulation in Algorithm 1, the "epsilon" referred to here is "epsilon hat" in the paper.

The sparse implementation of this algorithm (used when the gradient is an IndexedSlices object, typically because of [`tf.gather`](https://www.tensorflow.org/api_docs/python/tf/gather)
 or an embedding lookup in the forward pass) does apply momentum to variable slices even if they were not used in the forward pass (meaning they have a gradient equal to zero). Momentum decay (beta1) is also applied to the entire momentum accumulator. This means that the sparse behavior is equivalent to the dense behavior (in contrast to some momentum implementations which ignore momentum unless a variable slice was actually used).

* * *

[Adam](https://keras.io/2/api/optimizers/adam/#adam)

[`Adam` class](https://keras.io/2/api/optimizers/adam/#adam-class)