[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/convert_to_tensor#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/convert_to_tensor)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/convert_to_tensor?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/convert_to_tensor#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/convert_to_tensor#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.convert\_to\_tensor Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/convert_to_tensor#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/convert_to_tensor#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/core.py#L1019-L1049)

Convert a NumPy array or Python array to a tensor.

tf.keras.ops.convert_to_tensor(
        x, dtype=None, sparse=None, ragged=None
    )

Native tensors for the current backend or left unchanged unless the `dtype`, `sparse` or `ragged` arguments are set.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A NumPy array, Python array (can be nested) or a backend tensor. |
| `dtype` | The target type. If `None`, the type of `x` is used. |
| `sparse` | Whether to keep sparse tensors. `False` will cause sparse tensors to be densified. The default value of `None` means that sparse tensors are kept only if the backend supports them. |
| `ragged` | Whether to keep ragged tensors. `False` will cause ragged tensors to be densified. The default value of `None` means that ragged tensors are kept only if the backend supports them. |

|     |
| --- |
| Returns<br>------- |     |
| A backend tensor of the specified `dtype` and sparseness. |     |

#### Example:

    x = np.array([1, 2, 3])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.