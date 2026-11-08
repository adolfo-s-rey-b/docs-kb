None

[KerasHub: Pretrained Models](https://keras.io/keras_hub/)

[Getting started](https://keras.io/keras_hub/getting_started/)
 [Developer guides](https://keras.io/keras_hub/guides/)
 [API documentation](https://keras.io/keras_hub/api/)
 [Modeling API](https://keras.io/keras_hub/api/base_classes/)
 [Model Architectures](https://keras.io/keras_hub/api/models/)
 [Tokenizers](https://keras.io/keras_hub/api/tokenizers/)
 [Preprocessing Layers](https://keras.io/keras_hub/api/preprocessing_layers/)
 [Modeling Layers](https://keras.io/keras_hub/api/modeling_layers/)
 [Samplers](https://keras.io/keras_hub/api/samplers/)
 [Metrics](https://keras.io/keras_hub/api/metrics/)
 [Pretrained models list](https://keras.io/keras_hub/presets/)

► [KerasHub: Pretrained Models](https://keras.io/keras_hub/)
 / [API documentation](https://keras.io/keras_hub/api/)
 / [Tokenizers](https://keras.io/keras_hub/api/tokenizers/)
 / UnicodeCodepointTokenizer

UnicodeCodepointTokenizer
=========================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/unicode_codepoint_tokenizer.py#L39)

### `UnicodeCodepointTokenizer` class

Copied!

`keras_hub.tokenizers.UnicodeCodepointTokenizer(     sequence_length=None,     lowercase=True,     normalization_form=None,     errors="replace",     replacement_char=65533,     input_encoding="UTF-8",     output_encoding="UTF-8",     vocabulary_size=None,     dtype="int32",     **kwargs )`

A unicode character tokenizer layer.

This tokenizer is a vocabulary free tokenizer which tokenizes text as unicode character codepoints.

Tokenizer outputs can either be padded and truncated with a `sequence_length` argument, or left un-truncated. The exact output will depend on the rank of the input tensors.

If input is a batch of strings (rank > 0): By default, the layer will output a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
 where the last dimension of the output is ragged. If `sequence_length` is set, the layer will output a dense [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 where all inputs have been padded or truncated to `sequence_length`.

If input is a scalar string (rank == 0): By default, the layer will output a dense [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 with static shape `[None]`. If `sequence_length` is set, the output will be a dense [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 of shape `[sequence_length]`.

The output dtype can be controlled via the `dtype` argument, which should be an integer type ("int16", "int32", etc.).

**Arguments**

*   **lowercase**: If `True`, the input text will be first lowered before tokenization.
*   **sequence\_length**: If set, the output will be converted to a dense tensor and padded/trimmed so all outputs are of sequence\_length.
*   **normalization\_form**: One of the following string values (None, 'NFC', 'NFKC', 'NFD', 'NFKD'). If set will normalize unicode to the given form before tokenizing.
*   **errors**: One of ('replace', 'ignore', 'strict'). Specifies the `detokenize()` behavior when an invalid codepoint is encountered. The value of `'strict'` will cause the tokenizer to produce a `InvalidArgument` error (or a `ValueError` when running without TensorFlow) on any invalid input formatting. A value of `'replace'` will cause the tokenizer to replace any invalid formatting in the input with the replacement\_char codepoint. A value of `'ignore'` will cause the tokenizer to skip any invalid formatting in the input and produce no corresponding output character.
*   **replacement\_char**: The unicode codepoint to use in place of invalid codepoints. (U+FFFD) is `65533`. Defaults to `65533`.
*   **input\_encoding**: One of ("UTF-8", "UTF-16-BE", or "UTF-32-BE"). One of The encoding of the input text. Defaults to `"UTF-8"`.
*   **output\_encoding**: One of ("UTF-8", "UTF-16-BE", or "UTF-32-BE"). The encoding of the output text. Defaults to `"UTF-8"`.
*   **vocabulary\_size**: Set the vocabulary `vocabulary_size`, by clamping all codepoints to the range \[0, vocabulary\_size). Effectively this will make the `vocabulary_size - 1` id the the OOV value.\
\
**Examples**\
\
Basic Usage.\
\
Copied!\
\
`>>> inputs = "Unicode Tokenizer" >>> tokenizer = keras_hub.tokenizers.UnicodeCodepointTokenizer() >>> outputs = tokenizer(inputs) >>> np.array(outputs) array([117, 110, 105,  99, 111, 100, 101,  32, 116, 111, 107, 101, 110,     105, 122, 101, 114], dtype=int32)`\
\
Ragged outputs.\
\
Copied!\
\
`>>> inputs = ["पुस्तक", "کتاب"] >>> tokenizer = keras_hub.tokenizers.UnicodeCodepointTokenizer() >>> seq1, seq2 = tokenizer(inputs) >>> np.array(seq1) array([2346, 2369, 2360, 2381, 2340, 2325]) >>> np.array(seq2) array([1705, 1578, 1575, 1576])`\
\
Dense outputs.\
\
Copied!\
\
`>>> inputs = ["पुस्तक", "کتاب"] >>> tokenizer = keras_hub.tokenizers.UnicodeCodepointTokenizer( ...     sequence_length=8) >>> seq1, seq2 = tokenizer(inputs) >>> np.array(seq1) array([2346, 2369, 2360, 2381, 2340, 2325,    0,    0], dtype=int32) >>> np.array(seq2) array([1705, 1578, 1575, 1576,    0,    0,    0,    0], dtype=int32)`\
\
Tokenize, then batch for ragged outputs.\
\
Copied!\
\
`>>> inputs = ["Book", "पुस्तक", "کتاب"] >>> tokenizer = keras_hub.tokenizers.UnicodeCodepointTokenizer() >>> ds = tf.data.Dataset.from_tensor_slices(inputs) >>> ds = ds.map(tokenizer) >>> ds = ds.apply(tf.data.experimental.dense_to_ragged_batch(3)) >>> ds.take(1).get_single_element() <tf.RaggedTensor [[98, 111, 111, 107],     [2346, 2369, 2360, 2381, 2340, 2325],     [1705, 1578, 1575, 1576]]>`\
\
Batch, then tokenize for ragged outputs.\
\
Copied!\
\
`>>> inputs = ["Book", "पुस्तक", "کتاب"] >>> tokenizer = keras_hub.tokenizers.UnicodeCodepointTokenizer() >>> ds = tf.data.Dataset.from_tensor_slices(inputs) >>> ds = ds.batch(3).map(tokenizer) >>> ds.take(1).get_single_element() <tf.RaggedTensor [[98, 111, 111, 107],     [2346, 2369, 2360, 2381, 2340, 2325],     [1705, 1578, 1575, 1576]]>`\
\
Tokenize, then batch for dense outputs (`sequence_length` provided).\
\
Copied!\
\
`>>> inputs = ["Book", "पुस्तक", "کتاب"] >>> tokenizer = keras_hub.tokenizers.UnicodeCodepointTokenizer( ...     sequence_length=5) >>> ds = tf.data.Dataset.from_tensor_slices(inputs) >>> ds = ds.map(tokenizer) >>> ds = ds.apply(tf.data.experimental.dense_to_ragged_batch(3)) >>> ds.take(1).get_single_element() <tf.Tensor: shape=(3, 5), dtype=int32, numpy= array([[  98,  111,  111,  107,    0],     [2346, 2369, 2360, 2381, 2340],     [1705, 1578, 1575, 1576,    0]], dtype=int32)>`\
\
Batch, then tokenize for dense outputs (`sequence_length` provided).\
\
Copied!\
\
`>>> inputs = ["Book", "पुस्तक", "کتاب"] >>> tokenizer = keras_hub.tokenizers.UnicodeCodepointTokenizer( ...     sequence_length=5) >>> ds = tf.data.Dataset.from_tensor_slices(inputs) >>> ds = ds.batch(3).map(tokenizer) >>> ds.take(1).get_single_element() <tf.Tensor: shape=(3, 5), dtype=int32, numpy= array([[  98,  111,  111,  107,    0],     [2346, 2369, 2360, 2381, 2340],     [1705, 1578, 1575, 1576,    0]], dtype=int32)>`\
\
Tokenization with truncation.\
\
Copied!\
\
`>>> inputs = ["I Like to Travel a Lot", "मैं किताबें पढ़ना पसंद करता हूं"] >>> tokenizer = keras_hub.tokenizers.UnicodeCodepointTokenizer( ...     sequence_length=5) >>> outputs = tokenizer(inputs) >>> np.array(outputs) array([[ 105,   32,  108,  105,  107],        [2350, 2376, 2306,   32, 2325]], dtype=int32)`\
\
Tokenization with vocabulary\_size.\
\
Copied!\
\
`>>> latin_ext_cutoff = 592 >>> tokenizer = keras_hub.tokenizers.UnicodeCodepointTokenizer( ...     vocabulary_size=latin_ext_cutoff) >>> outputs = tokenizer("¿Cómo estás?") >>> np.array(outputs) array([191,  99, 243, 109, 111,  32, 101, 115, 116, 225, 115,  63],       dtype=int32) >>> outputs = tokenizer("आप कैसे हैं") >>> np.array(outputs) array([591, 591,  32, 591, 591, 591, 591,  32, 591, 591, 591],       dtype=int32)`\
\
Detokenization.\
\
Copied!\
\
`>>> inputs = tf.constant([110, 105, 110, 106,  97], dtype="int32") >>> tokenizer = keras_hub.tokenizers.UnicodeCodepointTokenizer() >>> tokenizer.detokenize(inputs) 'ninja'`\
\
Detokenization with padding.\
\
Copied!\
\
`>>> tokenizer = keras_hub.tokenizers.UnicodeCodepointTokenizer( ...     sequence_length=7) >>> dataset = tf.data.Dataset.from_tensor_slices(["a b c", "b c", "a"]) >>> dataset = dataset.map(tokenizer) >>> dataset.take(1).get_single_element() <tf.Tensor: shape=(7,), dtype=int32,     numpy=array([97, 32, 98, 32, 99,  0,  0], dtype=int32)> >>> detokunbatched = dataset.map(tokenizer.detokenize) >>> detokunbatched.take(1).get_single_element() <tf.Tensor: shape=(), dtype=string, numpy=b'a b c'>`\
\
Detokenization with invalid bytes.\
\
Copied!\
\
`>>> inputs = tf.constant([110, 105, 10000000, 110, 106,  97]) >>> tokenizer = keras_hub.tokenizers.UnicodeCodepointTokenizer( ...     errors="replace", replacement_char=88) >>> tokenizer.detokenize(inputs) 'niXnja'`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/unicode_codepoint_tokenizer.py#L393)\
\
### `tokenize` method\
\
Copied!\
\
`UnicodeCodepointTokenizer.tokenize(inputs)`\
\
Transform input tensors of strings into output tokens.\
\
**Arguments**\
\
*   **inputs**: Input tensor, or dict/list/tuple of input tensors.\
*   **\*args**: Additional positional arguments.\
*   **\*\*kwargs**: Additional keyword arguments.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/unicode_codepoint_tokenizer.py#L439)\
\
### `detokenize` method\
\
Copied!\
\
`UnicodeCodepointTokenizer.detokenize(inputs)`\
\
Transform tokens back into strings.\
\
**Arguments**\
\
*   **inputs**: Input tensor, or dict/list/tuple of input tensors.\
*   **\*args**: Additional positional arguments.\
*   **\*\*kwargs**: Additional keyword arguments.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/unicode_codepoint_tokenizer.py#L292)\
\
### `get_vocabulary` method\
\
Copied!\
\
`UnicodeCodepointTokenizer.get_vocabulary()`\
\
Get the tokenizer vocabulary as a list of strings terms.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/unicode_codepoint_tokenizer.py#L286)\
\
### `vocabulary_size` method\
\
Copied!\
\
`UnicodeCodepointTokenizer.vocabulary_size()`\
\
Get the size of the tokenizer vocabulary.\
\
None implies no vocabulary size was provided\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/unicode_codepoint_tokenizer.py#L457)\
\
### `token_to_id` method\
\
Copied!\
\
`UnicodeCodepointTokenizer.token_to_id(token)`\
\
Convert a string token to an integer id.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/unicode_codepoint_tokenizer.py#L448)\
\
### `id_to_token` method\
\
Copied!\
\
`UnicodeCodepointTokenizer.id_to_token(id)`\
\
Convert an integer id to a string token.\
\
* * *\
\
[UnicodeCodepointTokenizer](https://keras.io/keras_hub/api/tokenizers/unicode_codepoint_tokenizer/#unicodecodepointtokenizer)\
\
[`UnicodeCodepointTokenizer` class](https://keras.io/keras_hub/api/tokenizers/unicode_codepoint_tokenizer/#unicodecodepointtokenizer-class)\
\
[`tokenize` method](https://keras.io/keras_hub/api/tokenizers/unicode_codepoint_tokenizer/#tokenize-method)\
\
[`detokenize` method](https://keras.io/keras_hub/api/tokenizers/unicode_codepoint_tokenizer/#detokenize-method)\
\
[`get_vocabulary` method](https://keras.io/keras_hub/api/tokenizers/unicode_codepoint_tokenizer/#getvocabulary-method)\
\
[`vocabulary_size` method](https://keras.io/keras_hub/api/tokenizers/unicode_codepoint_tokenizer/#vocabularysize-method)\
\
[`token_to_id` method](https://keras.io/keras_hub/api/tokenizers/unicode_codepoint_tokenizer/#tokentoid-method)\
\
[`id_to_token` method](https://keras.io/keras_hub/api/tokenizers/unicode_codepoint_tokenizer/#idtotoken-method)