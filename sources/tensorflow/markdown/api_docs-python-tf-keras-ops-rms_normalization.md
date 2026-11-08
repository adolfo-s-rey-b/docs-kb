[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/rms_normalization#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.rms\_normalization Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/nn.py#L2981-L3018)

Performs Root Mean Square (RMS) normalization on `x`.

#### View aliases

**Main aliases**

[`tf.keras.ops.nn.rms_normalization`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/rms_normalization)

tf.keras.ops.rms_normalization(
        x, scale=None, axis=-1, epsilon=None
    )

The Keras operation implements the operation as described in [Root Mean Square Layer Normalization](https://arxiv.org/pdf/1910.07467)
 by Biao Zhang et al.

The operation is different from LayerNormalization with RMS scaling.

It is defined as `rms_normalization(x) = x * rsqrt(mean(square(x))) * scale`

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |
| `scale` | Optional scaling factor for the normalization. |
| `axis` | The axis or axes along which to perform normalization. Defaults to `-1`. |
| `epsilon` | A lower bound value for the norm. Defaults to [`backend.epsilon()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/epsilon)<br>. |

|     |
| --- |
| Returns<br>------- |     |
| The normalized array. |     |

#### Example:

    x = keras.random.normal((1, 10))

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.