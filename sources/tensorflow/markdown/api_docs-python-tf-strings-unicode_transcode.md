[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_transcode#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_transcode)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_transcode?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fstrings%2Funicode_transcode&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_transcode#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_transcode#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_transcode#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.strings.unicode\_transcode Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_transcode#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_transcode#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_transcode#returns)
    

Transcode the input text from a source encoding to a destination encoding.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.strings.unicode_transcode`](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_transcode)

tf.strings.unicode_transcode(
        input: Annotated[Any, _atypes.String],
        input_encoding: str,
        output_encoding: str,
        errors: str = 'replace',
        replacement_char: int = 65533,
        replace_control_characters: bool = False,
        name=None
    ) -> Annotated[Any, _atypes.String]

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Unicode strings](https://www.tensorflow.org/text/guide/unicode) |

The input is a string tensor of any shape. The output is a string tensor of the same shape containing the transcoded strings. Output strings are always valid unicode. If the input contains invalid encoding positions, the `errors` attribute sets the policy for how to deal with them. If the default error-handling policy is used, invalid formatting will be substituted in the output by the `replacement_char`. If the errors policy is to `ignore`, any invalid encoding positions in the input are skipped and not included in the output. If it set to `strict` then any invalid formatting will result in an InvalidArgument error.

This operation can be used with `output_encoding = input_encoding` to enforce correct formatting for inputs even if they are already in the desired encoding.

If the input is prefixed by a Byte Order Mark needed to determine encoding (e.g. if the encoding is UTF-16 and the BOM indicates big-endian), then that BOM will be consumed and not emitted into the output. If the input encoding is marked with an explicit endianness (e.g. UTF-16-BE), then the BOM is interpreted as a non-breaking-space and is preserved in the output (including always for UTF-8).

The end result is that if the input is marked as an explicit endianness the transcoding is faithful to all codepoints in the source. If it is not marked with an explicit endianness, the BOM is not considered part of the string itself but as metadata, and so is not preserved in the output.

#### Examples:

    tf.strings.unicode_transcode(["Hello", "TensorFlow", "2.x"], "UTF-8", "UTF-16-BE")

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor` of type `string`. The text to be processed. Can have any shape. |
| `input_encoding` | A `string`. Text encoding of the input strings. This is any of the encodings supported by ICU ucnv algorithmic converters. Examples: `"UTF-16", "US ASCII", "UTF-8"`. |
| `output_encoding` | A `string` from: `"UTF-8", "UTF-16-BE", "UTF-32-BE"`. The unicode encoding to use in the output. Must be one of `"UTF-8", "UTF-16-BE", "UTF-32-BE"`. Multi-byte encodings will be big-endian. |
| `errors` | An optional `string` from: `"strict", "replace", "ignore"`. Defaults to `"replace"`. Error handling policy when there is invalid formatting found in the input. The value of 'strict' will cause the operation to produce a InvalidArgument error on any invalid input formatting. A value of 'replace' (the default) will cause the operation to replace any invalid formatting in the input with the `replacement_char` codepoint. A value of 'ignore' will cause the operation to skip any invalid formatting in the input and produce no corresponding output character. |
| `replacement_char` | An optional `int`. Defaults to `65533`. The replacement character codepoint to be used in place of any invalid formatting in the input when `errors='replace'`. Any valid unicode codepoint may be used. The default value is the default unicode replacement character is 0xFFFD or U+65533.)<br><br>Note that for UTF-8, passing a replacement character expressible in 1 byte, such as ' ', will preserve string alignment to the source since invalid bytes will be replaced with a 1-byte replacement. For UTF-16-BE and UTF-16-LE, any 1 or 2 byte replacement character will preserve byte alignment to the source. |
| `replace_control_characters` | An optional `bool`. Defaults to `False`. Whether to replace the C0 control characters (00-1F) with the `replacement_char`. Default is false. |
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

Last updated 2024-04-26 UTC.