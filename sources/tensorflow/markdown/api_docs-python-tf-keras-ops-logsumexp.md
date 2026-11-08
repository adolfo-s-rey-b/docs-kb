[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/logsumexp#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/logsumexp)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/logsumexp?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/logsumexp#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/logsumexp#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.logsumexp Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/logsumexp#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/logsumexp#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/math.py#L335-L359)

Computes the logarithm of sum of exponentials of elements in a tensor.

tf.keras.ops.logsumexp(
        x, axis=None, keepdims=False
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |
| `axis` | An integer or a tuple of integers specifying the axis/axes along which to compute the sum. If `None`, the sum is computed over all elements. Defaults to `None`. |
| `keepdims` | A boolean indicating whether to keep the dimensions of the input tensor when computing the sum. Defaults to `False`. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor containing the logarithm of the sum of exponentials of elements in `x`. |     |

#### Example:

    x = keras.ops.convert_to_tensor([1., 2., 3.])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.