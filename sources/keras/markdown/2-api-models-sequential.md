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
 / The Sequential class

The Sequential class
====================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/engine/sequential.py#L47)

### `Sequential` class

Copied!

`tf_keras.Sequential(layers=None, name=None)`

`Sequential` groups a linear stack of layers into a [`tf.keras.Model`](https://www.tensorflow.org/api_docs/python/tf/keras/Model)
.

`Sequential` provides training and inference features on this model.

**Examples**

Copied!

``model = tf.keras.Sequential() model.add(tf.keras.Input(shape=(16,))) model.add(tf.keras.layers.Dense(8))  # Note that you can also omit the initial `Input`. # In that case the model doesn't have any weights until the first call # to a training/evaluation method (since it isn't yet built): model = tf.keras.Sequential() model.add(tf.keras.layers.Dense(8)) model.add(tf.keras.layers.Dense(4)) # model.weights not created yet  # Whereas if you specify an `Input`, the model gets built # continuously as you are adding layers: model = tf.keras.Sequential() model.add(tf.keras.Input(shape=(16,))) model.add(tf.keras.layers.Dense(4)) len(model.weights) # Returns "2"  # When using the delayed-build pattern (no input shape specified), you can # choose to manually build your model by calling # `build(batch_input_shape)`: model = tf.keras.Sequential() model.add(tf.keras.layers.Dense(8)) model.add(tf.keras.layers.Dense(4)) model.build((None, 16)) len(model.weights) # Returns "4"  # Note that when using the delayed-build pattern (no input shape specified), # the model gets built the first time you call `fit`, `eval`, or `predict`, # or the first time you call the model on some input data. model = tf.keras.Sequential() model.add(tf.keras.layers.Dense(8)) model.add(tf.keras.layers.Dense(1)) model.compile(optimizer='sgd', loss='mse') # This builds the model for the first time: model.fit(x, y, batch_size=32, epochs=10)``

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/engine/sequential.py#L148)

### `add` method

Copied!

`Sequential.add(layer)`

Adds a layer instance on top of the layer stack.

**Arguments**

*   **layer**: layer instance.

**Raises**

*   **TypeError**: If `layer` is not a layer instance.
*   **ValueError**: In case the `layer` argument does not know its input shape.
*   **ValueError**: In case the `layer` argument has multiple output tensors, or is already connected somewhere else (forbidden in `Sequential` models).

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/engine/sequential.py#L243)

### `pop` method

Copied!

`Sequential.pop()`

Removes the last layer in the model.

**Raises**

*   **TypeError**: if there are no layers in the model.

* * *

[The Sequential class](https://keras.io/2/api/models/sequential/#the-sequential-class)

[`Sequential` class](https://keras.io/2/api/models/sequential/#sequential-class)

[`add` method](https://keras.io/2/api/models/sequential/#add-method)

[`pop` method](https://keras.io/2/api/models/sequential/#pop-method)