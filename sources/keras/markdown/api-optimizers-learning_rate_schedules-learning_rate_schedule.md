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
 / LearningRateSchedule

LearningRateSchedule
====================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/schedules/learning_rate_schedule.py#L10)

### `LearningRateSchedule` class

Copied!

`keras.optimizers.schedules.LearningRateSchedule()`

The learning rate schedule base class.

You can use a learning rate schedule to modulate how the learning rate of your optimizer changes over time.

Several built-in learning rate schedules are available, such as [`keras.optimizers.schedules.ExponentialDecay`](https://keras.io/api/optimizers/learning_rate_schedules/exponential_decay#exponentialdecay-class)
 or [`keras.optimizers.schedules.PiecewiseConstantDecay`](https://keras.io/api/optimizers/learning_rate_schedules/piecewise_constant_decay#piecewiseconstantdecay-class)
:

Copied!

`lr_schedule = keras.optimizers.schedules.ExponentialDecay(     initial_learning_rate=1e-2,     decay_steps=10000,     decay_rate=0.9) optimizer = keras.optimizers.SGD(learning_rate=lr_schedule)`

A `LearningRateSchedule` instance can be passed in as the `learning_rate` argument of any optimizer.

To implement your own schedule object, you should implement the `__call__` method, which takes a `step` argument (scalar integer tensor, the current training step count). Like for any other Keras object, you can also optionally make your object serializable by implementing the `get_config` and `from_config` methods.

**Example**

Copied!

`class MyLRSchedule(keras.optimizers.schedules.LearningRateSchedule):      def __init__(self, initial_learning_rate):         self.initial_learning_rate = initial_learning_rate      def __call__(self, step):         return self.initial_learning_rate / (step + 1)  optimizer = keras.optimizers.SGD(learning_rate=MyLRSchedule(0.1))`

* * *

[LearningRateSchedule](https://keras.io/api/optimizers/learning_rate_schedules/learning_rate_schedule/#learningrateschedule)

[`LearningRateSchedule` class](https://keras.io/api/optimizers/learning_rate_schedules/learning_rate_schedule/#learningrateschedule-class)