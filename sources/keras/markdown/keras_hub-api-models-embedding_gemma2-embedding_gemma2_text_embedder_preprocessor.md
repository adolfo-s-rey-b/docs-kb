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
 / [EmbeddingGemma2](https://keras.io/keras_hub/api/models/embedding_gemma2/)
 / EmbeddingGemma2TextEmbedderPreprocessor layer

EmbeddingGemma2TextEmbedderPreprocessor layer
=============================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/embedding_gemma2/embedding_gemma2_text_embedder_preprocessor.py#L37)

### `EmbeddingGemma2TextEmbedderPreprocessor` class

Copied!

`keras_hub.models.EmbeddingGemma2TextEmbedderPreprocessor(     tokenizer,     image_converter=None,     audio_converter=None,     video_converter=None,     sequence_length=512,     truncate="round_robin",     **kwargs )`

EmbeddingGemma2 text embedder preprocessor.

Turns raw text, images, videos and audio into the inputs of [`keras_hub.models.EmbeddingGemma2Backbone`](https://keras.io/keras_hub/api/models/embedding_gemma2/embedding_gemma2_backbone#embeddinggemma2backbone-class)
. Text is tokenized and packed to `sequence_length`; each image, video or audio clip is converted by the matching converter and its placeholder token in the text is expanded to the right number of soft tokens, with the positions of those tokens returned as `vision_indices` / `audio_indices`.

Inputs are a `dict` with any of the keys `"texts"`, `"images"`, `"videos"`, `"audio"`, or a bare string / list of strings. A modality given without text gets a prompt made of its placeholder alone. Unbatched inputs (a single string, a rank-3 image, a rank-4 video, a rank-1 waveform) return unbatched outputs.

Two limits apply: one image per prompt (a rank-3 image, or a rank-4 batch with one image per example), and `"images"` and `"videos"` cannot be combined in a single call — pass them in separate calls. Both raise a `ValueError`.

Python lists and NumPy arrays run through a pure-Python path that does not need TensorFlow; inside [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)
 the TensorFlow path is used.

**Arguments**

*   **tokenizer**: An `EmbeddingGemma2Tokenizer` instance.
*   **image\_converter**: An `EmbeddingGemma2ImageConverter`, or `None` to disable image inputs.
*   **audio\_converter**: An `EmbeddingGemma2AudioConverter`, or `None` to disable audio inputs.
*   **video\_converter**: An `EmbeddingGemma2VideoConverter`, or `None` to disable video inputs.
*   **sequence\_length**: int. Length every packed sequence is padded or truncated to. Image, video and audio soft tokens count against it (up to `max_soft_tokens` per image or video frame, and up to 750 per 30 s audio clip), and a `ValueError` is raised when packing would truncate any of them. Defaults to `512`.
*   **truncate**: string. The truncation algorithm of [`keras_hub.layers.MultiSegmentPacker`](https://keras.io/keras_hub/api/preprocessing_layers/multi_segment_packer#multisegmentpacker-class)
    . Defaults to `"round_robin"`.

**Examples**

Copied!

`preprocessor = (     keras_hub.models.EmbeddingGemma2TextEmbedderPreprocessor.from_preset(         "embedding_gemma2"     ) ) preprocessor("What is the capital of France?") preprocessor({"texts": ["<|image|> describe this"], "images": [image]})`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`EmbeddingGemma2TextEmbedderPreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )`

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
| [embedding\_gemma2](https://www.kaggle.com/models/keras/embedding-gemma2/keras/embedding_gemma2/1) | 744.37M | EmbeddingGemma 2: 744M-parameter, 24-layer multimodal embedding model built on Gemma 4. Embeds text, images, video and audio into a 768-dimensional space. |

* * *

### `tokenizer` property

Copied!

`keras_hub.models.EmbeddingGemma2TextEmbedderPreprocessor.tokenizer`

The tokenizer used to tokenize strings.

* * *

### `image_converter` property

Copied!

`keras_hub.models.EmbeddingGemma2TextEmbedderPreprocessor.image_converter`

The image converter used to preprocess image data.

* * *

### `audio_converter` property

Copied!

`keras_hub.models.EmbeddingGemma2TextEmbedderPreprocessor.audio_converter`

The audio converter used to preprocess audio data.

* * *

### `video_converter` property

Copied!

`keras_hub.models.EmbeddingGemma2TextEmbedderPreprocessor.video_converter`

The video converter used to preprocess video data.

* * *

[EmbeddingGemma2TextEmbedderPreprocessor layer](https://keras.io/keras_hub/api/models/embedding_gemma2/embedding_gemma2_text_embedder_preprocessor/#embeddinggemma2textembedderpreprocessor-layer)

[`EmbeddingGemma2TextEmbedderPreprocessor` class](https://keras.io/keras_hub/api/models/embedding_gemma2/embedding_gemma2_text_embedder_preprocessor/#embeddinggemma2textembedderpreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/embedding_gemma2/embedding_gemma2_text_embedder_preprocessor/#frompreset-method)

[`tokenizer` property](https://keras.io/keras_hub/api/models/embedding_gemma2/embedding_gemma2_text_embedder_preprocessor/#tokenizer-property)

[`image_converter` property](https://keras.io/keras_hub/api/models/embedding_gemma2/embedding_gemma2_text_embedder_preprocessor/#imageconverter-property)

[`audio_converter` property](https://keras.io/keras_hub/api/models/embedding_gemma2/embedding_gemma2_text_embedder_preprocessor/#audioconverter-property)

[`video_converter` property](https://keras.io/keras_hub/api/models/embedding_gemma2/embedding_gemma2_text_embedder_preprocessor/#videoconverter-property)