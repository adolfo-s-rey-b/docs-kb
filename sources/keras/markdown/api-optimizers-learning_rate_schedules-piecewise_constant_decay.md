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
 / PiecewiseConstantDecay

PiecewiseConstantDecay
======================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/schedules/learning_rate_schedule.py#L187)

### `PiecewiseConstantDecay` class

Copied!

`keras.optimizers.schedules.PiecewiseConstantDecay(     boundaries, values, name="PiecewiseConstant" )`

A `LearningRateSchedule` that uses a piecewise constant decay schedule.

The function returns a 1-arg callable to compute the piecewise constant when passed the current optimizer step. This can be useful for changing the learning rate value across different invocations of optimizer functions.

**Example**

use a learning rate that's 1.0 for the first 100001 steps, 0.5 for the next 10000 steps, and 0.1 for any additional steps.

Copied!

`step = ops.array(0) boundaries = [100000, 110000] values = [1.0, 0.5, 0.1] learning_rate_fn = keras.optimizers.schedules.PiecewiseConstantDecay(     boundaries, values)  # Later, whenever we perform an optimization step, we pass in the step. learning_rate = learning_rate_fn(step)`

You can pass this schedule directly into a [`keras.optimizers.Optimizer`](https://keras.io/api/optimizers#optimizer-class)
 as the learning rate. The learning rate schedule is also serializable and deserializable using `keras.optimizers.schedules.serialize` and `keras.optimizers.schedules.deserialize`.

**Arguments**

*   **boundaries**: A list of Python numbers with strictly increasing entries, and with all elements having the same type as the optimizer step.
*   **values**: A list of Python numbers that specifies the values for the intervals defined by `boundaries`. It should have one more element than `boundaries`, and all elements should have the same type.
*   **name**: A string. Optional name of the operation. Defaults to `"PiecewiseConstant"`.

**Returns**

A 1-arg callable learning rate schedule that takes the current optimizer step and outputs the decayed learning rate, a scalar tensor of the same type as the boundary tensors.

The output of the 1-arg function that takes the `step` is `values[0]` when `step <= boundaries[0]`, `values[1]` when `step > boundaries[0]` and `step <= boundaries[1]`, ..., and `values[-1]` when `step > boundaries[-1]`.

**Raises**

*   **ValueError**: if the number of elements in the `boundaries` and `values` lists do not match.

* * *

[PiecewiseConstantDecay](https://keras.io/api/optimizers/learning_rate_schedules/piecewise_constant_decay/#piecewiseconstantdecay)

[`PiecewiseConstantDecay` class](https://keras.io/api/optimizers/learning_rate_schedules/piecewise_constant_decay/#piecewiseconstantdecay-class)