[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/override_value#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/override_value)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/override_value?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/override_value#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/override_value#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.flags.override\_value Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/override_value#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/override_value#raises)
    

Overrides the value of the provided flag.

tf.compat.v1.flags.override_value(
        flag_holder: _flagvalues.FlagHolder[_T], value: _T
    ) -> None

This value takes precedent over the default value and, when called after flag parsing, any value provided at the command line.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `flag_holder` | FlagHolder, the flag to modify. |
| `value` | The new value. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `IllegalFlagValueError` | The value did not pass the flag parser or validators. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.