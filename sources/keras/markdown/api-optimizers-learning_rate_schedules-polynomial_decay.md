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
 / [Learning rate schedules API](https://keras.io/api/optimizers/learning_rate_schedules/)
 / PolynomialDecay

PolynomialDecay
===============

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/schedules/learning_rate_schedule.py#L304)

### `PolynomialDecay` class

Copied!

`keras.optimizers.schedules.PolynomialDecay(     initial_learning_rate,     decay_steps,     end_learning_rate=0.0001,     power=1.0,     cycle=False,     name="PolynomialDecay", )`

A `LearningRateSchedule` that uses a polynomial decay schedule.

It is commonly observed that a monotonically decreasing learning rate, whose degree of change is carefully chosen, results in a better performing model. This schedule applies a polynomial decay function to an optimizer step, given a provided `initial_learning_rate`, to reach an `end_learning_rate` in the given `decay_steps`.

It requires a `step` value to compute the decayed learning rate. You can just pass a backend variable that you increment at each training step.

The schedule is a 1-arg callable that produces a decayed learning rate when passed the current optimizer step. This can be useful for changing the learning rate value across different invocations of optimizer functions. It is computed as:

Copied!

`def decayed_learning_rate(step):     step = min(step, decay_steps)     return ((initial_learning_rate - end_learning_rate) *             (1 - step / decay_steps) ^ (power)            ) + end_learning_rate`

If `cycle` is True then a multiple of `decay_steps` is used, the first one that is bigger than `step`.

Copied!

`def decayed_learning_rate(step):     decay_steps = decay_steps * ceil(step / decay_steps)     return ((initial_learning_rate - end_learning_rate) *             (1 - step / decay_steps) ^ (power)            ) + end_learning_rate`

You can pass this schedule directly into a [`keras.optimizers.Optimizer`](https://keras.io/api/optimizers#optimizer-class)
 as the learning rate. **Example**

Fit a model while decaying from 0.1 to 0.01 in 10000 steps using

sqrt (i.e. power=0.5):

Copied!

`... starter_learning_rate = 0.1 end_learning_rate = 0.01 decay_steps = 10000 learning_rate_fn = keras.optimizers.schedules.PolynomialDecay(     starter_learning_rate,     decay_steps,     end_learning_rate,     power=0.5)  model.compile(optimizer=keras.optimizers.SGD(                   learning_rate=learning_rate_fn),               loss='sparse_categorical_crossentropy',               metrics=['accuracy'])  model.fit(data, labels, epochs=5)`

The learning rate schedule is also serializable and deserializable using `keras.optimizers.schedules.serialize` and `keras.optimizers.schedules.deserialize`.

**Arguments**

*   **initial\_learning\_rate**: A Python float. The initial learning rate.
*   **decay\_steps**: A Python integer. Must be positive. See the decay computation above.
*   **end\_learning\_rate**: A Python float. The minimal end learning rate.
*   **power**: A Python float. The power of the polynomial. Defaults to `1.0`.
*   **cycle**: A boolean, whether it should cycle beyond decay\_steps.
*   **name**: String. Optional name of the operation. Defaults to `"PolynomialDecay"`.

**Returns**

A 1-arg callable learning rate schedule that takes the current optimizer step and outputs the decayed learning rate, a scalar tensor of the same type as `initial_learning_rate`.

* * *

[PolynomialDecay](https://keras.io/api/optimizers/learning_rate_schedules/polynomial_decay/#polynomialdecay)

[`PolynomialDecay` class](https://keras.io/api/optimizers/learning_rate_schedules/polynomial_decay/#polynomialdecay-class)