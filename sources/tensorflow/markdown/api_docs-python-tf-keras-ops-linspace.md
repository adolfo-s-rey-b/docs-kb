[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/linspace#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/linspace)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/linspace?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/linspace#args)
    
*   [Note](https://www.tensorflow.org/api_docs/python/tf/keras/ops/linspace#note)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/linspace#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.linspace Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/linspace#args)
    
*   [Note](https://www.tensorflow.org/api_docs/python/tf/keras/ops/linspace#note)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/linspace#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4655-L4699)

Return evenly spaced numbers over a specified interval.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.linspace`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/linspace)

tf.keras.ops.linspace(
        start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0
    )

Returns `num` evenly spaced samples, calculated over the interval `[start, stop]`.

The endpoint of the interval can optionally be excluded.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `start` | The starting value of the sequence. |
| `stop` | The end value of the sequence, unless `endpoint` is set to `False`. In that case, the sequence consists of all but the last of `num + 1` evenly spaced samples, so that `stop` is excluded. Note that the step size changes when `endpoint` is `False`. |
| `num` | Number of samples to generate. Defaults to `50`. Must be non-negative. |
| `endpoint` | If `True`, `stop` is the last sample. Otherwise, it is not included. Defaults to `True`. |
| `retstep` | If `True`, return `(samples, step)`, where `step` is the spacing between samples. |
| `dtype` | The type of the output tensor. |
| `axis` | The axis in the result to store the samples. Relevant only if start or stop are array-like. Defaults to `0`. |

|     |
| --- |
| Note<br>---- |     |
| Torch backend does not support `axis` argument. |     |

|     |
| --- |
| Returns<br>------- |     |
| A tensor of evenly spaced numbers. If `retstep` is `True`, returns `(samples, step)` |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.