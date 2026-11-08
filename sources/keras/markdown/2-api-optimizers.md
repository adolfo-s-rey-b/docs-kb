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
 / Optimizers

Optimizers
==========

*   [SGD](https://keras.io/2/api/optimizers/sgd/)
    
*   [RMSprop](https://keras.io/2/api/optimizers/rmsprop/)
    
*   [Adam](https://keras.io/2/api/optimizers/adam/)
    
*   [AdamW](https://keras.io/2/api/optimizers/adamw/)
    
*   [Adadelta](https://keras.io/2/api/optimizers/adadelta/)
    
*   [Adagrad](https://keras.io/2/api/optimizers/adagrad/)
    
*   [Adamax](https://keras.io/2/api/optimizers/adamax/)
    
*   [Adafactor](https://keras.io/2/api/optimizers/adafactor/)
    
*   [Nadam](https://keras.io/2/api/optimizers/Nadam/)
    
*   [Ftrl](https://keras.io/2/api/optimizers/ftrl/)
    

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/optimizers/optimizer.py#L1272)

### `apply_gradients` method

Copied!

`Optimizer.apply_gradients(     grads_and_vars, name=None, skip_gradients_aggregation=False, **kwargs )`

Apply gradients to variables.

**Arguments**

*   **grads\_and\_vars**: List of `(gradient, variable)` pairs.
*   **name**: string, defaults to None. The name of the namescope to use when creating variables. If None, `self.name` will be used.
*   **skip\_gradients\_aggregation**: If true, gradients aggregation will not be performed inside optimizer. Usually this arg is set to True when you write custom code aggregating gradients outside the optimizer.
*   **\*\*kwargs**: keyword arguments only used for backward compatibility.

**Returns**

A [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
, representing the current iteration.

**Raises**

*   **TypeError**: If `grads_and_vars` is malformed.
*   **RuntimeError**: If called in a cross-replica context.

* * *

### `variables` property

Copied!

`tf_keras.optimizers.Optimizer.variables`

Returns variables of this optimizer.

* * *

[Optimizers](https://keras.io/2/api/optimizers/#optimizers)

[`apply_gradients` method](https://keras.io/2/api/optimizers/#applygradients-method)

[`variables` property](https://keras.io/2/api/optimizers/#variables-property)