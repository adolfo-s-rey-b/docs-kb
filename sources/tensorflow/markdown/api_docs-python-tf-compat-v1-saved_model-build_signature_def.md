[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/build_signature_def#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/build_signature_def)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/build_signature_def?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/build_signature_def#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/build_signature_def#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.saved\_model.build\_signature\_def Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/build_signature_def#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/build_signature_def#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/saved_model/signature_def_utils_impl.py#L30-L79)

Utility function to build a SignatureDef protocol buffer.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.saved_model.signature_def_utils.build_signature_def`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/build_signature_def)

tf.compat.v1.saved_model.build_signature_def(
        inputs=None, outputs=None, method_name=None, defaults=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `inputs` | Inputs of the SignatureDef defined as a proto map of string to tensor info. |
| `outputs` | Outputs of the SignatureDef defined as a proto map of string to tensor info. |
| `method_name` | Method name of the SignatureDef as a string. |
| `defaults` | Defaults of the SignatureDef defined as a proto map of string to TensorProto. |

|     |
| --- |
| Returns<br>------- |     |
| A SignatureDef protocol buffer constructed based on the supplied arguments. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.