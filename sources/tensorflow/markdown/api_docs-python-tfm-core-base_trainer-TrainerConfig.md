[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig#methods)
    *   [as\_dict](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig#as_dict)
        
    *   [from\_args](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig#from_args)
        
    *   [from\_json](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig#from_json)
        
    *   [from\_yaml](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig#from_yaml)
        
    *   [get](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig#get)
        
    *   [lock](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig#lock)
        
    *   [override](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig#override)
        
    *   [replace](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig#replace)
        
    *   [validate](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig#validate)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig#__contains__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.core.base\_trainer.TrainerConfig Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig#methods)
    *   [as\_dict](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig#as_dict)
        
    *   [from\_args](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig#from_args)
        
    *   [from\_json](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig#from_json)
        
    *   [from\_yaml](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig#from_yaml)
        
    *   [get](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig#get)
        
    *   [lock](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig#lock)
        
    *   [override](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig#override)
        
    *   [replace](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig#replace)
        
    *   [validate](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig#validate)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig#__contains__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/core/config_definitions.py#L210-L285)

Configuration for trainer.

Inherits From: [`Config`](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/Config)
, [`ParamsDict`](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/ParamsDict)

#### View aliases

**Main aliases**

[`tfm.core.config_definitions.TrainerConfig`](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig)

tfm.core.base_trainer.TrainerConfig(
        default_params: dataclasses.InitVar[Optional[Mapping[str, Any]]] = None,
        restrictions: dataclasses.InitVar[Optional[List[str]]] = None,
        optimizer_config: tfm.optimization.OptimizationConfig = dataclasses.field(default_factory=OptimizationConfig),
        train_tf_while_loop: bool = True,
        train_tf_function: bool = True,
        eval_tf_function: bool = True,
        eval_tf_while_loop: bool = False,
        allow_tpu_summary: bool = False,
        steps_per_loop: int = 1000,
        summary_interval: int = 1000,
        checkpoint_interval: int = 1000,
        max_to_keep: int = 5,
        continuous_eval_timeout: int = (60 * 60),
        train_steps: int = 0,
        validation_steps: int = -1,
        validation_interval: int = 1000,
        best_checkpoint_export_subdir: str = '',
        best_checkpoint_eval_metric: str = '',
        best_checkpoint_metric_comp: str = 'higher',
        loss_upper_bound: float = 1000000.0,
        recovery_begin_steps: int = 0,
        recovery_max_trials: int = 0,
        validation_summary_subdir: str = 'validation',
        preemption_on_demand_checkpoint: bool = True
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `default_params` | a Python dict or another ParamsDict object including the default parameters to initialize. |
| `restrictions` | a list of strings, which define a list of restrictions to ensure the consistency of different parameters internally. Each restriction string is defined as a binary relation with a set of operators, including {'==', '!=', '<', '<=', '>', '>='}. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `optimizer_config` | optimizer config, it includes optimizer, learning rate, and warmup schedule configs. |
| `train_tf_while_loop` | whether or not to use tf while loop. |
| `train_tf_function` | whether or not to use tf\_function for training loop. |
| `eval_tf_function` | whether or not to use tf\_function for eval. |
| `eval_tf_while_loop` | whether or not to use tf while loop for eval. |
| `allow_tpu_summary` | Whether to allow summary happen inside the XLA program runs on TPU through automatic outside compilation. |
| `steps_per_loop` | number of steps per loop to report training metrics. This can also be used to reduce host worker communication in a TPU setup. |
| `summary_interval` | number of steps between each summary. |
| `checkpoint_interval` | number of steps between checkpoints. |
| `max_to_keep` | max checkpoints to keep. |
| `continuous_eval_timeout` | maximum number of seconds to wait between checkpoints, if set to None, continuous eval will wait indefinitely. This is only used continuous\_train\_and\_eval and continuous\_eval modes. Default value is 1 hrs. |
| `train_steps` | number of train steps. |
| `validation_steps` | number of eval steps. If -1, the entire eval dataset is used. |
| `validation_interval` | number of training steps to run between evaluations. |
| `best_checkpoint_export_subdir` | if set, the trainer will keep track of the best evaluation metric, and export the corresponding best checkpoint under `model_dir/best_checkpoint_export_subdir`. Note that this only works if mode contains eval (such as `train_and_eval`, `continuous_eval`, and `continuous_train_and_eval`). |
| `best_checkpoint_eval_metric` | for exporting the best checkpoint, which evaluation metric the trainer should monitor. This can be any evaluation metric appears on tensorboard. |
| `best_checkpoint_metric_comp` | for exporting the best checkpoint, how the trainer should compare the evaluation metrics. This can be either `higher` (higher the better) or `lower` (lower the better). |
| `validation_summary_subdir` | A 'str', sub directory for saving eval summary. |
| `preemption_on_demand_checkpoint` | whether or not to save on-demand checkpoints after a preemption. |
| `BUILDER` |     |
| `default_params` | Dataclass field |
| `restrictions` | Dataclass field |
| `loss_upper_bound` | Dataclass field |
| `recovery_begin_steps` | Dataclass field |
| `recovery_max_trials` | Dataclass field |

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
| allow\_tpu\_summary | `False` |
| best\_checkpoint\_eval\_metric | `''` |
| best\_checkpoint\_export\_subdir | `''` |
| best\_checkpoint\_metric\_comp | `'higher'` |
| checkpoint\_interval | `1000` |
| continuous\_eval\_timeout | `3600` |
| default\_params | `None` |
| eval\_tf\_function | `True` |
| eval\_tf\_while\_loop | `False` |
| loss\_upper\_bound | `1000000.0` |
| max\_to\_keep | `5` |
| preemption\_on\_demand\_checkpoint | `True` |
| recovery\_begin\_steps | `0` |
| recovery\_max\_trials | `0` |
| restrictions | `None` |
| steps\_per\_loop | `1000` |
| summary\_interval | `1000` |
| train\_steps | `0` |
| train\_tf\_function | `True` |
| train\_tf\_while\_loop | `True` |
| validation\_interval | `1000` |
| validation\_steps | `-1` |
| validation\_summary\_subdir | `'validation'` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.