[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/batch_normalization#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/batch_normalization)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/batch_normalization?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/batch_normalization#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/batch_normalization#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.batch\_normalization Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/batch_normalization#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/batch_normalization#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/nn.py#L2422-L2478)

Normalizes `x` by `mean` and `variance`.

#### View aliases

**Main aliases**

[`tf.keras.ops.nn.batch_normalization`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/batch_normalization)

tf.keras.ops.batch_normalization(
        x, mean, variance, axis, offset=None, scale=None, epsilon=0.001
    )

This op is typically used by the batch normalization step in a neural network. It normalizes the input tensor along the given axis.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |
| `mean` | A mean vector of the same length as the `axis` dimension of the input thensor. |
| `variance` | A variance vector of the same length as the `axis` dimension of the input tensor. |
| `axis` | Integer, the axis that should be normalized. |
| `offset` | An offset vector of the same length as the `axis` dimension of the input tensor. If not `None`, `offset` is added to the normalized tensor. Defaults to `None`. |
| `scale` | A scale vector of the same length as the `axis` dimension of the input tensor. If not `None`, the normalized tensor is multiplied by `scale`. Defaults to `None`. |
| `epsilon` | Small float added to variance to avoid dividing by zero. Defaults to 1e-3. |

|     |
| --- |
| Returns<br>------- |     |
| The normalized tensor. |     |

#### Example:

    x = keras.ops.convert_to_tensor(

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.