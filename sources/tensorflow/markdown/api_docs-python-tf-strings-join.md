[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/strings/join#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/strings/join)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/strings/join?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/strings/join#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/join#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/join#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.strings.join Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/strings/join#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/join#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/join#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/string_ops.py#L551-L583)

Perform element-wise concatenation of a list of string tensors.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.string_join`](https://www.tensorflow.org/api_docs/python/tf/strings/join)
, [`tf.compat.v1.strings.join`](https://www.tensorflow.org/api_docs/python/tf/strings/join)

tf.strings.join(
        inputs, separator='', name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Ragged tensors](https://www.tensorflow.org/guide/ragged_tensor) | *   [Text generation with an RNN](https://www.tensorflow.org/text/tutorials/text_generation)<br>    <br>*   [Sending Different Data To Particular Clients With federated\_language.federated\_select](https://www.tensorflow.org/federated/tutorials/federated_select)<br>    <br>*   [Image captioning with visual attention](https://www.tensorflow.org/text/tutorials/image_captioning)<br>    <br>*   [Neural machine translation with attention](https://www.tensorflow.org/text/tutorials/nmt_with_attention) |

Given a list of string tensors of same shape, performs element-wise concatenation of the strings of the same index in all tensors.

    tf.strings.join(['abc','def']).numpy()

The reduction version of this elementwise operation is [`tf.strings.reduce_join`](https://www.tensorflow.org/api_docs/python/tf/strings/reduce_join)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `inputs` | A list of [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> objects of same size and [`tf.string`](https://www.tensorflow.org/api_docs/python/tf#string)<br> dtype. |
| `separator` | A string added between each string being joined. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A [`tf.string`](https://www.tensorflow.org/api_docs/python/tf#string)<br> tensor. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.