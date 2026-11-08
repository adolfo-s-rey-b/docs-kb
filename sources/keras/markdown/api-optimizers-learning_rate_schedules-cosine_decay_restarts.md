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
 / CosineDecayRestarts

CosineDecayRestarts
===================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/schedules/learning_rate_schedule.py#L767)

### `CosineDecayRestarts` class

Copied!

`keras.optimizers.schedules.CosineDecayRestarts(     initial_learning_rate,     first_decay_steps,     t_mul=2.0,     m_mul=1.0,     alpha=0.0,     name="SGDRDecay", )`

A `LearningRateSchedule` that uses a cosine decay schedule with restarts.

See [Loshchilov & Hutter, ICLR2016](https://arxiv.org/abs/1608.03983)
, SGDR: Stochastic Gradient Descent with Warm Restarts.

When training a model, it is often useful to lower the learning rate as the training progresses. This schedule applies a cosine decay function with restarts to an optimizer step, given a provided initial learning rate. It requires a `step` value to compute the decayed learning rate. You can just pass a backend variable that you increment at each training step.

The schedule is a 1-arg callable that produces a decayed learning rate when passed the current optimizer step. This can be useful for changing the learning rate value across different invocations of optimizer functions.

The learning rate multiplier first decays from 1 to `alpha` for `first_decay_steps` steps. Then, a warm restart is performed. Each new warm restart runs for `t_mul` times more steps and with `m_mul` times initial learning rate as the new learning rate.

**Example**

Copied!

`first_decay_steps = 1000 lr_decayed_fn = (     keras.optimizers.schedules.CosineDecayRestarts(         initial_learning_rate,         first_decay_steps))`

You can pass this schedule directly into a [`keras.optimizers.Optimizer`](https://keras.io/api/optimizers#optimizer-class)
 as the learning rate. The learning rate schedule is also serializable and deserializable using `keras.optimizers.schedules.serialize` and `keras.optimizers.schedules.deserialize`.

**Arguments**

*   **initial\_learning\_rate**: A Python float. The initial learning rate.
*   **first\_decay\_steps**: A Python integer. Number of steps to decay over.
*   **t\_mul**: A Python float. Used to derive the number of iterations in the i-th period.
*   **m\_mul**: A Python float. Used to derive the initial learning rate of the i-th period.
*   **alpha**: A Python float. Minimum learning rate value as a fraction of the `initial_learning_rate`.
*   **name**: String. Optional name of the operation. Defaults to `"SGDRDecay"`.

**Returns**

A 1-arg callable learning rate schedule that takes the current optimizer step and outputs the decayed learning rate, a scalar tensor of the same type as `initial_learning_rate`.

* * *

[CosineDecayRestarts](https://keras.io/api/optimizers/learning_rate_schedules/cosine_decay_restarts/#cosinedecayrestarts)

[`CosineDecayRestarts` class](https://keras.io/api/optimizers/learning_rate_schedules/cosine_decay_restarts/#cosinedecayrestarts-class)