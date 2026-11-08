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
 / Gemma3nAudioConverter

Gemma3nAudioConverter
=====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/gemma3n/gemma3n_audio_converter.py#L23)

### `Gemma3nAudioConverter` class

Copied!

`keras_hub.layers.Gemma3nAudioConverter(     feature_size,     sampling_rate,     padding_value,     return_attention_mask,     frame_length_ms,     hop_length_ms,     min_frequency,     max_frequency,     preemphasis,     preemphasis_htk_flavor,     fft_overdrive,     dither,     input_scale_factor,     mel_floor,     per_bin_mean,     per_bin_stddev,     padding_side,     seed=None,     **kwargs )`

Converts raw audio waveforms into log-mel spectrograms.

This layer preprocesses 1D audio signals into 2D log-mel spectrograms suitable for the Gemma3n audio encoder. The conversion process involves padding or truncating the raw audio to a consistent length, applying optional dithering, input scaling, and preemphasis, and then computing the Short-Time Fourier Transform (STFT) with a Hann window. The resulting magnitude spectrogram is converted to the mel scale using a mel filterbank, after which the log-mel spectrogram is calculated by taking the logarithm. Finally, the layer can optionally normalize these features using provided per-bin mean and standard deviation statistics, and it returns both the spectrogram and an attention mask indicating which frames are valid.

**Arguments**

*   **feature\_size**: int. The number of mel bins to generate.
*   **sampling\_rate**: int. The expected sampling rate of the input audio.
*   **padding\_value**: float. The value to use for padding the raw audio.
*   **return\_attention\_mask**: bool. Whether to return an attention mask.
*   **frame\_length\_ms**: float. The length of each STFT frame in milliseconds.
*   **hop\_length\_ms**: float. The step size between STFT frames in milliseconds.
*   **min\_frequency**: float. The lowest frequency for the mel filterbank.
*   **max\_frequency**: float. The highest frequency for the mel filterbank.
*   **preemphasis**: float. The coefficient for the preemphasis filter. Set to 0.0 to disable.
*   **preemphasis\_htk\_flavor**: bool. Whether to use the HTK-style preemphasis.
*   **fft\_overdrive**: bool. If True, doubles the FFT length.
*   **dither**: float. Amount of dithering to add to the waveform. Set to 0.0 to disable.
*   **input\_scale\_factor**: float. Factor to scale the input waveform by.
*   **mel\_floor**: float. A minimum value (floor) to apply before taking the logarithm.
*   **per\_bin\_mean**: list or None. A list of mean values for each mel bin, used for normalization.
*   **per\_bin\_stddev**: list or None. A list of standard deviation values for each mel bin, used for normalization.
*   **padding\_side**: str. Which side to pad the audio on ('right' or 'left').
*   **seed**: int or None. A base seed for the dither random number generator. It is not used as the generator seed directly: each record's seed is derived by combining this value with a hash of that record's unpadded samples, so dithering is deterministic per record and independent of how records are batched. Only used when `dither > 0.0`. If `None`, a base seed is drawn at random.

**Call arguments**

*   **raw\_speech**: A raw audio waveform tensor, list of waveforms, or numpy array. Can be unbatched (1D) or batched (list of 1D arrays).
*   **padding**: str or bool. Padding strategy for batches. Options are `"longest"` (pad to longest sequence in batch), `True` (same as "longest"), or `False` (no padding). Defaults to `"longest"`.
*   **max\_length**: int. Maximum length to truncate or pad to. Defaults to 480000.
*   **truncation**: bool. Whether to truncate sequences longer than `max_length`. Defaults to `True`.
*   **pad\_to\_multiple\_of**: int or None. If set, pad the sequence length to a multiple of this value. Defaults to 128.
*   **return\_attention\_mask**: bool. Whether to return an attention mask indicating valid (non-padded) frames. Defaults to `True`.

**Examples**

Copied!

`import numpy as np  # Create a simple audio signal (1 second of 440 Hz sine wave). audio = np.sin(     2 * np.pi * 440 * np.linspace(0, 1, 16000, dtype=np.float32) )  # Initialize the audio converter converter = keras_hub.layers.Gemma3nAudioConverter(     feature_size=128,     sampling_rate=16000,     padding_value=0.0,     return_attention_mask=True,     frame_length_ms=32.0,     hop_length_ms=10.0,     min_frequency=125.0,     max_frequency=7600.0,     preemphasis=0.97,     preemphasis_htk_flavor=True,     fft_overdrive=True,     dither=0.0,     input_scale_factor=1.0,     mel_floor=1e-5,     per_bin_mean=None,     per_bin_stddev=None,     padding_side="right", )  # Convert audio to log-mel spectrogram. features, mask = converter(audio) print(features.shape)  # (num_frames, 128) print(mask.shape)      # (num_frames,)  # Convert a batch of audio with padding. audio_1 = np.sin(     2 * np.pi * 440 * np.linspace(0, 1, 16000, dtype=np.float32) ) audio_2 = np.sin(     2 * np.pi * 880 * np.linspace(0, 0.5, 8000, dtype=np.float32) ) features, mask = converter(     [audio_1, audio_2],     padding="longest",     pad_to_multiple_of=128, ) print(features.shape)  # (2, num_frames, 128)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/layers/preprocessing/audio_converter.py#L47)

### `from_preset` method

Copied!

`Gemma3nAudioConverter.from_preset(preset, **kwargs)`

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
| [gemma3n\_e2b](https://www.kaggle.com/models/keras/gemma-3n/keras/gemma3n_e2b/1) | 5.44B | Gemma 3n E2B multimodal model (~5B total, ~2B effective parameters) supporting multimodal inputs and optimized for on-device deployment. |
| [gemma3n\_e2b\_it](https://www.kaggle.com/models/keras/gemma-3n/keras/gemma3n_e2b_it/1) | 5.44B | Instruction-tuned Gemma 3n E2B multimodal model (~5B total, ~2B effective parameters) supporting multimodal inputs and optimized for on-device deployment. |
| [gemma3n\_e4b](https://www.kaggle.com/models/keras/gemma-3n/keras/gemma3n_e4b/1) | 7.85B | Gemma 3n E4B multimodal with ( ~8B total ~4B effective parameters ), supporting multimodal inputs and optimized for on-device deployment. |
| [gemma3n\_e4b\_it](https://www.kaggle.com/models/keras/gemma-3n/keras/gemma3n_e4b_it/1) | 7.85B | Instruction-tuned Gemma 3n E4B multimodal with ~8B total (~4B effective parameters ), supporting multimodal inputs and optimized for on-device deployment. |

* * *

[Gemma3nAudioConverter](https://keras.io/keras_hub/api/models/gemma3n/gemma3n_audio_converter/#gemma3naudioconverter)

[`Gemma3nAudioConverter` class](https://keras.io/keras_hub/api/models/gemma3n/gemma3n_audio_converter/#gemma3naudioconverter-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/gemma3n/gemma3n_audio_converter/#frompreset-method)