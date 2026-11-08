[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/strings/substr#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/strings/substr)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/strings/substr?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/strings/substr#used-in-the-notebooks)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/strings/substr#raises)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/substr#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/substr#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.strings.substr Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/strings/substr#used-in-the-notebooks)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/strings/substr#raises)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/substr#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/substr#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/string_ops.py#L441-L445)

Return substrings from `Tensor` of strings.

tf.strings.substr(
        input, pos, len, unit='BYTE', name=None
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [tf.data: Build TensorFlow input pipelines](https://www.tensorflow.org/guide/data)<br>    <br>*   [Ragged tensors](https://www.tensorflow.org/guide/ragged_tensor)<br>    <br>*   [Unicode strings](https://www.tensorflow.org/text/guide/unicode) |

For each string in the input `Tensor`, creates a substring starting at index `pos` with a total length of `len`.

If `len` defines a substring that would extend beyond the length of the input string, or if `len` is negative, then as many characters as possible are used.

A negative `pos` indicates distance within the string backwards from the end.

If `pos` specifies an index which is out of range for any of the input strings, then an `InvalidArgumentError` is thrown.

`pos` and `len` must have the same shape, otherwise a `ValueError` is thrown on Op creation.

* * *

Examples

Using scalar `pos` and `len`:

input = [b'Hello', b'World']
    position = 1
    length = 3
    
    output = [b'ell', b'orl']

Using `pos` and `len` with same shape as `input`:

input = [[b'ten', b'eleven', b'twelve'],\
             [b'thirteen', b'fourteen', b'fifteen'],\
             [b'sixteen', b'seventeen', b'eighteen']]
    position = [[1, 2, 3],\
                [1, 2, 3],\
                [1, 2, 3]]
    length =   [[2, 3, 4],\
                [4, 3, 2],\
                [5, 5, 5]]
    
    output = [[b'en', b'eve', b'lve'],\
              [b'hirt', b'urt', b'te'],\
              [b'ixtee', b'vente', b'hteen']]

Broadcasting `pos` and `len` onto `input`:

input = [[b'ten', b'eleven', b'twelve'],\
             [b'thirteen', b'fourteen', b'fifteen'],\
             [b'sixteen', b'seventeen', b'eighteen'],\
             [b'nineteen', b'twenty', b'twentyone']]
    position = [1, 2, 3]
    length =   [1, 2, 3]
    
    output = [[b'e', b'ev', b'lve'],\
              [b'h', b'ur', b'tee'],\
              [b'i', b've', b'hte'],\
              [b'i', b'en', b'nty']]

Broadcasting `input` onto `pos` and `len`:

input = b'thirteen'
    position = [1, 5, 7]
    length =   [3, 2, 1]
    
    output = [b'hir', b'ee', b'n']

|     |
| --- |
| Raises<br>------ |     |
| *   `ValueError`: If the first argument cannot be converted to a Tensor of `dtype string`.<br>*   `InvalidArgumentError`: If indices are out of range.<br>*   `ValueError`: If `pos` and `len` are not the same shape. |     |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor` of type `string`. Tensor of strings |
| `pos` | A `Tensor`. Must be one of the following types: `int32`, `int64`. Scalar defining the position of first character in each substring |
| `len` | A `Tensor`. Must have the same type as `pos`. Scalar defining the number of characters to include in each substring |
| `unit` | An optional `string` from: `"BYTE", "UTF8_CHAR"`. Defaults to `"BYTE"`. The unit that is used to create the substring. One of: `"BYTE"` (for defining position and length by bytes) or `"UTF8_CHAR"` (for the UTF-8 encoded Unicode code points). The default is `"BYTE"`. Results are undefined if `unit=UTF8_CHAR` and the `input` strings do not contain structurally valid UTF-8. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `string`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.