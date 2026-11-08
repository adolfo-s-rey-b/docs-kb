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
 / CosineDecayRestarts

CosineDecayRestarts
===================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/optimizers/schedules/learning_rate_schedule.py#L771)

### `CosineDecayRestarts` class

Copied!

`tf_keras.optimizers.schedules.CosineDecayRestarts(     initial_learning_rate, first_decay_steps, t_mul=2.0, m_mul=1.0, alpha=0.0, name=None )`

A LearningRateSchedule that uses a cosine decay schedule with restarts.

See [Loshchilov & Hutter, ICLR2016](https://arxiv.org/abs/1608.03983)
, SGDR: Stochastic Gradient Descent with Warm Restarts.

When training a model, it is often useful to lower the learning rate as the training progresses. This schedule applies a cosine decay function with restarts to an optimizer step, given a provided initial learning rate. It requires a `step` value to compute the decayed learning rate. You can just pass a TensorFlow variable that you increment at each training step.

The schedule is a 1-arg callable that produces a decayed learning rate when passed the current optimizer step. This can be useful for changing the learning rate value across different invocations of optimizer functions.

The learning rate multiplier first decays from 1 to `alpha` for `first_decay_steps` steps. Then, a warm restart is performed. Each new warm restart runs for `t_mul` times more steps and with `m_mul` times initial learning rate as the new learning rate.

Example usage:

Copied!

`first_decay_steps = 1000 lr_decayed_fn = (   tf.keras.optimizers.schedules.CosineDecayRestarts(       initial_learning_rate,       first_decay_steps))`

You can pass this schedule directly into a [`tf.keras.optimizers.Optimizer`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Optimizer)
 as the learning rate. The learning rate schedule is also serializable and deserializable using [`tf.keras.optimizers.schedules.serialize`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/serialize)
 and [`tf.keras.optimizers.schedules.deserialize`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/deserialize)
.

**Returns**

A 1-arg callable learning rate schedule that takes the current optimizer step and outputs the decayed learning rate, a scalar `Tensor` of the same type as `initial_learning_rate`.

* * *

[CosineDecayRestarts](https://keras.io/2/api/optimizers/learning_rate_schedules/cosine_decay_restarts/#cosinedecayrestarts)

[`CosineDecayRestarts` class](https://keras.io/2/api/optimizers/learning_rate_schedules/cosine_decay_restarts/#cosinedecayrestarts-class)