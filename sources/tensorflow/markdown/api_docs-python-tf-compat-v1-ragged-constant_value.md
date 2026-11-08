[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/constant_value#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/constant_value)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/constant_value?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/constant_value#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/constant_value#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/constant_value#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.ragged.constant\_value Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/constant_value#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/constant_value#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/constant_value#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_factory_ops.py#L96-L162)

Constructs a RaggedTensorValue from a nested Python list.

tf.compat.v1.ragged.constant_value(
        pylist,
        dtype=None,
        ragged_rank=None,
        inner_shape=None,
        row_splits_dtype='int64'
    ) -> Union[tf.compat.v1.ragged.RaggedTensorValue, np.ndarray]

#### Example:

    tf.compat.v1.ragged.constant_value([[1, 2], [3], [4, 5, 6]])

All scalar values in `pylist` must have the same nesting depth `K`, and the returned `RaggedTensorValue` will have rank `K`. If `pylist` contains no scalar values, then `K` is one greater than the maximum depth of empty lists in `pylist`. All scalar values in `pylist` must be compatible with `dtype`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `pylist` | A nested `list`, `tuple` or `np.ndarray`. Any nested element that is not a `list` or `tuple` must be a scalar value compatible with `dtype`. |
| `dtype` | `numpy.dtype`. The type of elements for the returned `RaggedTensor`. If not specified, then a default is chosen based on the scalar values in `pylist`. |
| `ragged_rank` | An integer specifying the ragged rank of the returned `RaggedTensorValue`. Must be nonnegative and less than `K`. Defaults to `max(0, K - 1)` if `inner_shape` is not specified. Defaults to \`max(0, K<br><br>*   1 - len(inner\_shape))`if`inner\_shape`is specified. </td> </tr><tr> <td>`inner\_shape`<a id="inner_shape"></a> </td> <td> A tuple of integers specifying the shape for individual inner values in the returned`RaggedTensorValue`. Defaults to`()`if`ragged\_rank`is not specified. If`ragged\_rank`is specified, then a default is chosen based on the contents of`pylist`. </td> </tr><tr> <td>`row\_splits\_dtype`<a id="row_splits_dtype"></a> </td> <td> data type for the constructed`RaggedTensorValue`'s row_splits. One of`numpy.int32`or`numpy.int64\`. |

|     |
| --- |
| Returns<br>------- |     |
| A `tf.RaggedTensorValue` or [`numpy.array`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/array)<br> with rank `K` and the specified `ragged_rank`, containing the values from `pylist`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If the scalar values in `pylist` have inconsistent nesting depth; or if ragged\_rank or inner\_shape are incompatible with `pylist`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.