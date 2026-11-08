None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [The Model class](https://keras.io/api/models/model/)
 [The Sequential class](https://keras.io/api/models/sequential/)
 [Model training APIs](https://keras.io/api/models/model_training_apis/)
 [Saving & serialization](https://keras.io/api/models/model_saving_apis/)
 [Knowledge distillation](https://keras.io/api/models/distillation/)
 [Layers API](https://keras.io/api/layers/)
 [Callbacks API](https://keras.io/api/callbacks/)
 [Ops API](https://keras.io/api/ops/)
 [Optimizers](https://keras.io/api/optimizers/)
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
 / [Models API](https://keras.io/api/models/)
 / The Sequential class

The Sequential class
====================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/models/sequential.py#L19)

### `Sequential` class

Copied!

`keras.Sequential(layers=None, trainable=True, name=None)`

`Sequential` groups a linear stack of layers into a `Model`.

**Examples**

Copied!

``model = keras.Sequential() model.add(keras.Input(shape=(16,))) model.add(keras.layers.Dense(8))  # Note that you can also omit the initial `Input`. # In that case the model doesn't have any weights until the first call # to a training/evaluation method (since it isn't yet built): model = keras.Sequential() model.add(keras.layers.Dense(8)) model.add(keras.layers.Dense(4)) # model.weights not created yet  # Whereas if you specify an `Input`, the model gets built # continuously as you are adding layers: model = keras.Sequential() model.add(keras.Input(shape=(16,))) model.add(keras.layers.Dense(8)) len(model.weights)  # Returns "2"  # When using the delayed-build pattern (no input shape specified), you can # choose to manually build your model by calling # `build(batch_input_shape)`: model = keras.Sequential() model.add(keras.layers.Dense(8)) model.add(keras.layers.Dense(4)) model.build((None, 16)) len(model.weights)  # Returns "4"  # Note that when using the delayed-build pattern (no input shape specified), # the model gets built the first time you call `fit`, `eval`, or `predict`, # or the first time you call the model on some input data. model = keras.Sequential() model.add(keras.layers.Dense(8)) model.add(keras.layers.Dense(1)) model.compile(optimizer='sgd', loss='mse') # This builds the model for the first time: model.fit(x, y, batch_size=32, epochs=10)``

**Guides and examples using `Sequential`**

*   [The Sequential model](https://keras.io/guides/sequential_model/)
    
*   [Customizing `fit()` with TensorFlow](https://keras.io/guides/custom_train_step_in_tensorflow/)
    
*   [Customizing `fit()` with PyTorch](https://keras.io/guides/custom_train_step_in_torch/)
    
*   [Writing a custom training loop in TensorFlow](https://keras.io/guides/writing_a_custom_training_loop_in_tensorflow/)
    
*   [Serialization & saving](https://keras.io/guides/serialization_and_saving/)
    
*   [Customizing saving & serialization](https://keras.io/guides/customizing_saving_and_serialization/)
    
*   [Writing your own callbacks](https://keras.io/guides/writing_your_own_callbacks/)
    
*   [Transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
    

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/models/sequential.py#L78)

### `add` method

Copied!

`Sequential.add(layer, rebuild=True)`

Adds a layer instance on top of the layer stack.

**Arguments**

*   **layer**: layer instance.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/models/sequential.py#L127)

### `pop` method

Copied!

`Sequential.pop(rebuild=True)`

Removes the last layer in the model.

**Arguments**

*   **rebuild**: `bool`. Whether to rebuild the model after removing the layer. Defaults to `True`.

**Returns**

*   **layer**: layer instance.

* * *

[The Sequential class](https://keras.io/api/models/sequential/#the-sequential-class)

[`Sequential` class](https://keras.io/api/models/sequential/#sequential-class)

[`add` method](https://keras.io/api/models/sequential/#add-method)

[`pop` method](https://keras.io/api/models/sequential/#pop-method)