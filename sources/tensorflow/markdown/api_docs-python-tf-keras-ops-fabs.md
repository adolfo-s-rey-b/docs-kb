[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fabs#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fabs)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fabs?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fabs#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fabs#returns)
    
*   [Example](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fabs#example)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.fabs Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fabs#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fabs#returns)
    
*   [Example](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fabs#example)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L206-L235)

Compute the absolute values element-wise.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.fabs`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fabs)

tf.keras.ops.fabs(
        x
    )

Integer or boolean inputs are automatically promoted to the default floating-point type. Complex values are not supported.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |

|     |
| --- |
| Returns<br>------- |     |
| An array containing the absolute value of each element in `x`. |     |

|     |
| --- |
| Example<br>------- |     |
| >>> x = keras.ops.convert_to_tensor([-1, 2], dtype="int32")<br>    </td><br>    </tr><br>    <br>    </table><br>    <br>    <br>    >>> keras.ops.fabs(x)<br>    array([1., 2.], dtype=float32)<br>     ```<br><br>Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)<br>, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)<br>. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)<br>. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)<br>.<br><br>Last updated 2026-10-31 UTC. |     |