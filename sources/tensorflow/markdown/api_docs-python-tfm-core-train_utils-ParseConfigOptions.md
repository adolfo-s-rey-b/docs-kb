[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/ParseConfigOptions#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/ParseConfigOptions)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/ParseConfigOptions?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fcore%2Ftrain_utils%2FParseConfigOptions&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/ParseConfigOptions#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/ParseConfigOptions#methods)
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/ParseConfigOptions#__contains__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/ParseConfigOptions#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/ParseConfigOptions#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.core.train\_utils.ParseConfigOptions Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/ParseConfigOptions#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/ParseConfigOptions#methods)
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/ParseConfigOptions#__contains__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/ParseConfigOptions#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/ParseConfigOptions#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/core/train_utils.py#L287-L297)

Use this dataclass instead of FLAGS to customize parse\_configuration().

tfm.core.train_utils.ParseConfigOptions(
        experiment: str,
        config_file: List[str],
        tpu: str = '',
        tf_data_service: str = '',
        params_override: str = ''
    )

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `experiment` | Dataclass field |
| `config_file` | Dataclass field |
| `tpu` | Dataclass field |
| `tf_data_service` | Dataclass field |
| `params_override` | Dataclass field |

Methods
-------

### `__contains__`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/train_utils.py#L296-L297)

__contains__(
        name
    )

### `__eq__`

__eq__(
        other
    )

Return self==value.

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| params\_override | `''` |
| tf\_data\_service | `''` |
| tpu | `''` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.