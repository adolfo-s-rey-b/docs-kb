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
 / [Categorical features preprocessing layers](https://keras.io/2/api/layers/preprocessing_layers/categorical/)
 / CategoryEncoding layer

CategoryEncoding layer
======================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/preprocessing/category_encoding.py#L35)

### `CategoryEncoding` class

Copied!

`tf_keras.layers.CategoryEncoding(     num_tokens=None, output_mode="multi_hot", sparse=False, **kwargs )`

A preprocessing layer which encodes integer features.

This layer provides options for condensing data into a categorical encoding when the total number of tokens are known in advance. It accepts integer values as inputs, and it outputs a dense or sparse representation of those inputs. For integer inputs where the total number of tokens is not known, use [`tf.keras.layers.IntegerLookup`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/IntegerLookup)
 instead.

For an overview and full list of preprocessing layers, see the preprocessing [guide](https://keras.io/guides/preprocessing_layers)
.

**Examples**

**One-hot encoding data**

Copied!

`>>> layer = tf.keras.layers.CategoryEncoding( ...           num_tokens=4, output_mode="one_hot") >>> layer([3, 2, 0, 1]) <tf.Tensor: shape=(4, 4), dtype=float32, numpy=   array([[0., 0., 0., 1.],          [0., 0., 1., 0.],          [1., 0., 0., 0.],          [0., 1., 0., 0.]], dtype=float32)>`

**Multi-hot encoding data**

Copied!

`>>> layer = tf.keras.layers.CategoryEncoding( ...           num_tokens=4, output_mode="multi_hot") >>> layer([[0, 1], [0, 0], [1, 2], [3, 1]]) <tf.Tensor: shape=(4, 4), dtype=float32, numpy=   array([[1., 1., 0., 0.],          [1., 0., 0., 0.],          [0., 1., 1., 0.],          [0., 1., 0., 1.]], dtype=float32)>`

**Using weighted inputs in `"count"` mode**

Copied!

`>>> layer = tf.keras.layers.CategoryEncoding( ...           num_tokens=4, output_mode="count") >>> count_weights = np.array([[.1, .2], [.1, .1], [.2, .3], [.4, .2]]) >>> layer([[0, 1], [0, 0], [1, 2], [3, 1]], count_weights=count_weights) <tf.Tensor: shape=(4, 4), dtype=float64, numpy=   array([[0.1, 0.2, 0. , 0. ],          [0.2, 0. , 0. , 0. ],          [0. , 0.2, 0.3, 0. ],          [0. , 0.2, 0. , 0.4]], dtype=float32)>`

**Arguments**

*   **num\_tokens**: The total number of tokens the layer should support. All inputs to the layer must integers in the range `0 <= value < num_tokens`, or an error will be thrown.
*   **output\_mode**: Specification for the output of the layer. Values can be `"one_hot"`, `"multi_hot"` or `"count"`, configuring the layer as follows:
    *   `"one_hot"`: Encodes each individual element in the input into an array of `num_tokens` size, containing a 1 at the element index. If the last dimension is size 1, will encode on that dimension. If the last dimension is not size 1, will append a new dimension for the encoded output.
    *   `"multi_hot"`: Encodes each sample in the input into a single array of `num_tokens` size, containing a 1 for each vocabulary term present in the sample. Treats the last dimension as the sample dimension, if input shape is `(..., sample_length)`, output shape will be `(..., num_tokens)`.
    *   `"count"`: Like `"multi_hot"`, but the int array contains a count of the number of times the token at that index appeared in the sample. For all output modes, currently only output up to rank 2 is supported. Defaults to `"multi_hot"`.
*   **sparse**: Boolean. If true, returns a `SparseTensor` instead of a dense `Tensor`. Defaults to `False`.

**Call arguments**

*   **inputs**: A 1D or 2D tensor of integer inputs.
*   **count\_weights**: A tensor in the same shape as `inputs` indicating the weight for each sample value when summing up in `count` mode. Not used in `"multi_hot"` or `"one_hot"` modes.

* * *

[CategoryEncoding layer](https://keras.io/2/api/layers/preprocessing_layers/categorical/category_encoding/#categoryencoding-layer)

[`CategoryEncoding` class](https://keras.io/2/api/layers/preprocessing_layers/categorical/category_encoding/#categoryencoding-class)