[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/declare_key_flag#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/declare_key_flag)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/declare_key_flag?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fflags%2Fdeclare_key_flag&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/declare_key_flag#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/declare_key_flag#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.flags.declare\_key\_flag Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/declare_key_flag#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/declare_key_flag#raises)
    

Declares one flag as key to the current module.

tf.compat.v1.flags.declare_key_flag(
        flag_name: (str | tf.compat.v1.flags.FlagHolder),
        flag_values: tf.compat.v1.flags.FlagValues = _flagvalues.FLAGS
    ) -> None

Key flags are flags that are deemed really important for a module. They are important when listing help messages; e.g., if the --helpshort command-line flag is used, then only the key flags of the main module are listed (instead of all flags, as in the case of --helpfull).

Sample usage::

flags.declare_key_flag('flag_1')

|     |     |
| --- | --- |
| Args<br>---- |     |
| `flag_name` | str \| :class:`FlagHolder`, the name or holder of an already declared flag. (Redeclaring flags as key, including flags implicitly key because they were declared in this module, is a no-op.) Positional-only parameter. |
| `flag_values` | :class:`FlagValues`, the FlagValues instance in which the flag will be declared as a key flag. This should almost never need to be overridden. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | Raised if flag\_name not defined as a Python flag. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.