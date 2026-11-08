[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/extension_type/as_dict#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/extension_type/as_dict)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/extension_type/as_dict?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/extension_type/as_dict#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/experimental/extension_type/as_dict#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.extension\_type.as\_dict Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/extension_type/as_dict#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/experimental/extension_type/as_dict#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/extension_type.py#L332-L349)

Extracts the attributes of `value` and their values to a dict format.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.experimental.extension_type.as_dict`](https://www.tensorflow.org/api_docs/python/tf/experimental/extension_type/as_dict)

tf.experimental.extension_type.as_dict(
        value
    )

Unlike `dataclasses.asdict()`, this function is not recursive and in case of nested `ExtensionType` objects, only the top level object is converted to a dict.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `value` | An `ExtensionType` object. |

|     |
| --- |
| Returns<br>------- |     |
| A dict that contains the attributes of `value` and their values. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.