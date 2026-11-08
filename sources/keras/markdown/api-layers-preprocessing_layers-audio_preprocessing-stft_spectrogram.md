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
 / STFTSpectrogram layer

STFTSpectrogram layer
=====================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/stft_spectrogram.py#L12)

### `STFTSpectrogram` class

Copied!

`keras.layers.STFTSpectrogram(     mode="log",     frame_length=256,     frame_step=None,     fft_length=None,     window="hann",     periodic=False,     scaling="density",     padding="valid",     expand_dims=False,     data_format=None,     **kwargs )`

Layer to compute the Short-Time Fourier Transform (STFT) on a 1D signal.

A layer that computes Spectrograms of the input signal to produce a spectrogram. This layers utilizes Short-Time Fourier Transform (STFT) by The layer computes Spectrograms based on STFT by utilizing convolution kernels, which allows parallelization on GPUs and trainable kernels for fine-tuning support. This layer allows different modes of output (e.g., log-scaled magnitude, phase, power spectral density, etc.) and provides flexibility in windowing, padding, and scaling options for the STFT calculation.

**Examples**

Apply it as a non-trainable preprocessing layer on 3 audio tracks of 1 channel, 10 seconds and sampled at 16 kHz.

Copied!

`>>> layer = keras.layers.STFTSpectrogram( ...     mode='log', ...     frame_length=256, ...     frame_step=128,   # 50% overlap ...     fft_length=512, ...     window="hann", ...     padding="valid", ...     trainable=False,  # non-trainable, preprocessing only ... ) >>> layer(keras.random.uniform(shape=(3, 160000, 1))).shape (3, 1249, 257)`

Apply it as a trainable processing layer on 3 stereo audio tracks of 2 channels, 10 seconds and sampled at 16 kHz. This is initialized as the non-trainable layer, but then can be trained jointly within a model.

Copied!

`>>> layer = keras.layers.STFTSpectrogram( ...     mode='log', ...     frame_length=256, ...     frame_step=128,    # 50% overlap ...     fft_length=512, ...     window="hamming",  # hamming windowing function ...     padding="same",    # padding to preserve the time dimension ...     trainable=True,    # trainable, this is the default in keras ... ) >>> layer(keras.random.uniform(shape=(3, 160000, 2))).shape (3, 1250, 514)`

Similar to the last example, but add an extra dimension so the output is an image to be used with image models. We apply this here on a signal of 3 input channels to output an image tensor, hence is directly applicable with an image model.

Copied!

`>>> layer = keras.layers.STFTSpectrogram( ...     mode='log', ...     frame_length=256, ...     frame_step=128, ...     fft_length=512, ...     padding="same", ...     expand_dims=True,  # this adds the extra dimension ... ) >>> layer(keras.random.uniform(shape=(3, 160000, 3))).shape (3, 1250, 257, 3)`

**Arguments**

*   **mode**: String, the output type of the spectrogram. Can be one of `"log"`, `"magnitude`", `"psd"`, `"real`", `"imag`", `"angle`", `"stft`". Defaults to `"log`".
*   **frame\_length**: Integer, The length of each frame (window) for STFT in samples. Defaults to 256.
*   **frame\_step**: Integer, the step size (hop length) between consecutive frames. If not provided, defaults to half the frame\_length. Defaults to `frame_length // 2`.
*   **fft\_length**: Integer, the size of frequency bins used in the Fast-Fourier Transform (FFT) to apply to each frame. Should be greater than or equal to `frame_length`. Recommended to be a power of two. Defaults to the smallest power of two that is greater than or equal to `frame_length`.
*   **window**: (String or array\_like), the windowing function to apply to each frame. Can be `"hann`" (default), `"hamming`", or a custom window provided as an array\_like.
*   **periodic**: Boolean, if True, the window function will be treated as periodic. Defaults to `False`.
*   **scaling**: String, type of scaling applied to the window. Can be `"density`", `"spectrum`", or None. Default is `"density`".
*   **padding**: String, padding strategy. Can be `"valid`" or `"same`". Defaults to `"valid"`.
*   **expand\_dims**: Boolean, if True, will expand the output into spectrograms into two dimensions to be compatible with image models. Defaults to `False`.
*   **data\_format**: String, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)` while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, weight)`. Defaults to `"channels_last"`.

**Raises**

*   **ValueError**: If an invalid value is provided for `"mode`", `"scaling`", `"padding`", or other input arguments.
*   **TypeError**: If the input data type is not one of `"float16`", `"float32`", or `"float64`".

**Input shape**

A 3D tensor of shape `(batch_size, time_length, input_channels)`, if `data_format=="channels_last"`, and of shape `(batch_size, input_channels, time_length)` if `data_format=="channels_first"`, where `time_length` is the length of the input signal, and `input_channels` is the number of input channels. The same kernels are applied to each channel independently.

**Output shape**

If `data_format=="channels_first" and not expand_dims`, a 3D tensor: `(batch_size, input_channels * freq_channels, new_time_length)` If `data_format=="channels_last" and not expand_dims`, a 3D tensor: `(batch_size, new_time_length, input_channels * freq_channels)` If `data_format=="channels_first" and expand_dims`, a 4D tensor: `(batch_size, input_channels, new_time_length, freq_channels)` If `data_format=="channels_last" and expand_dims`, a 4D tensor: `(batch_size, new_time_length, freq_channels, input_channels)`

where `new_time_length` depends on the padding, and `freq_channels` is the number of FFT bins `(fft_length // 2 + 1)`.

* * *

[STFTSpectrogram layer](https://keras.io/api/layers/preprocessing_layers/audio_preprocessing/stft_spectrogram/#stftspectrogram-layer)

[`STFTSpectrogram` class](https://keras.io/api/layers/preprocessing_layers/audio_preprocessing/stft_spectrogram/#stftspectrogram-class)