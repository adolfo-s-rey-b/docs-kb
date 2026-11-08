[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/IndexedSlicesSpec#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/IndexedSlicesSpec)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/IndexedSlicesSpec?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/IndexedSlicesSpec#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/IndexedSlicesSpec#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/IndexedSlicesSpec#methods)
    *   [experimental\_as\_proto](https://www.tensorflow.org/api_docs/python/tf/IndexedSlicesSpec#experimental_as_proto)
        
    *   [experimental\_from\_proto](https://www.tensorflow.org/api_docs/python/tf/IndexedSlicesSpec#experimental_from_proto)
        
    *   [experimental\_type\_proto](https://www.tensorflow.org/api_docs/python/tf/IndexedSlicesSpec#experimental_type_proto)
        
    *   [is\_compatible\_with](https://www.tensorflow.org/api_docs/python/tf/IndexedSlicesSpec#is_compatible_with)
        
    *   [is\_subtype\_of](https://www.tensorflow.org/api_docs/python/tf/IndexedSlicesSpec#is_subtype_of)
        
    *   [most\_specific\_common\_supertype](https://www.tensorflow.org/api_docs/python/tf/IndexedSlicesSpec#most_specific_common_supertype)
        
    *   [most\_specific\_compatible\_type](https://www.tensorflow.org/api_docs/python/tf/IndexedSlicesSpec#most_specific_compatible_type)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/IndexedSlicesSpec#__eq__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/IndexedSlicesSpec#__ne__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.IndexedSlicesSpec Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/IndexedSlicesSpec#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/IndexedSlicesSpec#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/IndexedSlicesSpec#methods)
    *   [experimental\_as\_proto](https://www.tensorflow.org/api_docs/python/tf/IndexedSlicesSpec#experimental_as_proto)
        
    *   [experimental\_from\_proto](https://www.tensorflow.org/api_docs/python/tf/IndexedSlicesSpec#experimental_from_proto)
        
    *   [experimental\_type\_proto](https://www.tensorflow.org/api_docs/python/tf/IndexedSlicesSpec#experimental_type_proto)
        
    *   [is\_compatible\_with](https://www.tensorflow.org/api_docs/python/tf/IndexedSlicesSpec#is_compatible_with)
        
    *   [is\_subtype\_of](https://www.tensorflow.org/api_docs/python/tf/IndexedSlicesSpec#is_subtype_of)
        
    *   [most\_specific\_common\_supertype](https://www.tensorflow.org/api_docs/python/tf/IndexedSlicesSpec#most_specific_common_supertype)
        
    *   [most\_specific\_compatible\_type](https://www.tensorflow.org/api_docs/python/tf/IndexedSlicesSpec#most_specific_compatible_type)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/IndexedSlicesSpec#__eq__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/IndexedSlicesSpec#__ne__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/indexed_slices.py#L203-L267)

Type specification for a [`tf.IndexedSlices`](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices)
.

Inherits From: [`TypeSpec`](https://www.tensorflow.org/api_docs/python/tf/TypeSpec)
, [`TraceType`](https://www.tensorflow.org/api_docs/python/tf/types/experimental/TraceType)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.IndexedSlicesSpec`](https://www.tensorflow.org/api_docs/python/tf/IndexedSlicesSpec)

tf.IndexedSlicesSpec(
        shape=None,
        dtype=tf.dtypes.float32,
        indices_dtype=tf.dtypes.int64,
        dense_shape_dtype=None,
        indices_shape=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `shape` | The dense shape of the `IndexedSlices`, or `None` to allow any dense shape. |
| `dtype` | [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br> of values in the `IndexedSlices`. |
| `indices_dtype` | [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br> of the `indices` in the `IndexedSlices`. One of [`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)<br> or [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br>. |
| `dense_shape_dtype` | [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br> of the `dense_shape` in the `IndexedSlices`. One of [`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)<br>, [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br>, or `None` (if the `IndexedSlices` has no `dense_shape` tensor). |
| `indices_shape` | The shape of the `indices` component, which indicates how many slices are in the `IndexedSlices`. |

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