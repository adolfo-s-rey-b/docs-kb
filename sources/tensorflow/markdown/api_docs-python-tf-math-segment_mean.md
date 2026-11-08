[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/segment_mean#main-content)

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
    

tf.math.segment\_mean Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

Computes the mean along segments of a tensor.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.math.segment_mean`](https://www.tensorflow.org/api_docs/python/tf/math/segment_mean)
, [`tf.compat.v1.segment_mean`](https://www.tensorflow.org/api_docs/python/tf/math/segment_mean)

tf.math.segment_mean(
        data: Annotated[Any, tf.raw_ops.Any],
        segment_ids: Annotated[Any, tf.raw_ops.Any],
        name=None
    ) -> Annotated[Any, tf.raw_ops.Any]

Read [the section on segmentation](https://tensorflow.org/api_docs/python/tf/math#Segmentation)
 for an explanation of segments.

Computes a tensor such that \\(output\_i = \\frac{\\sum\_j data\_j}{N}\\) where `mean` is over `j` such that `segment_ids[j] == i` and `N` is the total number of values summed.

If the mean is empty for a given segment ID `i`, `output[i] = 0`.

![](https://www.tensorflow.org/images/SegmentMean.png)

#### For example:

    c = tf.constant([[1.0,2,3,4], [4, 3, 2, 1], [5,6,7,8]])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `data` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`. |
| `segment_ids` | A `Tensor`. Must be one of the following types: `int32`, `int64`. A 1-D tensor whose size is equal to the size of `data`'s first dimension. Values should be sorted and can be repeated. |
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