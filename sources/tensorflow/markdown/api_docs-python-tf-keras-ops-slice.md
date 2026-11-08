[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/slice#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/slice)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/slice?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fops%2Fslice&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/slice#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/slice#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.slice Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/slice#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/slice#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/core.py#L467-L495)

Return a slice of an input tensor.

tf.keras.ops.slice(
        inputs, start_indices, shape
    )

At a high level, this operation is an explicit replacement for array slicing e.g. `inputs[start_indices: start_indices + shape]`. Unlike slicing via brackets, this operation will accept tensor start indices on all backends, which is useful when indices dynamically computed via other tensor operations.

inputs = np.zeros((5, 5))
    start_indices = np.array([3, 3])
    shape = np.array([2, 2])
    inputs = keras.ops.slice(inputs, start_indices, shape)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `inputs` | A tensor, the tensor to be updated. |
| `start_indices` | A list/tuple of shape `(inputs.ndim,)`, specifying the starting indices for updating. |
| `shape` | The full shape of the returned slice. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor, has the same shape and dtype as `inputs`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.