[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/ragged/segment_ids_to_row_splits#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/ragged/segment_ids_to_row_splits)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/ragged/segment_ids_to_row_splits?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fragged%2Fsegment_ids_to_row_splits&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/ragged/segment_ids_to_row_splits#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/ragged/segment_ids_to_row_splits#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Was this helpful?

tf.ragged.segment\_ids\_to\_row\_splits Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/ragged/segment_ids_to_row_splits#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/ragged/segment_ids_to_row_splits#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/segment_id_ops.py#L75-L134)

Generates the RaggedTensor `row_splits` corresponding to a segmentation.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.ragged.segment_ids_to_row_splits`](https://www.tensorflow.org/api_docs/python/tf/ragged/segment_ids_to_row_splits)

tf.ragged.segment_ids_to_row_splits(
        segment_ids, num_segments=None, out_type=None, name=None
    )

Returns an integer vector `splits`, where `splits[0] = 0` and `splits[i] = splits[i-1] + count(segment_ids==i)`. Example:

    print(tf.ragged.segment_ids_to_row_splits([0, 0, 0, 2, 2, 3, 4, 4, 4]))

|     |     |
| --- | --- |
| Args<br>---- |     |
| `segment_ids` | A 1-D integer Tensor. |
| `num_segments` | A scalar integer indicating the number of segments. Defaults to `max(segment_ids) + 1` (or zero if `segment_ids` is empty). |
| `out_type` | The dtype for the return value. Defaults to `segment_ids.dtype`, or [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> if `segment_ids` does not have a dtype. |
| `name` | A name prefix for the returned tensor (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A sorted 1-D integer Tensor, with `shape=[num_segments + 1]`. |     |

Was this helpful?

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.