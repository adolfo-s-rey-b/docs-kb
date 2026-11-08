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
 / [Flux](https://keras.io/keras_hub/api/models/flux/)
 / FluxTextToImagePreprocessor layer

FluxTextToImagePreprocessor layer
=================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/flux/flux_text_to_image_preprocessor.py#L9)

### `FluxTextToImagePreprocessor` class

Copied!

`keras_hub.models.FluxTextToImagePreprocessor(     clip_l_preprocessor, t5_preprocessor=None, **kwargs )`

Flux text-to-image model preprocessor.

This preprocessing layer is meant for use with [`keras_hub.models.FluxTextToImagePreprocessor`](https://keras.io/keras_hub/api/models/flux/flux_text_to_image_preprocessor#fluxtexttoimagepreprocessor-class)
.

For use with generation, the layer exposes one methods `generate_preprocess()`.

**Arguments**

*   **clip\_l\_preprocessor**: A [`keras_hub.models.CLIPPreprocessor`](https://keras.io/keras_hub/api/models/clip/clip_preprocessor#clippreprocessor-class)
     instance.
*   **t5\_preprocessor**: An optional [`keras_hub.models.T5Preprocessor`](https://keras.io/keras_hub/api/models/t5/t5_preprocessor#t5preprocessor-class)
     instance.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`FluxTextToImagePreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )`

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

[FluxTextToImagePreprocessor layer](https://keras.io/keras_hub/api/models/flux/flux_text_to_image_preprocessor/#fluxtexttoimagepreprocessor-layer)

[`FluxTextToImagePreprocessor` class](https://keras.io/keras_hub/api/models/flux/flux_text_to_image_preprocessor/#fluxtexttoimagepreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/flux/flux_text_to_image_preprocessor/#frompreset-method)