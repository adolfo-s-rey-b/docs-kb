[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/register_validator#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/register_validator)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/register_validator?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/register_validator#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/register_validator#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.flags.register\_validator Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/register_validator#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/register_validator#raises)
    

Adds a constraint, which will be enforced during program execution.

tf.compat.v1.flags.register_validator(
        flag_name,
        checker,
        message='Flag validation failed',
        flag_values=_flagvalues.FLAGS
    )

The constraint is validated when flags are initially parsed, and after each change of the corresponding flag's value.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `flag_name` | str \| FlagHolder, name or holder of the flag to be checked. Positional-only parameter. |
| `checker` | callable, a function to validate the flag.<br><br>*   input - A single positional argument: The value of the corresponding flag (string, boolean, etc. This value will be passed to checker by the library).<br>    <br>*   output - bool, True if validator constraint is satisfied. If constraint is not satisfied, it should either `return False` or `raise flags.ValidationError(desired_error_message)`. |
| `message` | str, error text to be shown to the user if checker returns False. If checker raises flags.ValidationError, message from the raised error will be shown. |
| `flag_values` | flags.FlagValues, optional FlagValues instance to validate against. |

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