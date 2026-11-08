[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType#methods)
    *   [experimental\_as\_proto](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType#experimental_as_proto)
        
    *   [experimental\_from\_proto](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType#experimental_from_proto)
        
    *   [experimental\_type\_proto](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType#experimental_type_proto)
        
    *   [is\_compatible\_with](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType#is_compatible_with)
        
    *   [is\_subtype\_of](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType#is_subtype_of)
        
    *   [most\_specific\_common\_supertype](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType#most_specific_common_supertype)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType#__eq__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType#__ne__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.dtypes.DType Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType#methods)
    *   [experimental\_as\_proto](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType#experimental_as_proto)
        
    *   [experimental\_from\_proto](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType#experimental_from_proto)
        
    *   [experimental\_type\_proto](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType#experimental_type_proto)
        
    *   [is\_compatible\_with](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType#is_compatible_with)
        
    *   [is\_subtype\_of](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType#is_subtype_of)
        
    *   [most\_specific\_common\_supertype](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType#most_specific_common_supertype)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType#__eq__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType#__ne__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/dtypes.py#L51-L288)

Represents the type of the elements in a `Tensor`.

Inherits From: [`TraceType`](https://www.tensorflow.org/api_docs/python/tf/types/experimental/TraceType)

#### View aliases

**Main aliases**

[`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)
, [`tf.compat.v1.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)

tf.dtypes.DType(
        type_enum, handle_data=None
    )

`DType`'s are used to specify the output data type for operations which require it, or to inspect the data type of existing `Tensor`'s.

#### Examples:

    tf.constant(1, dtype=tf.int64)

See [`tf.dtypes`](https://www.tensorflow.org/api_docs/python/tf/dtypes)
 for a complete list of `DType`'s defined.

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `as_datatype_enum` | Returns a `types_pb2.DataType` enum value based on this data type. |
| `as_numpy_dtype` | Returns a Python `type` object based on this `DType`. |
| `base_dtype` | Returns a non-reference `DType` based on this `DType` (for TF1).<br><br>Programs written for TensorFlow 2.x do not need this attribute. It exists only for compatibility with TensorFlow 1.x, which used reference `DType`s in the implementation of [`tf.compat.v1.Variable`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Variable)<br>. In TensorFlow 2.x, [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)<br> is implemented without reference types. |
| `is_bool` | Returns whether this is a boolean data type. |
| `is_complex` | Returns whether this is a complex floating point type. |
| `is_floating` | Returns whether this is a (non-quantized, real) floating point type. |
| `is_integer` | Returns whether this is a (non-quantized) integer type. |
| `is_numeric` | Returns whether this is a numeric data type. |
| `is_numpy_compatible` | Returns whether this data type has a compatible NumPy data type. |
| `is_quantized` | Returns whether this is a quantized data type. |
| `is_unsigned` | Returns whether this type is unsigned.<br><br>Non-numeric, unordered, and quantized types are not considered unsigned, and this function returns `False`. |
| `limits` | Return intensity limits, i.e.<br><br>(min, max) tuple, of the dtype. Args: clip\_negative : bool, optional If True, clip the negative range (i.e. return 0 for min intensity) even if the image dtype allows negative values. Returns min, max : tuple Lower and upper intensity limits. |
| `max` | Returns the maximum representable value in this data type. |
| `min` | Returns the minimum representable value in this data type. |
| `name` |     |
| `real_dtype` | Returns the `DType` corresponding to this `DType`'s real part. |
| `size` |     |

Methods
-------

### `experimental_as_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/dtypes.py#L260-L262)

experimental_as_proto() -> types_pb2.SerializedDType

Returns a proto representation of the Dtype instance.

### `experimental_from_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/dtypes.py#L255-L258)

@classmethod

Returns a Dtype instance based on the serialized proto.

### `experimental_type_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/dtypes.py#L250-L253)

@classmethod

Returns the type of proto associated with DType serialization.

### `is_compatible_with`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/dtypes.py#L194-L214)

is_compatible_with(
        other
    )

Returns True if the `other` DType will be converted to this DType (TF1).

Programs written for TensorFlow 2.x do not need this function. Instead, they can do equality comparison on `DType` objects directly: `tf.as_dtype(this) == tf.as_dtype(other)`.

This function exists only for compatibility with TensorFlow 1.x, where it additionally allows conversion from a reference type (used by [`tf.compat.v1.Variable`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Variable)
) to its base type.

|     |     |
| --- | --- |
| Args |     |
| `other` | A `DType` (or object that may be converted to a `DType`). |

|     |
| --- |
| Returns |     |
| True if a Tensor of the `other` `DType` will be implicitly converted to this `DType`. |     |

### `is_subtype_of`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/dtypes.py#L216-L218)

is_subtype_of(
        other: tf.types.experimental.TraceType
    ) -> bool

See tf.types.experimental.TraceType base class.

### `most_specific_common_supertype`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/dtypes.py#L220-L223)

most_specific_common_supertype(
        types: Sequence[tf.types.experimental.TraceType]
    ) -> Optional['DType']

See tf.types.experimental.TraceType base class.

### `__eq__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/dtypes.py#L264-L275)

__eq__(
        other
    )

Returns True iff this DType refers to the same type as `other`.

### `__ne__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/dtypes.py#L277-L279)

__ne__(
        other
    )

Returns True iff self != other.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.