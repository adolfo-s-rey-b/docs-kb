[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/logspace#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/logspace)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/logspace?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/logspace#args)
    
*   [Note](https://www.tensorflow.org/api_docs/python/tf/keras/ops/logspace#note)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/logspace#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.logspace Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/logspace#args)
    
*   [Note](https://www.tensorflow.org/api_docs/python/tf/keras/ops/logspace#note)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/logspace#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L5029-L5067)

Returns numbers spaced evenly on a log scale.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.logspace`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/logspace)

tf.keras.ops.logspace(
        start, stop, num=50, endpoint=True, base=10, dtype=None, axis=0
    )

In linear space, the sequence starts at `base ** start` and ends with `base ** stop` (see `endpoint` below).

|     |     |
| --- | --- |
| Args<br>---- |     |
| `start` | The starting value of the sequence. |
| `stop` | The final value of the sequence, unless `endpoint` is `False`. In that case, `num + 1` values are spaced over the interval in log-space, of which all but the last (a sequence of length `num`) are returned. |
| `num` | Number of samples to generate. Defaults to `50`. |
| `endpoint` | If `True`, `stop` is the last sample. Otherwise, it is not included. Defaults to `True`. |
| `base` | The base of the log space. Defaults to `10`. |
| `dtype` | The type of the output tensor. |
| `axis` | The axis in the result to store the samples. Relevant only if start or stop are array-like. |

|     |
| --- |
| Note<br>---- |     |
| Torch backend does not support `axis` argument. |     |

|     |
| --- |
| Returns<br>------- |     |
| A tensor of evenly spaced samples on a log scale. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.