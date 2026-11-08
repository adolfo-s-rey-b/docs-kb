[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_segment_sqrt_n#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_segment_sqrt_n)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_segment_sqrt_n?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fsparse_segment_sqrt_n&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_segment_sqrt_n#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_segment_sqrt_n#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.sparse\_segment\_sqrt\_n Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_segment_sqrt_n#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_segment_sqrt_n#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L5149-L5197)

Computes the sum along sparse segments of a tensor divided by the sqrt(N).

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.sparse.segment_sqrt_n`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_segment_sqrt_n)

tf.compat.v1.sparse_segment_sqrt_n(
        data,
        indices,
        segment_ids,
        name=None,
        num_segments=None,
        sparse_gradient=False
    )

`N` is the size of the segment being reduced.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `data` | A `Tensor` with data that will be assembled in the output. |
| `indices` | A 1-D `Tensor` with indices into `data`. Has same rank as `segment_ids`. |
| `segment_ids` | A 1-D `Tensor` with indices into the output `Tensor`. Values should be sorted and can be repeated. |
| `name` | A name for the operation (optional). |
| `num_segments` | An optional int32 scalar. Indicates the size of the output `Tensor`. |
| `sparse_gradient` | An optional `bool`. Defaults to `False`. If `True`, the gradient of this function will be sparse (IndexedSlices) instead of dense (Tensor). |

|     |
| --- |
| Returns<br>------- |     |
| A `tensor` of the shape as data, except for dimension 0 which has size `k`, the number of segments specified via `num_segments` or inferred for the last element in `segments_ids`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.