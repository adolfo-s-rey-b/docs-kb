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
 / [Modeling API](https://keras.io/keras_hub/api/base_classes/)
 / Preprocessor

Preprocessor
============

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L15)

### `Preprocessor` class

Copied!

`keras_hub.models.Preprocessor()`

Base class for preprocessing layers.

A `Preprocessor` layer provides a complete preprocessing setup for a given task. It handles tokenization, audio/image conversion, and any other necessary preprocessing steps.

This class can be subclassed similar to any `keras.layers.Layer`, by defining `build()`, `call()` and `get_config()` methods. All subclasses should set the `tokenizer` or `audio_converter` or `image_converter` properties during construction as needed.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`Preprocessor.from_preset(preset, config_file="preprocessor.json", **kwargs)`

Instantiate a [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 from a model preset.

A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as one of:

1.  a built-in preset identifier like `'bert_base_en'`
2.  a Kaggle Models handle like `'kaggle://user/bert/keras/bert_base_en'`
3.  a Hugging Face handle like `'hf://user/bert_base_en'`
4.  a path to a local preset directory like `'./bert_base_en'`

For any `Preprocessor` subclass, you can run `cls.presets.keys()` to list all built-in presets available on the class.

As there are usually multiple preprocessing classes for a given model, this method should be called on a specific subclass like `keras_hub.models.BertTextClassifierPreprocessor.from_preset()`.

**Arguments**

*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.

**Examples**

Copied!

`# Load a preprocessor for Gemma generation. preprocessor = keras_hub.models.CausalLMPreprocessor.from_preset(     "gemma_2b_en", )  # Load a preprocessor for Bert classification. preprocessor = keras_hub.models.TextClassifierPreprocessor.from_preset(     "bert_base_en", )`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L254)

### `save_to_preset` method

Copied!

`Preprocessor.save_to_preset(preset_dir)`

Save preprocessor to a preset directory.

**Arguments**

*   **preset\_dir**: The path to the local model preset directory.

* * *

### `tokenizer` property

Copied!

`keras_hub.models.Preprocessor.tokenizer`

The tokenizer used to tokenize strings.

* * *

[Preprocessor](https://keras.io/keras_hub/api/base_classes/preprocessor/#preprocessor)

[`Preprocessor` class](https://keras.io/keras_hub/api/base_classes/preprocessor/#preprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/base_classes/preprocessor/#frompreset-method)

[`save_to_preset` method](https://keras.io/keras_hub/api/base_classes/preprocessor/#savetopreset-method)

[`tokenizer` property](https://keras.io/keras_hub/api/base_classes/preprocessor/#tokenizer-property)