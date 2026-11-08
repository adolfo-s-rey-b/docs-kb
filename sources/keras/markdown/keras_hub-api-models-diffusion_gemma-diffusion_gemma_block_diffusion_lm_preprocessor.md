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
 / [DiffusionGemma](https://keras.io/keras_hub/api/models/diffusion_gemma/)
 / DiffusionGemmaBlockDiffusionLMPreprocessor layer

DiffusionGemmaBlockDiffusionLMPreprocessor layer
================================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/diffusion_gemma/diffusion_gemma_block_diffusion_lm_preprocessor.py#L34)

### `DiffusionGemmaBlockDiffusionLMPreprocessor` class

Copied!

`keras_hub.models.DiffusionGemmaBlockDiffusionLMPreprocessor(     tokenizer,     image_converter=None,     sequence_length=1024,     canvas_length=256,     add_start_token=True,     add_end_token=True,     max_images_per_prompt=2,     num_vision_tokens_per_image=280,     stop_token_ids=None,     **kwargs )`

Preprocessing layer for DiffusionGemma diffusion language model tasks.

Tokenizes and packs prompt strings, optionally expanding image placeholders. The task model creates the canvas during generation.

This layer supports two operational modes: - **Text-only**: no converters provided; plain string or dict with `"prompts"` key accepted. - **Image**: pass an `image_converter`; the prompt may contain `<|image|>` placeholders that are expanded to per-patch soft tokens.

The preprocessor accepts input as plain strings **or** as dicts with the following keys:

*   `"prompts"` (required): string or batch of strings.
*   `"responses"` (optional): string or batch of strings used only during training (the `call()` path).
*   `"images"` (optional): image tensor(s) matching `<|image|>` occurrences in the prompts.

During generation (`generate_preprocess()`), only the packed prompt tokens are returned. The canvas is initialised inside `generate_step` via `_init_canvas` so that `_encode_prompt` always receives the prompt alone, matching the HuggingFace encoder/decoder split.

**Arguments**

*   **tokenizer**: A `keras_hub.models.DiffusionGemmaTokenizer` instance.
*   **image\_converter**: A [`keras_hub.layers.DiffusionGemmaImageConverter`](https://keras.io/keras_hub/api/models/diffusion_gemma/diffusion_gemma_image_converter#diffusiongemmaimageconverter-class)
     instance. Defaults to `None`.
*   **sequence\_length**: int. Maximum prompt sequence length. Defaults to `1024`.
*   **canvas\_length**: int. Number of canvas tokens. The preprocessor stores and serializes this value but does not use it. The task model `canvas_length` sets the canvas size. Defaults to `256`.
*   **add\_start\_token**: bool. Whether to prepend the BOS token. Defaults to `True`.
*   **add\_end\_token**: bool. Whether to append the EOS token after the prompt. Defaults to `True`.
*   **max\_images\_per\_prompt**: int. Maximum number of images per sample. Defaults to `2`.
*   **num\_vision\_tokens\_per\_image**: int. Vision placeholder tokens per image. Defaults to `280`.
*   **stop\_token\_ids**: Optional tuple of token IDs. Stripped from decoded text during `generate_postprocess()`, in addition to the tokenizer's special tokens. Defaults to `None`.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`DiffusionGemmaBlockDiffusionLMPreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )`

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
| [diffusion\_gemma\_26b\_a4b\_it](https://www.kaggle.com/models/keras/diffusion-gemma/keras/diffusion_gemma_26b_a4b_it/1) | 25.82B | DiffusionGemma 26B MoE instruction-tuned model. 25.8B total parameters (3.8B active), 30 layers, 128 experts. |

* * *

### `tokenizer` property

Copied!

`keras_hub.models.DiffusionGemmaBlockDiffusionLMPreprocessor.tokenizer`

The tokenizer used to tokenize strings.

* * *

### `image_converter` property

Copied!

`keras_hub.models.DiffusionGemmaBlockDiffusionLMPreprocessor.image_converter`

The image converter used to preprocess image data.

* * *

[DiffusionGemmaBlockDiffusionLMPreprocessor layer](https://keras.io/keras_hub/api/models/diffusion_gemma/diffusion_gemma_block_diffusion_lm_preprocessor/#diffusiongemmablockdiffusionlmpreprocessor-layer)

[`DiffusionGemmaBlockDiffusionLMPreprocessor` class](https://keras.io/keras_hub/api/models/diffusion_gemma/diffusion_gemma_block_diffusion_lm_preprocessor/#diffusiongemmablockdiffusionlmpreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/diffusion_gemma/diffusion_gemma_block_diffusion_lm_preprocessor/#frompreset-method)

[`tokenizer` property](https://keras.io/keras_hub/api/models/diffusion_gemma/diffusion_gemma_block_diffusion_lm_preprocessor/#tokenizer-property)

[`image_converter` property](https://keras.io/keras_hub/api/models/diffusion_gemma/diffusion_gemma_block_diffusion_lm_preprocessor/#imageconverter-property)