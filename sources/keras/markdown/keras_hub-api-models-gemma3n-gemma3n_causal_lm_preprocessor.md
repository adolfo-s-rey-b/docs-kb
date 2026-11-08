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
 / [Gemma3n](https://keras.io/keras_hub/api/models/gemma3n/)
 / Gemma3nCausalLMPreprocessor layer

Gemma3nCausalLMPreprocessor layer
=================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/gemma3n/gemma3n_causal_lm_preprocessor.py#L27)

### `Gemma3nCausalLMPreprocessor` class

Copied!

`keras_hub.models.Gemma3nCausalLMPreprocessor(     tokenizer,     image_converter=None,     audio_converter=None,     sequence_length=1024,     add_start_token=True,     add_end_token=True,     max_images_per_prompt=2,     num_vision_tokens_per_image=256,     max_audios_per_prompt=2,     num_audio_tokens_per_audio=188,     **kwargs )`

Gemma3n Causal LM preprocessor.

This preprocessing layer is meant for use with [`keras_hub.models.Gemma3nCausalLM`](https://keras.io/keras_hub/api/models/gemma3n/gemma3n_causal_lm#gemma3ncausallm-class)
. It can be configured in three ways: text-only, text + vision, and text + vision + audio, based on whether the passed values of `image_converter` and `audio_converter` are None. For text-only, it takes in batches of strings. For text + vision, it takes in batches of images and strings. For text + vision + audio, it takes in batches of images, audio, and strings. It returns outputs in a `(x, y, sample_weight)` format, where the `y` label is the next token id in the `x` sequence. `sample_weight` is 0 for "prompt" tokens, and 1 for "response" tokens, so that the loss is computed only on the "response" tokens.

For the text + vision case, this layer replaces instances of `<start_of_image>` token in the prompt with `num_vision_tokens_per_image` placeholder tokens. It also returns indices of where these vision tokens are present so that in the model, image embeddings can be placed in the right position in the sequence of text embeddings.

For the text + audio case, this layer replaces instances of `<start_of_audio>` token in the prompt with `num_audio_tokens_per_audio` placeholder tokens. It also returns indices of where these audio tokens are present so that in the model, audio embeddings can be placed in the right position in the sequence of text embeddings.

Note that if `max_images_per_prompt` is 2, you can pass either 0, 1, 2 images per sample. The value 0 corresponds to text-only input. Similarly, if `max_audios_per_prompt` is 2, you can pass either 0, 1, 2 audio clips per sample.

For use with generation, the layer also exposes two methods `generate_preprocess()` and `generate_postprocess()`. When this preprocessor is attached to a [`keras_hub.models.Gemma3nCausalLM`](https://keras.io/keras_hub/api/models/gemma3n/gemma3n_causal_lm#gemma3ncausallm-class)
 instance, these methods will be called implicitly in `generate()`. They can also be called standalone (e.g. to precompute preprocessing inputs for generation in a separate process).

**Arguments**

*   **tokenizer**: A `keras_hub.models.Gemma3nTokenizer` instance.
*   **image\_converter**: A [`keras_hub.layers.ImageConverter`](https://keras.io/keras_hub/api/preprocessing_layers/image_converter#imageconverter-class)
     instance. Defaults to `None`.
*   **audio\_converter**: A [`keras_hub.layers.AudioConverter`](https://keras.io/keras_hub/api/preprocessing_layers/audio_converter#audioconverter-class)
     instance. Defaults to `None`.
*   **sequence\_length**: The length of the packed inputs. Defaults to 1024.
*   **add\_start\_token**: If `True`, the preprocessor will prepend the tokenizer start token to each input sequence. Defaults to `True`.
*   **add\_end\_token**: If `True`, the preprocessor will append the tokenizer end token to each input sequence. Defaults to `True`.
*   **max\_images\_per\_prompt**: int. Permissible number of images per sample in the batch. Defaults to 2.
*   **num\_vision\_tokens\_per\_image**: int. Number of vision placeholder tokens per image. Defaults to 256.
*   **max\_audios\_per\_prompt**: int. Permissible number of audio clips per sample in the batch. Defaults to 2.
*   **num\_audio\_tokens\_per\_audio**: int. Number of audio placeholder tokens per audio clip. Defaults to 188.

**Call arguments**

*   **x**: A string, [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
     or list of python strings.
*   **y**: Label data. Should always be `None` as the layer generates labels.
*   **sample\_weight**: Label weights. Should always be `None` as the layer generates label weights.
*   **sequence\_length**: Pass to override the configured `sequence_length` of the layer.

**Examples**

Copied!

``# === Language === # Load the preprocessor from a preset. preprocessor = keras_hub.models.Gemma3nCausalLMPreprocessor.from_preset(     "gemma3n_2b_it" )  # Unbatched inputs. preprocessor(     {         "prompts": "What is the capital of India?",         "responses": "New Delhi",     } )  # Batched inputs. preprocessor(     {         "prompts": [             "What is the capital of India?",             "What is the capital of Spain?"         ],         "responses": ["New Delhi", "Madrid"],     } )  # Apply preprocessing to a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset). features = {     "prompts": [         "What is the capital of India?",         "What is the capital of Spain?"     ],     "responses": ["New Delhi", "Madrid"], }  ds = tf.data.Dataset.from_tensor_slices(features) ds = ds.map(preprocessor, num_parallel_calls=tf.data.AUTOTUNE)  # Prepare tokens for generation (no end token). preprocessor.generate_preprocess(["The quick brown fox jumped."])  # Map generation outputs back to strings. preprocessor.generate_postprocess({     'token_ids': np.array([[2, 818, 3823, 8864, 37423, 32694, 236761, 0]]),     'padding_mask': np.array([[ 1, 1, 1, 1, 1, 1, 1, 0]]), })  # === Vision and Language === # Load the preprocessor from a preset. preprocessor = keras_hub.models.Gemma3nCausalLMPreprocessor.from_preset(     "gemma3n_2b_it" )  # Text-only inputs (unbatched). preprocessor(     {         "prompts": "What is the capital of India?",         "responses": "New Delhi",     } )  # Text-only inputs (batched). preprocessor(     {         "prompts": [             "What is the capital of India?",             "What is the capital of Spain?"         ],         "responses": ["New Delhi", "Madrid"],     } )  # Unbatched inputs, with one image. preprocessor(     {         "prompts": "this is a lily <start_of_image>",         "responses": "pristine!",         "images": np.ones((768, 768, 3), dtype="float32")     } )  # Unbatched inputs, with two images. preprocessor(     {         "prompts": "lily: <start_of_image>, sunflower: <start_of_image>",         "responses": "pristine!",         "images": [             np.ones((768, 768, 3), dtype="float32"),             np.ones((768, 768, 3), dtype="float32")         ],     } )  # Batched inputs, one image per prompt. preprocessor(     {         "prompts": [             "this is a lily: <start_of_image>",             "this is a sunflower: <start_of_image>"         ],         "responses": ["pristine!", "radiant!"],         "images": [             np.ones((768, 768, 3), dtype="float32"),             np.ones((768, 768, 3), dtype="float32")         ]     } )  # === Audio and Language === # Unbatched inputs, with one audio clip. preprocessor(     {         "prompts": "transcribe this: <start_of_audio>",         "responses": "hello world",         "audios": np.ones((16000,), dtype="float32")     } )  # === Vision, Audio and Language === # Unbatched inputs, with one image and one audio. preprocessor(     {         "prompts": "image: <start_of_image>, audio: <start_of_audio>",         "responses": "multimodal!",         "images": np.ones((768, 768, 3), dtype="float32"),         "audios": np.ones((16000,), dtype="float32")     } )``

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`Gemma3nCausalLMPreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )`

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
| [gemma3n\_e2b](https://www.kaggle.com/models/keras/gemma-3n/keras/gemma3n_e2b/1) | 5.44B | Gemma 3n E2B multimodal model (~5B total, ~2B effective parameters) supporting multimodal inputs and optimized for on-device deployment. |
| [gemma3n\_e2b\_it](https://www.kaggle.com/models/keras/gemma-3n/keras/gemma3n_e2b_it/1) | 5.44B | Instruction-tuned Gemma 3n E2B multimodal model (~5B total, ~2B effective parameters) supporting multimodal inputs and optimized for on-device deployment. |
| [gemma3n\_e4b](https://www.kaggle.com/models/keras/gemma-3n/keras/gemma3n_e4b/1) | 7.85B | Gemma 3n E4B multimodal with ( ~8B total ~4B effective parameters ), supporting multimodal inputs and optimized for on-device deployment. |
| [gemma3n\_e4b\_it](https://www.kaggle.com/models/keras/gemma-3n/keras/gemma3n_e4b_it/1) | 7.85B | Instruction-tuned Gemma 3n E4B multimodal with ~8B total (~4B effective parameters ), supporting multimodal inputs and optimized for on-device deployment. |

* * *

### `tokenizer` property

Copied!

`keras_hub.models.Gemma3nCausalLMPreprocessor.tokenizer`

The tokenizer used to tokenize strings.

* * *

[Gemma3nCausalLMPreprocessor layer](https://keras.io/keras_hub/api/models/gemma3n/gemma3n_causal_lm_preprocessor/#gemma3ncausallmpreprocessor-layer)

[`Gemma3nCausalLMPreprocessor` class](https://keras.io/keras_hub/api/models/gemma3n/gemma3n_causal_lm_preprocessor/#gemma3ncausallmpreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/gemma3n/gemma3n_causal_lm_preprocessor/#frompreset-method)

[`tokenizer` property](https://keras.io/keras_hub/api/models/gemma3n/gemma3n_causal_lm_preprocessor/#tokenizer-property)