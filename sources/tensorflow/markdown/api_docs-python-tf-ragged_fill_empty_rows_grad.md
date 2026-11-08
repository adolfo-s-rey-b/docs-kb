[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/ragged_fill_empty_rows_grad#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/ragged_fill_empty_rows_grad)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/ragged_fill_empty_rows_grad?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fragged_fill_empty_rows_grad&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/ragged_fill_empty_rows_grad#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/ragged_fill_empty_rows_grad#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.ragged\_fill\_empty\_rows\_grad Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/ragged_fill_empty_rows_grad#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/ragged_fill_empty_rows_grad#returns)
    

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.ragged_fill_empty_rows_grad`](https://www.tensorflow.org/api_docs/python/tf/ragged_fill_empty_rows_grad)

tf.ragged_fill_empty_rows_grad(
        reverse_index_map: Annotated[Any, _atypes.Int64],
        grad_values: Annotated[Any, TV_RaggedFillEmptyRowsGrad_T],
        name=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `reverse_index_map` | A `Tensor` of type `int64`. |
| `grad_values` | A `Tensor`. |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| A tuple of `Tensor` objects (d\_values, d\_default\_value). |     |
| `d_values` | A `Tensor`. Has the same type as `grad_values`. |
| `d_default_value` | A `Tensor`. Has the same type as `grad_values`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.