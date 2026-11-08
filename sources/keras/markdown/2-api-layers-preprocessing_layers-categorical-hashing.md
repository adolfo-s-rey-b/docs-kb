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
 / Hashing layer

Hashing layer
=============

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/preprocessing/hashing.py#L34)

### `Hashing` class

Copied!

`tf_keras.layers.Hashing(     num_bins, mask_value=None, salt=None, output_mode="int", sparse=False, **kwargs )`

A preprocessing layer which hashes and bins categorical features.

This layer transforms categorical inputs to hashed output. It element-wise converts a ints or strings to ints in a fixed range. The stable hash function uses `tensorflow::ops::Fingerprint` to produce the same output consistently across all platforms.

This layer uses [FarmHash64](https://github.com/google/farmhash)
 by default, which provides a consistent hashed output across different platforms and is stable across invocations, regardless of device and context, by mixing the input bits thoroughly.

If you want to obfuscate the hashed output, you can also pass a random `salt` argument in the constructor. In that case, the layer will use the [SipHash64](https://github.com/google/highwayhash)
 hash function, with the `salt` value serving as additional input to the hash function.

For an overview and full list of preprocessing layers, see the preprocessing [guide](https://keras.io/guides/preprocessing_layers)
.

**Example (FarmHash64)**

Copied!

`>>> layer = tf.keras.layers.Hashing(num_bins=3) >>> inp = [['A'], ['B'], ['C'], ['D'], ['E']] >>> layer(inp) <tf.Tensor: shape=(5, 1), dtype=int64, numpy=   array([[1],          [0],          [1],          [1],          [2]])>`

**Example (FarmHash64) with a mask value**

Copied!

`>>> layer = tf.keras.layers.Hashing(num_bins=3, mask_value='') >>> inp = [['A'], ['B'], [''], ['C'], ['D']] >>> layer(inp) <tf.Tensor: shape=(5, 1), dtype=int64, numpy=   array([[1],          [1],          [0],          [2],          [2]])>`

**Example (SipHash64)**

Copied!

`>>> layer = tf.keras.layers.Hashing(num_bins=3, salt=[133, 137]) >>> inp = [['A'], ['B'], ['C'], ['D'], ['E']] >>> layer(inp) <tf.Tensor: shape=(5, 1), dtype=int64, numpy=   array([[1],          [2],          [1],          [0],          [2]])>`

**Example (Siphash64 with a single integer, same as `salt=[133, 133]`)**

Copied!

`>>> layer = tf.keras.layers.Hashing(num_bins=3, salt=133) >>> inp = [['A'], ['B'], ['C'], ['D'], ['E']] >>> layer(inp) <tf.Tensor: shape=(5, 1), dtype=int64, numpy=   array([[0],          [0],          [2],          [1],          [0]])>`

**Arguments**

*   **num\_bins**: Number of hash bins. Note that this includes the `mask_value` bin, so the effective number of bins is `(num_bins - 1)` if `mask_value` is set.
*   **mask\_value**: A value that represents masked inputs, which are mapped to index 0. `None` means no mask term will be added and the hashing will start at index 0. Defaults to `None`.
*   **salt**: A single unsigned integer or None. If passed, the hash function used will be SipHash64, with these values used as an additional input (known as a "salt" in cryptography). These should be non-zero. If `None`, uses the FarmHash64 hash function. It also supports tuple/list of 2 unsigned integer numbers, see reference paper for details. Defaults to `None`.
*   **output\_mode**: Specification for the output of the layer. Values can bes `"int"`, `"one_hot"`, `"multi_hot"`, or `"count"` configuring the layer as follows:
    *   `"int"`: Return the integer bin indices directly.
    *   `"one_hot"`: Encodes each individual element in the input into an array the same size as `num_bins`, containing a 1 at the input's bin index. If the last dimension is size 1, will encode on that dimension. If the last dimension is not size 1, will append a new dimension for the encoded output.
    *   `"multi_hot"`: Encodes each sample in the input into a single array the same size as `num_bins`, containing a 1 for each bin index index present in the sample. Treats the last dimension as the sample dimension, if input shape is `(..., sample_length)`, output shape will be `(..., num_tokens)`.
    *   `"count"`: As `"multi_hot"`, but the int array contains a count of the number of times the bin index appeared in the sample. Defaults to `"int"`.
*   **sparse**: Boolean. Only applicable to `"one_hot"`, `"multi_hot"`, and `"count"` output modes. If True, returns a `SparseTensor` instead of a dense `Tensor`. Defaults to `False`.
*   **\*\*kwargs**: Keyword arguments to construct a layer.

**Input shape**

A single or list of string, int32 or int64 `Tensor`, `SparseTensor` or `RaggedTensor` of shape `(batch_size, ...,)`

**Output shape**

An int64 `Tensor`, `SparseTensor` or `RaggedTensor` of shape `(batch_size, ...)`. If any input is `RaggedTensor` then output is `RaggedTensor`, otherwise if any input is `SparseTensor` then output is `SparseTensor`, otherwise the output is `Tensor`.

**Reference**

*   [SipHash with salt](https://www.131002.net/siphash/siphash.pdf)
    

* * *

[Hashing layer](https://keras.io/2/api/layers/preprocessing_layers/categorical/hashing/#hashing-layer)

[`Hashing` class](https://keras.io/2/api/layers/preprocessing_layers/categorical/hashing/#hashing-class)