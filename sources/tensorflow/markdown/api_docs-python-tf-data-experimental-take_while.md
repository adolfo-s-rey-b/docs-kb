[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/take_while#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/take_while)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/take_while?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/take_while#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/take_while#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.take\_while Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/take_while#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/take_while#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/take_while_ops.py#L20-L38)

A transformation that stops dataset iteration based on a `predicate`. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.take_while`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/take_while)

tf.data.experimental.take_while(
        predicate
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `predicate` | A function that maps a nested structure of tensors (having shapes and types defined by `self.output_shapes` and `self.output_types`) to a scalar [`tf.bool`](https://www.tensorflow.org/api_docs/python/tf#bool)<br> tensor. |

|     |
| --- |
| Returns<br>------- |     |
| A `Dataset` transformation function, which can be passed to [`tf.data.Dataset.apply`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#apply)<br>. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.