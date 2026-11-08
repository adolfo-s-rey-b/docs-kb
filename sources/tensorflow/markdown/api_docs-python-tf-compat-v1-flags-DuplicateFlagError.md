[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DuplicateFlagError#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DuplicateFlagError)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DuplicateFlagError?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DuplicateFlagError#methods)
    *   [from\_flag](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DuplicateFlagError#from_flag)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.flags.DuplicateFlagError Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DuplicateFlagError#methods)
    *   [from\_flag](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DuplicateFlagError#from_flag)
        

Raised if there is a flag naming conflict.

Inherits From: [`Error`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/Error)

Methods
-------

### `from_flag`

@classmethod

Creates a DuplicateFlagError by providing flag name and values.

|     |     |
| --- | --- |
| Args |     |
| `flagname` | The name of the flag being redefined. |
| `flag_values` | The FlagValues instance containing the first definition of flagname. |
| `other_flag_values` | If it is not None, it should be the FlagValues object where the second definition of flagname occurs. If it is None, we assume that we're being called when attempting to create the flag a second time, and we use the module calling this one as the source of the second definition. |

|     |
| --- |
| Returns |     |
| An instance of DuplicateFlagError. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.