None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [Layers API](https://keras.io/api/layers/)
 [The base Layer class](https://keras.io/api/layers/base_layer/)
 [Layer activations](https://keras.io/api/layers/activations/)
 [Layer weight initializers](https://keras.io/api/layers/initializers/)
 [Layer weight regularizers](https://keras.io/api/layers/regularizers/)
 [Layer weight constraints](https://keras.io/api/layers/constraints/)
 [Core layers](https://keras.io/api/layers/core_layers/)
 [Convolution layers](https://keras.io/api/layers/convolution_layers/)
 [Pooling layers](https://keras.io/api/layers/pooling_layers/)
 [Recurrent layers](https://keras.io/api/layers/recurrent_layers/)
 [Preprocessing layers](https://keras.io/api/layers/preprocessing_layers/)
 [Normalization layers](https://keras.io/api/layers/normalization_layers/)
 [Regularization layers](https://keras.io/api/layers/regularization_layers/)
 [Attention layers](https://keras.io/api/layers/attention_layers/)
 [Reshaping layers](https://keras.io/api/layers/reshaping_layers/)
 [Merging layers](https://keras.io/api/layers/merging_layers/)
 [Activation layers](https://keras.io/api/layers/activation_layers/)
 [Backend-specific layers](https://keras.io/api/layers/backend_specific_layers/)
 [Callbacks API](https://keras.io/api/callbacks/)
 [Ops API](https://keras.io/api/ops/)
 [Optimizers](https://keras.io/api/optimizers/)
 [Metrics](https://keras.io/api/metrics/)
 [Losses](https://keras.io/api/losses/)
 [Data loading](https://keras.io/api/data_loading/)
 [Tree API](https://keras.io/api/tree/)
 [Built-in small datasets](https://keras.io/api/datasets/)
 [Keras Applications](https://keras.io/api/applications/)
 [Mixed precision](https://keras.io/api/mixed_precision/)
 [Multi-device distribution](https://keras.io/api/distribution/)
 [RNG API](https://keras.io/api/random/)
 [Quantizers](https://keras.io/api/quantizers/)
 [Scope](https://keras.io/api/scope/)
 [Rematerialization](https://keras.io/api/rematerialization/)
 [Utilities](https://keras.io/api/utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

► [Keras 3 API documentation](https://keras.io/api/)
 / [Layers API](https://keras.io/api/layers/)
 / [Preprocessing layers](https://keras.io/api/layers/preprocessing_layers/)
 / [Audio preprocessing layers](https://keras.io/api/layers/preprocessing_layers/audio_preprocessing/)
 / MelSpectrogram layer

MelSpectrogram layer
====================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/mel_spectrogram.py#L9)

### `MelSpectrogram` class

Copied!

`keras.layers.MelSpectrogram(     fft_length=2048,     sequence_stride=512,     sequence_length=None,     window="hann",     sampling_rate=16000,     num_mel_bins=128,     min_freq=20.0,     max_freq=None,     power_to_db=True,     top_db=80.0,     mag_exp=2.0,     min_power=1e-10,     ref_power=1.0,     **kwargs )`

A preprocessing layer to convert raw audio signals to Mel spectrograms.

This layer takes `float32`/`float64` single or batched audio signal as inputs and computes the Mel spectrogram using Short-Time Fourier Transform and Mel scaling. The input should be a 1D (unbatched) or 2D (batched) tensor representing audio signals. The output will be a 2D or 3D tensor representing Mel spectrograms.

A spectrogram is an image-like representation that shows the frequency spectrum of a signal over time. It uses x-axis to represent time, y-axis to represent frequency, and each pixel to represent intensity. Mel spectrograms are a special type of spectrogram that use the mel scale, which approximates how humans perceive sound. They are commonly used in speech and music processing tasks like speech recognition, speaker identification, and music genre classification.

**Note:** This layer is safe to use inside a [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)
 or `grain` pipeline (independently of which backend you're using).

**References**

*   [Spectrogram](https://en.wikipedia.org/wiki/Spectrogram)
    ,
*   [Mel scale](https://en.wikipedia.org/wiki/Mel_scale)
    .

**Arguments**

*   **fft\_length**: Integer, size of the FFT window.
*   **sequence\_stride**: Integer, number of samples between successive STFT columns.
*   **sequence\_length**: Integer, size of the window used for applying `window` to each audio frame. If `None`, defaults to `fft_length`.
*   **window**: String, name of the window function to use. Available values are `"hann"` and `"hamming"`. If `window` is a tensor, it will be used directly as the window and its length must be `sequence_length`. If `window` is `None`, no windowing is used. Defaults to `"hann"`.
*   **sampling\_rate**: Integer, sample rate of the input signal.
*   **num\_mel\_bins**: Integer, number of mel bins to generate.
*   **min\_freq**: Float, minimum frequency of the mel bins.
*   **max\_freq**: Float, maximum frequency of the mel bins. If `None`, defaults to `sampling_rate / 2`.
*   **power\_to\_db**: If True, convert the power spectrogram to decibels.
*   **top\_db**: Float, minimum negative cut-off `max(10 * log10(S)) - top_db`.
*   **mag\_exp**: Float, exponent for the magnitude spectrogram. 1 for magnitude, 2 for power, etc. Default is 2.
*   **ref\_power**: Float, the power is scaled relative to it `10 * log10(S / ref_power)`.
*   **min\_power**: Float, minimum value for power and `ref_power`.

**Examples**

**Unbatched audio signal**

Copied!

`>>> layer = keras.layers.MelSpectrogram(num_mel_bins=64, ...                                     sampling_rate=8000, ...                                     sequence_stride=256, ...                                     fft_length=2048) >>> layer(keras.random.uniform(shape=(16000,))).shape (64, 63)`

**Batched audio signal**

Copied!

`>>> layer = keras.layers.MelSpectrogram(num_mel_bins=80, ...                                     sampling_rate=8000, ...                                     sequence_stride=128, ...                                     fft_length=2048) >>> layer(keras.random.uniform(shape=(2, 16000))).shape (2, 80, 125)`

**Input shape**

1D (unbatched) or 2D (batched) tensor with shape:`(..., samples)`.

**Output shape**

2D (unbatched) or 3D (batched) tensor with shape:`(..., num_mel_bins, time)`.

* * *

[MelSpectrogram layer](https://keras.io/api/layers/preprocessing_layers/audio_preprocessing/mel_spectrogram/#melspectrogram-layer)

[`MelSpectrogram` class](https://keras.io/api/layers/preprocessing_layers/audio_preprocessing/mel_spectrogram/#melspectrogram-class)