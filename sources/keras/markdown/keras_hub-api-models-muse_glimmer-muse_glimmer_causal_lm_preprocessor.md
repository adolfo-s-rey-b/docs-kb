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
 / [MuseGlimmer](https://keras.io/keras_hub/api/models/muse_glimmer/)
 / MuseGlimmerCausalLMPreprocessor layer

MuseGlimmerCausalLMPreprocessor layer
=====================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/muse_glimmer/muse_glimmer_causal_lm_preprocessor.py#L136)

### `MuseGlimmerCausalLMPreprocessor` class

Copied!

`keras_hub.models.MuseGlimmerCausalLMPreprocessor(     tokenizer,     image_converter=None,     video_converter=None,     sequence_length=1024,     add_start_token=True,     add_end_token=True,     **kwargs )`

MuseGlimmer causal LM preprocessor with optional image/video inputs.

For text-only usage this behaves identically to the base `CausalLMPreprocessor`. When an `image_converter`/`video_converter` is provided and the input contains `"images"`/`"videos"`, each occurrence of the tokenizer's `image_token_id`/`video_token_id` placeholder in the prompt expands to the layout of the Hugging Face processor, and `vision_indices` are computed for scattering the vision encoder's output into the text embedding sequence. MuseGlimmer uses standard sequential text positions throughout — no M-RoPE is needed, since spatial awareness lives entirely inside the vision tower.

The layout of an image is the image start token, one placeholder per merged vision token, and the image end token. The layout of a video is the video start token, then one block per temporal group, and the video end token. A block holds the text `Time: {seconds:.1f}s` and one placeholder per merged vision token of the group. The video separator token sits between two blocks. The seconds value is the index of the first frame of the group, divided by the source frame rate. A prompt needs one placeholder per item, also for a video.

A placeholder that already sits between its own start and end tokens takes only the inner part of the layout. The delimiter tokens then do not appear twice.

For training, each prompt needs the same number of same-size media items. `sample_weight` is zero where the label is a vision placeholder.

The input dict can have a `"video_fps"` entry: one frame rate for all videos, or one per prompt or per video. If the number of prompts equals the number of videos, the values apply per video. Without it, the video converter uses its `source_fps`. A training batch needs the same frame count for all videos.

**Arguments**

*   **tokenizer**: A `MuseGlimmerTokenizer` instance.
*   **image\_converter**: A `MuseGlimmerImageConverter` instance, or `None`.
*   **video\_converter**: A `MuseGlimmerVideoConverter` instance, or `None`.
*   **sequence\_length**: int. The length of the packed inputs.
*   **add\_start\_token**: bool. Whether to prepend the tokenizer's start token. Defaults to `True`.
*   **add\_end\_token**: bool. Whether to append the tokenizer's end token. Defaults to `True`.

**Example**

Preprocess prompts for training and for generation.

Copied!

``preprocessor = keras_hub.models.MuseGlimmerCausalLMPreprocessor.from_preset(     "muse_glimmer_30b", sequence_length=512 ) # Call the preprocessor for training. It returns `(x, y, sample_weight)`. x, y, sample_weight = preprocessor(["What is a plane?"]) x, y, sample_weight = preprocessor({     "prompts": ["Describe <|image|>"],     "images": np.ones((1, 224, 224, 3), dtype="float32"), }) # Call `generate_preprocess` for generation. It returns the model inputs. preprocessor.generate_preprocess(["What is a plane?"]) preprocessor.generate_preprocess({     "prompts": ["Describe <|image|>"],     "images": np.ones((1, 224, 224, 3), dtype="float32"), })``

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`MuseGlimmerCausalLMPreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )`

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
| [muse\_glimmer\_30b\_assistant](https://www.kaggle.com/models/keras/museglimmer/keras/muse_glimmer_30b_assistant/1) | 2.56B | MuseGlimmer 30B DFlash Assistant model: 5-layer speculative-decoding drafter for the 30B model. Drafts a 16-token block-diffusion denoised block per forward pass, conditioned on the target model's hidden states. This model must NOT be used standalone. It is designed exclusively as a draft model used from the target model's generation loop. |
| [muse\_glimmer\_30b](https://www.kaggle.com/models/keras/museglimmer/keras/muse_glimmer_30b/1) | 29.78B | 30B-parameter dense causal decoder with an attached windowed-attention perception encoder, distilled from Muse Spark for local agentic use. |

* * *

### `tokenizer` property

Copied!

`keras_hub.models.MuseGlimmerCausalLMPreprocessor.tokenizer`

The tokenizer used to tokenize strings.

* * *

### `image_converter` property

Copied!

`keras_hub.models.MuseGlimmerCausalLMPreprocessor.image_converter`

The image converter used to preprocess image data.

* * *

### `video_converter` property

Copied!

`keras_hub.models.MuseGlimmerCausalLMPreprocessor.video_converter`

The video converter used to preprocess video data.

* * *

[MuseGlimmerCausalLMPreprocessor layer](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_causal_lm_preprocessor/#museglimmercausallmpreprocessor-layer)

[`MuseGlimmerCausalLMPreprocessor` class](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_causal_lm_preprocessor/#museglimmercausallmpreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_causal_lm_preprocessor/#frompreset-method)

[`tokenizer` property](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_causal_lm_preprocessor/#tokenizer-property)

[`image_converter` property](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_causal_lm_preprocessor/#imageconverter-property)

[`video_converter` property](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_causal_lm_preprocessor/#videoconverter-property)