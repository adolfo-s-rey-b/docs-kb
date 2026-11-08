[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_split_with_offsets#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_split_with_offsets)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_split_with_offsets?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_split_with_offsets#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_split_with_offsets#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.strings.unicode\_split\_with\_offsets Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_split_with_offsets#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_split_with_offsets#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_string_ops.py#L343-L406)

Splits each string into a sequence of code points with start offsets.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.strings.unicode_split_with_offsets`](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_split_with_offsets)

tf.strings.unicode_split_with_offsets(
        input,
        input_encoding,
        errors='replace',
        replacement_char=65533,
        name=None
    )

This op is similar to `tf.strings.decode(...)`, but it also returns the start offset for each character in its respective string. This information can be used to align the characters with the original byte sequence.

Returns a tuple `(chars, start_offsets)` where:

*   `chars[i1...iN, j]` is the substring of `input[i1...iN]` that encodes its `j`th character, when decoded using `input_encoding`.
*   `start_offsets[i1...iN, j]` is the start byte offset for the `j`th character in `input[i1...iN]`, when decoded using `input_encoding`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | An `N` dimensional potentially ragged `string` tensor with shape `[D1...DN]`. `N` must be statically known. |
| `input_encoding` | String name for the unicode encoding that should be used to decode each string. |
| `errors` | Specifies the response when an input string can't be converted using the indicated encoding. One of:<br><br>*   `'strict'`: Raise an exception for any illegal substrings.<br>*   `'replace'`: Replace illegal substrings with `replacement_char`.<br>*   `'ignore'`: Skip illegal substrings. |
| `replacement_char` | The replacement codepoint to be used in place of invalid substrings in `input` when `errors='replace'`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A tuple of `N+1` dimensional tensors `(codepoints, start_offsets)`.<br><br>*   `codepoints` is an `int32` tensor with shape `[D1...DN, (num_chars)]`.<br>*   `offsets` is an `int64` tensor with shape `[D1...DN, (num_chars)]`.<br><br>The returned tensors are [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>s if `input` is a scalar, or [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)<br>s otherwise. |     |

#### Example:

    input = [s.encode('utf8') for s in (u'G\xf6\xf6dnight', u'\U0001f60a')]

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.