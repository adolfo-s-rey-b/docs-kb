[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/sparse/fill_empty_rows#main-content)

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
    

tf.sparse.fill\_empty\_rows Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/sparse_ops.py#L2109-L2173)

Fills empty rows in the input 2-D `SparseTensor` with a default value.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.sparse.fill_empty_rows`](https://www.tensorflow.org/api_docs/python/tf/sparse/fill_empty_rows)
, [`tf.compat.v1.sparse_fill_empty_rows`](https://www.tensorflow.org/api_docs/python/tf/sparse/fill_empty_rows)

tf.sparse.fill_empty_rows(
        sp_input, default_value, name=None
    )

This op adds entries with the specified `default_value` at index `[row, 0]` for any row in the input that does not already have a value.

For example, suppose `sp_input` has shape `[5, 6]` and non-empty values:

[0, 1]: a
    [0, 3]: b
    [2, 0]: c
    [3, 1]: d

Rows 1 and 4 are empty, so the output will be of shape `[5, 6]` with values:

[0, 1]: a
    [0, 3]: b
    [1, 0]: default_value
    [2, 0]: c
    [3, 1]: d
    [4, 0]: default_value

Note that the input may have empty columns at the end, with no effect on this op.

The output `SparseTensor` will be in row-major order and will have the same shape as the input.

This op also returns an indicator vector such that

empty_row_indicator[i] = True iff row i was an empty row.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `sp_input` | A `SparseTensor` with shape `[N, M]`. |
| `default_value` | The value to fill for empty rows, with the same type as `sp_input.` |
| `name` | A name prefix for the returned tensors (optional) |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `sp_ordered_output` | A `SparseTensor` with shape `[N, M]`, and with all empty rows filled in with `default_value`. |
| `empty_row_indicator` | A bool vector of length `N` indicating whether each input row was empty. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If `sp_input` is not a `SparseTensor`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.