[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fvision%2Fconfigs%2Fmaskrcnn%2FROISampler&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler#methods)
    *   [as\_dict](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler#as_dict)
        
    *   [from\_args](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler#from_args)
        
    *   [from\_json](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler#from_json)
        
    *   [from\_yaml](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler#from_yaml)
        
    *   [get](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler#get)
        
    *   [lock](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler#lock)
        
    *   [override](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler#override)
        
    *   [replace](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler#replace)
        
    *   [validate](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler#validate)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler#__contains__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.configs.maskrcnn.ROISampler Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler#methods)
    *   [as\_dict](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler#as_dict)
        
    *   [from\_args](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler#from_args)
        
    *   [from\_json](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler#from_json)
        
    *   [from\_yaml](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler#from_yaml)
        
    *   [get](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler#get)
        
    *   [lock](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler#lock)
        
    *   [override](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler#override)
        
    *   [replace](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler#replace)
        
    *   [validate](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler#validate)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler#__contains__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/configs/maskrcnn.py#L125-L135)

Inherits From: [`Config`](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/Config)
, [`ParamsDict`](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/ParamsDict)

tfm.vision.configs.maskrcnn.ROISampler(
        default_params: dataclasses.InitVar[Optional[Mapping[str, Any]]] = None,
        restrictions: dataclasses.InitVar[Optional[List[str]]] = None,
        mix_gt_boxes: bool = True,
        num_sampled_rois: int = 512,
        foreground_fraction: float = 0.25,
        foreground_iou_threshold: float = 0.5,
        background_iou_high_threshold: float = 0.5,
        background_iou_low_threshold: float = 0.0,
        cascade_iou_thresholds: Optional[List[float]] = None
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
| `mix_gt_boxes` | Dataclass field |
| `num_sampled_rois` | Dataclass field |
| `foreground_fraction` | Dataclass field |
| `foreground_iou_threshold` | Dataclass field |
| `background_iou_high_threshold` | Dataclass field |
| `background_iou_low_threshold` | Dataclass field |
| `cascade_iou_thresholds` | Dataclass field |

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
| background\_iou\_high\_threshold | `0.5` |
| background\_iou\_low\_threshold | `0.0` |
| cascade\_iou\_thresholds | `None` |
| default\_params | `None` |
| foreground\_fraction | `0.25` |
| foreground\_iou\_threshold | `0.5` |
| mix\_gt\_boxes | `True` |
| num\_sampled\_rois | `512` |
| restrictions | `None` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.