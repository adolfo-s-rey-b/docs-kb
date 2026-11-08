[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/tensor_summary#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.summary.tensor\_summary Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/summary/summary.py#L555-L608)

Outputs a `Summary` protocol buffer with a serialized tensor.proto.

tf.compat.v1.summary.tensor_summary(
        name,
        tensor,
        summary_description=None,
        collections=None,
        summary_metadata=None,
        family=None,
        display_name=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `name` | A name for the generated node. If display\_name is not set, it will also serve as the tag name in TensorBoard. (In that case, the tag name will inherit tf name scopes.) |
| `tensor` | A tensor of any type and shape to serialize. |
| `summary_description` | A long description of the summary sequence. Markdown is supported. |
| `collections` | Optional list of graph collections keys. The new summary op is added to these collections. Defaults to `[GraphKeys.SUMMARIES]`. |
| `summary_metadata` | Optional SummaryMetadata proto (which describes which plugins may use the summary value). |
| `family` | Optional; if provided, used as the prefix of the summary tag, which controls the name used for display on TensorBoard when display\_name is not set. |
| `display_name` | A string used to name this data in TensorBoard. If this is not set, then the node name will be used instead. |

|     |
| --- |
| Returns<br>------- |     |
| A scalar `Tensor` of type `string`. The serialized `Summary` protocol buffer. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.