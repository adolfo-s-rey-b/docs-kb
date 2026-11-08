[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/ragged/row_splits_to_segment_ids#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/ragged/row_splits_to_segment_ids)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/ragged/row_splits_to_segment_ids?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fragged%2Frow_splits_to_segment_ids&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/ragged/row_splits_to_segment_ids#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/ragged/row_splits_to_segment_ids#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/ragged/row_splits_to_segment_ids#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.ragged.row\_splits\_to\_segment\_ids Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/ragged/row_splits_to_segment_ids#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/ragged/row_splits_to_segment_ids#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/ragged/row_splits_to_segment_ids#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/segment_id_ops.py#L31-L70)

Generates the segmentation corresponding to a RaggedTensor `row_splits`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.ragged.row_splits_to_segment_ids`](https://www.tensorflow.org/api_docs/python/tf/ragged/row_splits_to_segment_ids)

tf.ragged.row_splits_to_segment_ids(
        splits, name=None, out_type=None
    )

Returns an integer vector `segment_ids`, where `segment_ids[i] == j` if `splits[j] <= i < splits[j+1]`. Example:

    print(tf.ragged.row_splits_to_segment_ids([0, 3, 3, 5, 6, 9]))

|     |     |
| --- | --- |
| Args<br>---- |     |
| `splits` | A sorted 1-D integer Tensor. `splits[0]` must be zero. |
| `name` | A name prefix for the returned tensor (optional). |
| `out_type` | The dtype for the return value. Defaults to `splits.dtype`, or [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> if `splits` does not have a dtype. |

|     |
| --- |
| Returns<br>------- |     |
| A sorted 1-D integer Tensor, with `shape=[splits[-1]]` |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `splits` is invalid. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.