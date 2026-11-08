[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/unsorted_segment_mean#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/unsorted_segment_mean)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/unsorted_segment_mean?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/unsorted_segment_mean#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/unsorted_segment_mean#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.unsorted\_segment\_mean Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/unsorted_segment_mean#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/unsorted_segment_mean#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L4558-L4610)

Computes the mean along segments of a tensor.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.math.unsorted_segment_mean`](https://www.tensorflow.org/api_docs/python/tf/math/unsorted_segment_mean)
, [`tf.compat.v1.unsorted_segment_mean`](https://www.tensorflow.org/api_docs/python/tf/math/unsorted_segment_mean)

tf.math.unsorted_segment_mean(
        data, segment_ids, num_segments, name=None
    )

Read [the section on segmentation](https://www.tensorflow.org/versions/r2.0/api_docs/python/tf/math#about_segmentation)
 for an explanation of segments.

This operator is similar to the [`tf.math.unsorted_segment_sum`](https://www.tensorflow.org/api_docs/python/tf/math/unsorted_segment_sum)
 operator. Instead of computing the sum over segments, it computes the mean of all entries belonging to a segment such that:

outputi\=1/Ni∑j...data\[j...\] where the sum is over tuples `j...` such that `segment_ids[j...] == i` with \\N\_i\\ being the number of occurrences of id \\i\\.

If there is no entry for a given segment ID `i`, it outputs 0.

If the given segment ID `i` is negative, the value is dropped and will not be added to the sum of the segment.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `data` | A `Tensor` with floating point or complex dtype. |
| `segment_ids` | An integer tensor whose shape is a prefix of `data.shape`. The values must be less than `num_segments`. The values are always validated to be in range on CPU, never validated on GPU. |
| `num_segments` | An integer scalar `Tensor`. The number of distinct segment IDs. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has same shape as data, except for the first `segment_ids.rank` dimensions, which are replaced with a single dimension which has size `num_segments`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.