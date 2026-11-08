[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/multi_hot#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/multi_hot)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/multi_hot?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/multi_hot#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/multi_hot#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.multi\_hot Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/multi_hot#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/multi_hot#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/nn.py#L2270-L2313)

Encodes integer labels as multi-hot vectors.

#### View aliases

**Main aliases**

[`tf.keras.ops.nn.multi_hot`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/multi_hot)

tf.keras.ops.multi_hot(
        inputs, num_classes=None, axis=-1, dtype=None, sparse=False, **kwargs
    )

This function encodes integer labels as multi-hot vectors, where each label is mapped to a binary value in the resulting vector.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `inputs` | Tensor of integer labels to be converted to multi-hot vectors. |
| `num_classes` | Integer, the total number of unique classes. |
| `axis` | (optional) Axis along which the multi-hot encoding should be added. Defaults to `-1`, which corresponds to the last dimension. |
| `dtype` | (optional) The data type of the resulting tensor. Default is backend's float type. |
| `sparse` | Whether to return a sparse tensor; for backends that support sparse tensors. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `Tensor` | The multi-hot encoded tensor. |

#### Example:

    data = keras.ops.convert_to_tensor([0, 4])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.