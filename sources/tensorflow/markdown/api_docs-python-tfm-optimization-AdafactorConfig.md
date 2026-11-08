[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig#methods)
    *   [as\_dict](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig#as_dict)
        
    *   [from\_args](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig#from_args)
        
    *   [from\_json](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig#from_json)
        
    *   [from\_yaml](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig#from_yaml)
        
    *   [get](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig#get)
        
    *   [lock](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig#lock)
        
    *   [override](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig#override)
        
    *   [replace](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig#replace)
        
    *   [validate](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig#validate)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig#__contains__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.optimization.AdafactorConfig Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig#methods)
    *   [as\_dict](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig#as_dict)
        
    *   [from\_args](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig#from_args)
        
    *   [from\_json](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig#from_json)
        
    *   [from\_yaml](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig#from_yaml)
        
    *   [get](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig#get)
        
    *   [lock](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig#lock)
        
    *   [override](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig#override)
        
    *   [replace](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig#replace)
        
    *   [validate](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig#validate)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig#__contains__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/configs/optimizer_config.py#L322-L340)

Configuration for Adafactor optimizer.

Inherits From: [`BaseOptimizerConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/BaseOptimizerConfig)
, [`Config`](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/Config)
, [`ParamsDict`](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/ParamsDict)

#### View aliases

**Main aliases**

[`tfm.optimization.opt_cfg.AdafactorConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig)

tfm.optimization.AdafactorConfig(
        default_params: dataclasses.InitVar[Optional[Mapping[str, Any]]] = None,
        restrictions: dataclasses.InitVar[Optional[List[str]]] = None,
        clipnorm: Optional[float] = None,
        clipvalue: Optional[float] = None,
        global_clipnorm: Optional[float] = None,
        name: str = 'Adafactor',
        factored: bool = True,
        multiply_by_parameter_scale: bool = True,
        beta1: Optional[float] = None,
        decay_rate: float = 0.8,
        step_offset: int = 0,
        clipping_threshold: float = 1.0,
        min_dim_size_to_factor: int = 128,
        epsilon1: float = 1e-30,
        epsilon2: float = 0.001,
        weight_decay: Optional[float] = None,
        include_in_weight_decay: Optional[str] = None
    )

The attributes for this class matches the arguments of the Adafactor implementation.

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
| `clipnorm` | Dataclass field |
| `clipvalue` | Dataclass field |
| `global_clipnorm` | Dataclass field |
| `name` | Dataclass field |
| `factored` | Dataclass field |
| `multiply_by_parameter_scale` | Dataclass field |
| `beta1` | Dataclass field |
| `decay_rate` | Dataclass field |
| `step_offset` | Dataclass field |
| `clipping_threshold` | Dataclass field |
| `min_dim_size_to_factor` | Dataclass field |
| `epsilon1` | Dataclass field |
| `epsilon2` | Dataclass field |
| `weight_decay` | Dataclass field |
| `include_in_weight_decay` | Dataclass field |

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
| beta1 | `None` |
| clipnorm | `None` |
| clipping\_threshold | `1.0` |
| clipvalue | `None` |
| decay\_rate | `0.8` |
| default\_params | `None` |
| epsilon1 | `1e-30` |
| epsilon2 | `0.001` |
| factored | `True` |
| global\_clipnorm | `None` |
| include\_in\_weight\_decay | `None` |
| min\_dim\_size\_to\_factor | `128` |
| multiply\_by\_parameter\_scale | `True` |
| name | `'Adafactor'` |
| restrictions | `None` |
| step\_offset | `0` |
| weight\_decay | `None` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.