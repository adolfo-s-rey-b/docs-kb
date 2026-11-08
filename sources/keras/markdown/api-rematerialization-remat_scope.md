None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
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
 [RematScope](https://keras.io/api/rematerialization/remat_scope/)
 [Remat](https://keras.io/api/rematerialization/remat/)
 [Utilities](https://keras.io/api/utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

► [Keras 3 API documentation](https://keras.io/api/)
 / [Rematerialization](https://keras.io/api/rematerialization/)
 / RematScope

RematScope
==========

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/remat.py#L8)

### `RematScope` class

Copied!

`keras.RematScope(mode="full", output_size_threshold=1024, layer_names=None)`

A context manager for enabling rematerialization in Keras.

Rematerialization (gradient checkpointing) trades memory for computation by recomputing intermediate activations during the backward pass. This is particularly useful for training large models or large batch sizes within limited memory constraints.

This should be used when initializing the layer (e.g., `layer(input)`). Rematerialization applies at execution time, not at creation time.

**Arguments**

*   **mode**: Rematerialization mode to apply. Options:
    *   `"full"`: Apply rematerialization globally to all supported operations.
    *   `"activations"`: Apply rematerialization to activations on any layers that contain `keras.activations` (e.g., `Dense(..., activation=relu)`).
    *   `"larger_than"`: Apply rematerialization to layers with output sizes larger than `output_size_threshold`.
    *   `"list_of_layers"`: Apply rematerialization to a specific list of layer names.
    *   `None`: Disable rematerialization.
*   **output\_size\_threshold**: Output size threshold for the `"larger_than"` mode. Layers producing outputs larger than this threshold will be rematerialized. Default is `1024`.
*   **layer\_names**: List of layer names for the `"list_of_layers"` mode. Default is an empty list.

**Examples**

Using "list\_of\_layers" mode:

Copied!

`from keras import RematScope input_tensor = tf.random.normal((1, 32, 32, 3)) with RematScope(mode="list_of_layers", layer_names=["dense_1", "conv2d_1"]):     layer1 = keras.layers.Dense(128, name="dense_1")     layer2 = keras.layers.Conv2D(64, (3, 3), name="conv2d_1")     layer3 = keras.layers.Dense(64, name="dense_2")     # Only layer1 and layer2 will apply rematerialization     output1 = layer1(input_tensor)     output2 = layer2(output1)     output3 = layer3(output2)`

Using "larger\_than" mode with a specific output size threshold:

Copied!

`with RematScope(mode="larger_than", output_size_threshold=2048):     layer = keras.layers.Conv2D(64, (3, 3))     output = layer(input_tensor)  # Conv2D outputs larger than 2048`

Nested scopes for fine-grained control:

Copied!

`with RematScope(mode="full"):     # Create layers     layer1 = keras.layers.Dense(128, activation='relu')     output1 = layer1(input_tensor)  # layer1 is fully rematerialized     with RematScope(mode="larger_than", output_size_threshold=512):         layer2 = keras.layers.Conv2D(32, (3, 3))         output2 = layer2(output1) # layer2 is conditionally rematerialized         # if output > 512`

* * *

[RematScope](https://keras.io/api/rematerialization/remat_scope/#rematscope)

[`RematScope` class](https://keras.io/api/rematerialization/remat_scope/#rematscope-class)