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
 / InverseTimeDecay

InverseTimeDecay
================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/schedules/learning_rate_schedule.py#L460)

### `InverseTimeDecay` class

Copied!

`keras.optimizers.schedules.InverseTimeDecay(     initial_learning_rate,     decay_steps,     decay_rate,     staircase=False,     name="InverseTimeDecay", )`

A `LearningRateSchedule` that uses an inverse time decay schedule.

When training a model, it is often useful to lower the learning rate as the training progresses. This schedule applies the inverse decay function to an optimizer step, given a provided initial learning rate. It requires a `step` value to compute the decayed learning rate. You can just pass a backend variable that you increment at each training step.

The schedule is a 1-arg callable that produces a decayed learning rate when passed the current optimizer step. This can be useful for changing the learning rate value across different invocations of optimizer functions. It is computed as:

Copied!

`def decayed_learning_rate(step):     return initial_learning_rate / (1 + decay_rate * step / decay_step)`

or, if `staircase` is `True`, as:

Copied!

`def decayed_learning_rate(step):     return initial_learning_rate /            (1 + decay_rate * floor(step / decay_step))`

You can pass this schedule directly into a [`keras.optimizers.Optimizer`](https://keras.io/api/optimizers#optimizer-class)
 as the learning rate. **Example**

Fit a Keras model when decaying 1/t with a rate of 0.5:

Copied!

`... initial_learning_rate = 0.1 decay_steps = 1.0 decay_rate = 0.5 learning_rate_fn = keras.optimizers.schedules.InverseTimeDecay(     initial_learning_rate, decay_steps, decay_rate)  model.compile(optimizer=keras.optimizers.SGD(                   learning_rate=learning_rate_fn),               loss='sparse_categorical_crossentropy',               metrics=['accuracy'])  model.fit(data, labels, epochs=5)`

**Arguments**

*   **initial\_learning\_rate**: A Python float. The initial learning rate.
*   **decay\_steps**: How often to apply decay.
*   **decay\_rate**: A Python number. The decay rate.
*   **staircase**: Whether to apply decay in a discrete staircase, as o pposed to continuous, fashion.
*   **name**: String. Optional name of the operation. Defaults to `"InverseTimeDecay"`.

**Returns**

A 1-arg callable learning rate schedule that takes the current optimizer step and outputs the decayed learning rate, a scalar tensor of the same type as `initial_learning_rate`.

* * *

[InverseTimeDecay](https://keras.io/api/optimizers/learning_rate_schedules/inverse_time_decay/#inversetimedecay)

[`InverseTimeDecay` class](https://keras.io/api/optimizers/learning_rate_schedules/inverse_time_decay/#inversetimedecay-class)