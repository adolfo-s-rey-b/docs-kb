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
 / [Numerical features preprocessing layers](https://keras.io/2/api/layers/preprocessing_layers/numerical/)
 / Discretization layer

Discretization layer
====================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/preprocessing/discretization.py#L136)

### `Discretization` class

Copied!

`tf_keras.layers.Discretization(     bin_boundaries=None,     num_bins=None,     epsilon=0.01,     output_mode="int",     sparse=False,     **kwargs )`

A preprocessing layer which buckets continuous features by ranges.

This layer will place each element of its input data into one of several contiguous ranges and output an integer index indicating which range each element was placed in.

For an overview and full list of preprocessing layers, see the preprocessing [guide](https://keras.io/guides/preprocessing_layers)
.

**Input shape**

Any [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 or [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
 of dimension 2 or higher.

**Output shape**

Same as input shape.

**Arguments**

*   **bin\_boundaries**: A list of bin boundaries. The leftmost and rightmost bins will always extend to `-inf` and `inf`, so `bin_boundaries=[0., 1., 2.]` generates bins `(-inf, 0.)`, `[0., 1.)`, `[1., 2.)`, and `[2., +inf)`. If this option is set, `adapt()` should not be called.\
*   **num\_bins**: The integer number of bins to compute. If this option is set, `adapt()` should be called to learn the bin boundaries.\
*   **epsilon**: Error tolerance, typically a small fraction close to zero (e.g. 0.01). Higher values of epsilon increase the quantile approximation, and hence result in more unequal buckets, but could improve performance and resource consumption.\
*   **output\_mode**: Specification for the output of the layer. Values can be `"int"`, `"one_hot"`, `"multi_hot"`, or `"count"` configuring the layer as follows:\
    *   `"int"`: Return the discretized bin indices directly.\
    *   `"one_hot"`: Encodes each individual element in the input into an array the same size as `num_bins`, containing a 1 at the input's bin index. If the last dimension is size 1, will encode on that dimension. If the last dimension is not size 1, will append a new dimension for the encoded output.\
    *   `"multi_hot"`: Encodes each sample in the input into a single array the same size as `num_bins`, containing a 1 for each bin index index present in the sample. Treats the last dimension as the sample dimension, if input shape is `(..., sample_length)`, output shape will be `(..., num_tokens)`.\
    *   `"count"`: As `"multi_hot"`, but the int array contains a count of the number of times the bin index appeared in the sample. Defaults to `"int"`.\
*   **sparse**: Boolean. Only applicable to `"one_hot"`, `"multi_hot"`, and `"count"` output modes. If True, returns a `SparseTensor` instead of a dense `Tensor`. Defaults to `False`.\
\
**Examples**\
\
Bucketize float values based on provided buckets.\
\
Copied!\
\
`>>> input = np.array([[-1.5, 1.0, 3.4, .5], [0.0, 3.0, 1.3, 0.0]]) >>> layer = tf.keras.layers.Discretization(bin_boundaries=[0., 1., 2.]) >>> layer(input) <tf.Tensor: shape=(2, 4), dtype=int64, numpy= array([[0, 2, 3, 1],        [1, 3, 2, 1]])>`\
\
Bucketize float values based on a number of buckets to compute.\
\
Copied!\
\
`>>> input = np.array([[-1.5, 1.0, 3.4, .5], [0.0, 3.0, 1.3, 0.0]]) >>> layer = tf.keras.layers.Discretization(num_bins=4, epsilon=0.01) >>> layer.adapt(input) >>> layer(input) <tf.Tensor: shape=(2, 4), dtype=int64, numpy= array([[0, 2, 3, 2],        [1, 3, 3, 1]])>`\
\
* * *\
\
[Discretization layer](https://keras.io/2/api/layers/preprocessing_layers/numerical/discretization/#discretization-layer)\
\
[`Discretization` class](https://keras.io/2/api/layers/preprocessing_layers/numerical/discretization/#discretization-class)