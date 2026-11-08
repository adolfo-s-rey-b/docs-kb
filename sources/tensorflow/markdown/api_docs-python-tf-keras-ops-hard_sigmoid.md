[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/hard_sigmoid#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/hard_sigmoid)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/hard_sigmoid?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/hard_sigmoid#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/hard_sigmoid#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.hard\_sigmoid Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/hard_sigmoid#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/hard_sigmoid#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/nn.py#L469-L498)

Hard sigmoid activation function.

#### View aliases

**Main aliases**

[`tf.keras.ops.nn.hard_sigmoid`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/hard_sigmoid)

tf.keras.ops.hard_sigmoid(
        x
    )

#### It is defined as:

`0 if x < -2.5`, `1 if x > 2.5`, `(0.2 * x) + 0.5 if -2.5 <= x <= 2.5`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor with the same shape as `x`. |     |

#### Example:

    x = np.array([-1., 0., 1.])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.