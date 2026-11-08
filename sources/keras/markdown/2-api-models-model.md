None

[Keras 3 API documentation](https://keras.io/api/)
 [Keras 2 API documentation](https://keras.io/2/api/)

[Models API](https://keras.io/2/api/models/)
 [The Model class](https://keras.io/2/api/models/model/)
 [The Sequential class](https://keras.io/2/api/models/sequential/)
 [Model training APIs](https://keras.io/2/api/models/model_training_apis/)
 [Saving & serialization](https://keras.io/2/api/models/model_saving_apis/)
 [Layers API](https://keras.io/2/api/layers/)
 [Callbacks API](https://keras.io/2/api/callbacks/)
 [Optimizers](https://keras.io/2/api/optimizers/)
 [Metrics](https://keras.io/2/api/metrics/)
 [Losses](https://keras.io/2/api/losses/)
 [Data loading](https://keras.io/2/api/data_loading/)
 [Built-in small datasets](https://keras.io/2/api/datasets/)
 [Keras Applications](https://keras.io/2/api/applications/)
 [Mixed precision](https://keras.io/2/api/mixed_precision/)
 [Utilities](https://keras.io/2/api/utils/)

► [Keras 2 API documentation](https://keras.io/2/api/)
 / [Models API](https://keras.io/2/api/models/)
 / The Model class

The Model class
===============

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/engine/training.py#L70)

### `Model` class

Copied!

`tf_keras.Model()`

A model grouping layers into an object with training/inference features.

**Arguments**

*   **inputs**: The input(s) of the model: a [`keras.Input`](https://keras.io/api/layers/core_layers/input#input-function)
     object or a combination of [`keras.Input`](https://keras.io/api/layers/core_layers/input#input-function)
     objects in a dict, list or tuple.
*   **outputs**: The output(s) of the model: a tensor that originated from [`keras.Input`](https://keras.io/api/layers/core_layers/input#input-function)
     objects or a combination of such tensors in a dict, list or tuple. See Functional API example below.
*   **name**: String, the name of the model.

There are two ways to instantiate a `Model`:

1 - With the "Functional API", where you start from `Input`, you chain layer calls to specify the model's forward pass, and finally you create your model from inputs and outputs:

Copied!

`import tensorflow as tf  inputs = tf.keras.Input(shape=(3,)) x = tf.keras.layers.Dense(4, activation=tf.nn.relu)(inputs) outputs = tf.keras.layers.Dense(5, activation=tf.nn.softmax)(x) model = tf.keras.Model(inputs=inputs, outputs=outputs)`

Note: Only dicts, lists, and tuples of input tensors are supported. Nested inputs are not supported (e.g. lists of list or dicts of dict).

A new Functional API model can also be created by using the intermediate tensors. This enables you to quickly extract sub-components of the model.

**Example**

Copied!

`inputs = keras.Input(shape=(None, None, 3)) processed = keras.layers.RandomCrop(width=32, height=32)(inputs) conv = keras.layers.Conv2D(filters=2, kernel_size=3)(processed) pooling = keras.layers.GlobalAveragePooling2D()(conv) feature = keras.layers.Dense(10)(pooling)  full_model = keras.Model(inputs, feature) backbone = keras.Model(processed, conv) activations = keras.Model(conv, feature)`

Note that the `backbone` and `activations` models are not created with [`keras.Input`](https://keras.io/api/layers/core_layers/input#input-function)
 objects, but with the tensors that are originated from [`keras.Input`](https://keras.io/api/layers/core_layers/input#input-function)
 objects. Under the hood, the layers and weights will be shared across these models, so that user can train the `full_model`, and use `backbone` or `activations` to do feature extraction. The inputs and outputs of the model can be nested structures of tensors as well, and the created models are standard Functional API models that support all the existing APIs.

2 - By subclassing the `Model` class: in that case, you should define your layers in `__init__()` and you should implement the model's forward pass in `call()`.

Copied!

`import tensorflow as tf  class MyModel(tf.keras.Model):    def __init__(self):     super().__init__()     self.dense1 = tf.keras.layers.Dense(4, activation=tf.nn.relu)     self.dense2 = tf.keras.layers.Dense(5, activation=tf.nn.softmax)    def call(self, inputs):     x = self.dense1(inputs)     return self.dense2(x)  model = MyModel()`

If you subclass `Model`, you can optionally have a `training` argument (boolean) in `call()`, which you can use to specify a different behavior in training and inference:

Copied!

`import tensorflow as tf  class MyModel(tf.keras.Model):    def __init__(self):     super().__init__()     self.dense1 = tf.keras.layers.Dense(4, activation=tf.nn.relu)     self.dense2 = tf.keras.layers.Dense(5, activation=tf.nn.softmax)     self.dropout = tf.keras.layers.Dropout(0.5)    def call(self, inputs, training=False):     x = self.dense1(inputs)     if training:       x = self.dropout(x, training=training)     return self.dense2(x)  model = MyModel()`

Once the model is created, you can config the model with losses and metrics with `model.compile()`, train the model with `model.fit()`, or use the model to do prediction with `model.predict()`.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/engine/training.py#L3461)

### `summary` method

Copied!

`Model.summary(     line_length=None,     positions=None,     print_fn=None,     expand_nested=False,     show_trainable=False,     layer_range=None, )`

Prints a string summary of the network.

**Arguments**

*   **line\_length**: Total length of printed lines (e.g. set this to adapt the display to different terminal window sizes).
*   **positions**: Relative or absolute positions of log elements in each line. If not provided, becomes `[0.3, 0.6, 0.70, 1.]`. Defaults to `None`.
*   **print\_fn**: Print function to use. By default, prints to `stdout`. If `stdout` doesn't work in your environment, change to `print`. It will be called on each line of the summary. You can set it to a custom function in order to capture the string summary.
*   **expand\_nested**: Whether to expand the nested models. Defaults to `False`.
*   **show\_trainable**: Whether to show if a layer is trainable. Defaults to `False`.
*   **layer\_range**: a list or tuple of 2 strings, which is the starting layer name and ending layer name (both inclusive) indicating the range of layers to be printed in summary. It also accepts regex patterns instead of exact name. In such case, start predicate will be the first element it matches to `layer_range[0]` and the end predicate will be the last element it matches to `layer_range[1]`. By default `None` which considers all layers of model.

**Raises**

*   **ValueError**: if `summary()` is called before the model is built.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/engine/training.py#L3527)

### `get_layer` method

Copied!

`Model.get_layer(name=None, index=None)`

Retrieves a layer based on either its name (unique) or index.

If `name` and `index` are both provided, `index` will take precedence. Indices are based on order of horizontal graph traversal (bottom-up).

**Arguments**

*   **name**: String, name of layer.
*   **index**: Integer, index of layer.

**Returns**

A layer instance.

* * *

[The Model class](https://keras.io/2/api/models/model/#the-model-class)

[`Model` class](https://keras.io/2/api/models/model/#model-class)

[`summary` method](https://keras.io/2/api/models/model/#summary-method)

[`get_layer` method](https://keras.io/2/api/models/model/#getlayer-method)