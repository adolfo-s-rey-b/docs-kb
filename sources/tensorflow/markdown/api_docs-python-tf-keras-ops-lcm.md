[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/lcm#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/lcm)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/lcm?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fops%2Flcm&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/lcm#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/lcm#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.lcm Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/lcm#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/lcm#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4486-L4505)

Least common multiple of `x1` and `x2`, element-wise.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.lcm`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/lcm)

tf.keras.ops.lcm(
        x1, x2
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x1` | First input tensor (integer type). |
| `x2` | Second input tensor (integer type). |

|     |
| --- |
| Returns<br>------- |     |
| Output tensor, element-wise least common multiple of `x1` and `x2`. |     |

#### Example:

    x1 = keras.ops.convert_to_tensor([2, 3, 4])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.