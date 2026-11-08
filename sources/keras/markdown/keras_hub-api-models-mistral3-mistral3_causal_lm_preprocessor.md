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
 / [Mistral3](https://keras.io/keras_hub/api/models/mistral3/)
 / Mistral3CausalLMPreprocessor layer

Mistral3CausalLMPreprocessor layer
==================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/mistral3/mistral3_causal_lm_preprocessor.py#L25)

### `Mistral3CausalLMPreprocessor` class

Copied!

`keras_hub.models.Mistral3CausalLMPreprocessor(     tokenizer,     image_converter=None,     sequence_length=1024,     add_start_token=True,     add_end_token=True,     spatial_merge_size=2,     **kwargs )`

Mistral3 Causal LM preprocessor.

This preprocessing layer is meant for use with [`keras_hub.models.Mistral3CausalLM`](https://keras.io/keras_hub/api/models/mistral3/mistral3_causal_lm#mistral3causallm-class)
. It takes in batches of prompts and (optionally, per-prompt) images and returns outputs in a `(x, y, sample_weight)` format, where the `y` label is the next token id in the `x` sequence.

`x` for `call()`/`generate_preprocess()` should be a dict with `"prompts"` (and optionally `"responses"`) and, for multimodal inputs, an `"images"` key. Images are matched to prompts by their `"[IMG]"` placeholder occurrences, consumed in order — `"images"` can be any reasonable nesting (a single image, a batched array, flat or per-prompt-grouped lists), as long as the total image count matches the total placeholder count. Omitting `"images"` (or passing `x` as a plain string/list of strings) preprocesses as plain text, matching HF's `Mistral3ForConditionalGeneration`, which also supports text-only calls.

For use with generation, the layer also exposes two methods `generate_preprocess()` and `generate_postprocess()`. When this preprocessor is attached to a [`keras_hub.models.Mistral3CausalLM`](https://keras.io/keras_hub/api/models/mistral3/mistral3_causal_lm#mistral3causallm-class)
 instance, these methods will be called implicitly in `generate()`. They can also be called standalone (e.g. to precompute preprocessing inputs for generation in a separate process).

**Arguments**

*   **tokenizer**: A `keras_hub.models.Mistral3Tokenizer` instance.
*   **image\_converter**: A [`keras_hub.layers.Mistral3ImageConverter`](https://keras.io/keras_hub/api/models/mistral3/mistral3_image_converter#mistral3imageconverter-class)
     instance or `None`.
*   **sequence\_length**: The length of the packed inputs.
*   **add\_start\_token**: If `True`, the preprocessor will prepend the tokenizer start token to each input sequence. Default is `True`.
*   **add\_end\_token**: If `True`, the preprocessor will append the tokenizer end token to each input sequence. Default is `True`.
*   **spatial\_merge\_size**: int. The multimodal projector's spatial merge size, used to compute how many image placeholder tokens each image expands to. Defaults to `2`.

**Call arguments**

*   **x**: A dict with `"prompts"` and, optionally, `"images"` keys.
*   **y**: Label data. Should always be `None` as the layer generates labels.
*   **sample\_weight**: Label weights. Should always be `None` as the layer generates label weights.
*   **sequence\_length**: Pass to override the configured `sequence_length` of the layer.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`Mistral3CausalLMPreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )`

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
| [ministral\_3\_3b\_base\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_3b_base_2512_en/1) | 3.85B | 3 billion parameter, 26-layer, pretrained Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_3b\_instruct\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_3b_instruct_2512_en/1) | 3.85B | 3 billion parameter, 26-layer, instruction-tuned Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_3b\_reasoning\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_3b_reasoning_2512_en/1) | 3.85B | 3 billion parameter, 26-layer, reasoning-tuned Ministral 3 model with a Pixtral vision encoder for image input. |
| [shieldstral\_1.0\_3b\_en](https://www.kaggle.com/models/keras/shieldstral/keras/shieldstral_1.0_3b_en/1) | 3.85B | 3 billion parameter, 26-layer Shieldstral model with a Pixtral vision encoder. The model checks text and image content against a safety policy written in natural language. The model returns one safety score for each input. |
| [ministral\_3\_8b\_base\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_8b_base_2512_en/1) | 8.92B | 8 billion parameter, 34-layer, pretrained Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_8b\_instruct\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_8b_instruct_2512_en/1) | 8.92B | 8 billion parameter, 34-layer, instruction-tuned Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_8b\_reasoning\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_8b_reasoning_2512_en/1) | 8.92B | 8 billion parameter, 34-layer, reasoning-tuned Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_14b\_base\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_14b_base_2512_en/1) | 13.95B | 14 billion parameter, 40-layer, pretrained Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_14b\_instruct\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_14b_instruct_2512_en/1) | 13.95B | 14 billion parameter, 40-layer, instruction-tuned Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_14b\_reasoning\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_14b_reasoning_2512_en/1) | 13.95B | 14 billion parameter, 40-layer, reasoning-tuned Ministral 3 model with a Pixtral vision encoder for image input. |
| [mistral\_small\_3.1\_24b\_base\_2503\_en](https://www.kaggle.com/models/keras/mistral3/keras/mistral_small_3.1_24b_base_2503_en/1) | 24.01B | 24 billion parameter, 40-layer, pretrained Mistral3 model with a Pixtral vision encoder for image input. |
| [mistral\_small\_3.1\_24b\_instruct\_2503\_en](https://www.kaggle.com/models/keras/mistral3/keras/mistral_small_3.1_24b_instruct_2503_en/1) | 24.01B | 24 billion parameter, 40-layer, instruction-tuned Mistral3 model with a Pixtral vision encoder for image input. |
| [mistral\_small\_3.2\_24b\_instruct\_2506\_en](https://www.kaggle.com/models/keras/mistral3/keras/mistral_small_3.2_24b_instruct_2506_en/1) | 24.01B | 24 billion parameter, 40-layer, instruction-tuned Mistral3 model with a Pixtral vision encoder for image input. An updated version of mistral\_small\_3.1\_24b\_instruct\_2503\_en with improved instruction-following and reduced repetition. |
| [devstral\_small\_2\_24b\_instruct\_2512\_en](https://www.kaggle.com/models/keras/devstral2/keras/devstral_small_2_24b_instruct_2512_en/1) | 24.01B | 24 billion parameter, 40-layer, instruction-tuned Devstral Small 2 model for agentic software engineering, with a Pixtral vision encoder for image input. |
| [magistral\_small\_2509\_en](https://www.kaggle.com/models/keras/magistral/keras/magistral_small_2509_en/1) | 24.01B | 24 billion parameter, 40-layer, reasoning-tuned Magistral Small model with a Pixtral vision encoder for image input. |

* * *

### `tokenizer` property

Copied!

`keras_hub.models.Mistral3CausalLMPreprocessor.tokenizer`

The tokenizer used to tokenize strings.

* * *

### `image_converter` property

Copied!

`keras_hub.models.Mistral3CausalLMPreprocessor.image_converter`

The image converter used to preprocess image data.

* * *

[Mistral3CausalLMPreprocessor layer](https://keras.io/keras_hub/api/models/mistral3/mistral3_causal_lm_preprocessor/#mistral3causallmpreprocessor-layer)

[`Mistral3CausalLMPreprocessor` class](https://keras.io/keras_hub/api/models/mistral3/mistral3_causal_lm_preprocessor/#mistral3causallmpreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/mistral3/mistral3_causal_lm_preprocessor/#frompreset-method)

[`tokenizer` property](https://keras.io/keras_hub/api/models/mistral3/mistral3_causal_lm_preprocessor/#tokenizer-property)

[`image_converter` property](https://keras.io/keras_hub/api/models/mistral3/mistral3_causal_lm_preprocessor/#imageconverter-property)