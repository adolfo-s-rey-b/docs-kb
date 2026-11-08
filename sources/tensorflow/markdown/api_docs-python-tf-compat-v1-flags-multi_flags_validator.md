[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/multi_flags_validator#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/multi_flags_validator)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/multi_flags_validator?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/multi_flags_validator#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/multi_flags_validator#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/multi_flags_validator#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.flags.multi\_flags\_validator Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/multi_flags_validator#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/multi_flags_validator#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/multi_flags_validator#raises)
    

A function decorator for defining a multi-flag validator.

tf.compat.v1.flags.multi_flags_validator(
        flag_names,
        message='Flag validation failed',
        flag_values=_flagvalues.FLAGS
    )

Registers the decorated function as a validator for flag\_names, e.g.::

@flags.multi_flags_validator(['foo', 'bar'])
    def _CheckFooBar(flags_dict):
      ...

See :func:`register_multi_flags_validator` for the specification of checker function.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `flag_names` | \[str \| FlagHolder\], a list of the flag names or holders to be checked. Positional-only parameter. |
| `message` | str, error text to be shown to the user if checker returns False. If checker raises flags.ValidationError, message from the raised error will be shown. |
| `flag_values` | flags.FlagValues, optional FlagValues instance to validate against. |

|     |
| --- |
| Returns<br>------- |     |
| A function decorator that registers its function argument as a validator. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `AttributeError` | Raised when a flag is not registered as a valid flag name. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.