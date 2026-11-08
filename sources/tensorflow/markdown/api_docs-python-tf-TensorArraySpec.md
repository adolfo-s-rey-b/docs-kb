[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/TensorArraySpec#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/TensorArraySpec)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/TensorArraySpec?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2FTensorArraySpec&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/TensorArraySpec#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/TensorArraySpec#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/TensorArraySpec#methods)
    *   [experimental\_as\_proto](https://www.tensorflow.org/api_docs/python/tf/TensorArraySpec#experimental_as_proto)
        
    *   [experimental\_from\_proto](https://www.tensorflow.org/api_docs/python/tf/TensorArraySpec#experimental_from_proto)
        
    *   [experimental\_type\_proto](https://www.tensorflow.org/api_docs/python/tf/TensorArraySpec#experimental_type_proto)
        
    *   [from\_value](https://www.tensorflow.org/api_docs/python/tf/TensorArraySpec#from_value)
        
    *   [is\_compatible\_with](https://www.tensorflow.org/api_docs/python/tf/TensorArraySpec#is_compatible_with)
        
    *   [is\_subtype\_of](https://www.tensorflow.org/api_docs/python/tf/TensorArraySpec#is_subtype_of)
        
    *   [most\_specific\_common\_supertype](https://www.tensorflow.org/api_docs/python/tf/TensorArraySpec#most_specific_common_supertype)
        
    *   [most\_specific\_compatible\_type](https://www.tensorflow.org/api_docs/python/tf/TensorArraySpec#most_specific_compatible_type)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/TensorArraySpec#__eq__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/TensorArraySpec#__ne__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.TensorArraySpec Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/TensorArraySpec#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/TensorArraySpec#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/TensorArraySpec#methods)
    *   [experimental\_as\_proto](https://www.tensorflow.org/api_docs/python/tf/TensorArraySpec#experimental_as_proto)
        
    *   [experimental\_from\_proto](https://www.tensorflow.org/api_docs/python/tf/TensorArraySpec#experimental_from_proto)
        
    *   [experimental\_type\_proto](https://www.tensorflow.org/api_docs/python/tf/TensorArraySpec#experimental_type_proto)
        
    *   [from\_value](https://www.tensorflow.org/api_docs/python/tf/TensorArraySpec#from_value)
        
    *   [is\_compatible\_with](https://www.tensorflow.org/api_docs/python/tf/TensorArraySpec#is_compatible_with)
        
    *   [is\_subtype\_of](https://www.tensorflow.org/api_docs/python/tf/TensorArraySpec#is_subtype_of)
        
    *   [most\_specific\_common\_supertype](https://www.tensorflow.org/api_docs/python/tf/TensorArraySpec#most_specific_common_supertype)
        
    *   [most\_specific\_compatible\_type](https://www.tensorflow.org/api_docs/python/tf/TensorArraySpec#most_specific_compatible_type)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/TensorArraySpec#__eq__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/TensorArraySpec#__ne__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/tensor_array_ops.py#L1363-L1491)

Type specification for a [`tf.TensorArray`](https://www.tensorflow.org/api_docs/python/tf/TensorArray)
.

Inherits From: [`TypeSpec`](https://www.tensorflow.org/api_docs/python/tf/TypeSpec)
, [`TraceType`](https://www.tensorflow.org/api_docs/python/tf/types/experimental/TraceType)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.TensorArraySpec`](https://www.tensorflow.org/api_docs/python/tf/TensorArraySpec)

tf.TensorArraySpec(
        element_shape=None,
        dtype=tf.dtypes.float32,
        dynamic_size=False,
        infer_shape=True
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `element_shape` | The shape of each element in the `TensorArray`. |
| `dtype` | Data type of the `TensorArray`. |
| `dynamic_size` | Whether the `TensorArray` can grow past its initial size. |
| `infer_shape` | Whether shape inference is enabled. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `value_type` |     |

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/tensor_array_ops.py#L1470-L1480)

@staticmethod

### `is_compatible_with`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/tensor_array_ops.py#L1425-L1434)

is_compatible_with(
        other
    )

Returns true if `spec_or_value` is compatible with this TypeSpec.

Prefer using "is\_subtype\_of" and "most\_specific\_common\_supertype" wherever possible.

|     |     |
| --- | --- |
| Args |     |
| `spec_or_value` | A TypeSpec or TypeSpec associated value to compare against. |

### `is_subtype_of`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/tensor_array_ops.py#L1390-L1394)

is_subtype_of(
        other
    )

Returns True if `self` is a subtype of `other`.

Implements the tf.types.experimental.func.TraceType interface.

If not overridden by a subclass, the default behavior is to assume the TypeSpec is covariant upon attributes that implement TraceType and invariant upon rest of the attributes as well as the structure and type of the TypeSpec.

|     |     |
| --- | --- |
| Args |     |
| `other` | A TraceType object. |

### `most_specific_common_supertype`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/tensor_array_ops.py#L1396-L1423)

most_specific_common_supertype(
        others
    )

Returns the most specific supertype of `self` and `others`.

|     |     |
| --- | --- |
| Args |     |
| `others` | A Sequence of `TypeSpec`. |

Returns `None` if a supertype does not exist.

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