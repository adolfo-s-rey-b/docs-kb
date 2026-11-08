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
 / Optimizers

Optimizers
==========

Available optimizers
--------------------

*   [SGD](https://keras.io/api/optimizers/sgd/)
    
*   [RMSprop](https://keras.io/api/optimizers/rmsprop/)
    
*   [Adam](https://keras.io/api/optimizers/adam/)
    
*   [AdamW](https://keras.io/api/optimizers/adamw/)
    
*   [Adadelta](https://keras.io/api/optimizers/adadelta/)
    
*   [Adagrad](https://keras.io/api/optimizers/adagrad/)
    
*   [Adamax](https://keras.io/api/optimizers/adamax/)
    
*   [Adafactor](https://keras.io/api/optimizers/adafactor/)
    
*   [Nadam](https://keras.io/api/optimizers/Nadam/)
    
*   [Ftrl](https://keras.io/api/optimizers/ftrl/)
    
*   [Lion](https://keras.io/api/optimizers/lion/)
    
*   [Lamb](https://keras.io/api/optimizers/lamb/)
    
*   [Loss Scale Optimizer](https://keras.io/api/optimizers/loss_scale_optimizer/)
    
*   [MultiOptimizer](https://keras.io/api/optimizers/multi_optimizer/)
    
*   [OptimizerMap](https://keras.io/api/optimizers/optimizer_map/)
    
*   [Muon](https://keras.io/api/optimizers/muon/)
    

* * *

Usage with `compile()` & `fit()`
--------------------------------

An optimizer is one of the two arguments required for compiling a Keras model:

Copied!

`import keras from keras import layers  model = keras.Sequential() model.add(layers.Dense(64, kernel_initializer='uniform', input_shape=(10,))) model.add(layers.Activation('softmax'))  opt = keras.optimizers.Adam(learning_rate=0.01) model.compile(loss='categorical_crossentropy', optimizer=opt)`

You can either instantiate an optimizer before passing it to `model.compile()` , as in the above example, or you can pass it by its string identifier. In the latter case, the default parameters for the optimizer will be used.

Copied!

`# pass optimizer by name: default parameters will be used model.compile(loss='categorical_crossentropy', optimizer='adam')`

* * *

Learning rate decay / scheduling
--------------------------------

You can use a [learning rate schedule](https://keras.io/api/optimizers/learning_rate_schedules)
 to modulate how the learning rate of your optimizer changes over time:

Copied!

`lr_schedule = keras.optimizers.schedules.ExponentialDecay(     initial_learning_rate=1e-2,     decay_steps=10000,     decay_rate=0.9) optimizer = keras.optimizers.SGD(learning_rate=lr_schedule)`

Check out [the learning rate schedule API documentation](https://keras.io/api/optimizers/learning_rate_schedules)
 for a list of available schedules.

* * *

Base Optimizer API
------------------

These methods and attributes are common to all Keras optimizers.

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/optimizer.py#L21)

### `Optimizer` class

Copied!

`keras.optimizers.Optimizer()`

Abstract optimizer base class.

If you intend to create your own optimization algorithm, please inherit from this class and override the following methods:

*   `build`: Create your optimizer-related variables, such as momentum variables in the SGD optimizer.
*   `update_step`: Implement your optimizer's variable updating logic.
*   `get_config`: serialization of the optimizer.

**Example**

Copied!

`class SGD(Optimizer):     def __init__(self, **kwargs):         super().__init__(**kwargs)         self.momentum = 0.9      def build(self, variables):         super().build(variables)         self.momentums = []         for variable in variables:             self.momentums.append(                 self.add_variable_from_reference(                     reference_variable=variable, name="momentum"                 )             )      def update_step(self, gradient, variable, learning_rate):         learning_rate = ops.cast(learning_rate, variable.dtype)         gradient = ops.cast(gradient, variable.dtype)         m = self.momentums[self._get_variable_index(variable)]         self.assign(             m,             ops.subtract(                 ops.multiply(m, ops.cast(self.momentum, variable.dtype)),                 ops.multiply(gradient, learning_rate),             ),         )         self.assign_add(variable, m)      def get_config(self):         config = super().get_config()         config.update(             {                 "momentum": self.momentum,                 "nesterov": self.nesterov,             }         )         return config`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/base_optimizer.py#L460)

### `apply_gradients` method

Copied!

`Optimizer.apply_gradients(grads_and_vars)`

* * *

### `variables` property

Copied!

`keras.optimizers.Optimizer.variables`

* * *

[Optimizers](https://keras.io/api/optimizers/#optimizers)

[Available optimizers](https://keras.io/api/optimizers/#available-optimizers)

[Usage with `compile()` & `fit()`](https://keras.io/api/optimizers/#usage-with-compile-amp-fit)

[Learning rate decay / scheduling](https://keras.io/api/optimizers/#learning-rate-decay--scheduling)

[Base Optimizer API](https://keras.io/api/optimizers/#base-optimizer-api)

[`Optimizer` class](https://keras.io/api/optimizers/#optimizer-class)

[`apply_gradients` method](https://keras.io/api/optimizers/#applygradients-method)

[`variables` property](https://keras.io/api/optimizers/#variables-property)