[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/classification_signature_def#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/classification_signature_def)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/classification_signature_def?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/classification_signature_def#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/classification_signature_def#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/classification_signature_def#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.saved\_model.classification\_signature\_def Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/classification_signature_def#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/classification_signature_def#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/classification_signature_def#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/saved_model/signature_def_utils_impl.py#L133-L193)

Creates classification signature from given examples and predictions.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.saved_model.signature_def_utils.classification_signature_def`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/classification_signature_def)

tf.compat.v1.saved_model.classification_signature_def(
        examples, classes, scores
    )

This function produces signatures intended for use with the TensorFlow Serving Classify API (tensorflow\_serving/apis/prediction\_service.proto), and so constrains the input and output types to those allowed by TensorFlow Serving.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `examples` | A string `Tensor`, expected to accept serialized tf.Examples. |
| `classes` | A string `Tensor`. Note that the ClassificationResponse message requires that class labels are strings, not integers or anything else. |
| `scores` | a float `Tensor`. |

|     |
| --- |
| Returns<br>------- |     |
| A classification-flavored signature\_def. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If examples is `None`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.