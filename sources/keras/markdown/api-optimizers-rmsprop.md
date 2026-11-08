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
 / RMSprop

RMSprop
=======

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/rmsprop.py#L6)

### `RMSprop` class

Copied!

`keras.optimizers.RMSprop(     learning_rate=0.001,     rho=0.9,     momentum=0.0,     epsilon=1e-07,     centered=False,     weight_decay=None,     clipnorm=None,     clipvalue=None,     global_clipnorm=None,     use_ema=False,     ema_momentum=0.99,     ema_overwrite_frequency=None,     loss_scale_factor=None,     gradient_accumulation_steps=None,     name=None,     **kwargs )`

Optimizer that implements the RMSprop algorithm.

The gist of RMSprop is to:

*   Maintain a moving (discounted) average of the square of gradients
*   Divide the gradient by the root of this average

This implementation of RMSprop uses plain momentum, not Nesterov momentum.

The centered version additionally maintains a moving average of the gradients, and uses that average to estimate the variance.

**Arguments**

*   **learning\_rate**: A float, a [`keras.optimizers.schedules.LearningRateSchedule`](https://keras.io/api/optimizers/learning_rate_schedules/learning_rate_schedule#learningrateschedule-class)
     instance, or a callable that takes no arguments and returns the actual value to use. The learning rate. Defaults to `0.001`.
*   **rho**: float, defaults to 0.9. Discounting factor for the old gradients.
*   **momentum**: float, defaults to 0.0. If not 0.0., the optimizer tracks the momentum value, with a decay rate equals to `1 - momentum`.
*   **epsilon**: A small constant for numerical stability. This epsilon is "epsilon hat" in the Kingma and Ba paper (in the formula just before Section 2.1), not the epsilon in Algorithm 1 of the paper. Defaults to 1e-7.
*   **centered**: Boolean. If `True`, gradients are normalized by the estimated variance of the gradient; if False, by the uncentered second moment. Setting this to `True` may help with training, but is slightly more expensive in terms of computation and memory. Defaults to `False`.
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

**Example**

Copied!

`>>> opt = keras.optimizers.RMSprop(learning_rate=0.1) >>> var1 = keras.backend.Variable(10.0) >>> loss = lambda: (var1 ** 2) / 2.0  # d(loss) / d(var1) = var1 >>> opt.minimize(loss, [var1]) >>> var1 9.683772`

**Reference**

*   [Hinton, 2012](http://www.cs.toronto.edu/~tijmen/csc321/slides/lecture_slides_lec6.pdf)
    

**Guides and examples using `RMSprop`**

*   [The Functional API](https://keras.io/guides/functional_api/)
    
*   [Training & evaluation with the built-in methods](https://keras.io/guides/training_with_built_in_methods/)
    
*   [Writing your own callbacks](https://keras.io/guides/writing_your_own_callbacks/)
    
*   [Traffic forecasting using graph neural networks and LSTM](https://keras.io/examples/timeseries/timeseries_traffic_forecasting/)
    
*   [Character-level text generation with LSTM](https://keras.io/examples/generative/lstm_character_level_text_generation/)
    
*   [Simple custom layer example: Antirectifier](https://keras.io/examples/keras_recipes/antirectifier/)
    

* * *

[RMSprop](https://keras.io/api/optimizers/rmsprop/#rmsprop)

[`RMSprop` class](https://keras.io/api/optimizers/rmsprop/#rmsprop-class)