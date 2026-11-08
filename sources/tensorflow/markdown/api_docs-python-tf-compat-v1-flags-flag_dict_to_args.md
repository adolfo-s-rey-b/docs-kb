[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/flag_dict_to_args#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/flag_dict_to_args)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/flag_dict_to_args?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fflags%2Fflag_dict_to_args&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/flag_dict_to_args#args)
    
*   [Yields](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/flag_dict_to_args#yields)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.flags.flag\_dict\_to\_args Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/flag_dict_to_args#args)
    
*   [Yields](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/flag_dict_to_args#yields)
    

Convert a dict of values into process call parameters.

tf.compat.v1.flags.flag_dict_to_args(
        flag_map: dict[str, Any], multi_flags: (set[str] | None) = None
    ) -> Iterable[str]

This method is used to convert a dictionary into a sequence of parameters for a binary that parses arguments using this module.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `flag_map` | dict, a mapping where the keys are flag names (strings). values are treated according to their type:<br><br>*   If value is `None`, then only the name is emitted.<br>*   If value is `True`, then only the name is emitted.<br>*   If value is `False`, then only the name prepended with 'no' is emitted.<br>    <br>*   If value is a string then `--name=value` is emitted.<br>    <br>*   If value is a collection, this will emit `--name=value1,value2,value3`, unless the flag name is in `multi_flags`, in which case this will emit `--name=value1 --name=value2 --name=value3`.<br>    <br>*   Everything else is converted to string an passed as such. |
| `multi_flags` | set, names (strings) of flags that should be treated as multi-flags. |

|     |
| --- |
| Yields<br>------ |     |
| sequence of string suitable for a subprocess execution. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.