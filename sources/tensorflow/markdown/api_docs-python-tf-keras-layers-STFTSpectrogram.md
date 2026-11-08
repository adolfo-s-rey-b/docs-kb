[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/STFTSpectrogram#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/STFTSpectrogram)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/STFTSpectrogram?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/STFTSpectrogram#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/layers/STFTSpectrogram#raises)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/STFTSpectrogram#input-shape)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/STFTSpectrogram#output-shape)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/STFTSpectrogram#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/STFTSpectrogram#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/STFTSpectrogram#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.STFTSpectrogram Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/STFTSpectrogram#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/layers/STFTSpectrogram#raises)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/STFTSpectrogram#input-shape)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/STFTSpectrogram#output-shape)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/STFTSpectrogram#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/STFTSpectrogram#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/STFTSpectrogram#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/stft_spectrogram.py#L12-L383)

Layer to compute the Short-Time Fourier Transform (STFT) on a 1D signal.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.STFTSpectrogram(
        mode='log',
        frame_length=256,
        frame_step=None,
        fft_length=None,
        window='hann',
        periodic=False,
        scaling='density',
        padding='valid',
        expand_dims=False,
        data_format=None,
        **kwargs
    )

A layer that computes Spectrograms of the input signal to produce a spectrogram. This layers utilizes Short-Time Fourier Transform (STFT) by The layer computes Spectrograms based on STFT by utilizing convolution kernels, which allows parallelization on GPUs and trainable kernels for fine-tuning support. This layer allows different modes of output (e.g., log-scaled magnitude, phase, power spectral density, etc.) and provides flexibility in windowing, padding, and scaling options for the STFT calculation.

#### Examples:

Apply it as a non-trainable preprocessing layer on 3 audio tracks of 1 channel, 10 seconds and sampled at 16 kHz.

    layer = keras.layers.STFTSpectrogram(

Apply it as a trainable processing layer on 3 stereo audio tracks of 2 channels, 10 seconds and sampled at 16 kHz. This is initialized as the non-trainable layer, but then can be trained jointly within a model.

    layer = keras.layers.STFTSpectrogram(

Similar to the last example, but add an extra dimension so the output is an image to be used with image models. We apply this here on a signal of 3 input channels to output an image tensor, hence is directly applicable with an image model.

    layer = keras.layers.STFTSpectrogram(

|     |     |
| --- | --- |
| Args<br>---- |     |
| `mode` | String, the output type of the spectrogram. Can be one of `"log"`, `"magnitude`", `"psd"`, `"real`", `"imag`", `"angle`", `"stft`". Defaults to `"log`". |
| `frame_length` | Integer, The length of each frame (window) for STFT in samples. Defaults to 256. |
| `frame_step` | Integer, the step size (hop length) between consecutive frames. If not provided, defaults to half the frame\_length. Defaults to `frame_length // 2`. |
| `fft_length` | Integer, the size of frequency bins used in the Fast-Fourier Transform (FFT) to apply to each frame. Should be greater than or equal to `frame_length`. Recommended to be a power of two. Defaults to the smallest power of two that is greater than or equal to `frame_length`. |
| `window` | (String or array\_like), the windowing function to apply to each frame. Can be `"hann`" (default), `"hamming`", or a custom window provided as an array\_like. |
| `periodic` | Boolean, if True, the window function will be treated as periodic. Defaults to `False`. |
| `scaling` | String, type of scaling applied to the window. Can be `"density`", `"spectrum`", or None. Default is `"density`". |
| `padding` | String, padding strategy. Can be `"valid`" or `"same`". Defaults to `"valid"`. |
| `expand_dims` | Boolean, if True, will expand the output into spectrograms into two dimensions to be compatible with image models. Defaults to `False`. |
| `data_format` | String, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)` while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, weight)`. Defaults to `"channels_last"`. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If an invalid value is provided for `"mode`", `"scaling`", `"padding`", or other input arguments. |
| `TypeError` | If the input data type is not one of `"float16`", `"float32`", or `"float64`". |

|     |
| --- |
| Input shape<br>----------- |     |
| A 3D tensor of shape `(batch_size, time_length, input_channels)`, if `data_format=="channels_last"`, and of shape `(batch_size, input_channels, time_length)` if `data_format=="channels_first"`, where `time_length` is the length of the input signal, and `input_channels` is the number of input channels. The same kernels are applied to each channel independently. |     |

|     |
| --- |
| Output shape<br>------------ |     |
| If `data_format=="channels_first" and not expand_dims`, a 3D tensor: `(batch_size, input_channels * freq_channels, new_time_length)` If `data_format=="channels_last" and not expand_dims`, a 3D tensor: `(batch_size, new_time_length, input_channels * freq_channels)` If `data_format=="channels_first" and expand_dims`, a 4D tensor: `(batch_size, input_channels, new_time_length, freq_channels)` If `data_format=="channels_last" and expand_dims`, a 4D tensor: `(batch_size, new_time_length, freq_channels, input_channels)`<br><br>where `new_time_length` depends on the padding, and `freq_channels` is the number of FFT bins `(fft_length // 2 + 1)`. |     |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |

Methods
-------

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

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.