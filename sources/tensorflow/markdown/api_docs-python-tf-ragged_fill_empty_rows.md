[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/ragged_fill_empty_rows#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/ragged_fill_empty_rows)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/ragged_fill_empty_rows?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/ragged_fill_empty_rows#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/ragged_fill_empty_rows#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.ragged\_fill\_empty\_rows Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/ragged_fill_empty_rows#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/ragged_fill_empty_rows#returns)
    

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.ragged_fill_empty_rows`](https://www.tensorflow.org/api_docs/python/tf/ragged_fill_empty_rows)

tf.ragged_fill_empty_rows(
        value_rowids: Annotated[Any, _atypes.Int64],
        values: Annotated[Any, TV_RaggedFillEmptyRows_T],
        nrows: Annotated[Any, _atypes.Int64],
        default_value: Annotated[Any, TV_RaggedFillEmptyRows_T],
        name=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `value_rowids` | A `Tensor` of type `int64`. |
| `values` | A `Tensor`. |
| `nrows` | A `Tensor` of type `int64`. |
| `default_value` | A `Tensor`. Must have the same type as `values`. |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| A tuple of `Tensor` objects (output\_value\_rowids, output\_values, empty\_row\_indicator, reverse\_index\_map). |     |
| `output_value_rowids` | A `Tensor` of type `int64`. |
| `output_values` | A `Tensor`. Has the same type as `values`. |
| `empty_row_indicator` | A `Tensor` of type `bool`. |
| `reverse_index_map` | A `Tensor` of type `int64`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.