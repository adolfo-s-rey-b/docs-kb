Loading \[MathJax\]/jax/element/mml/optable/BasicLatin.js

[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/unsorted_segment_max#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/unsorted_segment_max)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/unsorted_segment_max?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fmath%2Funsorted_segment_max&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/unsorted_segment_max#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/unsorted_segment_max#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.unsorted\_segment\_max Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/unsorted_segment_max#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/unsorted_segment_max#returns)
    

Computes the maximum along segments of a tensor.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.math.unsorted_segment_max`](https://www.tensorflow.org/api_docs/python/tf/math/unsorted_segment_max)
, [`tf.compat.v1.unsorted_segment_max`](https://www.tensorflow.org/api_docs/python/tf/math/unsorted_segment_max)

tf.math.unsorted_segment_max(
        data: Annotated[Any, tf.raw_ops.Any],
        segment_ids: Annotated[Any, tf.raw_ops.Any],
        num_segments: Annotated[Any, tf.raw_ops.Any],
        name=None
    ) -> Annotated[Any, tf.raw_ops.Any]

Read [the section on segmentation](https://tensorflow.org/api_docs/python/tf/math#Segmentation)
 for an explanation of segments.

This operator is similar to [`tf.math.unsorted_segment_sum`](https://www.tensorflow.org/api_docs/python/tf/math/unsorted_segment_sum)
, Instead of computing the sum over segments, it computes the maximum such that:

outputi\=max where max is over tuples `j...` such that `segment_ids[j...] == i`.

If the maximum is empty for a given segment ID `i`, it outputs the smallest possible value for the specific numeric type, `output[i] = numeric_limits<T>::lowest()`.

If the given segment ID `i` is negative, then the corresponding value is dropped, and will not be included in the result.

![](https://www.tensorflow.org/images/UnsortedSegmentMax.png)

#### For example:

    c = tf.constant([[1,2,3,4], [5,6,7,8], [4,3,2,1]])

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