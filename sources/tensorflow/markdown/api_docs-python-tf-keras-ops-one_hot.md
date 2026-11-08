[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/one_hot#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/one_hot)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/one_hot?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/one_hot#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/one_hot#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.one\_hot Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/one_hot#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/one_hot#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/nn.py#L1932-L1978)

Converts integer tensor `x` into a one-hot tensor.

#### View aliases

**Main aliases**

[`tf.keras.ops.nn.one_hot`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/one_hot)

tf.keras.ops.one_hot(
        x, num_classes, axis=-1, dtype=None, sparse=False
    )

The one-hot encoding is a representation where each integer value is converted into a binary vector with a length equal to `num_classes`, and the index corresponding to the integer value is marked as 1, while all other indices are marked as 0.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Integer tensor to be encoded. The shape can be arbitrary, but the dtype should be integer. |
| `num_classes` | Number of classes for the one-hot encoding. |
| `axis` | Axis along which the encoding is performed. `-1` represents the last axis. Defaults to `-1`. |
| `dtype` | (Optional) Data type of the output tensor. If not provided, it defaults to the default data type of the backend. |
| `sparse` | Whether to return a sparse tensor; for backends that support sparse tensors. |

|     |
| --- |
| Returns<br>------- |     |
| Integer tensor: One-hot encoded tensor with the same shape as `x` except for the specified `axis` dimension, which will have a length of `num_classes`. The dtype of the output tensor is determined by `dtype` or the default data type of the backend. |     |

#### Example:

    x = keras.ops.convert_to_tensor([1, 3, 2, 0])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.