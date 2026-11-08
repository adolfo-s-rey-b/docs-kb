[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/sparse/segment_mean#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/sparse/segment_mean)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/sparse/segment_mean?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/segment_mean#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/segment_mean#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.sparse.segment\_mean Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/segment_mean#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/segment_mean#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L5098-L5146)

Computes the mean along sparse segments of a tensor.

tf.sparse.segment_mean(
        data,
        indices,
        segment_ids,
        num_segments=None,
        name=None,
        sparse_gradient=False
    )

Read [the section on segmentation](https://www.tensorflow.org/versions/r2.0/api_docs/python/tf/math#about_segmentation)
 for an explanation of segments.

Like [`tf.math.segment_mean`](https://www.tensorflow.org/api_docs/python/tf/math/segment_mean)
, but `segment_ids` can have rank less than `data`'s first dimension, selecting a subset of dimension 0, specified by `indices`. `segment_ids` is allowed to have missing ids, in which case the output will be zeros at those indices. In those cases `num_segments` is used to determine the size of the output.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `data` | A `Tensor` with data that will be assembled in the output. |
| `indices` | A 1-D `Tensor` with indices into `data`. Has same rank as `segment_ids`. |
| `segment_ids` | A 1-D `Tensor` with indices into the output `Tensor`. Values should be sorted and can be repeated. |
| `num_segments` | An optional int32 scalar. Indicates the size of the output `Tensor`. |
| `name` | A name for the operation (optional). |
| `sparse_gradient` | An optional `bool`. Defaults to `False`. If `True`, the gradient of this function will be sparse (`IndexedSlices`) instead of dense (`Tensor`). The sparse gradient will contain one non-zero row for each unique index in `indices`. |

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