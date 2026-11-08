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
 / CosineDecay

CosineDecay
===========

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/schedules/learning_rate_schedule.py#L572)

### `CosineDecay` class

Copied!

`keras.optimizers.schedules.CosineDecay(     initial_learning_rate,     decay_steps,     alpha=0.0,     name="CosineDecay",     warmup_target=None,     warmup_steps=0, )`

A `LearningRateSchedule` that uses a cosine decay with optional warmup.

See [Loshchilov & Hutter, ICLR2016](https://arxiv.org/abs/1608.03983)
, SGDR: Stochastic Gradient Descent with Warm Restarts.

For the idea of a linear warmup of our learning rate, see [Goyal et al.](https://arxiv.org/pdf/1706.02677.pdf)
.

When we begin training a model, we often want an initial increase in our learning rate followed by a decay. If `warmup_target` is an int, this schedule applies a linear increase per optimizer step to our learning rate from `initial_learning_rate` to `warmup_target` for a duration of `warmup_steps`. Afterwards, it applies a cosine decay function taking our learning rate from `warmup_target` to `warmup_target * alpha` for a duration of `decay_steps`. If `warmup_target` is None we skip warmup and our decay will take our learning rate from `initial_learning_rate` to `initial_learning_rate * alpha`. It requires a `step` value to compute the learning rate. You can just pass a backend variable that you increment at each training step.

The schedule is a 1-arg callable that produces a warmup followed by a decayed learning rate when passed the current optimizer step. This can be useful for changing the learning rate value across different invocations of optimizer functions.

Our warmup is computed as:

Copied!

`def warmup_learning_rate(step):     completed_fraction = step / warmup_steps     total_delta = target_warmup - initial_learning_rate     return completed_fraction * total_delta`

And our decay is computed as:

Copied!

`if warmup_target is None:     initial_decay_lr = initial_learning_rate else:     initial_decay_lr = warmup_target  def decayed_learning_rate(step):     step = min(step, decay_steps)     cosine_decay = 0.5 * (1 + cos(pi * step / decay_steps))     decayed = (1 - alpha) * cosine_decay + alpha     return initial_decay_lr * decayed`

Example usage without warmup:

Copied!

`decay_steps = 1000 initial_learning_rate = 0.1 lr_decayed_fn = keras.optimizers.schedules.CosineDecay(     initial_learning_rate, decay_steps)`

Example usage with warmup:

Copied!

`decay_steps = 1000 initial_learning_rate = 0 warmup_steps = 1000 target_learning_rate = 0.1 lr_warmup_decayed_fn = keras.optimizers.schedules.CosineDecay(     initial_learning_rate, decay_steps, warmup_target=target_learning_rate,     warmup_steps=warmup_steps )`

You can pass this schedule directly into a [`keras.optimizers.Optimizer`](https://keras.io/api/optimizers#optimizer-class)
 as the learning rate. The learning rate schedule is also serializable and deserializable using `keras.optimizers.schedules.serialize` and `keras.optimizers.schedules.deserialize`.

**Arguments**

*   **initial\_learning\_rate**: A Python float. The initial learning rate.
*   **decay\_steps**: A Python int. Number of steps to decay over.
*   **alpha**: A Python float. Minimum learning rate value for decay as a fraction of `warmup_target` or, if `warmup_target` is None, `initial_learning_rate`.
*   **name**: String. Optional name of the operation. Defaults to `"CosineDecay"`.
*   **warmup\_target**: A Python float. The target learning rate for our warmup phase. Will cast to the `initial_learning_rate` datatype. Setting to `None` will skip warmup and begins decay phase from `initial_learning_rate`. Otherwise scheduler will warmup from `initial_learning_rate` to `warmup_target`.
*   **warmup\_steps**: A Python int. Number of steps to warmup over.

**Returns**

A 1-arg callable learning rate schedule that takes the current optimizer step and outputs the decayed learning rate, a scalar tensor of the same type as `initial_learning_rate`.

* * *

[CosineDecay](https://keras.io/api/optimizers/learning_rate_schedules/cosine_decay/#cosinedecay)

[`CosineDecay` class](https://keras.io/api/optimizers/learning_rate_schedules/cosine_decay/#cosinedecay-class)