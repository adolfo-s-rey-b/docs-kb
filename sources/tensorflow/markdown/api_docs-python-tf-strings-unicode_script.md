[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_script#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_script)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_script?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_script#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_script#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_script#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.strings.unicode\_script Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_script#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_script#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_script#returns)
    

Determine the script codes of a given tensor of Unicode integer code points.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.strings.unicode_script`](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_script)

tf.strings.unicode_script(
        input: Annotated[Any, _atypes.Int32], name=None
    ) -> Annotated[Any, _atypes.Int32]

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Unicode strings](https://www.tensorflow.org/text/guide/unicode) |

This operation converts Unicode code points to script codes corresponding to each code point. Script codes correspond to International Components for Unicode (ICU) UScriptCode values.

See [ICU project docs](http://icu-project.org/apiref/icu4c/uscript_8h.html)
 for more details on script codes.

For an example, see the unicode strings guide on [unicode scripts](https://www.tensorflow.org/tutorials/load_data/unicode#representing_unicode)
.

Returns -1 (USCRIPT\_INVALID\_CODE) for invalid codepoints. Output shape will match input shape.

#### Examples:

    tf.strings.unicode_script([1, 31, 38])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor` of type `int32`. A Tensor of int32 Unicode code points. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `int32`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.