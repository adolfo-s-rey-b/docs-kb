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
 / compute\_word\_piece\_vocabulary function

compute\_word\_piece\_vocabulary function
=========================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/word_piece_tokenizer_trainer.py#L15)

### `compute_word_piece_vocabulary` function

Copied!

`keras_hub.tokenizers.compute_word_piece_vocabulary(     data,     vocabulary_size,     vocabulary_output_file=None,     lowercase=False,     strip_accents=False,     split=True,     split_on_cjk=True,     suffix_indicator="##",     reserved_tokens=["[PAD]", "[CLS]", "[SEP]", "[UNK]", "[MASK]"], )`

A utility to train a WordPiece vocabulary.

Trains a WordPiece vocabulary from an input dataset or a list of filenames.

For custom data loading and pretokenization (`split=False`), the input `data` should be a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
. If `data` is a list of filenames, the file format is required to be plain text files, and the text would be read in line by line during training.

**Arguments**

*   **data**: A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
    , or a list of filenames.
*   **vocabulary\_size**: int. The maximum size of a vocabulary to be trained.
*   **vocabulary\_output\_file**: str. The location to write a vocabulary file. defaults to `None`.
*   **lowercase**: bool. If `True`, the input text will be lowercased before tokenization. Defaults to `False`.
*   **strip\_accents**: bool. If `True`, all accent marks will be removed from text before tokenization. Defaults to `False`.
*   **split**: bool. If `True`, input will be split on whitespace and punctuation marks, and all punctuation marks will be kept as tokens. If `False`, input should be split ("pre-tokenized") before calling the tokenizer, and passed as a dense or ragged tensor of whole words. `split` is required to be `True` when `data` is a list of filenames. Defaults to `True`.
*   **split\_on\_cjk**: bool. If `True`, input will be split on CJK characters, i.e., Chinese, Japanese, Korean and Vietnamese characters (https://en.wikipedia.org/wiki/CJK\_Unified\_Ideographs\_(Unicode\_block)). Note that this is applicable only when `split` is `True`. Defaults to `True`.
*   **suffix\_indicator**: str. The characters prepended to a WordPiece to indicate that it is a suffix to another subword. E.g. `"##ing"`. Defaults to `"##"`.
*   **reserved\_tokens**: list of strings. A list of tokens that must be included in the vocabulary.

**Returns**

Returns a list of vocabulary terms.

**Examples**

Basic Usage (from Dataset).

Copied!

`>>> inputs = tf.data.Dataset.from_tensor_slices(["bat sat pat mat rat"]) >>> vocab = compute_word_piece_vocabulary(inputs, 13) >>> vocab ['[PAD]', '[CLS]', '[SEP]', '[UNK]', '[MASK]', 'a', 'b', 'm', 'p', 'r', 's', 't', '##at'] >>> tokenizer = keras_hub.tokenizers.WordPieceTokenizer( ...     vocabulary=vocab, ...     oov_token="[UNK]", ... ) >>> outputs = inputs.map(tokenizer.tokenize) >>> for x in outputs: ...     print(x) tf.Tensor([ 6 12 10 12  8 12  7 12  9 12], shape=(10,), dtype=int32)`

Basic Usage (from filenames).

Copied!

`with open("test.txt", "w+") as f:     f.write("bat sat pat mat rat\n") inputs = ["test.txt"] vocab = keras_hub.tokenizers.compute_word_piece_vocabulary(inputs, 13)`

Custom Split Usage (from Dataset).

Copied!

`>>> def normalize_and_split(x): ...     "Strip punctuation and split on whitespace." ...     x = tf.strings.regex_replace(x, r"\p{P}", "") ...     return tf.strings.split(x) >>> inputs = tf.data.Dataset.from_tensor_slices(["bat sat: pat mat rat.\n"]) >>> split_inputs = inputs.map(normalize_and_split) >>> vocab = compute_word_piece_vocabulary( ...     split_inputs, 13, split=False, ... ) >>> vocab ['[PAD]', '[CLS]', '[SEP]', '[UNK]', '[MASK]', 'a', 'b', 'm', 'p', 'r', 's', 't', '##at'] >>> tokenizer = keras_hub.tokenizers.WordPieceTokenizer(vocabulary=vocab) >>> inputs.map(tokenizer.tokenize)`

Custom Split Usage (from filenames).

Copied!

`def normalize_and_split(x):     "Strip punctuation and split on whitespace."     x = tf.strings.regex_replace(x, r"\p{P}", "")     return tf.strings.split(x) with open("test.txt", "w+") as f:     f.write("bat sat: pat mat rat.\n") inputs = tf.data.TextLineDataset(["test.txt"]) split_inputs = inputs.map(normalize_and_split) vocab = keras_hub.tokenizers.compute_word_piece_vocabulary(     split_inputs, 13, split=False ) tokenizer = keras_hub.tokenizers.WordPieceTokenizer(vocabulary=vocab) inputs.map(tokenizer.tokenize)`

* * *

[compute\_word\_piece\_vocabulary function](https://keras.io/keras_hub/api/tokenizers/compute_word_piece_vocabulary/#computewordpiecevocabulary-function)

[`compute_word_piece_vocabulary` function](https://keras.io/keras_hub/api/tokenizers/compute_word_piece_vocabulary/#computewordpiecevocabulary-function)