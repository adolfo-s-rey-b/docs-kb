[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/string_to_number#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.string\_to\_number Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/string_ops.py#L491-L500)

Converts each string in the input Tensor to the specified numeric type.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.strings.to_number`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/string_to_number)

tf.compat.v1.string_to_number(
        string_tensor=None,
        out_type=tf.dtypes.float32,
        name=None,
        input=None
    )

(Note that int32 overflow results in an error while float overflow results in a rounded value.)

#### Example:

    strings = ["5.0", "3.0", "7.0"]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `string_tensor` | A `Tensor` of type `string`. |
| `out_type` | An optional [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br> from: `tf.float32, tf.float64, tf.int32, tf.int64, tf.uint32, tf.uint64`. Defaults to [`tf.float32`](https://www.tensorflow.org/api_docs/python/tf#float32)<br>. The numeric type to interpret each string in `string_tensor` as. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `out_type`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.