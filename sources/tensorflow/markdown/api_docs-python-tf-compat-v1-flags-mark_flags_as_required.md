[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/mark_flags_as_required#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/mark_flags_as_required)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/mark_flags_as_required?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/mark_flags_as_required#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/mark_flags_as_required#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.flags.mark\_flags\_as\_required Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/mark_flags_as_required#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/mark_flags_as_required#raises)
    

Ensures that flags are not None during program execution.

tf.compat.v1.flags.mark_flags_as_required(
        flag_names, flag_values=_flagvalues.FLAGS
    )

If your module might be imported by others, and you only wish to make the flag required when the module is directly executed, call this method like this::

if __name__ == '__main__':
      flags.mark_flags_as_required(['flag1', 'flag2', 'flag3'])
      app.run()

|     |     |
| --- | --- |
| Args<br>---- |     |
| `flag_names` | Sequence\[str \| FlagHolder\], names or holders of the flags. |
| `flag_values` | flags.FlagValues, optional FlagValues instance where the flags are defined. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `AttributeError` | If any of flag name has not already been defined as a flag. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.