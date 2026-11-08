[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/strings/format#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/strings/format)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/strings/format?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fstrings%2Fformat&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Example](https://www.tensorflow.org/api_docs/python/tf/strings/format#example)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/format#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/format#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/strings/format#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.strings.format Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Example](https://www.tensorflow.org/api_docs/python/tf/strings/format#example)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/format#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/format#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/strings/format#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/string_ops.py#L115-L176)

Formats a string template using a list of tensors.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.strings.format`](https://www.tensorflow.org/api_docs/python/tf/strings/format)

tf.strings.format(
        template, inputs, placeholder='{}', summarize=3, name=None
    )

Formats a string template using a list of tensors, abbreviating tensors by only printing the first and last `summarize` elements of each dimension (recursively). If formatting only one tensor into a template, the tensor does not have to be wrapped in a list.

|     |
| --- |
| Example<br>------- |     |
| Formatting a single-tensor template:<br><br>    tensor = tf.range(5)<br><br>Formatting a multi-tensor template:<br><br>    tensor_a = tf.range(2) |     |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `template` | A string template to format tensor values into. |
| `inputs` | A list of `Tensor` objects, or a single Tensor. The list of tensors to format into the template string. If a solitary tensor is passed in, the input tensor will automatically be wrapped as a list. |
| `placeholder` | An optional `string`. Defaults to `{}`. At each placeholder occurring in the template, a subsequent tensor will be inserted. |
| `summarize` | An optional `int`. Defaults to `3`. When formatting the tensors, show the first and last `summarize` entries of each tensor dimension (recursively). If set to -1, all elements of the tensor will be shown. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A scalar `Tensor` of type `string`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if the number of placeholders does not match the number of inputs. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.