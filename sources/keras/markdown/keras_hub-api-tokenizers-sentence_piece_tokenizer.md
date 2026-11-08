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
 / SentencePieceTokenizer

SentencePieceTokenizer
======================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/sentence_piece_tokenizer.py#L31)

### `SentencePieceTokenizer` class

Copied!

`keras_hub.tokenizers.SentencePieceTokenizer(     proto=None,     sequence_length=None,     dtype="int32",     add_bos=False,     add_eos=False,     **kwargs )`

A SentencePiece tokenizer layer.

This layer provides an implementation of SentencePiece tokenization as described in the [SentencePiece paper](https://arxiv.org/abs/1808.06226)
 and the [SentencePiece package](https://pypi.org/project/sentencepiece/)
. The tokenization will run entirely within the Tensorflow graph, and can be saved inside a [`keras.Model`](https://keras.io/api/models/model#model-class)
.

By default, the layer will output a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
 where the last dimension of the output is ragged after whitespace splitting and sub-word tokenizing. If `sequence_length` is set, the layer will output a dense [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 where all inputs have been padded or truncated to `sequence_length`. The output dtype can be controlled via the `dtype` argument, which should be either an integer or string type.

**Arguments**

*   **proto**: Either a `string` path to a SentencePiece proto file, or a `bytes` object with a serialized SentencePiece proto. See the [SentencePiece repository](https://github.com/google/sentencepiece)
     for more details on the format.
*   **sequence\_length**: If set, the output will be converted to a dense tensor and padded/trimmed so all outputs are of `sequence_length`.
*   **add\_bos**: Add beginning of sentence token to the result.
*   **add\_eos**: Add end of sentence token to the result. Token is always truncated if output is longer than specified `sequence_length`.

**References**

*   [Kudo and Richardson, 2018](https://arxiv.org/abs/1808.06226)
    

**Examples**

From bytes.

Copied!

`def train_sentence_piece_bytes(ds, size):     bytes_io = io.BytesIO()     sentencepiece.SentencePieceTrainer.train(         sentence_iterator=ds.as_numpy_iterator(),         model_writer=bytes_io,         vocab_size=size,     )     return bytes_io.getvalue()  # Train a sentencepiece proto. ds = tf.data.Dataset.from_tensor_slices(["the quick brown fox."]) proto = train_sentence_piece_bytes(ds, 20) # Tokenize inputs. tokenizer = keras_hub.tokenizers.SentencePieceTokenizer(proto=proto) ds = ds.map(tokenizer)`

From a file.

Copied!

`def train_sentence_piece_file(ds, path, size):     with open(path, "wb") as model_file:         sentencepiece.SentencePieceTrainer.train(             sentence_iterator=ds.as_numpy_iterator(),             model_writer=model_file,             vocab_size=size,         )  # Train a sentencepiece proto. ds = tf.data.Dataset.from_tensor_slices(["the quick brown fox."]) proto = train_sentence_piece_file(ds, "model.spm", 20) # Tokenize inputs. tokenizer = keras_hub.tokenizers.SentencePieceTokenizer(proto="model.spm") ds = ds.map(tokenizer)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/sentence_piece_tokenizer.py#L417)

### `tokenize` method

Copied!

`SentencePieceTokenizer.tokenize(inputs)`

Transform input tensors of strings into output tokens.

**Arguments**

*   **inputs**: Input tensor, or dict/list/tuple of input tensors.
*   **\*args**: Additional positional arguments.
*   **\*\*kwargs**: Additional keyword arguments.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/sentence_piece_tokenizer.py#L482)

### `detokenize` method

Copied!

`SentencePieceTokenizer.detokenize(inputs)`

Transform tokens back into strings.

**Arguments**

*   **inputs**: Input tensor, or dict/list/tuple of input tensors.
*   **\*args**: Additional positional arguments.
*   **\*\*kwargs**: Additional keyword arguments.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/sentence_piece_tokenizer.py#L268)

### `get_vocabulary` method

Copied!

`SentencePieceTokenizer.get_vocabulary()`

Get the tokenizer vocabulary.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/sentence_piece_tokenizer.py#L263)

### `vocabulary_size` method

Copied!

`SentencePieceTokenizer.vocabulary_size()`

Get the integer size of the tokenizer vocabulary.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/sentence_piece_tokenizer.py#L294)

### `token_to_id` method

Copied!

`SentencePieceTokenizer.token_to_id(token)`

Convert a string token to an integer id.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/sentence_piece_tokenizer.py#L281)

### `id_to_token` method

Copied!

`SentencePieceTokenizer.id_to_token(id)`

Convert an integer id to a string token.

* * *

[SentencePieceTokenizer](https://keras.io/keras_hub/api/tokenizers/sentence_piece_tokenizer/#sentencepiecetokenizer)

[`SentencePieceTokenizer` class](https://keras.io/keras_hub/api/tokenizers/sentence_piece_tokenizer/#sentencepiecetokenizer-class)

[`tokenize` method](https://keras.io/keras_hub/api/tokenizers/sentence_piece_tokenizer/#tokenize-method)

[`detokenize` method](https://keras.io/keras_hub/api/tokenizers/sentence_piece_tokenizer/#detokenize-method)

[`get_vocabulary` method](https://keras.io/keras_hub/api/tokenizers/sentence_piece_tokenizer/#getvocabulary-method)

[`vocabulary_size` method](https://keras.io/keras_hub/api/tokenizers/sentence_piece_tokenizer/#vocabularysize-method)

[`token_to_id` method](https://keras.io/keras_hub/api/tokenizers/sentence_piece_tokenizer/#tokentoid-method)

[`id_to_token` method](https://keras.io/keras_hub/api/tokenizers/sentence_piece_tokenizer/#idtotoken-method)