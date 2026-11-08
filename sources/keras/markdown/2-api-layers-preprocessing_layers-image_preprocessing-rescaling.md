None

[Keras 3 API documentation](https://keras.io/api/)
 [Keras 2 API documentation](https://keras.io/2/api/)

[Models API](https://keras.io/2/api/models/)
 [Layers API](https://keras.io/2/api/layers/)
 [The base Layer class](https://keras.io/2/api/layers/base_layer/)
 [Layer activations](https://keras.io/2/api/layers/activations/)
 [Layer weight initializers](https://keras.io/2/api/layers/initializers/)
 [Layer weight regularizers](https://keras.io/2/api/layers/regularizers/)
 [Layer weight constraints](https://keras.io/2/api/layers/constraints/)
 [Core layers](https://keras.io/2/api/layers/core_layers/)
 [Convolution layers](https://keras.io/2/api/layers/convolution_layers/)
 [Pooling layers](https://keras.io/2/api/layers/pooling_layers/)
 [Recurrent layers](https://keras.io/2/api/layers/recurrent_layers/)
 [Preprocessing layers](https://keras.io/2/api/layers/preprocessing_layers/)
 [Normalization layers](https://keras.io/2/api/layers/normalization_layers/)
 [Regularization layers](https://keras.io/2/api/layers/regularization_layers/)
 [Attention layers](https://keras.io/2/api/layers/attention_layers/)
 [Reshaping layers](https://keras.io/2/api/layers/reshaping_layers/)
 [Merging layers](https://keras.io/2/api/layers/merging_layers/)
 [Activation layers](https://keras.io/2/api/layers/activation_layers/)
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
 / [Layers API](https://keras.io/2/api/layers/)
 / [Preprocessing layers](https://keras.io/2/api/layers/preprocessing_layers/)
 / [Image preprocessing layers](https://keras.io/2/api/layers/preprocessing_layers/image_preprocessing/)
 / Rescaling layer

Rescaling layer
===============

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/preprocessing/image_preprocessing.py#L320)

### `Rescaling` class

Copied!

`tf_keras.layers.Rescaling(scale, offset=0.0, **kwargs)`

A preprocessing layer which rescales input values to a new range.

This layer rescales every value of an input (often an image) by multiplying by `scale` and adding `offset`.

For instance:

1.  To rescale an input in the `[0, 255]` range to be in the `[0, 1]` range, you would pass `scale=1./255`.
    
2.  To rescale an input in the `[0, 255]` range to be in the `[-1, 1]` range, you would pass `scale=1./127.5, offset=-1`.
    

The rescaling is applied both during training and inference. Inputs can be of integer or floating point dtype, and by default the layer will output floats.

For an overview and full list of preprocessing layers, see the preprocessing [guide](https://keras.io/guides/preprocessing_layers)
.

**Input shape**

Arbitrary.

**Output shape**

Same as input.

**Arguments**

*   **scale**: Float, the scale to apply to the inputs.
*   **offset**: Float, the offset to apply to the inputs.

* * *

[Rescaling layer](https://keras.io/2/api/layers/preprocessing_layers/image_preprocessing/rescaling/#rescaling-layer)

[`Rescaling` class](https://keras.io/2/api/layers/preprocessing_layers/image_preprocessing/rescaling/#rescaling-class)