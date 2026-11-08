[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/diagonal#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/diagonal)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/diagonal?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/diagonal#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/diagonal#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.diagonal Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/diagonal#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/diagonal#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L2739-L2806)

Return specified diagonals.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.diagonal`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/diagonal)

tf.keras.ops.diagonal(
        x, offset=0, axis1=0, axis2=1
    )

If `x` is 2-D, returns the diagonal of `x` with the given offset, i.e., the collection of elements of the form `x[i, i+offset]`.

If `x` has more than two dimensions, the axes specified by `axis1` and `axis2` are used to determine the 2-D sub-array whose diagonal is returned.

The shape of the resulting array can be determined by removing `axis1` and `axis2` and appending an index to the right equal to the size of the resulting diagonals.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |
| `offset` | Offset of the diagonal from the main diagonal. Can be positive or negative. Defaults to `0`.(main diagonal). |
| `axis1` | Axis to be used as the first axis of the 2-D sub-arrays. Defaults to `0`.(first axis). |
| `axis2` | Axis to be used as the second axis of the 2-D sub-arrays. Defaults to `1` (second axis). |

|     |
| --- |
| Returns<br>------- |     |
| Tensor of diagonals. |     |

#### Examples:

    from keras.src import ops

    x = ops.arange(8).reshape((2, 2, 2))

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.