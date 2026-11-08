[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/signal/dct#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/signal/dct)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/signal/dct?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/signal/dct#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/signal/dct#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/signal/dct#raises)
    
*   [scipy compatibility](https://www.tensorflow.org/api_docs/python/tf/signal/dct#scipy-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.signal.dct Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/signal/dct#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/signal/dct#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/signal/dct#raises)
    
*   [scipy compatibility](https://www.tensorflow.org/api_docs/python/tf/signal/dct#scipy-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/signal/dct_ops.py#L50-L97)

Computes the 1D [Discrete Cosine Transform (DCT)](https://en.wikipedia.org/wiki/Discrete_cosine_transform)
 of `input`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.signal.dct`](https://www.tensorflow.org/api_docs/python/tf/signal/dct)
, [`tf.compat.v1.spectral.dct`](https://www.tensorflow.org/api_docs/python/tf/signal/dct)

tf.signal.dct(
        input, type=2, n=None, axis=-1, norm=None, name=None
    )

Types I, II, III and IV are supported. Type I is implemented using a length `2N` padded [`tf.signal.rfft`](https://www.tensorflow.org/api_docs/python/tf/signal/rfft)
. Type II is implemented using a length `2N` padded [`tf.signal.rfft`](https://www.tensorflow.org/api_docs/python/tf/signal/rfft)
, as described here: [Type 2 DCT using 2N FFT padded (Makhoul)](https://dsp.stackexchange.com/a/10606)
. Type III is a fairly straightforward inverse of Type II (i.e. using a length `2N` padded [`tf.signal.irfft`](https://www.tensorflow.org/api_docs/python/tf/signal/irfft)
). Type IV is calculated through 2N length DCT2 of padded signal and picking the odd indices.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `[..., samples]` `float32`/`float64` `Tensor` containing the signals to take the DCT of. |
| `type` | The DCT type to perform. Must be 1, 2, 3 or 4. |
| `n` | The length of the transform. If length is less than sequence length, only the first n elements of the sequence are considered for the DCT. If n is greater than the sequence length, zeros are padded and then the DCT is computed as usual. |
| `axis` | For future expansion. The axis to compute the DCT along. Must be `-1`. |
| `norm` | The normalization to apply. `None` for no normalization or `'ortho'` for orthonormal normalization. |
| `name` | An optional name for the operation. |

|     |
| --- |
| Returns<br>------- |     |
| A `[..., samples]` `float32`/`float64` `Tensor` containing the DCT of `input`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `type` is not `1`, `2`, `3` or `4`, `axis` is not `-1`, `n` is not `None` or greater than 0, or `norm` is not `None` or `'ortho'`. |
| `ValueError` | If `type` is `1` and `norm` is `ortho`. |

scipy compatibility
-------------------

Equivalent to [scipy.fftpack.dct](https://docs.scipy.org/doc/scipy-1.4.0/reference/generated/scipy.fftpack.dct.html)
 for Type-I, Type-II, Type-III and Type-IV DCT.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.