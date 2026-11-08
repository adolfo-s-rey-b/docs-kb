[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/dstack#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/dstack)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/dstack?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/dstack#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/dstack#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.dstack Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/dstack#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/dstack#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L3008-L3040)

Stack tensors in sequence depth wise (along third axis).

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.dstack`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/dstack)

tf.keras.ops.dstack(
        xs
    )

This is equivalent to concatenation along the third axis after 2-D tensors of shape `(M, N)` have been reshaped to `(M, N, 1)` and 1-D tensors of shape `(N,)` have been reshaped to `(1, N, 1)`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `xs` | Sequence of tensors. |

|     |
| --- |
| Returns<br>------- |     |
| The tensor formed by stacking the given tensors. |     |

#### Examples:

    import keras

    x = keras.ops.array([[1], [2], [3]])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.