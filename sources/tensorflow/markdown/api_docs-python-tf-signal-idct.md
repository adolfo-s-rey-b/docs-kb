[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/signal/idct#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/signal/idct)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/signal/idct?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/signal/idct#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/signal/idct#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/signal/idct#raises)
    
*   [scipy compatibility](https://www.tensorflow.org/api_docs/python/tf/signal/idct#scipy-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.signal.idct Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/signal/idct#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/signal/idct#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/signal/idct#raises)
    
*   [scipy compatibility](https://www.tensorflow.org/api_docs/python/tf/signal/idct#scipy-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/signal/dct_ops.py#L212-L256)

Computes the 1D [Inverse Discrete Cosine Transform (DCT)](https://en.wikipedia.org/wiki/Discrete_cosine_transform#Inverse_transforms)
 of `input`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.signal.idct`](https://www.tensorflow.org/api_docs/python/tf/signal/idct)
, [`tf.compat.v1.spectral.idct`](https://www.tensorflow.org/api_docs/python/tf/signal/idct)

tf.signal.idct(
        input, type=2, n=None, axis=-1, norm=None, name=None
    )

Currently Types I, II, III, IV are supported. Type III is the inverse of Type II, and vice versa.

Note that you must re-normalize by 1/(2n) to obtain an inverse if `norm` is not `'ortho'`. That is: `signal == idct(dct(signal)) * 0.5 / signal.shape[-1]`. When `norm='ortho'`, we have: `signal == idct(dct(signal, norm='ortho'), norm='ortho')`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `[..., samples]` `float32`/`float64` `Tensor` containing the signals to take the DCT of. |
| `type` | The IDCT type to perform. Must be 1, 2, 3 or 4. |
| `n` | For future expansion. The length of the transform. Must be `None`. |
| `axis` | For future expansion. The axis to compute the DCT along. Must be `-1`. |
| `norm` | The normalization to apply. `None` for no normalization or `'ortho'` for orthonormal normalization. |
| `name` | An optional name for the operation. |

|     |
| --- |
| Returns<br>------- |     |
| A `[..., samples]` `float32`/`float64` `Tensor` containing the IDCT of `input`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `type` is not `1`, `2` or `3`, `n` is not `None,`axis`is not`\-1`, or`norm`is not`None`or`'ortho'\`. |

scipy compatibility
-------------------

Equivalent to [scipy.fftpack.idct](https://docs.scipy.org/doc/scipy-1.4.0/reference/generated/scipy.fftpack.idct.html)
 for Type-I, Type-II, Type-III and Type-IV DCT.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.