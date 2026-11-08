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
 / Remat

Remat
=====

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/remat.py#L137)

### `remat` function

Copied!

`keras.remat(f)`

Applies rematerialization to a function or layer for memory optimization.

Rematerialization is a memory optimization technique that trades off computation for memory. Instead of storing intermediate results (e.g. activations) for backpropagation, they are recomputed during the backward pass. This reduces peak memory usage at the cost of increased computation time, allowing the training of larger models or using larger batch sizes within the same memory constraints.

**Arguments**

*   **f**: A callable function, to which rematerialization is applied. This is typically a computationally expensive operation where intermediate states can be recomputed instead of stored.

**Returns**

A wrapped function that applies rematerialization. The returned function defines a custom gradient, ensuring that during the backward pass, the forward computation is recomputed as needed.

**Example**

Copied!

`from keras import Model class CustomRematLayer(layers.Layer):     def __init__(self, **kwargs):         super().__init__(**kwargs)         self.remat_function = remat(self.intermediate_function)      def intermediate_function(self, x):         for _ in range(2):             x = x + x * 0.1  # Simple scaled transformation         return x      def call(self, inputs):         return self.remat_function(inputs)  # Define a simple model using the custom layer inputs = layers.Input(shape=(4,)) x = layers.Dense(4, activation="relu")(inputs) x = CustomRematLayer()(x)  # Custom layer with rematerialization outputs = layers.Dense(1)(x)  # Create and compile the model model = Model(inputs=inputs, outputs=outputs) model.compile(optimizer="sgd", loss="mse")`

* * *

[Remat](https://keras.io/api/rematerialization/remat/#remat)

[`remat` function](https://keras.io/api/rematerialization/remat/#remat-function)