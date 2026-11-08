[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/NoneTensorSpec#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/NoneTensorSpec)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/NoneTensorSpec?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2FNoneTensorSpec&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/NoneTensorSpec#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/NoneTensorSpec#methods)
    *   [experimental\_as\_proto](https://www.tensorflow.org/api_docs/python/tf/NoneTensorSpec#experimental_as_proto)
        
    *   [experimental\_from\_proto](https://www.tensorflow.org/api_docs/python/tf/NoneTensorSpec#experimental_from_proto)
        
    *   [experimental\_type\_proto](https://www.tensorflow.org/api_docs/python/tf/NoneTensorSpec#experimental_type_proto)
        
    *   [from\_value](https://www.tensorflow.org/api_docs/python/tf/NoneTensorSpec#from_value)
        
    *   [is\_compatible\_with](https://www.tensorflow.org/api_docs/python/tf/NoneTensorSpec#is_compatible_with)
        
    *   [is\_subtype\_of](https://www.tensorflow.org/api_docs/python/tf/NoneTensorSpec#is_subtype_of)
        
    *   [most\_specific\_common\_supertype](https://www.tensorflow.org/api_docs/python/tf/NoneTensorSpec#most_specific_common_supertype)
        
    *   [most\_specific\_compatible\_shape](https://www.tensorflow.org/api_docs/python/tf/NoneTensorSpec#most_specific_compatible_shape)
        
    *   [most\_specific\_compatible\_type](https://www.tensorflow.org/api_docs/python/tf/NoneTensorSpec#most_specific_compatible_type)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/NoneTensorSpec#__eq__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/NoneTensorSpec#__ne__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.NoneTensorSpec Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/NoneTensorSpec#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/NoneTensorSpec#methods)
    *   [experimental\_as\_proto](https://www.tensorflow.org/api_docs/python/tf/NoneTensorSpec#experimental_as_proto)
        
    *   [experimental\_from\_proto](https://www.tensorflow.org/api_docs/python/tf/NoneTensorSpec#experimental_from_proto)
        
    *   [experimental\_type\_proto](https://www.tensorflow.org/api_docs/python/tf/NoneTensorSpec#experimental_type_proto)
        
    *   [from\_value](https://www.tensorflow.org/api_docs/python/tf/NoneTensorSpec#from_value)
        
    *   [is\_compatible\_with](https://www.tensorflow.org/api_docs/python/tf/NoneTensorSpec#is_compatible_with)
        
    *   [is\_subtype\_of](https://www.tensorflow.org/api_docs/python/tf/NoneTensorSpec#is_subtype_of)
        
    *   [most\_specific\_common\_supertype](https://www.tensorflow.org/api_docs/python/tf/NoneTensorSpec#most_specific_common_supertype)
        
    *   [most\_specific\_compatible\_shape](https://www.tensorflow.org/api_docs/python/tf/NoneTensorSpec#most_specific_compatible_shape)
        
    *   [most\_specific\_compatible\_type](https://www.tensorflow.org/api_docs/python/tf/NoneTensorSpec#most_specific_compatible_type)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/NoneTensorSpec#__eq__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/NoneTensorSpec#__ne__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/none_tensor.py#L33-L84)

Type specification for `None` value.

Inherits From: [`TypeSpec`](https://www.tensorflow.org/api_docs/python/tf/TypeSpec)
, [`TraceType`](https://www.tensorflow.org/api_docs/python/tf/types/experimental/TraceType)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.NoneTensorSpec`](https://www.tensorflow.org/api_docs/python/tf/NoneTensorSpec)

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `value_type` | The Python type for values that are compatible with this TypeSpec.<br><br>In particular, all values that are compatible with this TypeSpec must be an instance of this type. |

Methods
-------

### `experimental_as_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/type_spec.py#L217-L222)

experimental_as_proto() -> struct_pb2.TypeSpecProto

Returns a proto representation of the TypeSpec instance.

Do NOT override for custom non-TF types.

### `experimental_from_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/type_spec.py#L204-L215)

@classmethod

Returns a TypeSpec instance based on the serialized proto.

Do NOT override for custom non-TF types.

|     |     |
| --- | --- |
| Args |     |
| `proto` | Proto generated using 'experimental\_as\_proto'. |

### `experimental_type_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/type_spec.py#L196-L202)

@classmethod

Returns the type of proto associated with TypeSpec serialization.

Do NOT override for custom non-TF types.

### `from_value`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/none_tensor.py#L58-L60)

@staticmethod

### `is_compatible_with`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/type_spec.py#L300-L321)

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/type_spec.py#L109-L146)

is_subtype_of(
        other: tf.types.experimental.TraceType
    ) -> bool

Returns True if `self` is a subtype of `other`.

Implements the tf.types.experimental.func.TraceType interface.

If not overridden by a subclass, the default behavior is to assume the TypeSpec is covariant upon attributes that implement TraceType and invariant upon rest of the attributes as well as the structure and type of the TypeSpec.

|     |     |
| --- | --- |
| Args |     |
| `other` | A TraceType object. |

### `most_specific_common_supertype`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/type_spec.py#L148-L194)

most_specific_common_supertype(
        others: Sequence[tf.types.experimental.TraceType]
    ) -> Optional['TypeSpec']

Returns the most specific supertype TypeSpec of `self` and `others`.

Implements the tf.types.experimental.func.TraceType interface.

If not overridden by a subclass, the default behavior is to assume the TypeSpec is covariant upon attributes that implement TraceType and invariant upon rest of the attributes as well as the structure and type of the TypeSpec.

|     |     |
| --- | --- |
| Args |     |
| `others` | A sequence of TraceTypes. |

### `most_specific_compatible_shape`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/none_tensor.py#L80-L84)

most_specific_compatible_shape(
        other
    )

### `most_specific_compatible_type`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/type_spec.py#L323-L341)

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/type_spec.py#L545-L548)

__eq__(
        other
    ) -> bool

Return self==value.

### `__ne__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/type_spec.py#L550-L551)

__ne__(
        other
    ) -> bool

Return self!=value.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.