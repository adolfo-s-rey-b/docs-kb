[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_encode#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_encode)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_encode?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_encode#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_encode#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_encode#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.strings.unicode\_encode Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_encode#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_encode#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_encode#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_string_ops.py#L88-L183)

Encodes each sequence of Unicode code points in `input` into a string.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.strings.unicode_encode`](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_encode)

tf.strings.unicode_encode(
        input,
        output_encoding,
        errors='replace',
        replacement_char=65533,
        name=None
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Unicode strings](https://www.tensorflow.org/text/guide/unicode)<br>    <br>*   [Tokenizing with TF Text](https://www.tensorflow.org/text/guide/tokenizers) |

`result[i1...iN]` is the string formed by concatenating the Unicode codepoints `input[1...iN, :]`, encoded using `output_encoding`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | An `N+1` dimensional potentially ragged integer tensor with shape `[D1...DN, num_chars]`. |
| `output_encoding` | Unicode encoding that should be used to encode each code point sequence. Can be `"UTF-8"`, `"UTF-16-BE"`, or `"UTF-32-BE"`. |
| `errors` | Specifies the response when a code point that is not a [Unicode scalar value](https://www.unicode.org/glossary/#unicode_scalar_value)<br> is encountered (optional). One of:<br><br>  * `'replace'`: Replace non-scalar-value with the<br>        `replacement_char`. (default)<br>      * `'ignore'`: Skip non-scalar-value .<br>      * `'strict'`: Raise an exception for any non-scalar-value. |
| `replacement_char` | The replacement character to be used in place of any invalid input when `errors='replace'`. Any Unicode scalar value may be used. The default value is the default Unicode replacement character which is 0xFFFD (U+65533). |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `N` dimensional `string` tensor with shape `[D1...DN]`. |     |

#### Example:

    input = tf.ragged.constant(

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.