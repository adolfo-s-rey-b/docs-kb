[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig#methods)
    *   [as\_dict](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig#as_dict)
        
    *   [from\_args](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig#from_args)
        
    *   [from\_json](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig#from_json)
        
    *   [from\_yaml](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig#from_yaml)
        
    *   [get](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig#get)
        
    *   [lock](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig#lock)
        
    *   [override](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig#override)
        
    *   [replace](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig#replace)
        
    *   [validate](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig#validate)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig#__contains__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.optimization.PowerAndLinearDecayLrConfig Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig#methods)
    *   [as\_dict](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig#as_dict)
        
    *   [from\_args](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig#from_args)
        
    *   [from\_json](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig#from_json)
        
    *   [from\_yaml](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig#from_yaml)
        
    *   [get](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig#get)
        
    *   [lock](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig#lock)
        
    *   [override](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig#override)
        
    *   [replace](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig#replace)
        
    *   [validate](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig#validate)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig#__contains__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/configs/learning_rate_config.py#L156-L188)

Configuration for DirectPower learning rate decay.

Inherits From: [`Config`](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/Config)
, [`ParamsDict`](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/ParamsDict)

#### View aliases

**Main aliases**

[`tfm.optimization.lr_cfg.PowerAndLinearDecayLrConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig)

tfm.optimization.PowerAndLinearDecayLrConfig(
        default_params: dataclasses.InitVar[Optional[Mapping[str, Any]]] = None,
        restrictions: dataclasses.InitVar[Optional[List[str]]] = None,
        name: str = 'PowerAndLinearDecay',
        initial_learning_rate: Optional[float] = None,
        total_decay_steps: Optional[int] = None,
        power: float = -0.5,
        linear_decay_fraction: float = 0.1,
        offset: int = 0
    )

The schedule has the following behavoir. Let offset\_step = step - offset.

1) offset\_step < 0, the actual learning rate equals initial\_learning\_rate. 2) offset\_step <= total\_decay\_steps \* (1 - linear\_decay\_fraction), the actual learning rate equals lr \* offset\_step^power. 3) total\_decay\_steps \* (1 - linear\_decay\_fraction) <= offset\_step < total\_decay\_steps, the actual learning rate equals lr \* offset\_step^power \* (total\_decay\_steps - offset\_step) / (total\_decay\_steps \* linear\_decay\_fraction). 4) offset\_step >= total\_decay\_steps, the actual learning rate equals zero.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `default_params` | a Python dict or another ParamsDict object including the default parameters to initialize. |
| `restrictions` | a list of strings, which define a list of restrictions to ensure the consistency of different parameters internally. Each restriction string is defined as a binary relation with a set of operators, including {'==', '!=', '<', '<=', '>', '>='}. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `name` | The name of the learning rate schedule. Defaults to PowerAndLinearDecay. |
| `initial_learning_rate` | A float. The initial learning rate. Defaults to None. |
| `total_decay_steps` | An int. The total number of steps for power + linear decay. Defaults to None. |
| `power` | A float. The order of the polynomial. Defaults to -0.5, for sqrt decay. |
| `linear_decay_fraction` | A float. In the last `linear_decay_fraction` steps, the learning rate will be multiplied by a linear decay. Defaults to 0.1. |
| `offset` | An int. The offset applied to steps. Defaults to 0. |
| `BUILDER` |     |
| `default_params` | Dataclass field |
| `restrictions` | Dataclass field |

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
| default\_params | `None` |
| initial\_learning\_rate | `None` |
| linear\_decay\_fraction | `0.1` |
| name | `'PowerAndLinearDecay'` |
| offset | `0` |
| power | `-0.5` |
| restrictions | `None` |
| total\_decay\_steps | `None` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.