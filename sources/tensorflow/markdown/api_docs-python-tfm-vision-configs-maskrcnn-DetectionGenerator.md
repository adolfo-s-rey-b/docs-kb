[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator#methods)
    *   [as\_dict](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator#as_dict)
        
    *   [from\_args](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator#from_args)
        
    *   [from\_json](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator#from_json)
        
    *   [from\_yaml](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator#from_yaml)
        
    *   [get](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator#get)
        
    *   [lock](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator#lock)
        
    *   [override](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator#override)
        
    *   [replace](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator#replace)
        
    *   [validate](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator#validate)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator#__contains__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.configs.maskrcnn.DetectionGenerator Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator#methods)
    *   [as\_dict](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator#as_dict)
        
    *   [from\_args](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator#from_args)
        
    *   [from\_json](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator#from_json)
        
    *   [from\_yaml](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator#from_yaml)
        
    *   [get](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator#get)
        
    *   [lock](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator#lock)
        
    *   [override](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator#override)
        
    *   [replace](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator#replace)
        
    *   [validate](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator#validate)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator#__contains__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/configs/maskrcnn.py#L144-L154)

Inherits From: [`Config`](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/Config)
, [`ParamsDict`](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/ParamsDict)

tfm.vision.configs.maskrcnn.DetectionGenerator(
        default_params: dataclasses.InitVar[Optional[Mapping[str, Any]]] = None,
        restrictions: dataclasses.InitVar[Optional[List[str]]] = None,
        apply_nms: bool = True,
        pre_nms_top_k: int = 5000,
        pre_nms_score_threshold: float = 0.05,
        nms_iou_threshold: float = 0.5,
        max_num_detections: int = 100,
        nms_version: str = 'v2',
        use_cpu_nms: bool = False,
        soft_nms_sigma: Optional[float] = None,
        use_sigmoid_probability: bool = False
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `default_params` | a Python dict or another ParamsDict object including the default parameters to initialize. |
| `restrictions` | a list of strings, which define a list of restrictions to ensure the consistency of different parameters internally. Each restriction string is defined as a binary relation with a set of operators, including {'==', '!=', '<', '<=', '>', '>='}. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `BUILDER` |     |
| `default_params` | Dataclass field |
| `restrictions` | Dataclass field |
| `apply_nms` | Dataclass field |
| `pre_nms_top_k` | Dataclass field |
| `pre_nms_score_threshold` | Dataclass field |
| `nms_iou_threshold` | Dataclass field |
| `max_num_detections` | Dataclass field |
| `nms_version` | Dataclass field |
| `use_cpu_nms` | Dataclass field |
| `soft_nms_sigma` | Dataclass field |
| `use_sigmoid_probability` | Dataclass field |

Methods
-------

### `as_dict`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/hyperparams/base_config.py#L315-L324)

as_dict()

Returns a dict representation of params\_dict.ParamsDict.

For the nested params\_dict.ParamsDict, a nested dict will be returned.

### `from_args`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/hyperparams/base_config.py#L349-L358)

@classmethod

Builds a config from the given list of arguments.

### `from_json`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/hyperparams/base_config.py#L344-L347)

@classmethod

Wrapper for `from_yaml`.

### `from_yaml`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/hyperparams/base_config.py#L335-L342)

@classmethod

### `get`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/hyperparams/params_dict.py#L142-L144)

get(
        key, value=None
    )

Accesses through built-in dictionary get method.

### `lock`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/hyperparams/params_dict.py#L204-L206)

lock()

Makes the ParamsDict immutable.

### `override`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/hyperparams/params_dict.py#L165-L181)

override(
        override_params, is_strict=True
    )

Override the ParamsDict with a set of given params.

|     |     |
| --- | --- |
| Args |     |
| `override_params` | a dict or a ParamsDict specifying the parameters to be overridden. |
| `is_strict` | a boolean specifying whether override is strict or not. If True, keys in `override_params` must be present in the ParamsDict. If False, keys in `override_params` can be different from what is currently defined in the ParamsDict. In this case, the ParamsDict will be extended to include the new keys. |

### `replace`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/hyperparams/base_config.py#L326-L333)

replace(
        **kwargs
    )

Overrides/returns a unlocked copy with the current config unchanged.

### `validate`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/hyperparams/params_dict.py#L222-L329)

validate()

Validate the parameters consistency based on the restrictions.

This method validates the internal consistency using the pre-defined list of restrictions. A restriction is defined as a string which specifies a binary operation. The supported binary operations are {'==', '!=', '<', '<=', '>', '>='}. Note that the meaning of these operators are consistent with the underlying Python immplementation. Users should make sure the define restrictions on their type make sense.

For example, for a ParamsDict like the following

a:
      a1: 1
      a2: 2
    b:
      bb:
        bb1: 10
        bb2: 20
      ccc:
        a1: 1
        a3: 3

one can define two restrictions like this \['a.a1 == b.ccc.a1', 'a.a2 <= b.bb.bb2'\]

|     |
| --- |
| What it enforces are |     |
| *   a.a1 = 1 == b.ccc.a1 = 1<br>*   a.a2 = 2 <= b.bb.bb2 = 20 |     |

|     |     |
| --- | --- |
| Raises |     |
| `KeyError` | if any of the following happens (1) any of parameters in any of restrictions is not defined in ParamsDict, (2) any inconsistency violating the restriction is found. |
| `ValueError` | if the restriction defined in the string is not supported. |

### `__contains__`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/hyperparams/params_dict.py#L138-L140)

__contains__(
        key
    )

Implements the membership test operator.

### `__eq__`

__eq__(
        other
    )

Return self==value.

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| IMMUTABLE\_TYPES | `(<class 'str'>, <class 'int'>, <class 'float'>, <class 'bool'>, <class 'NoneType'>)` |
| RESERVED\_ATTR | `['_locked', '_restrictions']` |
| SEQUENCE\_TYPES | `(<class 'list'>, <class 'tuple'>)` |
| apply\_nms | `True` |
| default\_params | `None` |
| max\_num\_detections | `100` |
| nms\_iou\_threshold | `0.5` |
| nms\_version | `'v2'` |
| pre\_nms\_score\_threshold | `0.05` |
| pre\_nms\_top\_k | `5000` |
| restrictions | `None` |
| soft\_nms\_sigma | `None` |
| use\_cpu\_nms | `False` |
| use\_sigmoid\_probability | `False` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.