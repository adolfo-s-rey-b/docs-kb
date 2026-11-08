[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/strings/bytes_split#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/strings/bytes_split)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/strings/bytes_split?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/strings/bytes_split#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/bytes_split#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/bytes_split#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.strings.bytes\_split Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/strings/bytes_split#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/bytes_split#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/bytes_split#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_string_ops.py#L40-L84)

Split string elements of `input` into bytes.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.strings.bytes_split`](https://www.tensorflow.org/api_docs/python/tf/strings/bytes_split)

tf.strings.bytes_split(
        input, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Introduction to Tensors](https://www.tensorflow.org/guide/tensor) | *   [Federated Learning for Text Generation](https://www.tensorflow.org/federated/tutorials/federated_learning_for_text_generation) |

#### Examples:

    tf.strings.bytes_split('hello').numpy()

Note that this op splits strings into bytes, not unicode characters. To split strings into unicode characters, use [`tf.strings.unicode_split`](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_split)
.

See also: [`tf.io.decode_raw`](https://www.tensorflow.org/api_docs/python/tf/io/decode_raw)
, [`tf.strings.split`](https://www.tensorflow.org/api_docs/python/tf/strings/split)
, [`tf.strings.unicode_split`](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_split)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A string `Tensor` or `RaggedTensor`: the strings to split. Must have a statically known rank (`N`). |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `RaggedTensor` of rank `N+1`: the bytes that make up the source strings. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.