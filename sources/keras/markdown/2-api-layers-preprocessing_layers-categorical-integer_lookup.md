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
 / IntegerLookup layer

IntegerLookup layer
===================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/preprocessing/integer_lookup.py#L28)

### `IntegerLookup` class

Copied!

`tf_keras.layers.IntegerLookup(     max_tokens=None,     num_oov_indices=1,     mask_token=None,     oov_token=-1,     vocabulary=None,     vocabulary_dtype="int64",     idf_weights=None,     invert=False,     output_mode="int",     sparse=False,     pad_to_max_tokens=False,     **kwargs )`

A preprocessing layer which maps integer features to contiguous ranges.

This layer maps a set of arbitrary integer input tokens into indexed integer output via a table-based vocabulary lookup. The layer's output indices will be contiguously arranged up to the maximum vocab size, even if the input tokens are non-continguous or unbounded. The layer supports multiple options for encoding the output via `output_mode`, and has optional support for out-of-vocabulary (OOV) tokens and masking.

The vocabulary for the layer must be either supplied on construction or learned via `adapt()`. During `adapt()`, the layer will analyze a data set, determine the frequency of individual integer tokens, and create a vocabulary from them. If the vocabulary is capped in size, the most frequent tokens will be used to create the vocabulary and all others will be treated as OOV.

There are two possible output modes for the layer. When `output_mode` is `"int"`, input integers are converted to their index in the vocabulary (an integer). When `output_mode` is `"multi_hot"`, `"count"`, or `"tf_idf"`, input integers are encoded into an array where each dimension corresponds to an element in the vocabulary.

The vocabulary can optionally contain a mask token as well as an OOV token (which can optionally occupy multiple indices in the vocabulary, as set by `num_oov_indices`). The position of these tokens in the vocabulary is fixed. When `output_mode` is `"int"`, the vocabulary will begin with the mask token at index 0, followed by OOV indices, followed by the rest of the vocabulary. When `output_mode` is `"multi_hot"`, `"count"`, or `"tf_idf"` the vocabulary will begin with OOV indices and instances of the mask token will be dropped.

For an overview and full list of preprocessing layers, see the preprocessing [guide](https://keras.io/guides/preprocessing_layers)
.

**Arguments**

*   **max\_tokens**: Maximum size of the vocabulary for this layer. This should only be specified when adapting the vocabulary or when setting `pad_to_max_tokens=True`. If None, there is no cap on the size of the vocabulary. Note that this size includes the OOV and mask tokens. Defaults to `None`.
*   **num\_oov\_indices**: The number of out-of-vocabulary tokens to use. If this value is more than 1, OOV inputs are modulated to determine their OOV value. If this value is 0, OOV inputs will cause an error when calling the layer. Defaults to `1`.
*   **mask\_token**: An integer token that represents masked inputs. When `output_mode` is `"int"`, the token is included in vocabulary and mapped to index 0. In other output modes, the token will not appear in the vocabulary and instances of the mask token in the input will be dropped. If set to None, no mask term will be added. Defaults to `None`.
*   **oov\_token**: Only used when `invert` is True. The token to return for OOV indices. Defaults to `-1`.
*   **vocabulary**: Optional. Either an array of integers or a string path to a text file. If passing an array, can pass a tuple, list, 1D numpy array, or 1D tensor containing the integer vocbulary terms. If passing a file path, the file should contain one line per term in the vocabulary. If this argument is set, there is no need to `adapt()` the layer.
*   **vocabulary\_dtype**: The dtype of the vocabulary terms, for example `"int64"` or `"int32"`. Defaults to `"int64"`.
*   **idf\_weights**: Only valid when `output_mode` is `"tf_idf"`. A tuple, list, 1D numpy array, or 1D tensor or the same length as the vocabulary, containing the floating point inverse document frequency weights, which will be multiplied by per sample term counts for the final `tf_idf` weight. If the `vocabulary` argument is set, and `output_mode` is `"tf_idf"`, this argument must be supplied.
*   **invert**: Only valid when `output_mode` is `"int"`. If True, this layer will map indices to vocabulary items instead of mapping vocabulary items to indices. Defaults to `False`.
*   **output\_mode**: Specification for the output of the layer. Values can be `"int"`, `"one_hot"`, `"multi_hot"`, `"count"`, or `"tf_idf"` configuring the layer as follows:
    *   `"int"`: Return the vocabulary indices of the input tokens.
    *   `"one_hot"`: Encodes each individual element in the input into an array the same size as the vocabulary, containing a 1 at the element index. If the last dimension is size 1, will encode on that dimension. If the last dimension is not size 1, will append a new dimension for the encoded output.
    *   `"multi_hot"`: Encodes each sample in the input into a single array the same size as the vocabulary, containing a 1 for each vocabulary term present in the sample. Treats the last dimension as the sample dimension, if input shape is (..., sample\_length), output shape will be (..., num\_tokens).
    *   `"count"`: As `"multi_hot"`, but the int array contains a count of the number of times the token at that index appeared in the sample.
    *   `"tf_idf"`: As `"multi_hot"`, but the TF-IDF algorithm is applied to find the value in each token slot. For `"int"` output, any shape of input and output is supported. For all other output modes, currently only output up to rank 2 is supported. Defaults to `"int"`.
*   **pad\_to\_max\_tokens**: Only applicable when `output_mode` is `"multi_hot"`, `"count"`, or `"tf_idf"`. If True, the output will have its feature axis padded to `max_tokens` even if the number of unique tokens in the vocabulary is less than max\_tokens, resulting in a tensor of shape \[batch\_size, max\_tokens\] regardless of vocabulary size. Defaults to False.
*   **sparse**: Boolean. Only applicable when `output_mode` is `"multi_hot"`, `"count"`, or `"tf_idf"`. If True, returns a `SparseTensor` instead of a dense `Tensor`. Defaults to `False`.

**Examples**

**Creating a lookup layer with a known vocabulary**

This example creates a lookup layer with a pre-existing vocabulary.

Copied!

`>>> vocab = [12, 36, 1138, 42] >>> data = tf.constant([[12, 1138, 42], [42, 1000, 36]])  # Note OOV tokens >>> layer = tf.keras.layers.IntegerLookup(vocabulary=vocab) >>> layer(data) <tf.Tensor: shape=(2, 3), dtype=int64, numpy= array([[1, 3, 4],        [4, 0, 2]])>`

**Creating a lookup layer with an adapted vocabulary**

This example creates a lookup layer and generates the vocabulary by analyzing the dataset.

Copied!

`>>> data = tf.constant([[12, 1138, 42], [42, 1000, 36]]) >>> layer = tf.keras.layers.IntegerLookup() >>> layer.adapt(data) >>> layer.get_vocabulary() [-1, 42, 1138, 1000, 36, 12]`

Note that the OOV token -1 have been added to the vocabulary. The remaining tokens are sorted by frequency (42, which has 2 occurrences, is first) then by inverse sort order.

Copied!

`>>> data = tf.constant([[12, 1138, 42], [42, 1000, 36]]) >>> layer = tf.keras.layers.IntegerLookup() >>> layer.adapt(data) >>> layer(data) <tf.Tensor: shape=(2, 3), dtype=int64, numpy= array([[5, 2, 1],        [1, 3, 4]])>`

**Lookups with multiple OOV indices**

This example demonstrates how to use a lookup layer with multiple OOV indices. When a layer is created with more than one OOV index, any OOV tokens are hashed into the number of OOV buckets, distributing OOV tokens in a deterministic fashion across the set.

Copied!

`>>> vocab = [12, 36, 1138, 42] >>> data = tf.constant([[12, 1138, 42], [37, 1000, 36]]) >>> layer = tf.keras.layers.IntegerLookup( ...     vocabulary=vocab, num_oov_indices=2) >>> layer(data) <tf.Tensor: shape=(2, 3), dtype=int64, numpy= array([[2, 4, 5],        [1, 0, 3]])>`

Note that the output for OOV token 37 is 1, while the output for OOV token 1000 is 0. The in-vocab terms have their output index increased by 1 from earlier examples (12 maps to 2, etc) in order to make space for the extra OOV token.

**One-hot output**

Configure the layer with `output_mode='one_hot'`. Note that the first `num_oov_indices` dimensions in the one\_hot encoding represent OOV values.

Copied!

`>>> vocab = [12, 36, 1138, 42] >>> data = tf.constant([12, 36, 1138, 42, 7]) # Note OOV tokens >>> layer = tf.keras.layers.IntegerLookup( ...     vocabulary=vocab, output_mode='one_hot') >>> layer(data) <tf.Tensor: shape=(5, 5), dtype=float32, numpy=   array([[0., 1., 0., 0., 0.],          [0., 0., 1., 0., 0.],          [0., 0., 0., 1., 0.],          [0., 0., 0., 0., 1.],          [1., 0., 0., 0., 0.]], dtype=float32)>`

**Multi-hot output**

Configure the layer with `output_mode='multi_hot'`. Note that the first `num_oov_indices` dimensions in the multi\_hot encoding represent OOV tokens

Copied!

`>>> vocab = [12, 36, 1138, 42] >>> data = tf.constant([[12, 1138, 42, 42], ...                     [42, 7, 36, 7]]) # Note OOV tokens >>> layer = tf.keras.layers.IntegerLookup( ...     vocabulary=vocab, output_mode='multi_hot') >>> layer(data) <tf.Tensor: shape=(2, 5), dtype=float32, numpy=   array([[0., 1., 0., 1., 1.],          [1., 0., 1., 0., 1.]], dtype=float32)>`

**Token count output**

Configure the layer with `output_mode='count'`. As with multi\_hot output, the first `num_oov_indices` dimensions in the output represent OOV tokens.

Copied!

`>>> vocab = [12, 36, 1138, 42] >>> data = tf.constant([[12, 1138, 42, 42], ...                     [42, 7, 36, 7]]) # Note OOV tokens >>> layer = tf.keras.layers.IntegerLookup( ...     vocabulary=vocab, output_mode='count') >>> layer(data) <tf.Tensor: shape=(2, 5), dtype=float32, numpy=   array([[0., 1., 0., 1., 2.],          [2., 0., 1., 0., 1.]], dtype=float32)>`

**TF-IDF output**

Configure the layer with `output_mode='tf_idf'`. As with multi\_hot output, the first `num_oov_indices` dimensions in the output represent OOV tokens.

Each token bin will output `token_count * idf_weight`, where the idf weights are the inverse document frequency weights per token. These should be provided along with the vocabulary. Note that the `idf_weight` for OOV tokens will default to the average of all idf weights passed in.

Copied!

`>>> vocab = [12, 36, 1138, 42] >>> idf_weights = [0.25, 0.75, 0.6, 0.4] >>> data = tf.constant([[12, 1138, 42, 42], ...                     [42, 7, 36, 7]]) # Note OOV tokens >>> layer = tf.keras.layers.IntegerLookup( ...     output_mode='tf_idf', vocabulary=vocab, idf_weights=idf_weights) >>> layer(data) <tf.Tensor: shape=(2, 5), dtype=float32, numpy=   array([[0.  , 0.25, 0.  , 0.6 , 0.8 ],          [1.0 , 0.  , 0.75, 0.  , 0.4 ]], dtype=float32)>`

To specify the idf weights for oov tokens, you will need to pass the entire vocabularly including the leading oov token.

Copied!

`>>> vocab = [-1, 12, 36, 1138, 42] >>> idf_weights = [0.9, 0.25, 0.75, 0.6, 0.4] >>> data = tf.constant([[12, 1138, 42, 42], ...                     [42, 7, 36, 7]]) # Note OOV tokens >>> layer = tf.keras.layers.IntegerLookup( ...     output_mode='tf_idf', vocabulary=vocab, idf_weights=idf_weights) >>> layer(data) <tf.Tensor: shape=(2, 5), dtype=float32, numpy=   array([[0.  , 0.25, 0.  , 0.6 , 0.8 ],          [1.8 , 0.  , 0.75, 0.  , 0.4 ]], dtype=float32)>`

When adapting the layer in tf\_idf mode, each input sample will be considered a document, and idf weight per token will be calculated as `log(1 + num_documents / (1 + token_document_count))`.

**Inverse lookup**

This example demonstrates how to map indices to tokens using this layer. (You can also use `adapt()` with `inverse=True`, but for simplicity we'll pass the vocab in this example.)

Copied!

`>>> vocab = [12, 36, 1138, 42] >>> data = tf.constant([[1, 3, 4], [4, 0, 2]]) >>> layer = tf.keras.layers.IntegerLookup(vocabulary=vocab, invert=True) >>> layer(data) <tf.Tensor: shape=(2, 3), dtype=int64, numpy= array([[  12, 1138,   42],        [  42,   -1,   36]])>`

Note that the first index correspond to the oov token by default.

**Forward and inverse lookup pairs**

This example demonstrates how to use the vocabulary of a standard lookup layer to create an inverse lookup layer.

Copied!

`>>> vocab = [12, 36, 1138, 42] >>> data = tf.constant([[12, 1138, 42], [42, 1000, 36]]) >>> layer = tf.keras.layers.IntegerLookup(vocabulary=vocab) >>> i_layer = tf.keras.layers.IntegerLookup( ...     vocabulary=layer.get_vocabulary(), invert=True) >>> int_data = layer(data) >>> i_layer(int_data) <tf.Tensor: shape=(2, 3), dtype=int64, numpy= array([[  12, 1138,   42],        [  42,   -1,   36]])>`

In this example, the input token 1000 resulted in an output of -1, since 1000 was not in the vocabulary - it got represented as an OOV, and all OOV tokens are returned as -1 in the inverse layer. Also, note that for the inverse to work, you must have already set the forward layer vocabulary either directly or via `adapt()` before calling `get_vocabulary()`.

* * *

[IntegerLookup layer](https://keras.io/2/api/layers/preprocessing_layers/categorical/integer_lookup/#integerlookup-layer)

[`IntegerLookup` class](https://keras.io/2/api/layers/preprocessing_layers/categorical/integer_lookup/#integerlookup-class)