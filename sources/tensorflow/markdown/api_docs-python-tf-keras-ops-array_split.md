[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/array_split#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/array_split)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/array_split?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/array_split#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/array_split#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.array\_split Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/array_split#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/array_split#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L9760-L9811)

Splits an array into multiple sub-arrays (unevenly).

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.array_split`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/array_split)

tf.keras.ops.array_split(
        x, indices_or_sections, axis=0
    )

This is similar to [`keras.ops.split`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/split)
, but it allows for unequal splits. `indices_or_sections` must be an integer that indicates the total number of sub-arrays to create. If the tensor cannot be divided evenly, the first `remainder` splits will have size `quotient + 1`, and the rest will have size `quotient`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |
| `indices_or_sections` | An integer indicating the number of sub-arrays to create. |
| `axis` | The axis along which to split. Defaults to 0. |

|     |
| --- |
| Returns<br>------- |     |
| A list of sub-tensors. |     |

#### Example:

    x = keras.ops.arange(10)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.