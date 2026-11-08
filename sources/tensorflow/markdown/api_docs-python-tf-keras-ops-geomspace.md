[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/geomspace#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/geomspace)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/geomspace?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fops%2Fgeomspace&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/geomspace#args)
    
*   [Note](https://www.tensorflow.org/api_docs/python/tf/keras/ops/geomspace#note)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/geomspace#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.geomspace Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/geomspace#args)
    
*   [Note](https://www.tensorflow.org/api_docs/python/tf/keras/ops/geomspace#note)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/geomspace#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L3860-L3897)

Returns numbers spaced evenly on a log scale (a geometric progression).

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.geomspace`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/geomspace)

tf.keras.ops.geomspace(
        start, stop, num=50, endpoint=True, dtype=None, axis=0
    )

This is similar to `logspace`, but with endpoints specified directly instead of as logarithms. Each output sample is a constant multiple of the previous.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `start` | The starting value of the sequence. |
| `stop` | The final value of the sequence, unless `endpoint` is `False`. In that case, `num + 1` values are spaced over the interval in log-space, of which all but the last (a sequence of length `num`) are returned. |
| `num` | Number of samples to generate. Defaults to `50`. |
| `endpoint` | If `True`, `stop` is the last sample. Otherwise, it is not included. Defaults to `True`. |
| `dtype` | The type of the output tensor. |
| `axis` | The axis in the result to store the samples. Relevant only if start or stop are array-like. |

|     |
| --- |
| Note<br>---- |     |
| Torch backend does not support `axis` argument. |     |

|     |
| --- |
| Returns<br>------- |     |
| A tensor of `num` samples, evenly spaced on a log scale. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.