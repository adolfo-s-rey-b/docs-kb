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
 / [Model Architectures](https://keras.io/keras_hub/api/models/)
 / [PARSeq](https://keras.io/keras_hub/api/models/parseq/)
 / PARSeqTokenizer

PARSeqTokenizer
===============

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/parseq/parseq_tokenizer.py#L32)

### `PARSeqTokenizer` class

Copied!

``keras_hub.tokenizers.PARSeqTokenizer(     vocabulary=[         "0",         "1",         "2",         "3",         "4",         "5",         "6",         "7",         "8",         "9",         "a",         "b",         "c",         "d",         "e",         "f",         "g",         "h",         "i",         "j",         "k",         "l",         "m",         "n",         "o",         "p",         "q",         "r",         "s",         "t",         "u",         "v",         "w",         "x",         "y",         "z",         "A",         "B",         "C",         "D",         "E",         "F",         "G",         "H",         "I",         "J",         "K",         "L",         "M",         "N",         "O",         "P",         "Q",         "R",         "S",         "T",         "U",         "V",         "W",         "X",         "Y",         "Z",         "!",         '"',         "#",         "$",         "%",         "&",         "'",         "(",         ")",         "*",         "+",         ",",         "-",         ".",         "/",         ":",         ";",         "<",         "=",         ">",         "?",         "@",         "[",         "\\",         "]",         "^",         "_",         "`",         "{",         "|",         "}",         "~",     ],     remove_whitespace=True,     normalize_unicode=True,     max_label_length=25,     dtype="int32",     **kwargs )``

A Tokenizer for PARSeq models, designed for OCR tasks.

This tokenizer converts strings into sequences of integer IDs or string tokens, and vice-versa. It supports various preprocessing steps such as whitespace removal, Unicode normalization, and limiting the maximum label length. It also provides functionality to save and load the vocabulary from a file.

**Arguments**

*   **vocabulary**: str. A string or iterable representing the vocabulary to use. If a string, it's treated as the path to a vocabulary file. If an iterable, it's treated as a list of characters forming the vocabulary. Defaults to `PARSEQ_VOCAB`.
*   **remove\_whitespace**: bool. Whether to remove whitespace characters from the input. Defaults to `True`.
*   **normalize\_unicode**: bool. Whether to normalize Unicode characters in the input using NFKD normalization and remove non-ASCII characters. Defaults to `True`.
*   **max\_label\_length**: int. The maximum length of the tokenized output. Longer labels will be truncated. Defaults to `25`.
*   **dtype**: str. The data type of the tokenized output. Must be an integer type (e.g., "int32") or a string type ("string"). Defaults to `"int32"`.
*   **\*\*kwargs**: Additional keyword arguments passed to the base `keras.layers.Layer` constructor.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/tokenizer.py#L213)

### `from_preset` method

Copied!

`PARSeqTokenizer.from_preset(preset, config_file="tokenizer.json", **kwargs)`

Instantiate a `keras_hub.models.Tokenizer` from a model preset.

A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as one of:

1.  a built-in preset identifier like `'bert_base_en'`
2.  a Kaggle Models handle like `'kaggle://user/bert/keras/bert_base_en'`
3.  a Hugging Face handle like `'hf://user/bert_base_en'`
4.  a path to a local preset directory like `'./bert_base_en'`

For any `Tokenizer` subclass, you can run `cls.presets.keys()` to list all built-in presets available on the class.

This constructor can be called in one of two ways. Either from the base class like `keras_hub.models.Tokenizer.from_preset()`, or from a model class like `keras_hub.models.GemmaTokenizer.from_preset()`. If calling from the base class, the subclass of the returning object will be inferred from the config in the preset directory.

**Arguments**

*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.
*   **load\_weights**: bool. If `True`, the weights will be loaded into the model architecture. If `False`, the weights will be randomly initialized.

**Examples**

Copied!

`# Load a preset tokenizer. tokenizer = keras_hub.tokenizer.Tokenizer.from_preset("bert_base_en")  # Tokenize some input. tokenizer("The quick brown fox tripped.")  # Detokenize some input. tokenizer.detokenize([5, 6, 7, 8, 9])`

* * *

[PARSeqTokenizer](https://keras.io/keras_hub/api/models/parseq/parseq_tokenizer/#parseqtokenizer)

[`PARSeqTokenizer` class](https://keras.io/keras_hub/api/models/parseq/parseq_tokenizer/#parseqtokenizer-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/parseq/parseq_tokenizer/#frompreset-method)