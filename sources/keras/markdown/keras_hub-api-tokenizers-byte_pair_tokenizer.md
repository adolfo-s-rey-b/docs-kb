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
 / BytePairTokenizer

BytePairTokenizer
=================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/byte_pair_tokenizer.py#L216)

### `BytePairTokenizer` class

Copied!

`keras_hub.tokenizers.BytePairTokenizer(     vocabulary=None,     merges=None,     sequence_length=None,     add_prefix_space=False,     unsplittable_tokens=None,     dtype="int32",     **kwargs )`

Bype-pair encoding tokenizer layer.

This BPE tokenizer provides the same functionality as the official GPT-2 tokenizer. Given the same `vocabulary` which maps tokens to ids, and `merges` which describes BPE merge rules, it should provide the same output as OpenAI implementation (https://github.com/openai/gpt-2/blob/master/src/encoder.py). Different from OpenAI, this implementation is graph-compatible, so you can use it within a [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)
 pipeline.

If input is a batch of strings (rank > 0): By default, the layer will output a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
 where the last dimension of the output is ragged. If `sequence_length` is set, the layer will output a dense [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 where all inputs have been padded or truncated to `sequence_length`. If input is a scalar string (rank == 0): By default, the layer will output a dense [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 with static shape `[None]`. If `sequence_length` is set, the output will be a dense [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 of shape `[sequence_length]`.

**Arguments**

*   **vocabulary**: string or dict, maps token to integer ids. If it is a string, it should be the file path to a json file.
*   **merges**: string or list, contains the merge rule. If it is a string, it should be the file path to merge rules. The merge rule file should have one merge rule per line.
*   **sequence\_length**: int. If set, the output will be padded or truncated to the `sequence_length`. Defaults to `None`.
*   **add\_prefix\_space**: bool. Whether to add an initial space to the input. This tokenizer is whitespace aware, and will tokenize a word with a leading space differently. Adding a prefix space to the first word will cause it to be tokenized equivalently to all subsequent words in the sequence. Defaults to `False`.
*   **unsplittable\_tokens**: list. A list of strings that will never be split during the word-level splitting applied before the byte-pair encoding. This can be used to ensure special tokens map to unique indices in the vocabulary, even if these special tokens contain splittable characters such as punctuation. Special tokens must still be included in `vocabulary`. Defaults to `None`.

**Examples**

Tokenize

Copied!

`>>> merge = ["b u", "t t", "e r", "bu tt", "butt er", "f l", "fl y"] >>> vocab = [] >>> [vocab.extend([a, b, a + b]) for a, b in [m.split(" ") for m in merge]] >>> vocab = sorted(set(vocab))  # Remove duplicates >>> vocab = dict([(token, i) for i, token in enumerate(vocab)]) >>> tokenizer = keras_hub.tokenizers.BytePairTokenizer(vocab, merge) >>> outputs = tokenizer("butterfly") >>> np.array(outputs) array([3, 8], dtype=int32) >>> seq1, seq2 = tokenizer(["butterfly", "butter"]) >>> np.array(seq1) array([3, 8]) >>> np.array(seq2) array([3]) >>> tokenizer = keras_hub.tokenizers.BytePairTokenizer( ...     vocab, merge, sequence_length=2) >>> seq1, seq2 = tokenizer(["butterfly", "butter"]) >>> np.array(seq1) array([3, 8], dtype=int32) >>> np.array(seq2) array([3, 0], dtype=int32)`

Detokenize

Copied!

`>>> tokenizer = keras_hub.tokenizers.BytePairTokenizer(vocab, merge) >>> tokenizer.detokenize([[3, 8]]) ['butterfly']`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/byte_pair_tokenizer.py#L832)

### `tokenize` method

Copied!

`BytePairTokenizer.tokenize(inputs)`

Transform input tensors of strings into output tokens.

**Arguments**

*   **inputs**: Input tensor, or dict/list/tuple of input tensors.
*   **\*args**: Additional positional arguments.
*   **\*\*kwargs**: Additional keyword arguments.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/byte_pair_tokenizer.py#L909)

### `detokenize` method

Copied!

`BytePairTokenizer.detokenize(inputs)`

Transform tokens back into strings.

**Arguments**

*   **inputs**: Input tensor, or dict/list/tuple of input tensors.
*   **\*args**: Additional positional arguments.
*   **\*\*kwargs**: Additional keyword arguments.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/byte_pair_tokenizer.py#L523)

### `get_vocabulary` method

Copied!

`BytePairTokenizer.get_vocabulary()`

Get the tokenizer vocabulary as a list of strings tokens.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/byte_pair_tokenizer.py#L528)

### `vocabulary_size` method

Copied!

`BytePairTokenizer.vocabulary_size()`

Get the integer size of the tokenizer vocabulary.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/byte_pair_tokenizer.py#L573)

### `token_to_id` method

Copied!

`BytePairTokenizer.token_to_id(token)`

Convert a string token to an integer id.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/byte_pair_tokenizer.py#L554)

### `id_to_token` method

Copied!

`BytePairTokenizer.id_to_token(id)`

Convert an integer id to a string token.

* * *

[BytePairTokenizer](https://keras.io/keras_hub/api/tokenizers/byte_pair_tokenizer/#bytepairtokenizer)

[`BytePairTokenizer` class](https://keras.io/keras_hub/api/tokenizers/byte_pair_tokenizer/#bytepairtokenizer-class)

[`tokenize` method](https://keras.io/keras_hub/api/tokenizers/byte_pair_tokenizer/#tokenize-method)

[`detokenize` method](https://keras.io/keras_hub/api/tokenizers/byte_pair_tokenizer/#detokenize-method)

[`get_vocabulary` method](https://keras.io/keras_hub/api/tokenizers/byte_pair_tokenizer/#getvocabulary-method)

[`vocabulary_size` method](https://keras.io/keras_hub/api/tokenizers/byte_pair_tokenizer/#vocabularysize-method)

[`token_to_id` method](https://keras.io/keras_hub/api/tokenizers/byte_pair_tokenizer/#tokentoid-method)

[`id_to_token` method](https://keras.io/keras_hub/api/tokenizers/byte_pair_tokenizer/#idtotoken-method)