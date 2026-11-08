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
 / InverseTimeDecay

InverseTimeDecay
================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/optimizers/schedules/learning_rate_schedule.py#L470)

### `InverseTimeDecay` class

Copied!

`tf_keras.optimizers.schedules.InverseTimeDecay(     initial_learning_rate, decay_steps, decay_rate, staircase=False, name=None )`

A LearningRateSchedule that uses an inverse time decay schedule.

When training a model, it is often useful to lower the learning rate as the training progresses. This schedule applies the inverse decay function to an optimizer step, given a provided initial learning rate. It requires a `step` value to compute the decayed learning rate. You can just pass a TensorFlow variable that you increment at each training step.

The schedule is a 1-arg callable that produces a decayed learning rate when passed the current optimizer step. This can be useful for changing the learning rate value across different invocations of optimizer functions. It is computed as:

Copied!

`def decayed_learning_rate(step):   return initial_learning_rate / (1 + decay_rate * step / decay_step)`

or, if `staircase` is `True`, as:

Copied!

`def decayed_learning_rate(step):   return initial_learning_rate / (1 + decay_rate * floor(step / decay_step))`

You can pass this schedule directly into a [`tf.keras.optimizers.Optimizer`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Optimizer)
 as the learning rate. **Example**

Fit a TF-Keras model when decaying 1/t with a rate of 0.5:

Copied!

`... initial_learning_rate = 0.1 decay_steps = 1.0 decay_rate = 0.5 learning_rate_fn = keras.optimizers.schedules.InverseTimeDecay(   initial_learning_rate, decay_steps, decay_rate)  model.compile(optimizer=tf.keras.optimizers.SGD(                   learning_rate=learning_rate_fn),               loss='sparse_categorical_crossentropy',               metrics=['accuracy'])  model.fit(data, labels, epochs=5)`

**Returns**

A 1-arg callable learning rate schedule that takes the current optimizer step and outputs the decayed learning rate, a scalar `Tensor` of the same type as `initial_learning_rate`.

* * *

[InverseTimeDecay](https://keras.io/2/api/optimizers/learning_rate_schedules/inverse_time_decay/#inversetimedecay)

[`InverseTimeDecay` class](https://keras.io/2/api/optimizers/learning_rate_schedules/inverse_time_decay/#inversetimedecay-class)