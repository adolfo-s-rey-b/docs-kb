[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig#methods)
    *   [as\_dict](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig#as_dict)
        
    *   [from\_args](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig#from_args)
        
    *   [from\_json](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig#from_json)
        
    *   [from\_yaml](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig#from_yaml)
        
    *   [get](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig#get)
        
    *   [lock](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig#lock)
        
    *   [override](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig#override)
        
    *   [replace](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig#replace)
        
    *   [validate](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig#validate)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig#__contains__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.configs.video\_classification.DataConfig Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig#methods)
    *   [as\_dict](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig#as_dict)
        
    *   [from\_args](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig#from_args)
        
    *   [from\_json](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig#from_json)
        
    *   [from\_yaml](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig#from_yaml)
        
    *   [get](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig#get)
        
    *   [lock](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig#lock)
        
    *   [override](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig#override)
        
    *   [replace](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig#replace)
        
    *   [validate](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig#validate)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig#__contains__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/configs/video_classification.py#L26-L68)

The base configuration for building datasets.

Inherits From: [`DataConfig`](https://www.tensorflow.org/api_docs/python/tfm/core/config_definitions/DataConfig)
, [`Config`](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/Config)
, [`ParamsDict`](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/ParamsDict)

tfm.vision.configs.video_classification.DataConfig(
        default_params: dataclasses.InitVar[Optional[Mapping[str, Any]]] = None,
        restrictions: dataclasses.InitVar[Optional[List[str]]] = None,
        input_path: Union[str, tfm.hyperparams.Config] = '',
        tfds_name: Union[str, tfm.hyperparams.Config] = '',
        tfds_split: str = '',
        global_batch_size: int = 128,
        is_training: bool = True,
        drop_remainder: bool = True,
        shuffle_buffer_size: int = 64,
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
        name: Optional[str] = None,
        file_type: Optional[str] = 'tfrecord',
        compressed_input: bool = False,
        split: str = 'train',
        variant_name: Optional[str] = None,
        feature_shape: Tuple[int, ...] = tfm.vision.configs.video_classification.DataConfig.feature_shape,
        temporal_stride: int = 1,
        random_stride_range: int = 0,
        num_test_clips: int = 1,
        num_test_crops: int = 1,
        num_classes: int = -1,
        num_examples: int = -1,
        data_format: str = 'channels_last',
        dtype: str = 'float32',
        label_dtype: str = 'int32',
        one_hot: bool = True,
        min_image_size: int = 256,
        zero_centering_image: bool = False,
        is_multilabel: bool = False,
        output_audio: bool = False,
        audio_feature: str = '',
        audio_feature_shape: Tuple[int, ...] = tfm.vision.configs.video_classification.DataConfig.audio_feature_shape,
        aug_min_aspect_ratio: float = 0.5,
        aug_max_aspect_ratio: float = 2.0,
        aug_min_area_ratio: float = 0.49,
        aug_max_area_ratio: float = 1.0,
        aug_random_rotation: bool = False,
        aug_type: Optional[tfm.vision.configs.common.Augmentation] = None,
        mixup_and_cutmix: Optional[tfm.vision.configs.common.MixupAndCutmix] = None,
        image_field_key: str = 'image/encoded',
        label_field_key: str = 'clip/label/index',
        input_image_format: str = 'jpeg'
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
| `name` | Dataclass field |
| `file_type` | Dataclass field |
| `compressed_input` | Dataclass field |
| `split` | Dataclass field |
| `variant_name` | Dataclass field |
| `feature_shape` | Dataclass field |
| `temporal_stride` | Dataclass field |
| `random_stride_range` | Dataclass field |
| `num_test_clips` | Dataclass field |
| `num_test_crops` | Dataclass field |
| `num_classes` | Dataclass field |
| `num_examples` | Dataclass field |
| `data_format` | Dataclass field |
| `dtype` | Dataclass field |
| `label_dtype` | Dataclass field |
| `one_hot` | Dataclass field |
| `min_image_size` | Dataclass field |
| `zero_centering_image` | Dataclass field |
| `is_multilabel` | Dataclass field |
| `output_audio` | Dataclass field |
| `audio_feature` | Dataclass field |
| `audio_feature_shape` | Dataclass field |
| `aug_min_aspect_ratio` | Dataclass field |
| `aug_max_aspect_ratio` | Dataclass field |
| `aug_min_area_ratio` | Dataclass field |
| `aug_max_area_ratio` | Dataclass field |
| `aug_random_rotation` | Dataclass field |
| `aug_type` | Dataclass field |
| `mixup_and_cutmix` | Dataclass field |
| `image_field_key` | Dataclass field |
| `label_field_key` | Dataclass field |
| `input_image_format` | Dataclass field |

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
| audio\_feature | `''` |
| audio\_feature\_shape | `(-1,)` |
| aug\_max\_area\_ratio | `1.0` |
| aug\_max\_aspect\_ratio | `2.0` |
| aug\_min\_area\_ratio | `0.49` |
| aug\_min\_aspect\_ratio | `0.5` |
| aug\_random\_rotation | `False` |
| aug\_type | `None` |
| autotune\_algorithm | `None` |
| block\_length | `1` |
| cache | `False` |
| compressed\_input | `False` |
| cycle\_length | `10` |
| data\_format | `'channels_last'` |
| default\_params | `None` |
| deterministic | `None` |
| drop\_remainder | `True` |
| dtype | `'float32'` |
| enable\_shared\_tf\_data\_service\_between\_parallel\_trainers | `False` |
| enable\_tf\_data\_service | `False` |
| feature\_shape | `(64, 224, 224, 3)` |
| file\_type | `'tfrecord'` |
| global\_batch\_size | `128` |
| image\_field\_key | `'image/encoded'` |
| input\_image\_format | `'jpeg'` |
| input\_path | `''` |
| is\_multilabel | `False` |
| is\_training | `True` |
| label\_dtype | `'int32'` |
| label\_field\_key | `'clip/label/index'` |
| min\_image\_size | `256` |
| mixup\_and\_cutmix | `None` |
| name | `None` |
| num\_classes | `-1` |
| num\_examples | `-1` |
| num\_test\_clips | `1` |
| num\_test\_crops | `1` |
| one\_hot | `True` |
| output\_audio | `False` |
| prefetch\_buffer\_size | `None` |
| ram\_budget | `None` |
| random\_stride\_range | `0` |
| restrictions | `None` |
| seed | `None` |
| sharding | `True` |
| shuffle\_buffer\_size | `64` |
| split | `'train'` |
| temporal\_stride | `1` |
| tf\_data\_service\_address | `None` |
| tf\_data\_service\_job\_name | `None` |
| tfds\_as\_supervised | `False` |
| tfds\_data\_dir | `''` |
| tfds\_name | `''` |
| tfds\_skip\_decoding\_feature | `''` |
| tfds\_split | `''` |
| trainer\_id | `None` |
| variant\_name | `None` |
| zero\_centering\_image | `False` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.