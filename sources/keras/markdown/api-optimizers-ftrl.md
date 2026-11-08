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
 / Ftrl

Ftrl
====

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/ftrl.py#L7)

### `Ftrl` class

Copied!

`keras.optimizers.Ftrl(     learning_rate=0.001,     learning_rate_power=-0.5,     initial_accumulator_value=0.1,     l1_regularization_strength=0.0,     l2_regularization_strength=0.0,     l2_shrinkage_regularization_strength=0.0,     beta=0.0,     weight_decay=None,     clipnorm=None,     clipvalue=None,     global_clipnorm=None,     use_ema=False,     ema_momentum=0.99,     ema_overwrite_frequency=None,     loss_scale_factor=None,     gradient_accumulation_steps=None,     name=None,     **kwargs )`

Optimizer that implements the FTRL algorithm.

"Follow The Regularized Leader" (FTRL) is an optimization algorithm developed at Google for click-through rate prediction in the early 2010s. It is most suitable for shallow models with large and sparse feature spaces. The algorithm is described by [McMahan et al., 2013](https://research.google.com/pubs/archive/41159.pdf)
. The Keras version has support for both online L2 regularization (the L2 regularization described in the paper above) and shrinkage-type L2 regularization (which is the addition of an L2 penalty to the loss function).

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

*   **learning\_rate**: A float, a [`keras.optimizers.schedules.LearningRateSchedule`](https://keras.io/api/optimizers/learning_rate_schedules/learning_rate_schedule#learningrateschedule-class)
     instance, or a callable that takes no arguments and returns the actual value to use. The learning rate. Defaults to `0.001`.
*   **learning\_rate\_power**: A float value, must be less or equal to zero. Controls how the learning rate decreases during training. Use zero for a fixed learning rate.
*   **initial\_accumulator\_value**: The starting value for accumulators. Only zero or positive values are allowed.
*   **l1\_regularization\_strength**: A float value, must be greater than or equal to zero. Defaults to `0.0`.
*   **l2\_regularization\_strength**: A float value, must be greater than or equal to zero. Defaults to `0.0`.
*   **l2\_shrinkage\_regularization\_strength**: A float value, must be greater than or equal to zero. This differs from L2 above in that the L2 above is a stabilization penalty, whereas this L2 shrinkage is a magnitude penalty. When input is sparse shrinkage will only happen on the active weights.
*   **beta**: A float value, representing the beta value from the paper. Defaults to `0.0`.
*   **name**: String. The name to use for momentum accumulator weights created by the optimizer.
*   **weight\_decay**: Float. If set, weight decay is applied.
*   **clipnorm**: Float. If set, the gradient of each weight is individually clipped so that its norm is no higher than this value.
*   **clipvalue**: Float. If set, the gradient of each weight is clipped to be no higher than this value.
*   **global\_clipnorm**: Float. If set, the gradient of all weights is clipped so that their global norm is no higher than this value.
*   **use\_ema**: Boolean, defaults to `False`. If `True`, exponential moving average (EMA) is applied. EMA consists of computing an exponential moving average of the weights of the model (as the weight values change after each training batch), and periodically overwriting the weights with their moving average.
*   **ema\_momentum**: Float, defaults to 0.99. Only used if `use_ema=True`. This is the momentum to use when computing the EMA of the model's weights: `new_average = ema_momentum * old_average + (1 - ema_momentum) * current_variable_value`.
*   **ema\_overwrite\_frequency**: Int or None, defaults to None. Only used if `use_ema=True`. Every `ema_overwrite_frequency` steps of iterations, we overwrite the model variable by its moving average. If None, the optimizer does not overwrite model variables in the middle of training, and you need to explicitly overwrite the variables at the end of training by calling `optimizer.finalize_variable_values()` (which updates the model variables in-place). When using the built-in `fit()` training loop, this happens automatically after the last epoch, and you don't need to do anything.
*   **loss\_scale\_factor**: Float or `None`. If a float, the scale factor will be multiplied the loss before computing gradients, and the inverse of the scale factor will be multiplied by the gradients before updating variables. Useful for preventing underflow during mixed precision training. Alternately, [`keras.optimizers.LossScaleOptimizer`](https://keras.io/api/optimizers/loss_scale_optimizer#lossscaleoptimizer-class)
     will automatically set a loss scale factor.
*   **gradient\_accumulation\_steps**: Int or `None`. If an int, model & optimizer variables will not be updated at every step; instead they will be updated every `gradient_accumulation_steps` steps, using the average value of the gradients since the last update. This is known as "gradient accumulation". This can be useful when your batch size is very small, in order to reduce gradient noise at each update step. EMA frequency will look at "accumulated" iterations value (optimizer steps // gradient\_accumulation\_steps). Learning rate schedules will look at "real" iterations value (optimizer steps).

* * *

[Ftrl](https://keras.io/api/optimizers/ftrl/#ftrl)

[`Ftrl` class](https://keras.io/api/optimizers/ftrl/#ftrl-class)