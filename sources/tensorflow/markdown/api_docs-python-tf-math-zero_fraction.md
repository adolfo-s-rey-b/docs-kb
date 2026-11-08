[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/zero_fraction#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/zero_fraction)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/zero_fraction?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/zero_fraction#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/zero_fraction#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.zero\_fraction Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/zero_fraction#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/zero_fraction#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_impl.py#L621-L660)

Returns the fraction of zeros in `value`.

#### View aliases

**Main aliases**

[`tf.nn.zero_fraction`](https://www.tensorflow.org/api_docs/python/tf/math/zero_fraction)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.math.zero_fraction`](https://www.tensorflow.org/api_docs/python/tf/math/zero_fraction)
, [`tf.compat.v1.nn.zero_fraction`](https://www.tensorflow.org/api_docs/python/tf/math/zero_fraction)

tf.math.zero_fraction(
        value, name=None
    )

If `value` is empty, the result is `nan`.

This is useful in summaries to measure and report sparsity. For example,

    z = tf.nn.relu(...)
        summ = tf.compat.v1.summary.scalar('sparsity', tf.nn.zero_fraction(z))

|     |     |
| --- | --- |
| Args<br>---- |     |
| `value` | A tensor of numeric type. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| The fraction of zeros in `value`, with type `float32`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.