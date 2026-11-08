[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/experimental/Counter#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/experimental/Counter)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/experimental/Counter?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/experimental/Counter#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/experimental/Counter#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.data.experimental.Counter Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/experimental/Counter#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/experimental/Counter#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/counter.py#L62-L65)

Creates a `Dataset` that counts from `start` in steps of size `step`. (deprecated)

tf.compat.v1.data.experimental.Counter(
        start=0,
        step=1,
        dtype=tf.dtypes.int64
    )

Unlike [`tf.data.Dataset.range`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#range)
 which will stop at some ending number, `Counter` will produce elements indefinitely.

    dataset = tf.data.experimental.Counter().take(5)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `start` | (Optional.) The starting value for the counter. Defaults to 0. |
| `step` | (Optional.) The step size for the counter. Defaults to 1. |
| `dtype` | (Optional.) The data type for counter elements. Defaults to [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br>. |

|     |
| --- |
| Returns<br>------- |     |
| A `Dataset` of scalar `dtype` elements. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.