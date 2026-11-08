[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/strings/regex_full_match#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/strings/regex_full_match)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/strings/regex_full_match?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fstrings%2Fregex_full_match&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/strings/regex_full_match#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/regex_full_match#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/regex_full_match#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.strings.regex\_full\_match Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/strings/regex_full_match#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/regex_full_match#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/regex_full_match#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/string_ops.py#L47-L69)

Check if the input matches the regex pattern.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.strings.regex_full_match`](https://www.tensorflow.org/api_docs/python/tf/strings/regex_full_match)

tf.strings.regex_full_match(
        input, pattern, name=None
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Subword tokenizers](https://www.tensorflow.org/text/guide/subwords_tokenizer) |

The input is a string tensor of any shape. The pattern is a scalar string tensor which is applied to every element of the input tensor. The boolean values (True or False) of the output tensor indicate if the input matches the regex pattern provided.

The pattern follows the re2 syntax ([https://github.com/google/re2/wiki/Syntax](https://github.com/google/re2/wiki/Syntax)
)

#### Examples:

    tf.strings.regex_full_match(["TF lib", "lib TF"], ".*lib$")

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor` of type `string`. A string tensor of the text to be processed. |
| `pattern` | A `Tensor` of type `string`. A scalar string tensor containing the regular expression to match the input. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `bool`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.