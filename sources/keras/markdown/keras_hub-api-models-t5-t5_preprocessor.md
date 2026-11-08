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
 / [T5](https://keras.io/keras_hub/api/models/t5/)
 / T5Preprocessor layer

T5Preprocessor layer
====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/t5/t5_preprocessor.py#L10)

### `T5Preprocessor` class

Copied!

`keras_hub.models.T5Preprocessor(     tokenizer, sequence_length=256, add_start_token=False, add_end_token=True, **kwargs )`

Base class for preprocessing layers.

A `Preprocessor` layer provides a complete preprocessing setup for a given task. It handles tokenization, audio/image conversion, and any other necessary preprocessing steps.

This class can be subclassed similar to any `keras.layers.Layer`, by defining `build()`, `call()` and `get_config()` methods. All subclasses should set the `tokenizer` or `audio_converter` or `image_converter` properties during construction as needed.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`T5Preprocessor.from_preset(preset, config_file="preprocessor.json", **kwargs)`

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

### `tokenizer` property

Copied!

`keras_hub.models.T5Preprocessor.tokenizer`

The tokenizer used to tokenize strings.

* * *

[T5Preprocessor layer](https://keras.io/keras_hub/api/models/t5/t5_preprocessor/#t5preprocessor-layer)

[`T5Preprocessor` class](https://keras.io/keras_hub/api/models/t5/t5_preprocessor/#t5preprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/t5/t5_preprocessor/#frompreset-method)

[`tokenizer` property](https://keras.io/keras_hub/api/models/t5/t5_preprocessor/#tokenizer-property)