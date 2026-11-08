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
 / [RWKV7](https://keras.io/keras_hub/api/models/rwkv7/)
 / RWKV7Tokenizer

RWKV7Tokenizer
==============

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/rwkv7/rwkv7_tokenizer.py#L208)

### `RWKVTokenizer` class

Copied!

`keras_hub.tokenizers.RWKVTokenizer(     vocabulary=None,     dtype="int32",     pad_token_id=0,     start_token_id=None,     end_token_id=None,     **kwargs )`

RWKV byte-level tokenizer with longest-match trie search.

This tokenizer maps raw text to a sequence of integer token ids using a fixed vocabulary and a greedy longest-match algorithm.

**Arguments**

*   **vocabulary**: list of strings, each line formatted as " ".
*   **dtype**: output dtype for tensor operations. Must be integer or string type.

**Examples**

Copied!

`vocab = ["0 ' ' 1", "1 '\n' 1", "2 'the' 3", "3 'hello' 5"] tok = RWKVTokenizer(vocabulary=vocab) tok("hello the")`

Output: \[3, 0, 2\]

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/tokenizer.py#L213)

### `from_preset` method

Copied!

`RWKVTokenizer.from_preset(preset, config_file="tokenizer.json", **kwargs)`

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

| Preset | Parameters | Description |
| --- | --- | --- |
| [rwkv7\_g1a\_0.1b\_en](https://www.kaggle.com/models/keras/rwkv7/keras/rwkv7_g1a_0.1b/1) | 150.00M | 150 million parameter RWKV7 model. Optimized for edge devices and mobile deployment. |
| [rwkv7\_g1a\_0.3b\_en](https://www.kaggle.com/models/keras/rwkv7/keras/rwkv7_g1a_0.3b/1) | 400.00M | 400 million parameter RWKV7 model. Small variant balancing speed and instruction following. |

* * *

[RWKV7Tokenizer](https://keras.io/keras_hub/api/models/rwkv7/rwkv7_tokenizer/#rwkv7tokenizer)

[`RWKVTokenizer` class](https://keras.io/keras_hub/api/models/rwkv7/rwkv7_tokenizer/#rwkvtokenizer-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/rwkv7/rwkv7_tokenizer/#frompreset-method)