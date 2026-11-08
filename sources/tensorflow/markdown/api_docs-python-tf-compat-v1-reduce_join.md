[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_join#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_join)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_join?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_join#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_join#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.reduce\_join Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_join#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_join#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/string_ops.py#L305-L329)

Joins all strings into a single string, or joins along an axis.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.strings.reduce_join`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_join)

tf.compat.v1.reduce_join(
        inputs,
        axis=None,
        keep_dims=None,
        separator='',
        name=None,
        reduction_indices=None,
        keepdims=None
    )

This is the reduction operation for the elementwise [`tf.strings.join`](https://www.tensorflow.org/api_docs/python/tf/strings/join)
 op.

    tf.strings.reduce_join([['abc','123'],\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `inputs` | A [`tf.string`](https://www.tensorflow.org/api_docs/python/tf#string)<br> tensor. |\
| `axis` | Which axis to join along. The default behavior is to join all elements, producing a scalar. |\
| `keepdims` | If true, retains reduced dimensions with length 1. |\
| `separator` | a string added between each string being joined. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A [`tf.string`](https://www.tensorflow.org/api_docs/python/tf#string)<br> tensor. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.