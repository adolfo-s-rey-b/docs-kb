[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/signal/vorbis_window#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/signal/vorbis_window)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/signal/vorbis_window?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/signal/vorbis_window#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/signal/vorbis_window#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.signal.vorbis\_window Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/signal/vorbis_window#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/signal/vorbis_window#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/signal/window_ops.py#L120-L142)

Generate a [Vorbis power complementary window](https://en.wikipedia.org/wiki/Modified_discrete_cosine_transform#Window_functions)
.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.signal.vorbis_window`](https://www.tensorflow.org/api_docs/python/tf/signal/vorbis_window)

tf.signal.vorbis_window(
        window_length,
        dtype=tf.dtypes.float32,
        name=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `window_length` | A scalar `Tensor` indicating the window length to generate. |
| `dtype` | The data type to produce. Must be a floating point type. |
| `name` | An optional name for the operation. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of shape `[window_length]` of type `dtype`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.