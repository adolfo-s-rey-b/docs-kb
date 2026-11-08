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
 / [Learning rate schedules API](https://keras.io/2/api/optimizers/learning_rate_schedules/)
 / PiecewiseConstantDecay

PiecewiseConstantDecay
======================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/optimizers/schedules/learning_rate_schedule.py#L209)

### `PiecewiseConstantDecay` class

Copied!

`tf_keras.optimizers.schedules.PiecewiseConstantDecay(boundaries, values, name=None)`

A LearningRateSchedule that uses a piecewise constant decay schedule.

The function returns a 1-arg callable to compute the piecewise constant when passed the current optimizer step. This can be useful for changing the learning rate value across different invocations of optimizer functions.

**Example**

use a learning rate that's 1.0 for the first 100001 steps, 0.5 for the next 10000 steps, and 0.1 for any additional steps.

Copied!

`step = tf.Variable(0, trainable=False) boundaries = [100000, 110000] values = [1.0, 0.5, 0.1] learning_rate_fn = keras.optimizers.schedules.PiecewiseConstantDecay(     boundaries, values)  # Later, whenever we perform an optimization step, we pass in the step. learning_rate = learning_rate_fn(step)`

You can pass this schedule directly into a [`tf.keras.optimizers.Optimizer`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Optimizer)
 as the learning rate. The learning rate schedule is also serializable and deserializable using [`tf.keras.optimizers.schedules.serialize`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/serialize)
 and [`tf.keras.optimizers.schedules.deserialize`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/deserialize)
.

**Returns**

A 1-arg callable learning rate schedule that takes the current optimizer step and outputs the decayed learning rate, a scalar `Tensor` of the same type as the boundary tensors.

The output of the 1-arg function that takes the `step` is `values[0]` when `step <= boundaries[0]`, `values[1]` when `step > boundaries[0]` and `step <= boundaries[1]`, ..., and values\[-1\] when `step > boundaries[-1]`.

* * *

[PiecewiseConstantDecay](https://keras.io/2/api/optimizers/learning_rate_schedules/piecewise_constant_decay/#piecewiseconstantdecay)

[`PiecewiseConstantDecay` class](https://keras.io/2/api/optimizers/learning_rate_schedules/piecewise_constant_decay/#piecewiseconstantdecay-class)