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
 / [Moonshine](https://keras.io/keras_hub/api/models/moonshine/)
 / MoonshineAudioConverter

MoonshineAudioConverter
=======================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/moonshine/moonshine_audio_converter.py#L16)

### `MoonshineAudioConverter` class

Copied!

`keras_hub.layers.MoonshineAudioConverter(     sampling_rate=16000, padding_value=0.0, do_normalize=False, **kwargs )`

Moonshine audio preprocessing layer.

This layer processes raw audio waveforms for the Moonshine ASR model. Audio is formatted as a batched tensor at a 16kHz sample rate and validated for length (0.1 to 64 seconds). The layer handles padding and optional normalization. It does not contain trainable weights.

**Arguments**

*   **sampling\_rate**: int, optional. The audio sampling rate in Hz. Defaults to 16,000.
*   **padding\_value**: float, optional. The value for padding. Defaults to 0.0.
*   **do\_normalize**: bool, optional. Whether to normalize inputs. Defaults to False.
*   **\*\*kwargs**: Additional keyword arguments passed to the base AudioConverter class for customizing the underlying preprocessing behavior.

**Call arguments**

*   **\- `inputs`**: The raw audio data to be processed. It should be a tensor of shape `(batch_size, time_steps, 1)` for mono audio. If the input has shape `(batch_size, time_steps)`, the layer will add the channel dimension.
*   **\- `sampling_rate`**: The sampling rate of the audio in Hz. If provided, it must match the expected sampling rate set during initialization (default is 16,000 Hz). If not provided, the expected sampling rate is taken from the initialization arguments.
*   **\- `padding`**: The padding strategy to apply. If provided, can be one of:
    *   `"longest"`: If `pad_to_multiple_of` is set, pads the audio to make the time\_steps dimension a multiple of `pad_to_multiple_of`.
    *   `"max_length"`: Pads or truncates the audio to `max_length` time steps. If `pad_to_multiple_of` is set, the target length will be the smallest multiple of `pad_to_multiple_of` that is greater than or equal to `max_length`.
    *   If not specified or `None`, no padding is applied.
*   **\- `max_length`**: The target number of time steps when `padding` is `"max_length"`. If not provided and `padding` is `"max_length"`, no padding or truncation is applied.
*   **\- `pad_to_multiple_of`**: If set, the padded time\_steps will be a multiple of this value for the chosen padding strategy.

**Examples**

Copied!

`import keras from keras_hub.layers import MoonshineAudioConverter  # Create a dummy audio input (1 second at 16kHz). dummy_audio = keras.ops.convert_to_tensor(     [[0.1] * 16000],     dtype="float32" ) dummy_audio = keras.ops.expand_dims(dummy_audio, axis=-1)  # Initialize the preprocessor. preprocessor = MoonshineAudioConverter(do_normalize=True)  # Process the audio. processed_audio = preprocessor(dummy_audio)  # Output shape. print(processed_audio.shape) # Expected: (1, 16000, 1) or padded length`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/layers/preprocessing/audio_converter.py#L47)

### `from_preset` method

Copied!

`MoonshineAudioConverter.from_preset(preset, **kwargs)`

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
| [moonshine\_tiny\_en](https://www.kaggle.com/models/keras/moonshine/Keras/moonshine_tiny_en/1) | 27.09M | Moonshine tiny model for English speech recognition. Developed by Useful Sensors for real-time transcription. |
| [moonshine\_base\_en](https://www.kaggle.com/models/keras/moonshine/Keras/moonshine_base_en/1) | 61.51M | Moonshine base model for English speech recognition. Developed by Useful Sensors for real-time transcription. |

* * *

[MoonshineAudioConverter](https://keras.io/keras_hub/api/models/moonshine/moonshine_audio_converter/#moonshineaudioconverter)

[`MoonshineAudioConverter` class](https://keras.io/keras_hub/api/models/moonshine/moonshine_audio_converter/#moonshineaudioconverter-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/moonshine/moonshine_audio_converter/#frompreset-method)