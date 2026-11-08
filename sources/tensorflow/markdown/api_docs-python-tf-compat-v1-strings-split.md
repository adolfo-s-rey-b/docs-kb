[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/strings/split#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/strings/split)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/strings/split?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/strings/split#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/strings/split#raises)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/strings/split#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.strings.split Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/strings/split#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/strings/split#raises)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/strings/split#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_string_ops.py#L594-L658)

Split elements of `input` based on `sep`.

tf.compat.v1.strings.split(
        input=None,
        sep=None,
        maxsplit=-1,
        result_type='SparseTensor',
        source=None,
        name=None
    )

Let N be the size of `input` (typically N will be the batch size). Split each element of `input` based on `sep` and return a `SparseTensor` or `RaggedTensor` containing the split tokens. Empty tokens are ignored.

#### Examples:

    print(tf.compat.v1.strings.split(['hello world', 'a b c']))

    print(tf.compat.v1.strings.split(['hello world', 'a b c'],

If `sep` is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings. For example, `input` of `"1<>2<><>3"` and `sep` of `"<>"` returns `["1", "2", "", "3"]`. If `sep` is None or an empty string, consecutive whitespace are regarded as a single separator, and the result will contain no empty strings at the start or end if the string has leading or trailing whitespace.

Note that the above mentioned behavior matches python's str.split.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A string `Tensor` of rank `N`, the strings to split. If `rank(input)` is not known statically, then it is assumed to be `1`. |
| `sep` | `0-D` string `Tensor`, the delimiter character. |
| `maxsplit` | An `int`. If `maxsplit > 0`, limit of the split of the result. |
| `result_type` | The tensor type for the result: one of `"RaggedTensor"` or `"SparseTensor"`. |
| `source` | alias for "input" argument. |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If sep is not a string. |

|     |
| --- |
| Returns<br>------- |     |
| A `SparseTensor` or `RaggedTensor` of rank `N+1`, the strings split according to the delimiter. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.