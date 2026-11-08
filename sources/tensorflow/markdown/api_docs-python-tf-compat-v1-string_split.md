[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/string_split#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/string_split)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/string_split?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/string_split#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/string_split#raises)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/string_split#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.string\_split Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/string_split#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/string_split#raises)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/string_split#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_string_ops.py#L529-L589)

Split elements of `source` based on `delimiter`. (deprecated arguments)

tf.compat.v1.string_split(
        source,
        sep=None,
        skip_empty=True,
        delimiter=None,
        result_type='SparseTensor',
        name=None
    )

Let N be the size of `source` (typically N will be the batch size). Split each element of `source` based on `delimiter` and return a `SparseTensor` or `RaggedTensor` containing the split tokens. Empty tokens are ignored.

If `sep` is an empty string, each element of the `source` is split into individual strings, each containing one byte. (This includes splitting multibyte sequences of UTF-8.) If delimiter contains multiple bytes, it is treated as a set of delimiters with each considered a potential split point.

#### Examples:

    print(tf.compat.v1.string_split(['hello world', 'a b c']))

    print(tf.compat.v1.string_split(['hello world', 'a b c'],

|     |     |
| --- | --- |
| Args<br>---- |     |
| `source` | `1-D` string `Tensor`, the strings to split. |
| `sep` | `0-D` string `Tensor`, the delimiter character, the string should be length 0 or 1. Default is ' '. |
| `skip_empty` | A `bool`. If `True`, skip the empty strings from the result. |
| `delimiter` | deprecated alias for `sep`. |
| `result_type` | The tensor type for the result: one of `"RaggedTensor"` or `"SparseTensor"`. |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If delimiter is not a string. |

|     |
| --- |
| Returns<br>------- |     |
| A `SparseTensor` or `RaggedTensor` of rank `2`, the strings split according to the delimiter. The first column of the indices corresponds to the row in `source` and the second column corresponds to the index of the split component in this row. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.