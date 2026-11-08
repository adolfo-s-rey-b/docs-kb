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
 / [Gemma4](https://keras.io/keras_hub/api/models/gemma4/)
 / Gemma4CausalLMPreprocessor layer

Gemma4CausalLMPreprocessor layer
================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/gemma4/gemma4_causal_lm_preprocessor.py#L56)

### `Gemma4CausalLMPreprocessor` class

Copied!

`keras_hub.models.Gemma4CausalLMPreprocessor(     tokenizer,     image_converter=None,     audio_converter=None,     video_converter=None,     sequence_length=1024,     add_start_token=True,     add_end_token=True,     max_images_per_prompt=2,     num_vision_tokens_per_image=280,     max_audio_clips_per_prompt=1,     num_audio_tokens_per_clip=750,     audio_input_feat_size=128,     num_frames_per_video=32,     num_vision_tokens_per_frame=70,     video_fps=24.0,     **kwargs )`

Gemma4 Causal LM preprocessor.

This preprocessing layer is meant for use with [`keras_hub.models.Gemma4CausalLM`](https://keras.io/keras_hub/api/models/gemma4/gemma4_causal_lm#gemma4causallm-class)
. It can be configured in three modes: text-only, text + image/video, and text + audio, based on whether `image_converter`, `video_converter`, or `audio_converter` are provided. It returns outputs in a `(x, y, sample_weight)` format, where the `y` label is the next token id in the `x` sequence. `sample_weight` is 0 for "prompt" tokens and 1 for "response" tokens, so that the loss is computed only on the "response" tokens.

For image inputs, this layer replaces each `<|image|>` placeholder in the prompt with `num_vision_tokens_per_image` soft tokens wrapped in `<|image>...<image|>` markers. It also returns indices of where these vision tokens are present so that image embeddings can be placed at the correct positions in the sequence.

For video inputs, each `<|video|>` placeholder is replaced with a sequence of per-frame blocks. Each block contains a timestamp and `num_vision_tokens_per_frame` soft tokens wrapped in `<|image>...<image|>` markers. The actual token count per frame is computed dynamically from the input frame dimensions.

For audio inputs, each `<|audio|>` placeholder is expanded to the exact number of audio tokens required for the clip, computed dynamically from the mel-spectrogram length.

By default, per-frame timestamps are computed from sequential indices `[0, 1, ..., N-1]` at `video_fps`. When your video was sampled at irregular intervals (e.g. every 8th frame of a 30 fps source), set `preprocessor.video_metadata` to a list of per-sample dicts before calling the preprocessor. Each dict accepts a `"frames_indices"` key (`list[int]`, the source frame indices that were sampled) and an optional `"fps"` key (`float`, defaults to `preprocessor.video_fps`). When `video_metadata` is `None` (the default) the preprocessor falls back to sequential indices at `video_fps`, so existing code is unaffected.

**Examples**

Using `video_metadata` to pass real frame indices and fps.

Copied!

`# One dict per sample in the batch. preprocessor.video_metadata = [     {"frames_indices": [0, 8, 16, 24], "fps": 30.0}, ] output = preprocessor({     "prompts": ["Describe this video: <|video|>"],     "responses": [""],     "videos": [my_video_frames],  # shape (N_frames, H, W, 3) }) preprocessor.video_metadata = None  # reset to default after use`

For use with generation, the layer also exposes two methods `generate_preprocess()` and `generate_postprocess()`. When this preprocessor is attached to a [`keras_hub.models.Gemma4CausalLM`](https://keras.io/keras_hub/api/models/gemma4/gemma4_causal_lm#gemma4causallm-class)
 instance, these methods will be called implicitly in `generate()`. They can also be called standalone (e.g. to precompute preprocessing inputs for generation in a separate process).

**Arguments**

*   **tokenizer**: A `keras_hub.models.Gemma4Tokenizer` instance.
*   **image\_converter**: A [`keras_hub.layers.Gemma4ImageConverter`](https://keras.io/keras_hub/api/models/gemma4/gemma4_image_converter#gemma4imageconverter-class)
     instance. Defaults to `None`.
*   **audio\_converter**: A [`keras_hub.layers.Gemma4AudioConverter`](https://keras.io/keras_hub/api/models/gemma4/gemma4_audio_converter#gemma4audioconverter-class)
     instance. Defaults to `None`.
*   **video\_converter**: A [`keras_hub.layers.Gemma4VideoConverter`](https://keras.io/keras_hub/api/models/gemma4/gemma4_video_converter#gemma4videoconverter-class)
     instance. Defaults to `None`.
*   **sequence\_length**: int. The length of the packed inputs. Defaults to `1024`.
*   **add\_start\_token**: bool. If `True`, the preprocessor will prepend the tokenizer start token to each input sequence. Defaults to `True`.
*   **add\_end\_token**: bool. If `True`, the preprocessor will append the tokenizer end token to each input sequence. Defaults to `True`.
*   **max\_images\_per\_prompt**: int. Maximum number of images per sample in the batch. Defaults to `2`.
*   **num\_vision\_tokens\_per\_image**: int. Number of vision placeholder tokens per image. Defaults to `280`.
*   **max\_audio\_clips\_per\_prompt**: int. Maximum number of audio clips per sample in the batch. Defaults to `1`.
*   **num\_audio\_tokens\_per\_clip**: int. Legacy parameter, no longer used for token calculation as audio expansion is now fully dynamic. Defaults to `750`.
*   **audio\_input\_feat\_size**: int. Number of mel-spectrogram frequency bins. Defaults to `128`.
*   **num\_frames\_per\_video**: int. Number of frames sampled from each video. Defaults to `32`.
*   **num\_vision\_tokens\_per\_frame**: int. Fallback number of vision placeholder tokens per video frame, used when a video converter is configured but no video input is provided. The actual count is computed dynamically from frame dimensions when videos are present. Defaults to `70`.
*   **video\_fps**: float. Frames-per-second used to compute per-frame timestamps in the expanded prompt. Defaults to `24.0`.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`Gemma4CausalLMPreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )`

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
| [gemma4\_instruct\_2b\_assistant](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_instruct_2b_assistant/1) | 77.73M | Gemma 4 E2B MTP Assistant model: 4-layer speculative-decoding assistant for the 2B-it model. Uses Multi-Token Prediction to propose candidate tokens and achieve inference speedups. This model must NOT be used standalone. It is designed exclusively as a draft model to be passed to the target model's generate() method via the assistant\_model argument. |
| [gemma4\_instruct\_4b\_assistant](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_instruct_4b_assistant/1) | 77.73M | Gemma 4 E4B MTP Assistant model: 4-layer speculative-decoding assistant for the 4B-it model. Uses Multi-Token Prediction to propose candidate tokens and achieve inference speedups. This model must NOT be used standalone. It is designed exclusively as a draft model to be passed to the target model's generate() method via the assistant\_model argument. |
| [gemma4\_instruct\_26b\_a4b\_assistant](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_instruct_26b_a4b_assistant/1) | 412.76M | Gemma 4 26B A4B MTP Assistant model: 4-layer speculative-decoding assistant for the 26B MoE model. Uses Multi-Token Prediction and a standard logit head to propose candidates. This model must NOT be used standalone. It is designed exclusively as a draft model to be passed to the target model's generate() method via the assistant\_model argument. |
| [gemma4\_instruct\_31b\_assistant](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_instruct_31b_assistant/1) | 454.71M | Gemma 4 31B MTP Assistant model: 4-layer speculative-decoding assistant for the 31B dense model. Uses Multi-Token Prediction and a standard logit head to propose candidates. This model must NOT be used standalone. It is designed exclusively as a draft model to be passed to the target model's generate() method via the assistant\_model argument. |
| [gemma4\_2b](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_2b/2) | 5.10B | Gemma 4 E2B base model: 2.3B effective parameters (5.1B total with Per-Layer Embeddings), 35-layer, audio+vision+text pretrained Gemma4 model. The 'E' denotes effective parameters — PLE gives each decoder layer its own token embedding table, maximizing parameter efficiency for on-device deployment. |
| [gemma4\_instruct\_2b](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_instruct_2b/2) | 5.10B | Gemma 4 E2B instruction-tuned model: 2.3B effective parameters (5.1B total with Per-Layer Embeddings), 35-layer, audio+vision+text instruction-tuned Gemma4 model. The 'E' denotes effective parameters — PLE gives each decoder layer its own token embedding table, maximizing parameter efficiency for on-device deployment. |
| [gemma4\_4b](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_4b/2) | 7.90B | Gemma 4 E4B base model: 4.5B effective parameters (7.9B total with Per-Layer Embeddings), 42-layer, audio+vision+text pretrained Gemma4 model. The 'E' denotes effective parameters — PLE gives each decoder layer its own token embedding table, maximizing parameter efficiency for on-device deployment. |
| [gemma4\_instruct\_4b](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_instruct_4b/2) | 7.90B | Gemma 4 E4B instruction-tuned model: 4.5B effective parameters (7.9B total with Per-Layer Embeddings), 42-layer, audio+vision+text instruction-tuned Gemma4 model. The 'E' denotes effective parameters — PLE gives each decoder layer its own token embedding table, maximizing parameter efficiency for on-device deployment. |
| [gemma4\_26b\_a4b](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_26b_a4b/2) | 26.00B | Gemma 4 26B A4B base model: Mixture-of-Experts (MoE) model with 26B total parameters and only 4B active parameters per forward pass, 30-layer, vision+text pretrained Gemma4 model. The 'A' denotes active parameters — by activating only a 4B subset during inference, this MoE model runs nearly as fast as a dense 4B model. |
| [gemma4\_instruct\_26b\_a4b](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_instruct_26b_a4b/2) | 26.00B | Gemma 4 26B A4B instruction-tuned model: Mixture-of-Experts (MoE) model with 26B total parameters and only 4B active parameters per forward pass, 30-layer, vision+text instruction-tuned Gemma4 model. The 'A' denotes active parameters — by activating only a 4B subset during inference, this MoE model runs nearly as fast as a dense 4B model. |
| [gemma4\_31b](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_31b/2) | 31.00B | Gemma 4 31B base model: 31B parameter, 60-layer, dense vision+text pretrained Gemma4 model. The dense model in the Gemma 4 family, offering maximum quality for deployments where inference speed is less of a constraint. |
| [gemma4\_instruct\_31b](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_instruct_31b/2) | 31.00B | Gemma 4 31B instruction-tuned model: 31B parameter, 60-layer, dense vision+text instruction-tuned Gemma4 model. The dense model in the Gemma 4 family, offering maximum quality for deployments where inference speed is less of a constraint. |

* * *

### `tokenizer` property

Copied!

`keras_hub.models.Gemma4CausalLMPreprocessor.tokenizer`

The tokenizer used to tokenize strings.

* * *

[Gemma4CausalLMPreprocessor layer](https://keras.io/keras_hub/api/models/gemma4/gemma4_causal_lm_preprocessor/#gemma4causallmpreprocessor-layer)

[`Gemma4CausalLMPreprocessor` class](https://keras.io/keras_hub/api/models/gemma4/gemma4_causal_lm_preprocessor/#gemma4causallmpreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/gemma4/gemma4_causal_lm_preprocessor/#frompreset-method)

[`tokenizer` property](https://keras.io/keras_hub/api/models/gemma4/gemma4_causal_lm_preprocessor/#tokenizer-property)