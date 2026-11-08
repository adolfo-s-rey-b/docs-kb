[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/mark_bool_flags_as_mutual_exclusive#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/mark_bool_flags_as_mutual_exclusive)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/mark_bool_flags_as_mutual_exclusive?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fflags%2Fmark_bool_flags_as_mutual_exclusive&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/mark_bool_flags_as_mutual_exclusive#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/mark_bool_flags_as_mutual_exclusive#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.flags.mark\_bool\_flags\_as\_mutual\_exclusive Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/mark_bool_flags_as_mutual_exclusive#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/mark_bool_flags_as_mutual_exclusive#raises)
    

Ensures that only one flag among flag\_names is True.

tf.compat.v1.flags.mark_bool_flags_as_mutual_exclusive(
        flag_names, required=False, flag_values=_flagvalues.FLAGS
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `flag_names` | \[str \| FlagHolder\], names or holders of flags. Positional-only parameter. |
| `required` | bool. If true, exactly one flag must be True. Otherwise, at most one flag can be True, and it is valid for all flags to be False. |
| `flag_values` | flags.FlagValues, optional FlagValues instance where the flags are defined. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | Raised when multiple FlagValues are used in the same invocation. This can occur when FlagHolders have different `_flagvalues` or when str-type flag\_names entries are present and the `flag_values` argument does not match that of provided FlagHolder(s). |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.