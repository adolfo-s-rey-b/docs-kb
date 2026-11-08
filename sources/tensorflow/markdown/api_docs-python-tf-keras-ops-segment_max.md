[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/segment_max#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/segment_max)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/segment_max?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/segment_max#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/segment_max#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.segment\_max Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/segment_max#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/segment_max#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/math.py#L104-L135)

Computes the max of segments in a tensor.

tf.keras.ops.segment_max(
        data, segment_ids, num_segments=None, sorted=False
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `data` | Input tensor. |
| `segment_ids` | A N-D tensor containing segment indices for each element in `data`. data.shape\[:len(segment\_ids.shape)\] should match. |
| `num_segments` | An integer representing the total number of segments. If not specified, it is inferred from the maximum value in `segment_ids`. |
| `sorted` | A boolean indicating whether `segment_ids` is sorted. Defaults to `False`. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor containing the max of segments, where each element represents the max of the corresponding segment in `data`. |     |

#### Example:

    data = keras.ops.convert_to_tensor([1, 2, 10, 20, 100, 200])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.