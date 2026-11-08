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
 / [Whisper](https://keras.io/keras_hub/api/models/whisper/)
 / WhisperTokenizer

WhisperTokenizer
================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/whisper/whisper_tokenizer.py#L15)

### `WhisperTokenizer` class

Copied!

`keras_hub.tokenizers.WhisperTokenizer(     vocabulary=None, merges=None, special_tokens=None, language_tokens=None, **kwargs )`

Whisper text tokenizer using Byte-Pair Encoding subword segmentation.

This tokenizer class will tokenize raw strings into integer sequences and is based on [`keras_hub.tokenizers.BytePairTokenizer`](https://keras.io/keras_hub/api/tokenizers/byte_pair_tokenizer#bytepairtokenizer-class)
. This tokenizer does not provide truncation or padding of inputs.

**Arguments**

*   **vocabulary**: string or dict, maps token to integer ids. If it is a string, it should be the file path to a json file.
*   **merges**: string or list, contains the merge rule. If it is a string, it should be the file path to merge rules. The merge rule file should have one merge rule per line. Every merge rule contains merge entities separated by a space.
*   **special\_tokens**: string or dict, maps special tokens to integer IDs. If it is a string, it should be the path to a JSON file.
*   **language\_tokens**: string or dict, maps language tokens to integer IDs. If not None, the tokenizer will be assumed to be a multilingual tokenizer.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/tokenizer.py#L213)

### `from_preset` method

Copied!

`WhisperTokenizer.from_preset(preset, config_file="tokenizer.json", **kwargs)`

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
| [whisper\_tiny\_en](https://www.kaggle.com/models/keras/whisper/keras/whisper_tiny_en/4) | 37.18M | 4-layer Whisper model. Trained on 438,000 hours of labelled English speech data. |
| [whisper\_tiny\_multi](https://www.kaggle.com/models/keras/whisper/keras/whisper_tiny_multi/4) | 37.76M | 4-layer Whisper model. Trained on 680,000 hours of labelled multilingual speech data. |
| [whisper\_base\_multi](https://www.kaggle.com/models/keras/whisper/keras/whisper_base_multi/4) | 72.59M | 6-layer Whisper model. Trained on 680,000 hours of labelled multilingual speech data. |
| [whisper\_base\_en](https://www.kaggle.com/models/keras/whisper/keras/whisper_base_en/4) | 124.44M | 6-layer Whisper model. Trained on 438,000 hours of labelled English speech data. |
| [whisper\_small\_en](https://www.kaggle.com/models/keras/whisper/keras/whisper_small_en/4) | 241.73M | 12-layer Whisper model. Trained on 438,000 hours of labelled English speech data. |
| [whisper\_small\_multi](https://www.kaggle.com/models/keras/whisper/keras/whisper_small_multi/4) | 241.73M | 12-layer Whisper model. Trained on 680,000 hours of labelled multilingual speech data. |
| [whisper\_medium\_en](https://www.kaggle.com/models/keras/whisper/keras/whisper_medium_en/4) | 763.86M | 24-layer Whisper model. Trained on 438,000 hours of labelled English speech data. |
| [whisper\_medium\_multi](https://www.kaggle.com/models/keras/whisper/keras/whisper_medium_multi/4) | 763.86M | 24-layer Whisper model. Trained on 680,000 hours of labelled multilingual speech data. |
| [whisper\_large\_multi](https://www.kaggle.com/models/keras/whisper/keras/whisper_large_multi/4) | 1.54B | 32-layer Whisper model. Trained on 680,000 hours of labelled multilingual speech data. |
| [whisper\_large\_multi\_v2](https://www.kaggle.com/models/keras/whisper/keras/whisper_large_multi_v2/4) | 1.54B | 32-layer Whisper model. Trained for 2.5 epochs on 680,000 hours of labelled multilingual speech data. An improved of `whisper_large_multi`. |

* * *

[WhisperTokenizer](https://keras.io/keras_hub/api/models/whisper/whisper_tokenizer/#whispertokenizer)

[`WhisperTokenizer` class](https://keras.io/keras_hub/api/models/whisper/whisper_tokenizer/#whispertokenizer-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/whisper/whisper_tokenizer/#frompreset-method)