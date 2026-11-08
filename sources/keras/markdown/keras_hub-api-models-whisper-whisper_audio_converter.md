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
 / [Whisper](https://keras.io/keras_hub/api/models/whisper/)
 / WhisperAudioConverter

WhisperAudioConverter
=====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/whisper/whisper_audio_converter.py#L16)

### `WhisperAudioConverter` class

Copied!

`keras_hub.layers.WhisperAudioConverter(     num_mels=80,     num_fft_bins=400,     stride=160,     sampling_rate=16000,     max_audio_length=30,     **kwargs )`

Whisper audio converter layer.

This layer takes in a batch of audio tensors, and computes the log-mel spectrogram features for each audio tensor.

The input audio tensor can either be of shape `(length_of_audio,)` or `(batch_size, length_of_audio)`. The output is a tensor of shape `(batch_size, num_frames, num_mels)`, where `num_frames` is `(max_audio_length * sampling_rate) / stride`.

**Arguments**

*   **num\_mels**: int. The number of mel-frequency filters. Defaults to `80`.
*   **num\_fft\_bins**: int. The size of the Fourier Transform in STFT. Defaults to `400`.
*   **stride**: int. The distance between neighboring sliding window frames while computing STFT. Defaults to `160`.
*   **sampling\_rate**: int. The sample rate of the audio. Defaults to `16000`.
*   **max\_audio\_length**: int. The length of each audio chunk in seconds. The input audio tensor will be padded/trimmed to `max_audio_length * sampling_rate`. Defaults to `30`.

**Examples**

Copied!

`audio_tensor = tf.ones((8000,), dtype="float32")  # Compute the log-mel spectrogram. audio_converter = keras_hub.layers.WhisperAudioConverter.from_preset(     "whisper_base_en", ) audio_converter(audio_tensor)  # Compute the log-mel spectrogram for a batch of audio tensors. audio_tensor_1 = tf.ones((8000,), dtype="float32") audio_tensor_2 = tf.ones((10000,), dtype="float32") audio_tensor = tf.ragged.stack([audio_tensor_1, audio_tensor_2], axis=0) audio_converter(audio_tensor)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/layers/preprocessing/audio_converter.py#L47)

### `from_preset` method

Copied!

`WhisperAudioConverter.from_preset(preset, **kwargs)`

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
| [whisper\_tiny\_en](https://www.kaggle.com/models/keras/whisper/keras/whisper_tiny_en/4) | 37.18M | 4-layer Whisper model. Trained on 438,000 hours of labelled English speech data. |
| [whisper\_tiny\_multi](https://www.kaggle.com/models/keras/whisper/keras/whisper_tiny_multi/4) | 37.76M | 4-layer Whisper model. Trained on 680,000 hours of labelled multilingual speech data. |
| [whisper\_base\_multi](https://www.kaggle.com/models/keras/whisper/keras/whisper_base_multi/4) | 72.59M | 6-layer Whisper model. Trained on 680,000 hours of labelled multilingual speech data. |
| [whisper\_base\_en](https://www.kaggle.com/models/keras/whisper/keras/whisper_base_en/4) | 124.44M | 6-layer Whisper model. Trained on 438,000 hours of labelled English speech data. |
| [whisper\_small\_en](https://www.kaggle.com/models/keras/whisper/keras/whisper_small_en/4) | 241.73M | 12-layer Whisper model. Trained on 438,000 hours of labelled English speech data. |
| [whisper\_small\_multi](https://www.kaggle.com/models/keras/whisper/keras/whisper_small_multi/4) | 241.73M | 12-layer Whisper model. Trained on 680,000 hours of labelled multilingual speech data. |
| [whisper\_medium\_en](https://www.kaggle.com/models/keras/whisper/keras/whisper_medium_en/4) | 763.86M | 24-layer Whisper model. Trained on 438,000 hours of labelled English speech data. |
| [whisper\_medium\_multi](https://www.kaggle.com/models/keras/whisper/keras/whisper_medium_multi/4) | 763.86M | 24-layer Whisper model. Trained on 680,000 hours of labelled multilingual speech data. |
| [whisper\_large\_multi](https://www.kaggle.com/models/keras/whisper/keras/whisper_large_multi/4) | 1.54B | 32-layer Whisper model. Trained on 680,000 hours of labelled multilingual speech data. |
| [whisper\_large\_multi\_v2](https://www.kaggle.com/models/keras/whisper/keras/whisper_large_multi_v2/4) | 1.54B | 32-layer Whisper model. Trained for 2.5 epochs on 680,000 hours of labelled multilingual speech data. An improved of `whisper_large_multi`. |

* * *

[WhisperAudioConverter](https://keras.io/keras_hub/api/models/whisper/whisper_audio_converter/#whisperaudioconverter)

[`WhisperAudioConverter` class](https://keras.io/keras_hub/api/models/whisper/whisper_audio_converter/#whisperaudioconverter-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/whisper/whisper_audio_converter/#frompreset-method)