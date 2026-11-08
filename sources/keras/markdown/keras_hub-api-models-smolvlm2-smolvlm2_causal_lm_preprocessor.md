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
 / [SmolVLM2](https://keras.io/keras_hub/api/models/smolvlm2/)
 / SmolVLM2CausalLMPreprocessor layer

SmolVLM2CausalLMPreprocessor layer
==================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/smolvlm2/smolvlm2_causal_lm_preprocessor.py#L120)

### `SmolVLM2CausalLMPreprocessor` class

Copied!

`keras_hub.models.SmolVLM2CausalLMPreprocessor(     tokenizer,     image_converter=None,     video_converter=None,     sequence_length=1024,     add_start_token=False,     add_end_token=True,     image_seq_len=64,     **kwargs )`

Preprocessor for SmolVLM2 causal language models.

This preprocessing layer handles tokenization and image processing for the SmolVLM2 model. It tokenizes text inputs, processes images via the image converter, and packs them into the format expected by `SmolVLM2CausalLM`.

For multimodal inputs, prompts should contain a single `<image>` placeholder per image. The preprocessor expands each `<image>` into the full HF-style token sequence:

Copied!

` ``<fake_token_around_image><row_R_col_C><image>×N ... `` ``<global-img><image>×N<fake_token_around_image>`` `

The expansion count `N` (`image_seq_len`) is computed as::

Copied!

`N = (max_image_size / patch_size)² / scale_factor²`

For text-only inputs, no `pixel_values` or `vision_indices` are returned; `SmolVLM2Backbone` fills in empty placeholders.

During training (`fit()`), image inputs are supported only when the image converter is created with `do_image_splitting=False`: the number of crops for a split image depends on its original size, which cannot be resolved inside the `[`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)` graph. The shipped preset default has `do_image_splitting=True`, so this must be changed before training. Video inputs are inference-only.

**Arguments**

*   **tokenizer**: A `SmolVLM2Tokenizer` instance.
*   **image\_converter**: A `SmolVLM2ImageConverter` instance or `None`.
*   **video\_converter**: A `SmolVLM2VideoConverter` instance or `None`.
*   **sequence\_length**: int. Maximum sequence length. Default `1024`.
*   **add\_start\_token**: bool. Whether to prepend BOS. Default `False` (matching HF's `add_bos_token`).
*   **add\_end\_token**: bool. Whether to append EOS. Default `True`.
*   **image\_seq\_len**: int. Number of `<image>` tokens per sub-image crop. Default `64` for the 256M preset (`(512/16)² / 4² = 64`).

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`SmolVLM2CausalLMPreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )`

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
| [smolvlm2\_256m\_video\_instruct](https://www.kaggle.com/models/keras/smolvlm2/keras/smolvlm2_256m_video_instruct/1) | 256.48M | 256 million parameter SmolVLM2 vision-language model with a 30-layer SmolLM2 text decoder and a 12-layer SigLIP vision encoder (512x512 images). Instruction-tuned for image and video understanding. |
| [smolvlm2\_500m\_video\_instruct](https://www.kaggle.com/models/keras/smolvlm2/keras/smolvlm2_500m_video_instruct/1) | 507.48M | 500 million parameter SmolVLM2 vision-language model with a 32-layer SmolLM2 text decoder and a 12-layer SigLIP vision encoder (512x512 images). Instruction-tuned for image and video understanding. |
| [smolvlm2\_2.2b\_instruct](https://www.kaggle.com/models/keras/smolvlm2/keras/smolvlm2_2.2b_instruct/1) | 2.25B | 2.2 billion parameter SmolVLM2 vision-language model with a 24-layer SmolLM2 text decoder and a 27-layer SigLIP vision encoder (384x384 images). Instruction-tuned for image and video understanding. |

* * *

### `tokenizer` property

Copied!

`keras_hub.models.SmolVLM2CausalLMPreprocessor.tokenizer`

The tokenizer used to tokenize strings.

* * *

### `image_converter` property

Copied!

`keras_hub.models.SmolVLM2CausalLMPreprocessor.image_converter`

The image converter used to preprocess image data.

* * *

### `video_converter` property

Copied!

`keras_hub.models.SmolVLM2CausalLMPreprocessor.video_converter`

The video converter used to preprocess video data.

* * *

[SmolVLM2CausalLMPreprocessor layer](https://keras.io/keras_hub/api/models/smolvlm2/smolvlm2_causal_lm_preprocessor/#smolvlm2causallmpreprocessor-layer)

[`SmolVLM2CausalLMPreprocessor` class](https://keras.io/keras_hub/api/models/smolvlm2/smolvlm2_causal_lm_preprocessor/#smolvlm2causallmpreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/smolvlm2/smolvlm2_causal_lm_preprocessor/#frompreset-method)

[`tokenizer` property](https://keras.io/keras_hub/api/models/smolvlm2/smolvlm2_causal_lm_preprocessor/#tokenizer-property)

[`image_converter` property](https://keras.io/keras_hub/api/models/smolvlm2/smolvlm2_causal_lm_preprocessor/#imageconverter-property)

[`video_converter` property](https://keras.io/keras_hub/api/models/smolvlm2/smolvlm2_causal_lm_preprocessor/#videoconverter-property)