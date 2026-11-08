[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/logical_not#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/logical_not)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/logical_not?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/logical_not#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/logical_not#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.logical\_not Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/logical_not#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/logical_not#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4935-L4954)

Computes the element-wise NOT of the given input tensor.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.logical_not`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/logical_not)

tf.keras.ops.logical_not(
        x
    )

Zeros are treated as `False` and non-zeros are treated as `True`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |

|     |
| --- |
| Returns<br>------- |     |
| Output tensor, element-wise logical NOT of the input. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.