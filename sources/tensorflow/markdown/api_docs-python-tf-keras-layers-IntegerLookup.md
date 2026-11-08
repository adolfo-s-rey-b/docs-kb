[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/IntegerLookup#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.IntegerLookup Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/integer_lookup.py#L10-L447)

A preprocessing layer that maps integers to (possibly encoded) indices.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.IntegerLookup(
        max_tokens=None,
        num_oov_indices=1,
        mask_token=None,
        oov_token=-1,
        vocabulary=None,
        vocabulary_dtype='int64',
        idf_weights=None,
        invert=False,
        output_mode='int',
        sparse=False,
        pad_to_max_tokens=False,
        oov_method='floormod',
        salt=None,
        name=None,
        **kwargs
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Working with preprocessing layers](https://www.tensorflow.org/guide/keras/preprocessing_layers) | *   [Load a pandas DataFrame](https://www.tensorflow.org/tutorials/load_data/pandas_dataframe)<br>    <br>*   [Classify structured data using Keras preprocessing layers](https://www.tensorflow.org/tutorials/structured_data/preprocessing_layers)<br>    <br>*   [Deep & Cross Network (DCN)](https://www.tensorflow.org/recommenders/examples/dcn) |

This layer maps a set of arbitrary integer input tokens into indexed integer output via a table-based vocabulary lookup. The layer's output indices will be contiguously arranged up to the maximum vocab size, even if the input tokens are non-continguous or unbounded. The layer supports multiple options for encoding the output via `output_mode`, and has optional support for out-of-vocabulary (OOV) tokens and masking.

The vocabulary for the layer must be either supplied on construction or learned via `adapt()`. During `adapt()`, the layer will analyze a data set, determine the frequency of individual integer tokens, and create a vocabulary from them. If the vocabulary is capped in size, the most frequent tokens will be used to create the vocabulary and all others will be treated as OOV.

There are two possible output modes for the layer. When `output_mode` is `"int"`, input integers are converted to their index in the vocabulary (an integer). When `output_mode` is `"multi_hot"`, `"count"`, or `"tf_idf"`, input integers are encoded into an array where each dimension corresponds to an element in the vocabulary.

The vocabulary can optionally contain a mask token as well as an OOV token (which can optionally occupy multiple indices in the vocabulary, as set by `num_oov_indices`). The position of these tokens in the vocabulary is fixed. When `output_mode` is `"int"`, the vocabulary will begin with the mask token at index 0, followed by OOV indices, followed by the rest of the vocabulary. When `output_mode` is `"multi_hot"`, `"count"`, or `"tf_idf"` the vocabulary will begin with OOV indices and instances of the mask token will be dropped.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `max_tokens` | Maximum size of the vocabulary for this layer. This should only be specified when adapting the vocabulary or when setting `pad_to_max_tokens=True`. If None, there is no cap on the size of the vocabulary. Note that this size includes the OOV and mask tokens. Defaults to `None`. |
| `num_oov_indices` | The number of out-of-vocabulary tokens to use. If this value is more than 1, OOV inputs are hashed or modulated to determine their OOV value (see `oov_method`). If this value is 0, OOV inputs will cause an error when calling the layer. Defaults to `1`. |
| `mask_token` | An integer token that represents masked inputs. When `output_mode` is `"int"`, the token is included in vocabulary and mapped to index 0. In other output modes, the token will not appear in the vocabulary and instances of the mask token in the input will be dropped. If set to None, no mask term will be added. Defaults to `None`. |
| `oov_token` | Only used when `invert` is `True`. The token to return for OOV indices. Defaults to `-1`. |
| `vocabulary` | Optional. Either an array of integers or a string path to a text file. If passing an array, can pass a tuple, list, 1D NumPy array, or 1D tensor containing the integer vocbulary terms. If passing a file path, the file should contain one line per term in the vocabulary. If this argument is set, there is no need to `adapt()` the layer. |
| `vocabulary_dtype` | The dtype of the vocabulary terms. Only `vocabulary_dtype='int64'` is supported at this time. Defaults to `"int64"`. |
| `idf_weights` | Only valid when `output_mode` is `"tf_idf"`. A tuple, list, 1D NumPy array, or 1D tensor or the same length as the vocabulary, containing the floating point inverse document frequency weights, which will be multiplied by per sample term counts for the final TF-IDF weight. If the `vocabulary` argument is set, and `output_mode` is `"tf_idf"`, this argument must be supplied. |
| `invert` | Only valid when `output_mode` is `"int"`. If `True`, this layer will map indices to vocabulary items instead of mapping vocabulary items to indices. Defaults to `False`. |
| `output_mode` | Specification for the output of the layer. Values can be `"int"`, `"one_hot"`, `"multi_hot"`, `"count"`, or `"tf_idf"` configuring the layer as follows:<br><br>*   `"int"`: Return the vocabulary indices of the input tokens.<br>*   `"one_hot"`: Encodes each individual element in the input into an array the same size as the vocabulary, containing a 1 at the element index. If the last dimension is size 1, will encode on that dimension. If the last dimension is not size 1, will append a new dimension for the encoded output.<br>*   `"multi_hot"`: Encodes each sample in the input into a single array the same size as the vocabulary, containing a 1 for each vocabulary term present in the sample. Treats the last dimension as the sample dimension, if input shape is `(..., sample_length)`, output shape will be `(..., num_tokens)`.<br>*   `"count"`: As `"multi_hot"`, but the int array contains a count of the number of times the token at that index appeared in the sample.<br>*   `"tf_idf"`: As `"multi_hot"`, but the TF-IDF algorithm is applied to find the value in each token slot. For `"int"` output, the output shape matches the input shape. For `"one_hot"` output, the output shape is `input_shape + (vocabulary_size,)`, where `input_shape` may have arbitrary rank. For other output modes (`"multi_hot"`, `"count"`, `"tf_idf"`), the output shape is `(batch_size, vocabulary_size)`. Defaults to `"int"`. |
| `pad_to_max_tokens` | Only applicable when `output_mode` is `"multi_hot"`, `"count"`, or `"tf_idf"`. If `True`, the output will have its feature axis padded to `max_tokens` even if the number of unique tokens in the vocabulary is less than `max_tokens`, resulting in a tensor of shape `(batch_size, max_tokens)` regardless of vocabulary size. Defaults to `False`. |
| `sparse` | Boolean. Only applicable to `"multi_hot"`, `"count"`, and `"tf_idf"` output modes. Only supported with TensorFlow backend. If `True`, returns a `SparseTensor` instead of a dense `Tensor`. Defaults to `False`. |
| `oov_method` | Only relevant when `num_oov_indices > 1`. Controls how OOV tokens are assigned to OOV buckets.*   `"floormod"` (default): uses `token % num_oov_indices`. Preserves backwards compatibility but can produce severe bucket imbalance when input IDs share a common factor with `num_oov_indices` (e.g. all-even IDs with an even bucket count).<br>*   `"farmhash"`: applies FarmHash64. Distributes OOV tokens uniformly regardless of the arithmetic structure of the input IDs. This parameter is ignored for string inputs, which always use FarmHash64. |
| `salt` | Only valid when `oov_method="farmhash"`. If passed, the hash function used for OOV bucket assignment will be SipHash64, with these values used as an additional input (known as a "salt" in cryptography). Can be a tuple or list of 2 integers, or a single integer (which is used for both key components). If `None` (default), FarmHash64 is used. Defaults to `None`. |

#### Examples:

**Creating a lookup layer with a known vocabulary**

This example creates a lookup layer with a pre-existing vocabulary.

    vocab = [12, 36, 1138, 42]

**Creating a lookup layer with an adapted vocabulary**

This example creates a lookup layer and generates the vocabulary by analyzing the dataset.

    data = np.array([[12, 1138, 42], [42, 1000, 36]])

Note that the OOV token -1 have been added to the vocabulary. The remaining tokens are sorted by frequency (42, which has 2 occurrences, is first) then by inverse sort order.

    data = np.array([[12, 1138, 42], [42, 1000, 36]])

**Lookups with multiple OOV indices**

This example demonstrates how to use a lookup layer with multiple OOV indices. When a layer is created with more than one OOV index, any OOV tokens are hashed or modulated into the number of OOV buckets, distributing OOV tokens in a deterministic fashion across the set. Use `oov_method` to control whether `floormod` or FarmHash64 is used.

    vocab = [12, 36, 1138, 42]

Note that the output for OOV token 37 is 1, while the output for OOV token 1000 is 0. The in-vocab terms have their output index increased by 1 from earlier examples (12 maps to 2, etc) in order to make space for the extra OOV token.

**Uniform OOV distribution with FarmHash**

This example shows how `oov_method="farmhash"` avoids the bucket imbalance that `"floormod"` produces for arithmetically structured input IDs.

    vocab = [10, 20, 30]

**One-hot output**

Configure the layer with `output_mode='one_hot'`. Note that the first `num_oov_indices` dimensions in the ont\_hot encoding represent OOV values.

    vocab = [12, 36, 1138, 42]

**Multi-hot output**

Configure the layer with `output_mode='multi_hot'`. Note that the first `num_oov_indices` dimensions in the multi\_hot encoding represent OOV tokens

    vocab = [12, 36, 1138, 42]

**Token count output**

Configure the layer with `output_mode='count'`. As with multi\_hot output, the first `num_oov_indices` dimensions in the output represent OOV tokens.

    vocab = [12, 36, 1138, 42]

**TF-IDF output**

Configure the layer with `output_mode='tf_idf'`. As with multi\_hot output, the first `num_oov_indices` dimensions in the output represent OOV tokens.

Each token bin will output `token_count * idf_weight`, where the idf weights are the inverse document frequency weights per token. These should be provided along with the vocabulary. Note that the `idf_weight` for OOV tokens will default to the average of all idf weights passed in.

    vocab = [12, 36, 1138, 42]

To specify the idf weights for oov tokens, you will need to pass the entire vocabulary including the leading oov token.

    vocab = [-1, 12, 36, 1138, 42]

When adapting the layer in `"tf_idf"` mode, each input sample will be considered a document, and IDF weight per token will be calculated as: `log(1 + num_documents / (1 + token_document_count))`.

**Inverse lookup**

This example demonstrates how to map indices to tokens using this layer. (You can also use `adapt()` with `inverse=True`, but for simplicity we'll pass the vocab in this example.)

    vocab = [12, 36, 1138, 42]

Note that the first index correspond to the oov token by default.

**Forward and inverse lookup pairs**

This example demonstrates how to use the vocabulary of a standard lookup layer to create an inverse lookup layer.

    vocab = [12, 36, 1138, 42]

In this example, the input token 1000 resulted in an output of -1, since 1000 was not in the vocabulary - it got represented as an OOV, and all OOV tokens are returned as -1 in the inverse layer. Also, note that for the inverse to work, you must have already set the forward layer vocabulary either directly or via `adapt()` before calling `get_vocabulary()`.

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |

Methods
-------

### `adapt`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/integer_lookup.py#L400-L429)

adapt(
        data, steps=None
    )

Computes a vocabulary of integer terms from tokens in a dataset.

Calling `adapt()` on an `IntegerLookup` layer is an alternative to passing in a precomputed vocabulary on construction via the `vocabulary` argument. An `IntegerLookup` layer should always be either adapted over a dataset or supplied with a vocabulary.

During `adapt()`, the layer will build a vocabulary of all integer tokens seen in the dataset, sorted by occurrence count, with ties broken by sort order of the tokens (high to low). At the end of `adapt()`, if `max_tokens` is set, the vocabulary will be truncated to `max_tokens` size. For example, adapting a layer with `max_tokens=1000` will compute the 1000 most frequent tokens occurring in the input dataset. If `output_mode='tf-idf'`, `adapt()` will also learn the document frequencies of each token in the input dataset.

|     |     |
| --- | --- |
| Arguments |     |
| `data` | The data to train on. It can be passed either as a batched [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>, as a list of integers, or as a NumPy array. |
| `steps` | Integer or `None`. Total number of steps (batches of samples) to process. If `data` is a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>, and `steps` is `None`, `adapt()` will run until the input dataset is exhausted. When passing an infinitely repeating dataset, you must specify the `steps` argument. This argument is not supported with array inputs or list inputs. |

### `finalize_state`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/index_lookup.py#L709-L772)

finalize_state()

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/operation.py#L322-L362)

@classmethod

Creates an operation from its config.

This method is the reverse of `get_config`, capable of instantiating the same operation from the config dictionary.

if "dtype" in config and isinstance(config["dtype"], dict):
        policy = dtype_policies.deserialize(config["dtype"])

|     |     |
| --- | --- |
| Args |     |
| `config` | A Python dictionary, typically the output of `get_config`. |

|     |
| --- |
| Returns |     |
| An operation instance. |     |

### `get_vocabulary`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/index_lookup.py#L333-L369)

get_vocabulary(
        include_special_tokens=True
    )

Returns the current vocabulary of the layer.

|     |     |
| --- | --- |
| Args |     |
| `include_special_tokens` | If `True`, the returned vocabulary will include mask and OOV tokens, and a term's index in the vocabulary will equal the term's index when calling the layer. If `False`, the returned vocabulary will not include any mask or OOV tokens. |

### `load_assets`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/index_lookup.py#L934-L952)

load_assets(
        dir_path
    )

### `reset_state`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/index_lookup.py#L774-L783)

reset_state()

### `save_assets`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/index_lookup.py#L924-L932)

save_assets(
        dir_path
    )

### `set_vocabulary`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/index_lookup.py#L411-L602)

set_vocabulary(
        vocabulary, idf_weights=None
    )

Sets vocabulary (and optionally document frequency) for this layer.

This method sets the vocabulary and idf weights for this layer directly, instead of analyzing a dataset through `adapt`. It should be used whenever the vocab (and optionally document frequency) information is already known. If vocabulary data is already present in the layer, this method will replace it.

|     |     |
| --- | --- |
| Args |     |
| `vocabulary` | Either an array or a string path to a text file. If passing an array, can pass a tuple, list, 1D numpy array, or 1D tensor containing the vocbulary terms. If passing a file path, the file should contain one line per term in the vocabulary. |
| `idf_weights` | A tuple, list, 1D numpy array, or 1D tensor of inverse document frequency weights with equal length to vocabulary. Must be set if `output_mode` is `"tf_idf"`. Should not be set otherwise. |

### `update_state`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/index_lookup.py#L668-L707)

update_state(
        data
    )

### `vocabulary_size`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/index_lookup.py#L371-L384)

vocabulary_size()

Gets the current size of the layer's vocabulary.

|     |
| --- |
| Returns |     |
| The integer size of the vocabulary, including optional mask and oov indices. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.