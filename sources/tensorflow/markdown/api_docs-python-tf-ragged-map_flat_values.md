[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/ragged/map_flat_values#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/ragged/map_flat_values)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/ragged/map_flat_values?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/ragged/map_flat_values#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/ragged/map_flat_values#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/ragged/map_flat_values#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/ragged/map_flat_values#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.ragged.map\_flat\_values Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/ragged/map_flat_values#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/ragged/map_flat_values#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/ragged/map_flat_values#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/ragged/map_flat_values#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_functional_ops.py#L25-L136)

Applies `op` to the `flat_values` of one or more RaggedTensors.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.ragged.map_flat_values`](https://www.tensorflow.org/api_docs/python/tf/ragged/map_flat_values)

tf.ragged.map_flat_values(
        op, *args, **kwargs
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Ragged tensors](https://www.tensorflow.org/guide/ragged_tensor) |

Replaces any `RaggedTensor` in `args` or `kwargs` with its `flat_values` tensor (which collapses all ragged dimensions), and then calls `op`. Returns a `RaggedTensor` that is constructed from the input `RaggedTensor`s' `nested_row_splits` and the value returned by the `op`.

If the input arguments contain multiple `RaggedTensor`s, then they must have identical `nested_row_splits`.

This operation is generally used to apply elementwise operations to each value in a `RaggedTensor`.

#### Examples:

    rt = tf.ragged.constant([[1, 2, 3], [], [4, 5], [6]])

Example with a non-elementwise operation (note that `map_flat_values` and `map_fn` return different results):

    rt = tf.ragged.constant([[1.0, 3.0], [], [3.0, 6.0, 3.0]])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `op` | The operation that should be applied to the RaggedTensor `flat_values`. `op` is typically an element-wise operation (such as math\_ops.add), but any operation that preserves the size of the outermost dimension can be used. I.e., `shape[0]` of the value returned by `op` must match `shape[0]` of the `RaggedTensor`s' `flat_values` tensors. |
| `*args` | Arguments for `op`. |
| `**kwargs` | Keyword arguments for `op`. |

|     |
| --- |
| Returns<br>------- |     |
| A `RaggedTensor` whose `ragged_rank` matches the `ragged_rank` of all input `RaggedTensor`s. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If args contains no `RaggedTensors`, or if the `nested_splits` of the input `RaggedTensor`s are not identical. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.