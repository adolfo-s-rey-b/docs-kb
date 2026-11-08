[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/ragged/constant#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/ragged/constant)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/ragged/constant?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fragged%2Fconstant&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/ragged/constant#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/ragged/constant#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/ragged/constant#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/ragged/constant#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.ragged.constant Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/ragged/constant#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/ragged/constant#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/ragged/constant#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/ragged/constant#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_factory_ops.py#L36-L93)

Constructs a constant RaggedTensor from a nested Python list.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.ragged.constant`](https://www.tensorflow.org/api_docs/python/tf/ragged/constant)

tf.ragged.constant(
        pylist,
        dtype=None,
        ragged_rank=None,
        inner_shape=None,
        name=None,
        row_splits_dtype=tf.dtypes.int64
    ) -> Union[tf.RaggedTensor, ops._EagerTensorBase, tf.Operation]

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Ragged tensors](https://www.tensorflow.org/guide/ragged_tensor)<br>    <br>*   [Introduction to Tensors](https://www.tensorflow.org/guide/tensor) | *   [TF Lattice Aggregate Function Models](https://www.tensorflow.org/lattice/tutorials/aggregate_function_models)<br>    <br>*   [TF.Text Metrics](https://www.tensorflow.org/text/tutorials/text_similarity) |

#### Example:

    tf.ragged.constant([[1, 2], [3], [4, 5, 6]])

All scalar values in `pylist` must have the same nesting depth `K`, and the returned `RaggedTensor` will have rank `K`. If `pylist` contains no scalar values, then `K` is one greater than the maximum depth of empty lists in `pylist`. All scalar values in `pylist` must be compatible with `dtype`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `pylist` | A nested `list`, `tuple` or `np.ndarray`. Any nested element that is not a `list`, `tuple` or `np.ndarray` must be a scalar value compatible with `dtype`. |
| `dtype` | The type of elements for the returned `RaggedTensor`. If not specified, then a default is chosen based on the scalar values in `pylist`. If there are no scalar values in `pylist`, then the default is [`tf.float32`](https://www.tensorflow.org/api_docs/python/tf#float32)<br>. |
| `ragged_rank` | An integer specifying the ragged rank of the returned `RaggedTensor`. Must be nonnegative and less than `K`. Defaults to `max(0, K - 1)` if `inner_shape` is not specified. Defaults to \`max(0, K<br><br>*   1 - len(inner\_shape))`if`inner\_shape`is specified. </td> </tr><tr> <td>`inner\_shape`<a id="inner_shape"></a> </td> <td> A tuple of integers specifying the shape for individual inner values in the returned`RaggedTensor`. Defaults to`()`if`ragged\_rank`is not specified. If`ragged\_rank`is specified, then a default is chosen based on the contents of`pylist`. </td> </tr><tr> <td>`name`<a id="name"></a> </td> <td> A name prefix for the returned tensor (optional). </td> </tr><tr> <td>`row\_splits\_dtype`<a id="row_splits_dtype"></a> </td> <td> data type for the constructed`RaggedTensor\`'s row\_splits. One of [`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)<br>     or [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br>    . |

|     |
| --- |
| Returns<br>------- |     |
| A potentially ragged tensor with rank `K` and the specified `ragged_rank`, containing the values from `pylist`. |     |

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