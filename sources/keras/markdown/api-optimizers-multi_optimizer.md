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
 / MultiOptimizer

MultiOptimizer
==============

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/multi_optimizer.py#L161)

### `MultiOptimizer` class

Copied!

`keras.optimizers.MultiOptimizer(optimizer_map, loss_scale_factor=None, name=None)`

An optimizer wrapper that delegates variables to different optimizers.

Initialize the object with an OptimizerMap instance or a callable function that returns an optimizer for a given variable.

**Example**

model.compile( optimizer=MultiOptimizer( OptimizerMap(default\_optimizer=optimizers.SGD(), {"encoder/.\*": optimizers.Adam()}) ), loss="binary\_crossentropy", )

Or using a callable
===================

def optimizer\_selector(variable): if "encoder" in variable.path: return optimizers.Adam() else: return optimizers.SGD()

model.compile( optimizer=MultiOptimizer(optimizer\_selector), loss="binary\_crossentropy", )

To access the attributes of the sub-optimizers, iterate over the optimizers using `.optimizers`:

For example:

optimizer = MultiOptimizer(OptimizerMap( default\_optimizer=optimizers.Adam() )) optimizer\['.encoder'\] = optimizers.SGD()

for optim in optimizer.optimizers: print(optim.learning\_rate) print(optim.iterations) print(optim.loss\_scale\_factor) ...

The MultiOptimizer class instances will not expose `learning_rate` attribute and will raise an error if accessed. This is because the learning rate might be different for different sub-optimizers.

Note: Optimizer-specific callbacks are not supported yet.

* * *

[MultiOptimizer](https://keras.io/api/optimizers/multi_optimizer/#multioptimizer)

[`MultiOptimizer` class](https://keras.io/api/optimizers/multi_optimizer/#multioptimizer-class)

[Or using a callable](https://keras.io/api/optimizers/multi_optimizer/#or-using-a-callable)