None

[KerasTuner: Hyperparam Tuning](https://keras.io/keras_tuner/)

[Getting started](https://keras.io/keras_tuner/getting_started/)
 [Developer guides](https://keras.io/keras_tuner/guides/)
 [API documentation](https://keras.io/keras_tuner/api/)
 [HyperParameters](https://keras.io/keras_tuner/api/hyperparameters/)
 [Tuners](https://keras.io/keras_tuner/api/tuners/)
 [Oracles](https://keras.io/keras_tuner/api/oracles/)
 [HyperModels](https://keras.io/keras_tuner/api/hypermodels/)
 [Errors](https://keras.io/keras_tuner/api/errors/)

► [KerasTuner: Hyperparam Tuning](https://keras.io/keras_tuner/)
 / [API documentation](https://keras.io/keras_tuner/api/)
 / HyperParameters

HyperParameters
===============

[\[source\]](https://github.com/keras-team/keras-tuner/tree/v1.4.8/keras_tuner/src/engine/hyperparameters/hyperparameters.py#L29)

### `HyperParameters` class

Copied!

`keras_tuner.HyperParameters()`

Container for both a hyperparameter space, and current values.

A `HyperParameters` instance can be pass to `HyperModel.build(hp)` as an argument to build a model.

To prevent the users from depending on inactive hyperparameter values, only active hyperparameters should have values in `HyperParameters.values`.

**Attributes**

*   **space**: A list of `HyperParameter` objects.
*   **values**: A dict mapping hyperparameter names to current values.

* * *

[\[source\]](https://github.com/keras-team/keras-tuner/tree/v1.4.8/keras_tuner/src/engine/hyperparameters/hyperparameters.py#L496)

### `Boolean` method

Copied!

`HyperParameters.Boolean(name, default=False, parent_name=None, parent_values=None)`

Choice between True and False.

**Arguments**

*   **name**: A string. the name of parameter. Must be unique for each `HyperParameter` instance in the search space.
*   **default**: Boolean, the default value to return for the parameter. If unspecified, the default value will be False.
*   **parent\_name**: Optional string, specifying the name of the parent `HyperParameter` to use as the condition to activate the current `HyperParameter`.
*   **parent\_values**: Optional list of the values of the parent `HyperParameter` to use as the condition to activate the current `HyperParameter`.

**Returns**

The value of the hyperparameter, or None if the hyperparameter is not active.

* * *

[\[source\]](https://github.com/keras-team/keras-tuner/tree/v1.4.8/keras_tuner/src/engine/hyperparameters/hyperparameters.py#L258)

### `Choice` method

Copied!

`HyperParameters.Choice(     name, values, ordered=None, default=None, parent_name=None, parent_values=None )`

Choice of one value among a predefined set of possible values.

**Arguments**

*   **name**: A string. the name of parameter. Must be unique for each `HyperParameter` instance in the search space.
*   **values**: A list of possible values. Values must be int, float, str, or bool. All values must be of the same type.
*   **ordered**: Optional boolean, whether the values passed should be considered to have an ordering. Defaults to `True` for float/int values. Must be `False` for any other values.
*   **default**: Optional default value to return for the parameter. If unspecified, the default value will be:
    *   None if None is one of the choices in `values`
    *   The first entry in `values` otherwise.
*   **parent\_name**: Optional string, specifying the name of the parent `HyperParameter` to use as the condition to activate the current `HyperParameter`.
*   **parent\_values**: Optional list of the values of the parent `HyperParameter` to use as the condition to activate the current `HyperParameter`.

**Returns**

The value of the hyperparameter, or None if the hyperparameter is not active.

* * *

[\[source\]](https://github.com/keras-team/keras-tuner/tree/v1.4.8/keras_tuner/src/engine/hyperparameters/hyperparameters.py#L525)

### `Fixed` method

Copied!

`HyperParameters.Fixed(name, value, parent_name=None, parent_values=None)`

Fixed, untunable value.

**Arguments**

*   **name**: A string. the name of parameter. Must be unique for each `HyperParameter` instance in the search space.
*   **value**: The value to use (can be any JSON-serializable Python type).
*   **parent\_name**: Optional string, specifying the name of the parent `HyperParameter` to use as the condition to activate the current `HyperParameter`.
*   **parent\_values**: Optional list of the values of the parent `HyperParameter` to use as the condition to activate the current `HyperParameter`.

**Returns**

The value of the hyperparameter, or None if the hyperparameter is not active.

* * *

[\[source\]](https://github.com/keras-team/keras-tuner/tree/v1.4.8/keras_tuner/src/engine/hyperparameters/hyperparameters.py#L401)

### `Float` method

Copied!

`HyperParameters.Float(     name,     min_value,     max_value,     step=None,     sampling="linear",     default=None,     parent_name=None,     parent_values=None, )`

Floating point value hyperparameter.

Example #1:

Copied!

`hp.Float(     "image_rotation_factor",     min_value=0,     max_value=1)`

All values in interval \[0, 1\] have equal probability of being sampled.

Example #2:

Copied!

`hp.Float(     "image_rotation_factor",     min_value=0,     max_value=1,     step=0.2)`

`step` is the minimum distance between samples. The possible values are \[0, 0.2, 0.4, 0.6, 0.8, 1.0\].

Example #3:

Copied!

`hp.Float(     "learning_rate",     min_value=0.001,     max_value=10,     step=10,     sampling="log")`

When `sampling="log"`, the `step` is multiplied between samples. The possible values are \[0.001, 0.01, 0.1, 1, 10\].

**Arguments**

*   **name**: A string. the name of parameter. Must be unique for each `HyperParameter` instance in the search space.
*   **min\_value**: Float, the lower bound of the range.
*   **max\_value**: Float, the upper bound of the range.
*   **step**: Optional float, the distance between two consecutive samples in the range. If left unspecified, it is possible to sample any value in the interval. If `sampling="linear"`, it will be the minimum additve between two samples. If `sampling="log"`, it will be the minimum multiplier between two samples.
*   **sampling**: String. One of "linear", "log", "reverse\_log". Defaults to "linear". When sampling value, it always start from a value in range \[0.0, 1.0). The `sampling` argument decides how the value is projected into the range of \[min\_value, max\_value\]. "linear": min\_value + value \* (max\_value - min\_value) "log": min\_value \* (max\_value / min\_value) ^ value "reverse\_log": (max\_value - min\_value \* ((max\_value / min\_value) ^ (1 - value) - 1))\
*   **default**: Float, the default value to return for the parameter. If unspecified, the default value will be `min_value`.\
*   **parent\_name**: Optional string, specifying the name of the parent `HyperParameter` to use as the condition to activate the current `HyperParameter`.\
*   **parent\_values**: Optional list of the values of the parent `HyperParameter` to use as the condition to activate the current `HyperParameter`.\
\
**Returns**\
\
The value of the hyperparameter, or None if the hyperparameter is not active.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras-tuner/tree/v1.4.8/keras_tuner/src/engine/hyperparameters/hyperparameters.py#L302)\
\
### `Int` method\
\
Copied!\
\
`HyperParameters.Int(     name,     min_value,     max_value,     step=None,     sampling="linear",     default=None,     parent_name=None,     parent_values=None, )`\
\
Integer hyperparameter.\
\
Note that unlike Python's `range` function, `max_value` is _included_ in the possible values this parameter can take on.\
\
Example #1:\
\
Copied!\
\
`hp.Int(     "n_layers",     min_value=6,     max_value=12)`\
\
The possible values are \[6, 7, 8, 9, 10, 11, 12\].\
\
Example #2:\
\
Copied!\
\
`hp.Int(     "n_layers",     min_value=6,     max_value=13,     step=3)`\
\
`step` is the minimum distance between samples. The possible values are \[6, 9, 12\].\
\
Example #3:\
\
Copied!\
\
`hp.Int(     "batch_size",     min_value=2,     max_value=32,     step=2,     sampling="log")`\
\
When `sampling="log"` the `step` is multiplied between samples. The possible values are \[2, 4, 8, 16, 32\].\
\
**Arguments**\
\
*   **name**: A string. the name of parameter. Must be unique for each `HyperParameter` instance in the search space.\
*   **min\_value**: Integer, the lower limit of range, inclusive.\
*   **max\_value**: Integer, the upper limit of range, inclusive.\
*   **step**: Optional integer, the distance between two consecutive samples in the range. If left unspecified, it is possible to sample any integers in the interval. If `sampling="linear"`, it will be the minimum additve between two samples. If `sampling="log"`, it will be the minimum multiplier between two samples.\
*   **sampling**: String. One of "linear", "log", "reverse\_log". Defaults to "linear". When sampling value, it always start from a value in range \[0.0, 1.0). The `sampling` argument decides how the value is projected into the range of \[min\_value, max\_value\]. "linear": min\_value + value \* (max\_value - min\_value) "log": min\_value \* (max\_value / min\_value) ^ value "reverse\_log": (max\_value - min\_value \* ((max\_value / min\_value) ^ (1 - value) - 1))\
*   **default**: Integer, default value to return for the parameter. If unspecified, the default value will be `min_value`.\
*   **parent\_name**: Optional string, specifying the name of the parent `HyperParameter` to use as the condition to activate the current `HyperParameter`.\
*   **parent\_values**: Optional list of the values of the parent `HyperParameter` to use as the condition to activate the current `HyperParameter`.\
\
**Returns**\
\
The value of the hyperparameter, or None if the hyperparameter is not active.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras-tuner/tree/v1.4.8/keras_tuner/src/engine/hyperparameters/hyperparameters.py#L87)\
\
### `conditional_scope` method\
\
Copied!\
\
`HyperParameters.conditional_scope(parent_name, parent_values)`\
\
Opens a scope to create conditional HyperParameters.\
\
All `HyperParameter`s created under this scope will only be active when the parent `HyperParameter` specified by `parent_name` is equal to one of the values passed in `parent_values`.\
\
When the condition is not met, creating a `HyperParameter` under this scope will register the `HyperParameter`, but will return `None` rather than a concrete value.\
\
Note that any Python code under this scope will execute regardless of whether the condition is met.\
\
This feature is for the `Tuner` to collect more information of the search space and the current trial. It is especially useful for model selection. If the parent `HyperParameter` is for model selection, the `HyperParameter`s in a model should only be active when the model selected, which can be implemented using `conditional_scope`.\
\
**Examples**\
\
Copied!\
\
`def MyHyperModel(HyperModel):     def build(self, hp):         model = Sequential()         model.add(Input(shape=(32, 32, 3)))         model_type = hp.Choice("model_type", ["mlp", "cnn"])         with hp.conditional_scope("model_type", ["mlp"]):             if model_type == "mlp":                 model.add(Flatten())                 model.add(Dense(32, activation='relu'))         with hp.conditional_scope("model_type", ["cnn"]):             if model_type == "cnn":                 model.add(Conv2D(64, 3, activation='relu'))                 model.add(GlobalAveragePooling2D())         model.add(Dense(10, activation='softmax'))         return model`\
\
**Arguments**\
\
*   **parent\_name**: A string, specifying the name of the parent `HyperParameter` to use as the condition to activate the current `HyperParameter`.\
*   **parent\_values**: A list of the values of the parent `HyperParameter` to use as the condition to activate the current `HyperParameter`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras-tuner/tree/v1.4.8/keras_tuner/src/engine/hyperparameters/hyperparameters.py#L238)\
\
### `get` method\
\
Copied!\
\
`HyperParameters.get(name)`\
\
Return the current value of this hyperparameter set.\
\
* * *\
\
[HyperParameters](https://keras.io/keras_tuner/api/hyperparameters/#hyperparameters)\
\
[`HyperParameters` class](https://keras.io/keras_tuner/api/hyperparameters/#hyperparameters-class)\
\
[`Boolean` method](https://keras.io/keras_tuner/api/hyperparameters/#boolean-method)\
\
[`Choice` method](https://keras.io/keras_tuner/api/hyperparameters/#choice-method)\
\
[`Fixed` method](https://keras.io/keras_tuner/api/hyperparameters/#fixed-method)\
\
[`Float` method](https://keras.io/keras_tuner/api/hyperparameters/#float-method)\
\
[`Int` method](https://keras.io/keras_tuner/api/hyperparameters/#int-method)\
\
[`conditional_scope` method](https://keras.io/keras_tuner/api/hyperparameters/#conditionalscope-method)\
\
[`get` method](https://keras.io/keras_tuner/api/hyperparameters/#get-method)