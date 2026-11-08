[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/unsorted_segment_min#main-content)

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
    

tf.math.unsorted\_segment\_min Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

Computes the minimum along segments of a tensor.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.math.unsorted_segment_min`](https://www.tensorflow.org/api_docs/python/tf/math/unsorted_segment_min)
, [`tf.compat.v1.unsorted_segment_min`](https://www.tensorflow.org/api_docs/python/tf/math/unsorted_segment_min)

tf.math.unsorted_segment_min(
        data: Annotated[Any, tf.raw_ops.Any],
        segment_ids: Annotated[Any, tf.raw_ops.Any],
        num_segments: Annotated[Any, tf.raw_ops.Any],
        name=None
    ) -> Annotated[Any, tf.raw_ops.Any]

Read [the section on segmentation](https://tensorflow.org/api_docs/python/tf/math#Segmentation)
 for an explanation of segments.

This operator is similar to [`tf.math.unsorted_segment_sum`](https://www.tensorflow.org/api_docs/python/tf/math/unsorted_segment_sum)
, Instead of computing the sum over segments, it computes the minimum such that:

\\(output\_i = \\min\_{j...} data\_\[j...\]\\) where min is over tuples `j...` such that `segment_ids[j...] == i`.

If the minimum is empty for a given segment ID `i`, it outputs the largest possible value for the specific numeric type, `output[i] = numeric_limits<T>::max()`.

#### For example:

    c = tf.constant([[1,2,3,4], [5,6,7,8], [4,3,2,1]])

If the given segment ID `i` is negative, then the corresponding value is dropped, and will not be included in the result.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `data` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`. |
| `segment_ids` | A `Tensor`. Must be one of the following types: `int32`, `int64`. A tensor whose shape is a prefix of `data.shape`. The values must be less than `num_segments`. |
| `num_segments` | A `Tensor`. Must be one of the following types: `int32`, `int64`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `data`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.