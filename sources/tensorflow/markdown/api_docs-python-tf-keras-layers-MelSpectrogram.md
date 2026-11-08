[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MelSpectrogram#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MelSpectrogram)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MelSpectrogram?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MelSpectrogram#args)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MelSpectrogram#input-shape)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MelSpectrogram#output-shape)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MelSpectrogram#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MelSpectrogram#methods)
    *   [convert\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MelSpectrogram#convert_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MelSpectrogram#from_config)
        
    *   [linear\_to\_mel\_weight\_matrix](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MelSpectrogram#linear_to_mel_weight_matrix)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.MelSpectrogram Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MelSpectrogram#args)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MelSpectrogram#input-shape)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MelSpectrogram#output-shape)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MelSpectrogram#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MelSpectrogram#methods)
    *   [convert\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MelSpectrogram#convert_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MelSpectrogram#from_config)
        
    *   [linear\_to\_mel\_weight\_matrix](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MelSpectrogram#linear_to_mel_weight_matrix)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/mel_spectrogram.py#L9-L380)

A preprocessing layer to convert raw audio signals to Mel spectrograms.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.MelSpectrogram(
        fft_length=2048,
        sequence_stride=512,
        sequence_length=None,
        window='hann',
        sampling_rate=16000,
        num_mel_bins=128,
        min_freq=20.0,
        max_freq=None,
        power_to_db=True,
        top_db=80.0,
        mag_exp=2.0,
        min_power=1e-10,
        ref_power=1.0,
        **kwargs
    )

This layer takes `float32`/`float64` single or batched audio signal as inputs and computes the Mel spectrogram using Short-Time Fourier Transform and Mel scaling. The input should be a 1D (unbatched) or 2D (batched) tensor representing audio signals. The output will be a 2D or 3D tensor representing Mel spectrograms.

A spectrogram is an image-like representation that shows the frequency spectrum of a signal over time. It uses x-axis to represent time, y-axis to represent frequency, and each pixel to represent intensity. Mel spectrograms are a special type of spectrogram that use the mel scale, which approximates how humans perceive sound. They are commonly used in speech and music processing tasks like speech recognition, speaker identification, and music genre classification.

#### References:

*   [Spectrogram](https://en.wikipedia.org/wiki/Spectrogram)
    ,
*   [Mel scale](https://en.wikipedia.org/wiki/Mel_scale)
    .

|     |     |
| --- | --- |
| Args<br>---- |     |
| `fft_length` | Integer, size of the FFT window. |
| `sequence_stride` | Integer, number of samples between successive STFT columns. |
| `sequence_length` | Integer, size of the window used for applying `window` to each audio frame. If `None`, defaults to `fft_length`. |
| `window` | String, name of the window function to use. Available values are `"hann"` and `"hamming"`. If `window` is a tensor, it will be used directly as the window and its length must be `sequence_length`. If `window` is `None`, no windowing is used. Defaults to `"hann"`. |
| `sampling_rate` | Integer, sample rate of the input signal. |
| `num_mel_bins` | Integer, number of mel bins to generate. |
| `min_freq` | Float, minimum frequency of the mel bins. |
| `max_freq` | Float, maximum frequency of the mel bins. If `None`, defaults to `sampling_rate / 2`. |
| `power_to_db` | If True, convert the power spectrogram to decibels. |
| `top_db` | Float, minimum negative cut-off `max(10 * log10(S)) - top_db`. |
| `mag_exp` | Float, exponent for the magnitude spectrogram. 1 for magnitude, 2 for power, etc. Default is 2. |
| `ref_power` | Float, the power is scaled relative to it `10 * log10(S / ref_power)`. |
| `min_power` | Float, minimum value for power and `ref_power`. |

#### Examples:

**Unbatched audio signal**

    layer = keras.layers.MelSpectrogram(num_mel_bins=64,

**Batched audio signal**

    layer = keras.layers.MelSpectrogram(num_mel_bins=80,

|     |
| --- |
| Input shape<br>----------- |     |
| 1D (unbatched) or 2D (batched) tensor with shape:`(..., samples)`. |     |

|     |
| --- |
| Output shape<br>------------ |     |
| 2D (unbatched) or 3D (batched) tensor with shape:`(..., num_mel_bins, time)`. |     |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |

Methods
-------

### `convert_weight`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/data_layer.py#L153-L159)

convert_weight(
        weight
    )

Convert the weight if it is from the a different backend.

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/operation.py#L322-L362)

@classmethod

Creates an operation from its config.

This method is the reverse of `get_config`, capable of instantiating the same operation from the config dictionary.

if "dtype" in config and isinstance(config["dtype"], dict):
        policy = dtype_policies.deserialize(config["dtype"])

|     |     |
| --- | --- |
| Args |     |
| `config` | A Python dictionary, typically the output of `get_config`. |

|     |
| --- |
| Returns |     |
| An operation instance. |     |

### `linear_to_mel_weight_matrix`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/mel_spectrogram.py#L202-L335)

linear_to_mel_weight_matrix(
        num_mel_bins=20,
        num_spectrogram_bins=129,
        sampling_rate=8000,
        lower_edge_hertz=125.0,
        upper_edge_hertz=3800.0,
        dtype='float32'
    )

Returns a matrix to warp linear scale spectrograms to the mel scale.

Returns a weight matrix that can be used to re-weight a tensor containing `num_spectrogram_bins` linearly sampled frequency information from `[0, sampling_rate / 2]` into `num_mel_bins` frequency information from `[lower_edge_hertz, upper_edge_hertz]` on the mel scale.

This function follows the [Hidden Markov Model Toolkit (HTK)](http://htk.eng.cam.ac.uk/)
 convention, defining the mel scale in terms of a frequency in hertz according to the following formula:

`mel(f) = 2595 * log10( 1 + f/700)`

In the returned matrix, all the triangles (filterbanks) have a peak value of 1.0.

For example, the returned matrix `A` can be used to right-multiply a spectrogram `S` of shape `[frames, num_spectrogram_bins]` of linear scale spectrum values (e.g. STFT magnitudes) to generate a "mel spectrogram" `M` of shape `[frames, num_mel_bins]`.

# `S` has shape [frames, num_spectrogram_bins]
    # `M` has shape [frames, num_mel_bins]
    M = keras.ops.matmul(S, A)

The matrix can be used with [`keras.ops.tensordot`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/tensordot)
 to convert an arbitrary rank `Tensor` of linear-scale spectral bins into the mel scale.

# S has shape [..., num_spectrogram_bins].
    # M has shape [..., num_mel_bins].
    M = keras.ops.tensordot(S, A, 1)

#### References:

*   [Mel scale (Wikipedia)](https://en.wikipedia.org/wiki/Mel_scale)
    

|     |     |
| --- | --- |
| Args |     |
| `num_mel_bins` | Python int. How many bands in the resulting mel spectrum. |
| `num_spectrogram_bins` | An integer `Tensor`. How many bins there are in the source spectrogram data, which is understood to be `fft_size // 2 + 1`, i.e. the spectrogram only contains the nonredundant FFT bins. |
| `sampling_rate` | An integer or float `Tensor`. Samples per second of the input signal used to create the spectrogram. Used to figure out the frequencies corresponding to each spectrogram bin, which dictates how they are mapped into the mel scale. |
| `lower_edge_hertz` | Python float. Lower bound on the frequencies to be included in the mel spectrum. This corresponds to the lower edge of the lowest triangular band. |
| `upper_edge_hertz` | Python float. The desired top edge of the highest frequency band. |
| `dtype` | The `DType` of the result matrix. Must be a floating point type. |

|     |
| --- |
| Returns |     |
| A tensor of shape `[num_spectrogram_bins, num_mel_bins]`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.