[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/signal/fftshift#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/signal/fftshift)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/signal/fftshift?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fsignal%2Ffftshift&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/signal/fftshift#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/signal/fftshift#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/signal/fftshift#numpy-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.signal.fftshift Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/signal/fftshift#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/signal/fftshift#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/signal/fftshift#numpy-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/signal/fft_ops.py#L612-L654)

Shift the zero-frequency component to the center of the spectrum.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.signal.fftshift`](https://www.tensorflow.org/api_docs/python/tf/signal/fftshift)

tf.signal.fftshift(
        x, axes=None, name=None
    )

This function swaps half-spaces for all axes listed (defaults to all). Note that `y[0]` is the Nyquist component only if `len(x)` is even.

#### For example:

x = tf.signal.fftshift([ 0.,  1.,  2.,  3.,  4., -5., -4., -3., -2., -1.])
    x.numpy() # array([-5., -4., -3., -2., -1.,  0.,  1.,  2.,  3.,  4.])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | `Tensor`, input tensor. |
| `axes` | `int` or shape `tuple`, optional Axes over which to shift. Default is None, which shifts all axes. |
| `name` | An optional name for the operation. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`, The shifted tensor. |     |

numpy compatibility
-------------------

Equivalent to numpy.fft.fftshift. [https://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.fftshift.html](https://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.fftshift.html)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.