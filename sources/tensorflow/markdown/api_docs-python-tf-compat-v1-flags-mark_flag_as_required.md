[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/mark_flag_as_required#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/mark_flag_as_required)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/mark_flag_as_required?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fflags%2Fmark_flag_as_required&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/mark_flag_as_required#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/mark_flag_as_required#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.flags.mark\_flag\_as\_required Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/mark_flag_as_required#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/mark_flag_as_required#raises)
    

Ensures that flag is not None during program execution.

tf.compat.v1.flags.mark_flag_as_required(
        flag_name, flag_values=_flagvalues.FLAGS
    )

Registers a flag validator, which will follow usual validator rules. Important note: validator will pass for any non-`None` value, such as `False`, `0` (zero), `''` (empty string) and so on.

If your module might be imported by others, and you only wish to make the flag required when the module is directly executed, call this method like this::

if __name__ == '__main__':
      flags.mark_flag_as_required('your_flag_name')
      app.run()

|     |     |
| --- | --- |
| Args<br>---- |     |
| `flag_name` | str \| FlagHolder, name or holder of the flag. Positional-only parameter. |
| `flag_values` | flags.FlagValues, optional :class:`~absl.flags.FlagValues` instance where the flag is defined. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `AttributeError` | Raised when flag\_name is not registered as a valid flag name. |
| `ValueError` | Raised when flag\_values is non-default and does not match the FlagValues of the provided FlagHolder instance. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.