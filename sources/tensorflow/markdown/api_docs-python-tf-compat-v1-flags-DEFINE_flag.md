[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_flag#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_flag)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_flag?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fflags%2FDEFINE_flag&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_flag#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_flag#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.flags.DEFINE\_flag Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_flag#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_flag#returns)
    

Registers a :class:`Flag` object with a :class:`FlagValues` object.

tf.compat.v1.flags.DEFINE_flag(
        flag, flag_values=_flagvalues.FLAGS, module_name=None, required=False
    )

By default, the global :const:`FLAGS` `FlagValue` object is used.

Typical users will use one of the more specialized DEFINE\_xxx functions, such as :func:`DEFINE_string` or :func:`DEFINE_integer`. But developers who need to create :class:`Flag` objects themselves should use this function to register their flags.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `flag` | :class:`Flag`, a flag that is key to the module. |
| `flag_values` | :class:`FlagValues`, the `FlagValues` instance with which the flag will be registered. This should almost never need to be overridden. |
| `module_name` | str, the name of the Python module declaring this flag. If not provided, it will be computed using the stack trace of this call. |
| `required` | bool, is this a required flag. This must be used as a keyword argument. |

|     |
| --- |
| Returns<br>------- |     |
| a handle to defined flag. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.