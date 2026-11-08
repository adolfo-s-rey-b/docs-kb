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
 / Gemma4AudioConverter

Gemma4AudioConverter
====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/gemma4/gemma4_audio_converter.py#L15)

### `Gemma4AudioConverter` class

Copied!

`keras_hub.layers.Gemma4AudioConverter(     num_mels=128,     num_fft_bins=512,     stride=160,     sampling_rate=16000,     max_audio_length=30,     min_frequency=0.0,     max_frequency=8000.0,     mel_floor=1e-05,     per_bin_mean=None,     per_bin_stddev=None,     frame_length=320,     **kwargs )`

Gemma4 audio feature extraction layer.

Converts raw audio waveforms into log-mel spectrogram features for the Gemma4 USM audio encoder. The processing pipeline is:

1.  Pad or trim the waveform to a fixed length of `max_audio_length * sampling_rate` samples.
2.  Compute a short-time Fourier transform using a Hann window with `center=True` to produce a power spectrogram.
3.  Apply an HTK-scale mel filterbank with Slaney normalisation.
4.  Apply log compression with a configurable floor value.
5.  Optionally subtract per-bin mean and divide by per-bin standard deviation.

**Arguments**

*   **num\_mels**: int. Number of mel filterbank channels. Defaults to `128`.
*   **num\_fft\_bins**: int. FFT window length in samples, also used as the STFT sequence length. Defaults to `400`.
*   **stride**: int. STFT hop length in samples. Defaults to `160`.
*   **sampling\_rate**: int. Expected sample rate of the input waveform in Hz. Defaults to `16000`.
*   **max\_audio\_length**: int. Maximum audio clip length in seconds. Inputs longer than this are trimmed; shorter inputs are zero-padded. Defaults to `30`.
*   **min\_frequency**: float. Lower frequency bound for the mel filterbank in Hz. Defaults to `0.0`.
*   **max\_frequency**: float. Upper frequency bound for the mel filterbank in Hz. Defaults to `8000.0`.
*   **mel\_floor**: float. Minimum value applied before the log compression for numerical stability. Defaults to `1e-5`.
*   **per\_bin\_mean**: list\[float\] or None. Per-channel mean subtracted after log compression. `None` disables mean subtraction. Defaults to `None`.
*   **per\_bin\_stddev**: list\[float\] or None. Per-channel standard deviation used to scale the output after mean subtraction. `None` disables scaling. Defaults to `None`.
*   **\*\*kwargs**: Additional keyword arguments forwarded to `[`keras\_hub.layers.AudioConverter`](/keras_hub/api/preprocessing_layers/audio_converter#audioconverter-class)`.

**Call arguments**

*   **audio**: array of shape `(num_samples,)` or `(batch_size, num_samples)`. Raw mono-channel audio waveform(s) at `sampling_rate` Hz.

**Returns**

Log-mel spectrogram of shape `(num_frames, num_mels)` for a 1-D input, or `(batch_size, num_frames, num_mels)` for a 2-D input, where `num_frames = num_samples // stride`.

**Examples**

Copied!

`import numpy as np import keras_hub  # Single waveform (1 second at 16 kHz). waveform = np.random.randn(16000).astype("float32") converter = keras_hub.layers.Gemma4AudioConverter() features = converter(waveform) print(features.shape)  # (100, 128)  # Batched waveforms. batch = np.random.randn(4, 16000).astype("float32") features = converter(batch) print(features.shape)  # (4, 100, 128)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/layers/preprocessing/audio_converter.py#L47)

### `from_preset` method

Copied!

`Gemma4AudioConverter.from_preset(preset, **kwargs)`

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

[Gemma4AudioConverter](https://keras.io/keras_hub/api/models/gemma4/gemma4_audio_converter/#gemma4audioconverter)

[`Gemma4AudioConverter` class](https://keras.io/keras_hub/api/models/gemma4/gemma4_audio_converter/#gemma4audioconverter-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/gemma4/gemma4_audio_converter/#frompreset-method)