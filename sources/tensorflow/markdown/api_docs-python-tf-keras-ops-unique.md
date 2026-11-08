[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/unique#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.unique Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L9886-L9983)

Finds the unique elements of a tensor.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.unique`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/unique)

tf.keras.ops.unique(
        x,
        sorted=True,
        return_index=False,
        return_inverse=False,
        return_counts=False,
        axis=None,
        size=None,
        fill_value=None
    )

This function returns the unique elements of an array, optionally sorted. When `size` is provided, the output shape is fixed, making it compatible with JIT compilation (e.g., JAX, TensorFlow Graph Mode).

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |
| `sorted` | Whether to sort the unique elements in ascending order. Defaults to `True`. |
| `return_index` | If `True`, also return the indices of the first occurrence of each unique element in `x`. Defaults to `False`. |
| `return_inverse` | If `True`, also return the indices of the unique tensor (for the specified axis, if provided) that can be used to reconstruct `x`. Defaults to `False`. |
| `return_counts` | If `True`, also return the number of times each unique item appears in `x`. Defaults to `False`. |
| `axis` | The axis to operate on. If `None`, `x` will be flattened. If an integer, the subarrays indexed by the given axis will be treated as the elements. Defaults to `None`. |
| `size` | Optional integer. If provided, the output will always have this fixed size. If the number of unique elements is less than `size`, the output will be padded with `fill_value`. If greater, the output will be truncated. |
| `fill_value` | The value used to pad the output when `size` is specified and there are fewer unique elements than `size`. Defaults to `0`. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor or a tuple of tensors.<br><br>*   `unique_values`: The unique values. Shape is `(size,)` if `size` is provided and `axis=None`.<br>*   `unique_index` (optional): The indices of the first occurrence of each unique element in `x`. Only provided if `return_index` is `True`.<br>*   `unique_inverse` (optional): The indices to reconstruct the original array. Only provided if `return_inverse` is `True`.<br>*   `unique_counts` (optional): The number of occurrences of each unique value. Only provided if `return_counts` is `True`. |     |

#### Examples:

    x = keras.ops.convert_to_tensor([3, 1, 2, 1, 3, 2])

Fixed size output with padding (JIT-compatible):

    x = keras.ops.convert_to_tensor([3, 1, 2, 1])

Fixed size output with truncation:

    x = keras.ops.convert_to_tensor([3, 1, 2, 1])

Return unique rows of a 2D array:

    x = keras.ops.convert_to_tensor([[1, 0, 0], [0, 1, 0], [1, 0, 0]])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.