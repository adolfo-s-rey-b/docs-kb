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
 / EmbeddingGemma2AudioConverter

EmbeddingGemma2AudioConverter
=============================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/embedding_gemma2/embedding_gemma2_audio_converter.py#L10)

### `EmbeddingGemma2AudioConverter` class

Copied!

`keras_hub.layers.EmbeddingGemma2AudioConverter(     num_mels=128,     num_fft_bins=512,     stride=160,     sampling_rate=16000,     max_audio_length=30,     min_frequency=0.0,     max_frequency=8000.0,     mel_floor=1e-05,     per_bin_mean=None,     per_bin_stddev=None,     frame_length=320,     **kwargs )`

EmbeddingGemma2 audio converter.

This converter is a subclass of `Gemma4AudioConverter` and shares the same functionality.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/layers/preprocessing/audio_converter.py#L47)

### `from_preset` method

Copied!

`EmbeddingGemma2AudioConverter.from_preset(preset, **kwargs)`

Instantiate a [`keras_hub.layers.AudioConverter`](https://keras.io/keras_hub/api/preprocessing_layers/audio_converter#audioconverter-class)
 from a model preset.

A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as one of:

1.  a built-in preset identifier like `'whisper_base_en'`
2.  a Kaggle Models handle like `'kaggle://user/whisper/keras/whisper_base_en'`
3.  a Hugging Face handle like `'hf://user/whisper_base_en'`
4.  a path to a local preset directory like `'./whisper_base_en'`

You can run `cls.presets.keys()` to list all built-in presets available on the class.

This constructor can be called in one of two ways. Either from the base class like `keras_hub.models.AudioConverter.from_preset()`, or from a model class like `keras_hub.models.WhisperAudioConverter.from_preset()`. If calling from the base class, the subclass of the returning object will be inferred from the config in the preset directory.

**Arguments**

*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.
*   **load\_weights**: bool. If `True`, the weights will be loaded into the model architecture. If `False`, the weights will be randomly initialized.

**Examples**

Copied!

`# Load an audio converter from a preset. converter = keras_hub.layers.AudioConverter.from_preset(     "whisper_base_en" ) # Convert some raw mono channel audio input. converter(np.ones(2, 1_000))`

| Preset | Parameters | Description |
| --- | --- | --- |
| [embedding\_gemma2](https://www.kaggle.com/models/keras/embedding-gemma2/keras/embedding_gemma2/1) | 744.37M | EmbeddingGemma 2: 744M-parameter, 24-layer multimodal embedding model built on Gemma 4. Embeds text, images, video and audio into a 768-dimensional space. |

* * *

[EmbeddingGemma2AudioConverter](https://keras.io/keras_hub/api/models/embedding_gemma2/embedding_gemma2_audio_converter/#embeddinggemma2audioconverter)

[`EmbeddingGemma2AudioConverter` class](https://keras.io/keras_hub/api/models/embedding_gemma2/embedding_gemma2_audio_converter/#embeddinggemma2audioconverter-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/embedding_gemma2/embedding_gemma2_audio_converter/#frompreset-method)