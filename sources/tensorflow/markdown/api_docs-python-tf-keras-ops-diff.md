[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/diff#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/diff)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/diff?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/diff#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/diff#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.diff Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/diff#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/diff#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L2827-L2859)

Calculate the n-th discrete difference along the given axis.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.diff`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/diff)

tf.keras.ops.diff(
        a, n=1, axis=-1
    )

The first difference is given by `out[i] = a[i+1] - a[i]` along the given axis, higher differences are calculated by using `diff` recursively.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `a` | Input tensor. |
| `n` | The number of times values are differenced. Defaults to `1`. |
| `axis` | Axis to compute discrete difference(s) along. Defaults to `-1`.(last axis). |

|     |
| --- |
| Returns<br>------- |     |
| Tensor of diagonals. |     |

#### Examples:

    from keras.src import ops

    x = ops.convert_to_tensor([[1, 3, 6, 10], [0, 5, 6, 8]])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.