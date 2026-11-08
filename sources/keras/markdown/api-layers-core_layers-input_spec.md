None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [Layers API](https://keras.io/api/layers/)
 [The base Layer class](https://keras.io/api/layers/base_layer/)
 [Layer activations](https://keras.io/api/layers/activations/)
 [Layer weight initializers](https://keras.io/api/layers/initializers/)
 [Layer weight regularizers](https://keras.io/api/layers/regularizers/)
 [Layer weight constraints](https://keras.io/api/layers/constraints/)
 [Core layers](https://keras.io/api/layers/core_layers/)
 [Convolution layers](https://keras.io/api/layers/convolution_layers/)
 [Pooling layers](https://keras.io/api/layers/pooling_layers/)
 [Recurrent layers](https://keras.io/api/layers/recurrent_layers/)
 [Preprocessing layers](https://keras.io/api/layers/preprocessing_layers/)
 [Normalization layers](https://keras.io/api/layers/normalization_layers/)
 [Regularization layers](https://keras.io/api/layers/regularization_layers/)
 [Attention layers](https://keras.io/api/layers/attention_layers/)
 [Reshaping layers](https://keras.io/api/layers/reshaping_layers/)
 [Merging layers](https://keras.io/api/layers/merging_layers/)
 [Activation layers](https://keras.io/api/layers/activation_layers/)
 [Backend-specific layers](https://keras.io/api/layers/backend_specific_layers/)
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
 / [Layers API](https://keras.io/api/layers/)
 / [Core layers](https://keras.io/api/layers/core_layers/)
 / InputSpec object

InputSpec object
================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/input_spec.py#L6)

### `InputSpec` class

Copied!

`keras.InputSpec(     dtype=None,     shape=None,     ndim=None,     max_ndim=None,     min_ndim=None,     axes=None,     allow_last_axis_squeeze=False,     name=None,     optional=False, )`

Specifies the rank, dtype and shape of every input to a layer.

Layers can expose (if appropriate) an `input_spec` attribute: an instance of `InputSpec`, or a nested structure of `InputSpec` instances (one per input tensor). These objects enable the layer to run input compatibility checks for input structure, input rank, input shape, and input dtype for the first argument of `Layer.__call__`.

A `None` entry in a shape is compatible with any dimension.

**Arguments**

*   **dtype**: Expected dtype of the input.
*   **shape**: Shape tuple, expected shape of the input (may include `None` for dynamic axes). Includes the batch size.
*   **ndim**: Integer, expected rank of the input.
*   **max\_ndim**: Integer, maximum rank of the input.
*   **min\_ndim**: Integer, minimum rank of the input.
*   **axes**: Dictionary mapping integer axes to a specific dimension value.
*   **allow\_last\_axis\_squeeze**: If `True`, allow inputs of rank N+1 as long as the last axis of the input is 1, as well as inputs of rank N-1 as long as the last axis of the spec is 1.
*   **name**: Expected key corresponding to this input when passing data as a dictionary.
*   **optional**: Boolean, whether the input is optional or not. An optional input can accept `None` values.

**Example**

Copied!

`class MyLayer(Layer):     def __init__(self):         super().__init__()         # The layer will accept inputs with         # shape (*, 28, 28) & (*, 28, 28, 1)         # and raise an appropriate error message otherwise.         self.input_spec = InputSpec(             shape=(None, 28, 28, 1),             allow_last_axis_squeeze=True)`

**Guides and examples using `InputSpec`**

*   [Exporting Keras models to LiteRT](https://keras.io/guides/litert_export/)
    

* * *

[InputSpec object](https://keras.io/api/layers/core_layers/input_spec/#inputspec-object)

[`InputSpec` class](https://keras.io/api/layers/core_layers/input_spec/#inputspec-class)