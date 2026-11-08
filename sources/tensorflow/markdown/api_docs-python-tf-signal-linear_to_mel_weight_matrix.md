[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/signal/linear_to_mel_weight_matrix#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/signal/linear_to_mel_weight_matrix)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/signal/linear_to_mel_weight_matrix?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/signal/linear_to_mel_weight_matrix#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/signal/linear_to_mel_weight_matrix#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/signal/linear_to_mel_weight_matrix#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.signal.linear\_to\_mel\_weight\_matrix Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/signal/linear_to_mel_weight_matrix#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/signal/linear_to_mel_weight_matrix#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/signal/linear_to_mel_weight_matrix#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/signal/mel_ops.py#L90-L216)

Returns a matrix to warp linear scale spectrograms to the [mel scale](https://en.wikipedia.org/wiki/Mel_scale)
.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.signal.linear_to_mel_weight_matrix`](https://www.tensorflow.org/api_docs/python/tf/signal/linear_to_mel_weight_matrix)

tf.signal.linear_to_mel_weight_matrix(
        num_mel_bins=20,
        num_spectrogram_bins=129,
        sample_rate=8000,
        lower_edge_hertz=125.0,
        upper_edge_hertz=3800.0,
        dtype=tf.dtypes.float32,
        name=None
    )

Returns a weight matrix that can be used to re-weight a `Tensor` containing `num_spectrogram_bins` linearly sampled frequency information from `[0, sample_rate / 2]` into `num_mel_bins` frequency information from `[lower_edge_hertz, upper_edge_hertz]` on the [mel scale](https://en.wikipedia.org/wiki/Mel_scale)
.

This function follows the [Hidden Markov Model Toolkit (HTK)](http://htk.eng.cam.ac.uk/)
 convention, defining the mel scale in terms of a frequency in hertz according to the following formula:

$$\textrm{mel}(f) = 2595 * \textrm{log}_{10}(1 + \frac{f}{700})$$

In the returned matrix, all the triangles (filterbanks) have a peak value of 1.0.

For example, the returned matrix `A` can be used to right-multiply a spectrogram `S` of shape `[frames, num_spectrogram_bins]` of linear scale spectrum values (e.g. STFT magnitudes) to generate a "mel spectrogram" `M` of shape `[frames, num_mel_bins]`.

# `S` has shape [frames, num_spectrogram_bins]
    # `M` has shape [frames, num_mel_bins]
    M = tf.matmul(S, A)

The matrix can be used with [`tf.tensordot`](https://www.tensorflow.org/api_docs/python/tf/tensordot)
 to convert an arbitrary rank `Tensor` of linear-scale spectral bins into the mel scale.

# S has shape [..., num_spectrogram_bins].
    # M has shape [..., num_mel_bins].
    M = tf.tensordot(S, A, 1)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `num_mel_bins` | Python int. How many bands in the resulting mel spectrum. |
| `num_spectrogram_bins` | An integer `Tensor`. How many bins there are in the source spectrogram data, which is understood to be `fft_size // 2 + 1`, i.e. the spectrogram only contains the nonredundant FFT bins. |
| `sample_rate` | An integer or float `Tensor`. Samples per second of the input signal used to create the spectrogram. Used to figure out the frequencies corresponding to each spectrogram bin, which dictates how they are mapped into the mel scale. |
| `lower_edge_hertz` | Python float. Lower bound on the frequencies to be included in the mel spectrum. This corresponds to the lower edge of the lowest triangular band. |
| `upper_edge_hertz` | Python float. The desired top edge of the highest frequency band. |
| `dtype` | The `DType` of the result matrix. Must be a floating point type. |
| `name` | An optional name for the operation. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of shape `[num_spectrogram_bins, num_mel_bins]`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `num_mel_bins`/`num_spectrogram_bins`/`sample_rate` are not positive, `lower_edge_hertz` is negative, frequency edges are incorrectly ordered, `upper_edge_hertz` is larger than the Nyquist frequency. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.