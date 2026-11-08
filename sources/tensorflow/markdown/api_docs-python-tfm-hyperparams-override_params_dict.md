[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/override_params_dict#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/override_params_dict)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/override_params_dict?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/override_params_dict#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/override_params_dict#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/override_params_dict#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.hyperparams.override\_params\_dict Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/override_params_dict#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/override_params_dict#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/override_params_dict#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/hyperparams/params_dict.py#L455-L497)

Override a given ParamsDict using a dict, JSON/YAML/CSV string or YAML file.

#### View aliases

**Main aliases**

[`tfm.hyperparams.params_dict.override_params_dict`](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/override_params_dict)

tfm.hyperparams.override_params_dict(
        params, dict_or_string_or_yaml_file, is_strict
    )

The logic of the function is outlined below:

1.  Test that the input is a dict. If not, proceed to 2.
2.  Tests that the input is a string. If not, raise unknown ValueError 2.1. Test if the string is in a CSV format. If so, parse. If not, proceed to 2.2. 2.2. Try loading the string as a YAML/JSON. If successful, parse to dict and use it to override. If not, proceed to 2.3. 2.3. Try using the string as a file path and load the YAML file.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `params` | a ParamsDict object to be overridden. |
| `dict_or_string_or_yaml_file` | a Python dict, JSON/YAML/CSV string or path to a YAML file specifying the parameters to be overridden. |
| `is_strict` | a boolean specifying whether override is strict or not. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `params` | the overridden ParamsDict object. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if failed to override the parameters. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.