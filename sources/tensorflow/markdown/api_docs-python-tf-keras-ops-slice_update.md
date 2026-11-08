[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/slice_update#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/slice_update)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/slice_update?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/slice_update#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/slice_update#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.slice\_update Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/slice_update#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/slice_update#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/core.py#L506-L539)

Update an input by slicing in a tensor of updated values.

tf.keras.ops.slice_update(
        inputs, start_indices, updates
    )

At a high level, this operation does `inputs[start_indices: start_indices + updates.shape] = updates`. Assume inputs is a tensor of shape `(D0, D1, ..., Dn)`, `start_indices` must be a list/tuple of n integers, specifying the starting indices. `updates` must have the same rank as `inputs`, and the size of each dim must not exceed `Di - start_indices[i]`. For example, if we have 2D inputs `inputs = np.zeros((5, 5))`, and we want to update the intersection of last 2 rows and last 2 columns as 1, i.e., `inputs[3:, 3:] = np.ones((2, 2))`, then we can use the code below:

inputs = np.zeros((5, 5))
    start_indices = [3, 3]
    updates = np.ones((2, 2))
    inputs = keras.ops.slice_update(inputs, start_indices, updates)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `inputs` | A tensor, the tensor to be updated. |
| `start_indices` | A list/tuple of shape `(inputs.ndim,)`, specifying the starting indices for updating. |
| `updates` | A tensor, the new values to be put to `inputs` at `indices`. `updates` must have the same rank as `inputs`. |

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