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
 / Gemma4VideoConverter

Gemma4VideoConverter
====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/gemma4/gemma4_video_converter.py#L10)

### `Gemma4VideoConverter` class

Copied!

`keras_hub.layers.Gemma4VideoConverter(     patch_size=16, max_soft_tokens=70, pooling_kernel_size=3, num_frames=32, **kwargs )`

Video converter for Gemma4.

This layer handles video inputs by sampling frames and delegating to `Gemma4ImageConverter` for frame-level processing.

**Arguments**

*   **patch\_size**: int. Size of each square patch in pixels. Defaults to `16`.
*   **max\_soft\_tokens**: int. Maximum number of pooled soft tokens per video frame. Defaults to `70`.
*   **pooling\_kernel\_size**: int. Spatial pooling kernel size applied after the vision encoder. Defaults to `3`.
*   **num\_frames**: int. Number of frames to uniformly sample from the video. Defaults to `32`.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/layers/preprocessing/video_converter.py#L35)

### `from_preset` method

Copied!

`Gemma4VideoConverter.from_preset(preset, **kwargs)`

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

[Gemma4VideoConverter](https://keras.io/keras_hub/api/models/gemma4/gemma4_video_converter/#gemma4videoconverter)

[`Gemma4VideoConverter` class](https://keras.io/keras_hub/api/models/gemma4/gemma4_video_converter/#gemma4videoconverter-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/gemma4/gemma4_video_converter/#frompreset-method)