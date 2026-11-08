[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerPredictionOutputs/Spec#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerPredictionOutputs/Spec)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerPredictionOutputs/Spec?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fuplift%2Ftypes%2FTwoTowerPredictionOutputs%2FSpec&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerPredictionOutputs/Spec#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerPredictionOutputs/Spec#methods)
    *   [experimental\_as\_proto](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerPredictionOutputs/Spec#experimental_as_proto)
        
    *   [experimental\_from\_proto](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerPredictionOutputs/Spec#experimental_from_proto)
        
    *   [experimental\_type\_proto](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerPredictionOutputs/Spec#experimental_type_proto)
        
    *   [from\_value](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerPredictionOutputs/Spec#from_value)
        
    *   [is\_compatible\_with](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerPredictionOutputs/Spec#is_compatible_with)
        
    *   [is\_subtype\_of](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerPredictionOutputs/Spec#is_subtype_of)
        
    *   [most\_specific\_common\_supertype](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerPredictionOutputs/Spec#most_specific_common_supertype)
        
    *   [most\_specific\_compatible\_type](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerPredictionOutputs/Spec#most_specific_compatible_type)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerPredictionOutputs/Spec#__eq__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerPredictionOutputs/Spec#__ne__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.uplift.types.TwoTowerPredictionOutputs.Spec Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerPredictionOutputs/Spec#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerPredictionOutputs/Spec#methods)
    *   [experimental\_as\_proto](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerPredictionOutputs/Spec#experimental_as_proto)
        
    *   [experimental\_from\_proto](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerPredictionOutputs/Spec#experimental_from_proto)
        
    *   [experimental\_type\_proto](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerPredictionOutputs/Spec#experimental_type_proto)
        
    *   [from\_value](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerPredictionOutputs/Spec#from_value)
        
    *   [is\_compatible\_with](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerPredictionOutputs/Spec#is_compatible_with)
        
    *   [is\_subtype\_of](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerPredictionOutputs/Spec#is_subtype_of)
        
    *   [most\_specific\_common\_supertype](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerPredictionOutputs/Spec#most_specific_common_supertype)
        
    *   [most\_specific\_compatible\_type](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerPredictionOutputs/Spec#most_specific_compatible_type)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerPredictionOutputs/Spec#__eq__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerPredictionOutputs/Spec#__ne__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/types.py#L90-L91)

Base class for tf.ExtensionType TypeSpec.

tfm.uplift.types.TwoTowerPredictionOutputs.Spec(
        shared_embedding,
        control_logits,
        treatment_logits,
        control_predictions,
        treatment_predictions,
        uplift
    )

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `shape` |     |

Methods
-------

### `experimental_as_proto`

experimental_as_proto() -> struct_pb2.TypeSpecProto

Returns a proto representation of the TypeSpec instance.

Do NOT override for custom non-TF types.

### `experimental_from_proto`

@classmethod

Returns a TypeSpec instance based on the serialized proto.

Do NOT override for custom non-TF types.

|     |     |
| --- | --- |
| Args |     |
| `proto` | Proto generated using 'experimental\_as\_proto'. |

### `experimental_type_proto`

@classmethod

Returns the type of proto associated with TypeSpec serialization.

Do NOT override for custom non-TF types.

### `from_value`

@classmethod

### `is_compatible_with`

is_compatible_with(
        spec_or_value
    )

Returns true if `spec_or_value` is compatible with this TypeSpec.

Prefer using "is\_subtype\_of" and "most\_specific\_common\_supertype" wherever possible.

|     |     |
| --- | --- |
| Args |     |
| `spec_or_value` | A TypeSpec or TypeSpec associated value to compare against. |

### `is_subtype_of`

is_subtype_of(
        other: trace.TraceType
    ) -> bool

Returns True if `self` is a subtype of `other`.

Implements the tf.types.experimental.func.TraceType interface.

If not overridden by a subclass, the default behavior is to assume the TypeSpec is covariant upon attributes that implement TraceType and invariant upon rest of the attributes as well as the structure and type of the TypeSpec.

|     |     |
| --- | --- |
| Args |     |
| `other` | A TraceType object. |

### `most_specific_common_supertype`

most_specific_common_supertype(
        others: Sequence[trace.TraceType]
    ) -> Optional['TypeSpec']

Returns the most specific supertype TypeSpec of `self` and `others`.

Implements the tf.types.experimental.func.TraceType interface.

If not overridden by a subclass, the default behavior is to assume the TypeSpec is covariant upon attributes that implement TraceType and invariant upon rest of the attributes as well as the structure and type of the TypeSpec.

|     |     |
| --- | --- |
| Args |     |
| `others` | A sequence of TraceTypes. |

### `most_specific_compatible_type`

most_specific_compatible_type(
        other: 'TypeSpec'
    ) -> 'TypeSpec'

Returns the most specific TypeSpec compatible with `self` and `other`. (deprecated)

Deprecated. Please use `most_specific_common_supertype` instead. Do not override this function.

|     |     |
| --- | --- |
| Args |     |
| `other` | A `TypeSpec`. |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If there is no TypeSpec that is compatible with both `self` and `other`. |

### `__eq__`

__eq__(
        other
    ) -> bool

Return self==value.

### `__ne__`

__ne__(
        other
    ) -> bool

Return self!=value.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.