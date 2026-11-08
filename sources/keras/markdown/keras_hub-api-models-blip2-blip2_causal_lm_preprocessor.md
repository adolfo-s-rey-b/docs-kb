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
 / [Blip2](https://keras.io/keras_hub/api/models/blip2/)
 / BLIP2CausalLMPreprocessor layer

BLIP2CausalLMPreprocessor layer
===============================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/blip2/blip2_causal_lm_preprocessor.py#L18)

### `BLIP2CausalLMPreprocessor` class

Copied!

`keras_hub.models.BLIP2CausalLMPreprocessor(     tokenizer,     image_converter=None,     sequence_length=512,     add_start_token=True,     add_end_token=True,     **kwargs )`

Multimodal preprocessor for the BLIP-2 Causal LM.

This preprocessing layer is meant for use with [`keras_hub.models.BLIP2CausalLM`](https://keras.io/keras_hub/api/models/blip2/blip2_causal_lm#blip2causallm-class)
. It can be configured in two ways: text-only and text + vision, based on whether the passed value of `image_converter` is `None`. For the former, it takes in batches of strings. For the latter, it takes in batches of images and strings. It returns outputs in a `(x, y, sample_weight)` format, where the `y` label is the next token id in the `x` sequence.

For use with generation, the layer also exposes two methods `generate_preprocess()` and `generate_postprocess()`. When this preprocessor is attached to a [`keras_hub.models.BLIP2CausalLM`](https://keras.io/keras_hub/api/models/blip2/blip2_causal_lm#blip2causallm-class)
 instance, these methods will be called implicitly in `generate()`. They can also be called standalone (e.g. to precompute preprocessing inputs for generation in a separate process).

**Arguments**

*   **tokenizer**: A `keras_hub.models.BLIP2OPTTokenizer` or `keras_hub.models.BLIP2FlanT5Tokenizer` instance. The actual tokenizer is resolved from the preset config when using `from_preset()`.
*   **image\_converter**: A `keras_hub.models.BLIP2ImageConverter` instance, or `None`. If `None`, the preprocessor operates in text-only mode.
*   **sequence\_length**: int. The maximum length of the packed token sequence. Defaults to `512`.
*   **add\_start\_token**: bool. Whether to prepend the tokenizer start token to each input sequence. Defaults to `True`.
*   **add\_end\_token**: bool. Whether to append the tokenizer end token to each input sequence. Defaults to `True`.

**Examples**

Copied!

`# Load from a preset. preprocessor = keras_hub.models.BLIP2CausalLMPreprocessor.from_preset(     "blip2_opt_2_7b" )  # Text-only input. preprocessor({"text": ["A photo of a cat", "A photo of a dog"]})  # Image + text input. preprocessor({     "images": np.random.randint(0, 256, (2, 500, 500, 3)),     "text": ["A photo of a cat", "A photo of a dog"], })  # Prepare tokens for generation. preprocessor.generate_preprocess({     "images": np.random.randint(0, 256, (500, 500, 3)),     "text": "A photo of", })  # Map generation outputs back to strings. preprocessor.generate_postprocess({     "token_ids": np.array([[0, 4, 5, 2, 1, 1]]),     "padding_mask": np.array([[1, 1, 1, 1, 0, 0]]), })`

**References**

*   [Li et al., 2023](https://arxiv.org/abs/2301.12597)
    

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`BLIP2CausalLMPreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )`

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

| Preset | Parameters | Description |
| --- | --- | --- |
| [blip2\_opt\_2.7b](https://www.kaggle.com/models/keras/blip2/keras/blip2_opt_2.7b/1) | 3.74B | BLIP-2 model using OPT-2.7B as the frozen language model. |
| [blip2\_flan\_t5\_xl](https://www.kaggle.com/models/keras/blip2/keras/blip2_flan_t5_xl/1) | 3.94B | BLIP-2 model using Flan-T5-XL (~3B) as the frozen language model. |
| [blip2\_opt\_6.7b](https://www.kaggle.com/models/keras/blip2/keras/blip2_opt_6.7b/1) | 7.75B | BLIP-2 model using OPT-6.7B as the frozen language model. |
| [blip2\_flan\_t5\_xxl](https://www.kaggle.com/models/keras/blip2/keras/blip2_flan_t5_xxl/1) | 12.23B | BLIP-2 model using Flan-T5-XXL (~11B) as the frozen language model. |

* * *

### `image_converter` property

Copied!

`keras_hub.models.BLIP2CausalLMPreprocessor.image_converter`

The image converter used to preprocess image data.

* * *

### `tokenizer` property

Copied!

`keras_hub.models.BLIP2CausalLMPreprocessor.tokenizer`

The tokenizer used to tokenize strings.

* * *

[BLIP2CausalLMPreprocessor layer](https://keras.io/keras_hub/api/models/blip2/blip2_causal_lm_preprocessor/#blip2causallmpreprocessor-layer)

[`BLIP2CausalLMPreprocessor` class](https://keras.io/keras_hub/api/models/blip2/blip2_causal_lm_preprocessor/#blip2causallmpreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/blip2/blip2_causal_lm_preprocessor/#frompreset-method)

[`image_converter` property](https://keras.io/keras_hub/api/models/blip2/blip2_causal_lm_preprocessor/#imageconverter-property)

[`tokenizer` property](https://keras.io/keras_hub/api/models/blip2/blip2_causal_lm_preprocessor/#tokenizer-property)