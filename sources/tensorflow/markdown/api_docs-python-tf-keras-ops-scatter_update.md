[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/scatter_update#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/scatter_update)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/scatter_update?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fops%2Fscatter_update&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/scatter_update#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/scatter_update#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.scatter\_update Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/scatter_update#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/scatter_update#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/core.py#L350-L427)

Update inputs via updates at scattered (sparse) indices.

tf.keras.ops.scatter_update(
        inputs, indices, updates, reduction=None
    )

At a high level, this operation does `inputs[indices] = updates`. Assume `inputs` is a tensor of shape `(D0, D1, ..., Dn)`, there are 2 main usages of `scatter_update`.

1.  `indices` is a 2D tensor of shape `(num_updates, n)`, where `num_updates` is the number of updates to perform, and `updates` is a 1D tensor of shape `(num_updates,)`. For example, if `inputs` is `zeros((4, 4, 4))`, and we want to update `inputs[1, 2, 3]` and `inputs[0, 1, 3]` as 1, then we can use:

inputs = np.zeros((4, 4, 4))
    indices = [[1, 2, 3], [0, 1, 3]]
    updates = np.array([1., 1.])
    inputs = keras.ops.scatter_update(inputs, indices, updates)

2 `indices` is a 2D tensor of shape `(num_updates, k)`, where `num_updates` is the number of updates to perform, and `k` (`k < n`) is the size of each index in `indices`. `updates` is a `n - k`\-D tensor of shape `(num_updates, inputs.shape[k:])`. For example, if `inputs = np.zeros((4, 4, 4))`, and we want to update `inputs[1, 2, :]` and `inputs[2, 3, :]` as `[1, 1, 1, 1]`, then `indices` would have shape `(num_updates, 2)` (`k = 2`), and `updates` would have shape `(num_updates, 4)` (`inputs.shape[2:] = 4`). See the code below:

inputs = np.zeros((4, 4, 4))
    indices = [[1, 2], [2, 3]]
    updates = np.array([[1., 1., 1, 1,], [1., 1., 1, 1,])\
    inputs = keras.ops.scatter_update(inputs, indices, updates)\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `inputs` | A tensor, the tensor to be updated. |\
| `indices` | A tensor or list/tuple of shape `(N, inputs.ndim)`, specifying indices to update. `N` is the number of indices to update, must be equal to the first dimension of `updates`. |\
| `updates` | A tensor, the new values to be put to `inputs` at `indices`. |\
| `reduction` | A string specifying the reduction operation to apply when multiple updates target the same index. Supported values are: `None` (default): Updates replace existing values (last write wins). `"add"`: Updates are added to existing values. `"max"`: The maximum of updates and existing values is kept. `"min"`: The minimum of updates and existing values is kept. `"mul"`: Updates are multiplied with existing values. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A tensor, has the same shape and dtype as `inputs`. |     |\
\
#### Example:\
\
Using `reduction="add"` to accumulate values at the same index:\
\
    inputs = np.zeros((4,))\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.