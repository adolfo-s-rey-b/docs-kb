[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/adopt_module_key_flags#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/adopt_module_key_flags)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/adopt_module_key_flags?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/adopt_module_key_flags#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/adopt_module_key_flags#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.flags.adopt\_module\_key\_flags Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/adopt_module_key_flags#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/adopt_module_key_flags#raises)
    

Declares that all flags key to a module are key to the current module.

tf.compat.v1.flags.adopt_module_key_flags(
        module: Any,
        flag_values: tf.compat.v1.flags.FlagValues = _flagvalues.FLAGS
    ) -> None

|     |     |
| --- | --- |
| Args<br>---- |     |
| `module` | module, the module object from which all key flags will be declared as key flags to the current module. |
| `flag_values` | :class:`FlagValues`, the FlagValues instance in which the flags will be declared as key flags. This should almost never need to be overridden. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `Error` | Raised when given an argument that is a module name (a string), instead of a module object. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.