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
 / compute\_sentence\_piece\_proto function

compute\_sentence\_piece\_proto function
========================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/sentence_piece_tokenizer_trainer.py#L15)

### `compute_sentence_piece_proto` function

Copied!

`keras_hub.tokenizers.compute_sentence_piece_proto(     data, vocabulary_size, model_type="unigram", proto_output_file=None, lowercase=False )`

A utility to train a SentencePiece vocabulary.

Trains a SentencePiece vocabulary from an input dataset or a list of filenames.

If `data` is a list of filenames, the file format is required to be plain text files, and the text will be read in line by line during training.

**Arguments**

*   **data**: A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
    , or a list of filenames.
*   **vocabulary\_size**: int. The maximum size of a vocabulary to be trained.
*   **model\_type**: str. The model algorithm must be one of `"unigram"`, `"bpe"`, `"word"` or `"char"`. Defaults to `"unigram"`.
*   **proto\_output\_file**: str. If provided it will be used as model\_file which is passed to model\_writer. If `None`, the model\_file will be `io.BytesIO` object. Defaults to `None`.
*   **lowercase**: bool. If True, the input text will be lowercased before tokenization. Defaults to `False`.

**Returns**

A `bytes` object with a serialized SentencePiece proto or `None` if proto\_output\_file if provided.

**Examples**

Basic Usage (from Dataset).

Copied!

`>>> inputs = tf.data.Dataset.from_tensor_slices(["Drifting Along"]) >>> proto = keras_hub.tokenizers.compute_sentence_piece_proto( ...     inputs, vocabulary_size=15) >>> tokenizer = keras_hub.tokenizers.SentencePieceTokenizer(proto=proto) >>> outputs = inputs.map(tokenizer) >>> for output in outputs: ...     print(output) tf.Tensor([ 4  8 12  5  9 14  5  6 13  4  7 10 11  6 13], shape=(15,), dtype=int32)`

Basic Usage (with files).

Copied!

`with open("test.txt", "w+") as f: f.write("Drifting Along\n") inputs = ["test.txt"] proto = keras_hub.tokenizers.compute_sentence_piece_proto(      inputs, vocabulary_size=15, proto_output_file="model.spm") tokenizer = keras_hub.tokenizers.SentencePieceTokenizer(proto="model.spm") ds = tf.data.Dataset.from_tensor_slices(["the quick brown fox."]) ds = ds.map(tokenizer)`

Usage with lowercase

Copied!

`>>> inputs = tf.data.Dataset.from_tensor_slices(["Drifting Along"]) >>> proto = keras_hub.tokenizers.compute_sentence_piece_proto( ...     inputs, vocabulary_size=15, lowercase=True) >>> tokenizer = keras_hub.tokenizers.SentencePieceTokenizer(proto=proto) >>> outputs = inputs.map(tokenizer) >>> for output in outputs: ...     print(output) tf.Tensor([ 4  8 12  5  9 14  5  6 13  4  7 10 11  6 13], shape=(15,), dtype=int32)`

* * *

[compute\_sentence\_piece\_proto function](https://keras.io/keras_hub/api/tokenizers/compute_sentence_piece_proto/#computesentencepieceproto-function)

[`compute_sentence_piece_proto` function](https://keras.io/keras_hub/api/tokenizers/compute_sentence_piece_proto/#computesentencepieceproto-function)