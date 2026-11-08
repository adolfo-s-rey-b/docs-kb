[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/sparsemax#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/sparsemax)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/sparsemax?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/sparsemax#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/sparsemax#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.sparsemax Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/sparsemax#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/sparsemax#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/nn.py#L1067-L1094)

Sparsemax activation function.

#### View aliases

**Main aliases**

[`tf.keras.ops.nn.sparsemax`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/sparsemax)

tf.keras.ops.sparsemax(
        x, axis=-1
    )

For each batch `i`, and class `j`, sparsemax activation function is defined as:

`sparsemax(x)[i, j] = max(x[i, j] - τ(x[i, :]), 0).`

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |
| `axis` | `int`, axis along which the sparsemax operation is applied. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor, output of sparsemax transformation. Has the same type and shape as `x`. |     |

#### Example:

    x = np.array([-1., 0., 1.])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.