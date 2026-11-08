[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig#methods)
    *   [as\_dict](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig#as_dict)
        
    *   [from\_args](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig#from_args)
        
    *   [from\_json](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig#from_json)
        
    *   [from\_yaml](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig#from_yaml)
        
    *   [get](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig#get)
        
    *   [lock](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig#lock)
        
    *   [override](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig#override)
        
    *   [replace](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig#replace)
        
    *   [validate](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig#validate)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig#__contains__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.configs.semantic\_segmentation.DataConfig Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig#methods)
    *   [as\_dict](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig#as_dict)
        
    *   [from\_args](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig#from_args)
        
    *   [from\_json](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig#from_json)
        
    *   [from\_yaml](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig#from_yaml)
        
    *   [get](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig#get)
        
    *   [lock](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig#lock)
        
    *   [override](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig#override)
        
    *   [replace](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig#replace)
        
    *   [validate](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig#validate)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig#__contains__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/configs/semantic_segmentation.py#L59-L96)

Input config for training.

Inherits From: [`DataConfig`](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig)
, [`Config`](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/Config)
, [`ParamsDict`](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/ParamsDict)

tfm.vision.configs.semantic_segmentation.DataConfig(
        default_params: dataclasses.InitVar[Optional[Mapping[str, Any]]] = None,
        restrictions: dataclasses.InitVar[Optional[List[str]]] = None,
        input_path: Union[Sequence[str], str, tfm.hyperparams.Config] = None,
        tfds_name: Union[str, tfm.hyperparams.Config] = '',
        tfds_split: str = '',
        global_batch_size: int = 0,
        is_training: bool = True,
        drop_remainder: bool = True,
        shuffle_buffer_size: int = 1000,
        cache: bool = False,
        cycle_length: int = 10,
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
        autotune_algorithm: Optional[str] = None,
        image_feature: tfm.vision.configs.semantic_segmentation.DenseFeatureConfig = dataclasses.field(default_factory=DenseFeatureConfig),
        output_size: List[int] = dataclasses.field(default_factory=list),
        crop_size: List[int] = dataclasses.field(default_factory=list),
        weights: Optional[tfm.hyperparams.Config] = None,
        dtype: str = 'float32',
        resize_eval_groundtruth: bool = True,
        groundtruth_padded_size: List[int] = dataclasses.field(default_factory=list),
        aug_scale_min: float = 1.0,
        aug_scale_max: float = 1.0,
        aug_rand_hflip: bool = True,
        preserve_aspect_ratio: bool = True,
        aug_policy: Optional[str] = None,
        file_type: str = 'tfrecord',
        decoder: Optional[tfm.vision.configs.common.DataDecoder] = dataclasses.field(default_factory=common.DataDecoder),
        additional_dense_features: List[tfm.vision.configs.semantic_segmentation.DenseFeatureConfig] = dataclasses.field(default_factory=list),
        centered_crop: bool = False
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
| `input_path` | Dataclass field |
| `tfds_name` | Dataclass field |
| `tfds_split` | Dataclass field |
| `global_batch_size` | Dataclass field |
| `is_training` | Dataclass field |
| `drop_remainder` | Dataclass field |
| `shuffle_buffer_size` | Dataclass field |
| `cache` | Dataclass field |
| `cycle_length` | Dataclass field |
| `block_length` | Dataclass field |
| `ram_budget` | Dataclass field |
| `deterministic` | Dataclass field |
| `sharding` | Dataclass field |
| `enable_tf_data_service` | Dataclass field |
| `tf_data_service_address` | Dataclass field |
| `tf_data_service_job_name` | Dataclass field |
| `tfds_data_dir` | Dataclass field |
| `tfds_as_supervised` | Dataclass field |
| `tfds_skip_decoding_feature` | Dataclass field |
| `enable_shared_tf_data_service_between_parallel_trainers` | Dataclass field |
| `apply_tf_data_service_before_batching` | Dataclass field |
| `trainer_id` | Dataclass field |
| `seed` | Dataclass field |
| `prefetch_buffer_size` | Dataclass field |
| `autotune_algorithm` | Dataclass field |
| `image_feature` | Dataclass field |
| `output_size` | Dataclass field |
| `crop_size` | Dataclass field |
| `weights` | Dataclass field |
| `dtype` | Dataclass field |
| `resize_eval_groundtruth` | Dataclass field |
| `groundtruth_padded_size` | Dataclass field |
| `aug_scale_min` | Dataclass field |
| `aug_scale_max` | Dataclass field |
| `aug_rand_hflip` | Dataclass field |
| `preserve_aspect_ratio` | Dataclass field |
| `aug_policy` | Dataclass field |
| `file_type` | Dataclass field |
| `decoder` | Dataclass field |
| `additional_dense_features` | Dataclass field |
| `centered_crop` | Dataclass field |

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
| aug\_policy | `None` |
| aug\_rand\_hflip | `True` |
| aug\_scale\_max | `1.0` |
| aug\_scale\_min | `1.0` |
| autotune\_algorithm | `None` |
| block\_length | `1` |
| cache | `False` |
| centered\_crop | `False` |
| cycle\_length | `10` |
| default\_params | `None` |
| deterministic | `None` |
| drop\_remainder | `True` |
| dtype | `'float32'` |
| enable\_shared\_tf\_data\_service\_between\_parallel\_trainers | `False` |
| enable\_tf\_data\_service | `False` |
| file\_type | `'tfrecord'` |
| global\_batch\_size | `0` |
| input\_path | `None` |
| is\_training | `True` |
| prefetch\_buffer\_size | `None` |
| preserve\_aspect\_ratio | `True` |
| ram\_budget | `None` |
| resize\_eval\_groundtruth | `True` |
| restrictions | `None` |
| seed | `None` |
| sharding | `True` |
| shuffle\_buffer\_size | `1000` |
| tf\_data\_service\_address | `None` |
| tf\_data\_service\_job\_name | `None` |
| tfds\_as\_supervised | `False` |
| tfds\_data\_dir | `''` |
| tfds\_name | `''` |
| tfds\_skip\_decoding\_feature | `''` |
| tfds\_split | `''` |
| trainer\_id | `None` |
| weights | `None` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.