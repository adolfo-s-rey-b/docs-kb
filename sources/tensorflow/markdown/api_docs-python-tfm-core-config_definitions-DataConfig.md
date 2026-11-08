[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig#methods)
    *   [as\_dict](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig#as_dict)
        
    *   [from\_args](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig#from_args)
        
    *   [from\_json](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig#from_json)
        
    *   [from\_yaml](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig#from_yaml)
        
    *   [get](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig#get)
        
    *   [lock](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig#lock)
        
    *   [override](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig#override)
        
    *   [replace](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig#replace)
        
    *   [validate](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig#validate)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig#__contains__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.core.config\_definitions.DataConfig Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig#methods)
    *   [as\_dict](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig#as_dict)
        
    *   [from\_args](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig#from_args)
        
    *   [from\_json](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig#from_json)
        
    *   [from\_yaml](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig#from_yaml)
        
    *   [get](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig#get)
        
    *   [lock](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig#lock)
        
    *   [override](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig#override)
        
    *   [replace](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig#replace)
        
    *   [validate](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig#validate)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig#__contains__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/core/config_definitions.py#L27-L136)

The base configuration for building datasets.

Inherits From: [`Config`](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/Config)
, [`ParamsDict`](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/ParamsDict)

tfm.core.config_definitions.DataConfig(
        default_params: dataclasses.InitVar[Optional[Mapping[str, Any]]] = None,
        restrictions: dataclasses.InitVar[Optional[List[str]]] = None,
        input_path: Union[Sequence[str], str, tfm.hyperparams.Config] = '',
        tfds_name: Union[str, tfm.hyperparams.Config] = '',
        tfds_split: str = '',
        global_batch_size: int = 0,
        is_training: Optional[bool] = None,
        drop_remainder: bool = True,
        shuffle_buffer_size: int = 100,
        cache: bool = False,
        cycle_length: Optional[int] = None,
        block_length: int = 1,
        ram_budget: Optional[int] = None,
        deterministic: Optional[bool] = None,
        sharding: bool = True,
        enable_tf_data_service: bool = False,
        tf_data_service_address: Optional[str] = None,
        tf_data_service_job_name: Optional[str] = None,
        tfds_data_dir: str = '',
        tfds_as_supervised: bool = False,
        tfds_skip_decoding_feature: str = '',
        enable_shared_tf_data_service_between_parallel_trainers: bool = False,
        apply_tf_data_service_before_batching: bool = False,
        trainer_id: Optional[str] = None,
        seed: Optional[int] = None,
        prefetch_buffer_size: Optional[int] = None,
        autotune_algorithm: Optional[str] = None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `default_params` | a Python dict or another ParamsDict object including the default parameters to initialize. |
| `restrictions` | a list of strings, which define a list of restrictions to ensure the consistency of different parameters internally. Each restriction string is defined as a binary relation with a set of operators, including {'==', '!=', '<', '<=', '>', '>='}. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `input_path` | The path to the input. It can be either (1) a str indicating a file path/pattern, or (2) a str indicating multiple file paths/patterns separated by comma (e.g "a, b, c" or no spaces "a,b,c"), or (3) a list of str, each of which is a file path/pattern or multiple file paths/patterns separated by comma, or (4) a dictionary of the previous three approaches for more advanced data mixing using named access. It should not be specified when the following `tfds_name` is specified. |
| `tfds_name` | The name of the tensorflow dataset (TFDS). It should not be specified when the above `input_path` is specified. |
| `tfds_split` | A str indicating which split of the data to load from TFDS. It is required when above `tfds_name` is specified. |
| `global_batch_size` | The global batch size across all replicas. |
| `is_training` | Whether this data is used for training or not. This flag is useful for consumers of this object to determine whether the data should be repeated or shuffled. |
| `drop_remainder` | Whether the last batch should be dropped in the case it has fewer than `global_batch_size` elements. |
| `shuffle_buffer_size` | The buffer size used for shuffling training data. |
| `cache` | Whether to cache dataset examples. If `True`, we will cache the dataset after applying the decode\_fn and parse\_fn. It can be used to avoid re-reading from disk, re-decoding and re-parsing the example on the second epoch, but it requires significant memory overhead. |
| `cycle_length` | The number of files that will be processed concurrently when interleaving files. |
| `block_length` | The number of consecutive elements to produce from each input element before cycling to another input element when interleaving files. |
| `ram_budget` | RAM budget for tf.data service in GB. If None, tf.data will use 50% of the available host RAM. |
| `deterministic` | A boolean controlling whether determinism should be enforced. |
| `sharding` | Whether sharding is used in the input pipeline. |
| `enable_tf_data_service` | A boolean indicating whether to enable tf.data service for the input pipeline. |
| `tf_data_service_address` | The URI of a tf.data service to offload preprocessing onto during training. The URI should be in the format "protocol://address", e.g. "grpc://tf-data-service:5050". It can be overridden by `FLAGS.tf_data_service` flag in the binary. |
| `tf_data_service_job_name` | The name of the tf.data service job. This argument makes it possible for multiple datasets to share the same job. The default behavior is that the dataset creates anonymous, exclusively owned jobs. |
| `tfds_data_dir` | A str specifying the directory to read/write TFDS data. |
| `tfds_as_supervised` | A bool. When loading dataset from TFDS, if True, the returned tf.data.Dataset will have a 2-tuple structure (input, label) according to builder.info.supervised\_keys; if False, the default, the returned tf.data.Dataset will have a dictionary with all the features. |
| `tfds_skip_decoding_feature` | A str to indicate which features are skipped for decoding when loading dataset from TFDS. Use comma to separate multiple features. The main use case is to skip the image/video decoding for better performance. |
| `enable_shared_tf_data_service_between_parallel_trainers` | A bool. When set to true, only a single tf.data service will be started, and it will be shared between all the trainer run simultaneously, e.g. using vizier to tune hyperparameters. This will save CPU and RAM resources compared to running separate tf.data service for each trainer. Notice that if batch size is different for different trainers, the field apply\_tf\_data\_service\_before\_batching also needs to be true so that only a single tf.data service instance will be created. In this case, tf.data service will be applied before batching operation. So make sure to not apply any processing steps after batching (e.g. in postprocess\_fn) since they wouldn't be paralleled by tf.data service and may slow down your tf.data pipeline. When using shared tf.data service, the tf.data dataset must be infinite, and slow trainer may skip certain training examples. More details about shared tf.data service can be found at: https://www.tensorflow.org/api\_docs/python/tf/data/experimental/service#sharing\_tfdata\_service\_with\_concurrent\_trainers. |
| `apply_tf_data_service_before_batching` | A bool. If set to True, tf.data service will be applied before batching operation. This is useful to make sure only a single tf.data service instance is created when enable\_shared\_tf\_data\_service\_between\_parallel\_trainers is true and batch size is changing between parallel trainers. |
| `trainer_id` | A string. The id of the trainer if there are multiple parallel trainer running at the same time, e.g. in vizier tuning case. It will be automatically set if this field is needed. Users does not need to set it when creating experiment configs. |
| `seed` | An optional seed to use for deterministic shuffling/preprocessing. |
| `prefetch_buffer_size` | An int specifying the buffer size of prefetch datasets. If None, the buffer size is autotuned. Specifying this is useful in case autotuning uses up too much memory by making the buffer size too high. |
| `autotune_algorithm` | If specified, use this algorithm for AUTOTUNE. See: https://www.tensorflow.org/api\_docs/python/tf/data/experimental/AutotuneAlgorithm |
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
| apply\_tf\_data\_service\_before\_batching | `False` |
| autotune\_algorithm | `None` |
| block\_length | `1` |
| cache | `False` |
| cycle\_length | `None` |
| default\_params | `None` |
| deterministic | `None` |
| drop\_remainder | `True` |
| enable\_shared\_tf\_data\_service\_between\_parallel\_trainers | `False` |
| enable\_tf\_data\_service | `False` |
| global\_batch\_size | `0` |
| input\_path | `''` |
| is\_training | `None` |
| prefetch\_buffer\_size | `None` |
| ram\_budget | `None` |
| restrictions | `None` |
| seed | `None` |
| sharding | `True` |
| shuffle\_buffer\_size | `100` |
| tf\_data\_service\_address | `None` |
| tf\_data\_service\_job\_name | `None` |
| tfds\_as\_supervised | `False` |
| tfds\_data\_dir | `''` |
| tfds\_name | `''` |
| tfds\_skip\_decoding\_feature | `''` |
| tfds\_split | `''` |
| trainer\_id | `None` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.