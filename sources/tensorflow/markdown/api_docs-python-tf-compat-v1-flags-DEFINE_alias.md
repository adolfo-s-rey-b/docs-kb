[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_alias#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_alias)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_alias?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_alias#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_alias#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_alias#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.flags.DEFINE\_alias Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_alias#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_alias#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_alias#raises)
    

Defines an alias flag for an existing one.

tf.compat.v1.flags.DEFINE_alias(
        name: str,
        original_name: str,
        flag_values: tf.compat.v1.flags.FlagValues = _flagvalues.FLAGS,
        module_name: (str | None) = None
    ) -> _flagvalues.FlagHolder[Any]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `name` | str, the flag name. |
| `original_name` | str, the original flag name. |
| `flag_values` | :class:`FlagValues`, the FlagValues instance with which the flag will be registered. This should almost never need to be overridden. |
| `module_name` | A string, the name of the module that defines this flag. |

|     |
| --- |
| Returns<br>------- |     |
| a handle to defined flag. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `flags.FlagError` | UnrecognizedFlagError: if the referenced flag doesn't exist. DuplicateFlagError: if the alias name has been used by some existing flag. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.