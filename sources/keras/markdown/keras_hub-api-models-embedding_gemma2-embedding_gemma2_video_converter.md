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
 / EmbeddingGemma2VideoConverter

EmbeddingGemma2VideoConverter
=============================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/embedding_gemma2/embedding_gemma2_video_converter.py#L15)

### `EmbeddingGemma2VideoConverter` class

Copied!

`keras_hub.layers.EmbeddingGemma2VideoConverter(     patch_size=16, max_soft_tokens=70, pooling_kernel_size=3, max_frames=32, **kwargs )`

Video converter for EmbeddingGemma2.

This layer handles video inputs by sampling frames and delegating to `EmbeddingGemma2ImageConverter` for frame-level processing.

Unlike `Gemma4VideoConverter` which always samples exactly `num_frames`, this converter keeps all frames up to `max_frames`. If the video exceeds `max_frames`, it uniformly samples `max_frames` frames.

This converter does not sample by frame rate. The Hugging Face processor first samples one frame per second when the video has `fps` metadata. To get the same frames, decode the video at 1 frame per second before calling this layer.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/layers/preprocessing/video_converter.py#L35)

### `from_preset` method

Copied!

`EmbeddingGemma2VideoConverter.from_preset(preset, **kwargs)`

Instantiate a `keras_hub.layers.VideoConverter` from a model preset.

A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as one of:

1.  a built-in preset identifier like `'gemma4_2b_it'`
2.  a Kaggle Models handle like `'kaggle://user/gemma4/keras/gemma4_2b_it'`
3.  a Hugging Face handle like `'hf://google/gemma-4-2b-it'`
4.  a path to a local preset directory like `'./gemma4_2b_it'`

You can run `cls.presets.keys()` to list all built-in presets available on the class.

This constructor can be called in one of two ways. Either from the base class like `keras_hub.models.VideoConverter.from_preset()`, or from a model class like `keras_hub.models.Gemma4VideoConverter.from_preset()`. If calling from the base class, the subclass of the returning object will be inferred from the config in the preset directory.

**Arguments**

*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.

**Examples**

Copied!

`# Load a video converter from a preset. converter = keras_hub.layers.VideoConverter.from_preset(     "hf://google/gemma-4-2b-it" )`

| Preset | Parameters | Description |
| --- | --- | --- |
| [embedding\_gemma2](https://www.kaggle.com/models/keras/embedding-gemma2/keras/embedding_gemma2/1) | 744.37M | EmbeddingGemma 2: 744M-parameter, 24-layer multimodal embedding model built on Gemma 4. Embeds text, images, video and audio into a 768-dimensional space. |

* * *

[EmbeddingGemma2VideoConverter](https://keras.io/keras_hub/api/models/embedding_gemma2/embedding_gemma2_video_converter/#embeddinggemma2videoconverter)

[`EmbeddingGemma2VideoConverter` class](https://keras.io/keras_hub/api/models/embedding_gemma2/embedding_gemma2_video_converter/#embeddinggemma2videoconverter-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/embedding_gemma2/embedding_gemma2_video_converter/#frompreset-method)