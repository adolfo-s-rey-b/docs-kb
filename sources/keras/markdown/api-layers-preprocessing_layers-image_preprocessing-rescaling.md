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
 / [Preprocessing layers](https://keras.io/api/layers/preprocessing_layers/)
 / [Image preprocessing layers](https://keras.io/api/layers/preprocessing_layers/image_preprocessing/)
 / Rescaling layer

Rescaling layer
===============

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/rescaling.py#L7)

### `Rescaling` class

Copied!

`keras.layers.Rescaling(scale, offset=0.0, **kwargs)`

A preprocessing layer which rescales input values to a new range.

This layer rescales every value of an input (often an image) by multiplying by `scale` and adding `offset`.

For instance:

1.  To rescale an input in the `[0, 255]` range to be in the `[0, 1]` range, you would pass `scale=1./255`.
    
2.  To rescale an input in the `[0, 255]` range to be in the `[-1, 1]` range, you would pass `scale=1./127.5, offset=-1`.
    

The rescaling is applied both during training and inference. Inputs can be of integer or floating point dtype, and by default the layer will output floats.

**Note:** This layer is safe to use inside a [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)
 or `grain` pipeline (independently of which backend you're using).

**Arguments**

*   **scale**: Float, the scale to apply to the inputs.
*   **offset**: Float, the offset to apply to the inputs.
*   **\*\*kwargs**: Base layer keyword arguments, such as `name` and `dtype`.

* * *

[Rescaling layer](https://keras.io/api/layers/preprocessing_layers/image_preprocessing/rescaling/#rescaling-layer)

[`Rescaling` class](https://keras.io/api/layers/preprocessing_layers/image_preprocessing/rescaling/#rescaling-class)