[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/strings/regex_replace#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/strings/regex_replace)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/strings/regex_replace?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/strings/regex_replace#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/regex_replace#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/regex_replace#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.strings.regex\_replace Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/strings/regex_replace#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/regex_replace#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/regex_replace#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/string_ops.py#L74-L112)

Replace elements of `input` matching regex `pattern` with `rewrite`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.regex_replace`](https://www.tensorflow.org/api_docs/python/tf/strings/regex_replace)
, [`tf.compat.v1.strings.regex_replace`](https://www.tensorflow.org/api_docs/python/tf/strings/regex_replace)

tf.strings.regex_replace(
        input, pattern, rewrite, replace_global=True, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Creating a custom Counterfactual Logit Pairing Dataset](https://www.tensorflow.org/responsible_ai/model_remediation/counterfactual/guide/creating_a_custom_counterfactual_dataset) | *   [Basic text classification](https://www.tensorflow.org/tutorials/keras/text_classification)<br>    <br>*   [Neural machine translation with attention](https://www.tensorflow.org/text/tutorials/nmt_with_attention)<br>    <br>*   [Warm-start embedding layer matrix](https://www.tensorflow.org/text/tutorials/warmstart_embedding_matrix)<br>    <br>*   [Word embeddings](https://www.tensorflow.org/text/tutorials/word_embeddings)<br>    <br>*   [Graph-based Neural Structured Learning in TFX](https://www.tensorflow.org/tfx/tutorials/tfx/neural_structured_learning) |

    tf.strings.regex_replace("Text with tags.<br /><b>contains html</b>",

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | string `Tensor`, the source strings to process. |
| `pattern` | string or scalar string `Tensor`, regular expression to use, see more details at https://github.com/google/re2/wiki/Syntax |
| `rewrite` | string or scalar string `Tensor`, value to use in match replacement, supports backslash-escaped digits (\\1 to \\9) which can be to insert text matching corresponding parenthesized group. |
| `replace_global` | `bool`, if `True` replace all non-overlapping matches, else replace only the first match. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| string `Tensor` of the same shape as `input` with specified replacements. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.