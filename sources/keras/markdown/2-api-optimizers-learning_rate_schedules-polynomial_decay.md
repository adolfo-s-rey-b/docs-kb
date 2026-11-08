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
 / PolynomialDecay

PolynomialDecay
===============

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/optimizers/schedules/learning_rate_schedule.py#L317)

### `PolynomialDecay` class

Copied!

`tf_keras.optimizers.schedules.PolynomialDecay(     initial_learning_rate,     decay_steps,     end_learning_rate=0.0001,     power=1.0,     cycle=False,     name=None, )`

A LearningRateSchedule that uses a polynomial decay schedule.

It is commonly observed that a monotonically decreasing learning rate, whose degree of change is carefully chosen, results in a better performing model. This schedule applies a polynomial decay function to an optimizer step, given a provided `initial_learning_rate`, to reach an `end_learning_rate` in the given `decay_steps`.

It requires a `step` value to compute the decayed learning rate. You can just pass a TensorFlow variable that you increment at each training step.

The schedule is a 1-arg callable that produces a decayed learning rate when passed the current optimizer step. This can be useful for changing the learning rate value across different invocations of optimizer functions. It is computed as:

Copied!

`def decayed_learning_rate(step):   step = min(step, decay_steps)   return ((initial_learning_rate - end_learning_rate) *           (1 - step / decay_steps) ^ (power)          ) + end_learning_rate`

If `cycle` is True then a multiple of `decay_steps` is used, the first one that is bigger than `step`.

Copied!

`def decayed_learning_rate(step):   decay_steps = decay_steps * ceil(step / decay_steps)   return ((initial_learning_rate - end_learning_rate) *           (1 - step / decay_steps) ^ (power)          ) + end_learning_rate`

You can pass this schedule directly into a [`tf.keras.optimizers.Optimizer`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Optimizer)
 as the learning rate. **Example**

Fit a model while decaying from 0.1 to 0.01 in 10000 steps using

sqrt (i.e. power=0.5):

Copied!

`... starter_learning_rate = 0.1 end_learning_rate = 0.01 decay_steps = 10000 learning_rate_fn = tf.keras.optimizers.schedules.PolynomialDecay(     starter_learning_rate,     decay_steps,     end_learning_rate,     power=0.5)  model.compile(optimizer=tf.keras.optimizers.SGD(                   learning_rate=learning_rate_fn),               loss='sparse_categorical_crossentropy',               metrics=['accuracy'])  model.fit(data, labels, epochs=5)`

The learning rate schedule is also serializable and deserializable using [`tf.keras.optimizers.schedules.serialize`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/serialize)
 and [`tf.keras.optimizers.schedules.deserialize`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/deserialize)
.

**Returns**

A 1-arg callable learning rate schedule that takes the current optimizer step and outputs the decayed learning rate, a scalar `Tensor` of the same type as `initial_learning_rate`.

* * *

[PolynomialDecay](https://keras.io/2/api/optimizers/learning_rate_schedules/polynomial_decay/#polynomialdecay)

[`PolynomialDecay` class](https://keras.io/2/api/optimizers/learning_rate_schedules/polynomial_decay/#polynomialdecay-class)