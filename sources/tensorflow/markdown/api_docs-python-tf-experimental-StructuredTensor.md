[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Examples](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#examples)
    
*   [Field Paths](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#field_paths)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#attributes)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#child_classes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#methods)
    *   [field\_names](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#field_names)
        
    *   [field\_value](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#field_value)
        
    *   [from\_fields](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#from_fields)
        
    *   [from\_fields\_and\_rank](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#from_fields_and_rank)
        
    *   [from\_pyval](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#from_pyval)
        
    *   [from\_shape](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#from_shape)
        
    *   [merge\_dims](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#merge_dims)
        
    *   [nrows](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#nrows)
        
    *   [partition\_outer\_dimension](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#partition_outer_dimension)
        
    *   [promote](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#promote)
        
    *   [to\_pyval](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#to_pyval)
        
    *   [with\_shape\_dtype](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#with_shape_dtype)
        
    *   [with\_updates](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#with_updates)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#__eq__)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#__getitem__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#__ne__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.StructuredTensor Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Examples](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#examples)
    
*   [Field Paths](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#field_paths)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#attributes)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#child_classes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#methods)
    *   [field\_names](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#field_names)
        
    *   [field\_value](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#field_value)
        
    *   [from\_fields](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#from_fields)
        
    *   [from\_fields\_and\_rank](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#from_fields_and_rank)
        
    *   [from\_pyval](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#from_pyval)
        
    *   [from\_shape](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#from_shape)
        
    *   [merge\_dims](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#merge_dims)
        
    *   [nrows](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#nrows)
        
    *   [partition\_outer\_dimension](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#partition_outer_dimension)
        
    *   [promote](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#promote)
        
    *   [to\_pyval](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#to_pyval)
        
    *   [with\_shape\_dtype](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#with_shape_dtype)
        
    *   [with\_updates](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#with_updates)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#__eq__)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#__getitem__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor#__ne__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/structured/structured_tensor.py#L59-L1187)

A multidimensional collection of structures with the same schema.

Inherits From: [`BatchableExtensionType`](https://www.tensorflow.org/api_docs/python/tf/experimental/BatchableExtensionType)
, [`ExtensionType`](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionType)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.experimental.StructuredTensor`](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor)

tf.experimental.StructuredTensor(
        fields: Mapping[str, _FieldValue],
        ragged_shape: dynamic_ragged_shape.DynamicRaggedShape
    )

A **`StructuredTensor`** is a multi-dimensional collection of **_structures_** with the same **_schema_**, where:

*   A **_schema_** is a collection of fields, each of which has a name and type.
*   A **_structure_** maps each field in the schema to a tensor value (which could be a nested StructuredTensor).

As an important special case, a 1D `StructuredTensor` encodes a 2D table, where columns are heterogeneous `Tensor`s, and rows are the aligned elements in each of those `Tensor`s.

Internally, StructuredTensors use a "field-major" encoding: for each leaf field, there is a single tensor that stores the value of that field for all structures in the `StructuredTensor`.

### Examples

    # A scalar StructuredTensor describing a single person.

    # A vector StructuredTensor describing three people.

### Field Paths

A _field path_ is a tuple of field names, specifying the path to a nested field.

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `rank` | The rank of this StructuredTensor. Guaranteed not to be `None`. |
| `row_partitions` | A tuple of `RowPartition`s defining the shape of this `StructuredTensor`.<br><br>When `self.rank <= 1`, this tuple will be empty.<br><br>When `self.rank > 1`, these `RowPartitions` define the shape of the `StructuredTensor` by describing how a flat (1D) list of structures can be repeatedly partitioned to form a higher-dimensional object. In particular, the flat list is first partitioned into sublists using `row_partitions[-1]`, and then those sublists are further partitioned using `row_partitions[-2]`, etc. The following examples show the row partitions used to describe several different `StructuredTensor`, each of which contains 8 copies of the same structure (`x`):<br><br>    x = {'a': 1, 'b': ['foo', 'bar', 'baz']}       # shape = [] (scalar)<br><br>    s1 = [[x, x, x, x], [x, x, x, x]]              # shape = [2, 4]<br><br>    s2 = [[x, x], [x, x], [x, x], [x, x]]          # shape = [4, 2]<br><br>    s3 = [[x, x, x], [], [x, x, x, x], [x]]        # shape = [2, None]<br><br>    s4 = [[[x, x], [x, x]], [[x, x], [x, x]]]      # shape = [2, 2, 2]<br><br>    s5 = [[[x, x], [x]], [[x, x]], [[x, x], [x]]]  # shape = [3, None, None]<br><br>Note that shapes for nested fields (such as `x['b']` in the above example) are not considered part of the shape of a `StructuredTensor`, and are not included in `row_partitions`.<br><br>If this `StructuredTensor` has a ragged shape (i.e., if any of the `row_partitions` is not uniform in size), then all fields will be encoded as either `RaggedTensor`s or `StructuredTensor`s with these `RowPartition`s used to define their outermost `self.rank` dimensions. |
| `shape` | The static shape of this StructuredTensor.<br><br>The returned `TensorShape` is guaranteed to have a known rank, but the individual dimension sizes may be unknown. |

Child Classes
-------------

[`class Spec`](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor/Spec)

Methods
-------

### `field_names`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/structured/structured_tensor.py#L678-L680)

field_names()

Returns the string field names for this `StructuredTensor`.

### `field_value`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/structured/structured_tensor.py#L682-L714)

field_value(
        field_name
    )

Returns the tensor value for the specified field or path.

If `field_name` is a `string`, then it names a field directly owned by this `StructuredTensor`. If this `StructuredTensor` has shape `[D1...DN]`, then the returned tensor will have shape `[D1...DN, V1...VM]`, where the slice `result[d1...dN]` contains the field value for the structure at `self[d1...dN]`.

If `field_name` is a `tuple` of `string`, then it specifies a path to a field owned by nested `StructuredTensor`. In particular, `struct.field_value((f1, f2, ..., fN))` is equivalent to `struct.field_value(f1).field_value(f2)....field_value(fN)`

|     |     |
| --- | --- |
| Args |     |
| `field_name` | `string` or `tuple` of `string`: The field whose values should be returned. |

|     |
| --- |
| Returns |     |
| `Tensor`, `StructuredTensor`, or `RaggedTensor`. |     |

|     |     |
| --- | --- |
| Raises |     |
| `KeyError` | If the given field\_name is not found. |

### `from_fields`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/structured/structured_tensor.py#L160-L248)

@classmethod

Creates a `StructuredTensor` from a dictionary of fields.

|     |     |
| --- | --- |
| Args |     |
| `fields` | A dictionary mapping from string to `Tensor`, `RaggedTensor`, or `StructuredTensor`, providing the values for individual fields in each structure. If `shape.rank > 0`, then every tensor in `fields` must have the same shape in the first `shape.rank` dimensions; and that shape must be compatible with `shape`; and `result[i1...iN][key] = fields[key][i1...iN]` (where `N==shape.rank`). |
| `shape` | A `TensorShape`: static information about the shape of the `StructuredTensor`. Must have a known `rank`. Defaults to scalar shape (i.e. `rank=0`). |
| `nrows` | scalar integer tensor containing the number of rows in this `StructuredTensor`. Should only be specified if `shape.rank > 0`. Default value is inferred from the `fields` values. If `fields` is empty, then this must be specified. |
| `row_partitions` | A list of `RowPartition`s describing the (possibly ragged) shape of this `StructuredTensor`. Should only be specified if `shape.rank > 1`. Default value is inferred from the `fields` values. If `fields` is empty, then this must be specified. |
| `validate` | If true, then add runtime validation ops that check that the field values all have compatible shapes in the outer `shape.rank` dimensions. |

|     |
| --- |
| Returns |     |
| A `StructuredTensor`. |     |

|     |
| --- |
| Examples |     |
| >>> tf.experimental.StructuredTensor.from_fields({'x': 1, 'y': [1, 2, 3]})<br>    <StructuredTensor(<br>      fields={<br>        "x": tf.Tensor(1, shape=(), dtype=int32),<br>        "y": tf.Tensor([1 2 3], shape=(3,), dtype=int32)},<br>      shape=())><br><br>    tf.experimental.StructuredTensor.from_fields( |     |

### `from_fields_and_rank`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/structured/structured_tensor.py#L250-L315)

@classmethod

Creates a `StructuredTensor` from a nonempty dictionary of fields.

Note that if the shape dtype is not specified, the shape dtype will be inferred from any fields that have a shape dtype. If fields differ, then int64 will be preferred to int32, because coercing from int32 to int64 is safer than coercing from int64 to int32.

If there are no ragged fields, then it will be int64 by default, but this will be changed to int32 in the future.

|     |     |
| --- | --- |
| Args |     |
| `fields` | A dictionary mapping from string to `Tensor`, `RaggedTensor`, or `StructuredTensor`, providing the values for individual fields in each structure. If `rank > 0`, then every tensor in `fields` must have the same shape in the first `rank` dimensions. Cannot be empty. |
| `rank` | The rank of the resulting structured tensor. |
| `validate` | If true, then add runtime validation ops that check that the field values all have compatible shapes in the outer `rank` dimensions. |
| `dtype` | If specified, then forces dtype of the shape to be this. |

|     |
| --- |
| Returns |     |
| A `StructuredTensor`. |     |

|     |
| --- |
| Examples |     |
| >>> tf.experimental.StructuredTensor.from_fields_and_rank(<br>    ...     {'x': 1, 'y': [1, 2, 3]}, 0)<br>    <StructuredTensor(<br>      fields={<br>        "x": tf.Tensor(1, shape=(), dtype=int32),<br>        "y": tf.Tensor([1 2 3], shape=(3,), dtype=int32)},<br>      shape=())><br>    >>> StructuredTensor.from_fields_and_rank({'foo': [1, 2], 'bar': [3, 4]},<br>    ...                              1)<br>    <StructuredTensor(<br>      fields={<br>        "bar": tf.Tensor([3 4], shape=(2,), dtype=int32),<br>        "foo": tf.Tensor([1 2], shape=(2,), dtype=int32)},<br>      shape=(2,))> |     |

### `from_pyval`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/structured/structured_tensor.py#L878-L903)

@classmethod

Constructs a StructuredTensor from a nested Python structure.

    tf.experimental.StructuredTensor.from_pyval(

Note that `StructuredTensor.from_pyval(pyval).to_pyval() == pyval`.

|     |     |
| --- | --- |
| Args |     |
| `pyval` | The nested Python structure that should be used to create the new `StructuredTensor`. |
| `typespec` | A [`StructuredTensor.Spec`](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor/Spec)<br> specifying the expected type for each field. If not specified, then all nested dictionaries are turned into StructuredTensors, and all nested lists are turned into Tensors (if rank<2) or RaggedTensors (if rank>=2). |

|     |
| --- |
| Returns |     |
| A `StructuredTensor`. |     |

### `from_shape`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/structured/structured_tensor.py#L146-L158)

@classmethod

Creates a `StructuredTensor` with no fields and ragged\_shape.

|     |     |
| --- | --- |
| Args |     |
| `ragged_shape` | the shape of the structured tensor. |

|     |
| --- |
| Returns |     |
| a StructuredTensor with no fields and ragged\_shape. |     |

### `merge_dims`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/structured/structured_tensor.py#L1096-L1135)

merge_dims(
        outer_axis, inner_axis
    )

Merges outer\_axis...inner\_axis into a single dimension.

Returns a copy of this RaggedTensor with the specified range of dimensions flattened into a single dimension, with elements in row-major order.

    st = tf.experimental.StructuredTensor.from_pyval(

|     |     |
| --- | --- |
| Args |     |
| `outer_axis` | `int`: The first dimension in the range of dimensions to merge. May be negative (to index from the last dimension). |
| `inner_axis` | `int`: The last dimension in the range of dimensions to merge. May be negative (to index from the last dimension). |

|     |
| --- |
| Returns |     |
| A copy of this tensor, with the specified dimensions merged into a single dimension. The shape of the returned tensor will be `self.shape[:outer_axis] + [N] + self.shape[inner_axis + 1:]`, where `N` is the total number of slices in the merged dimensions. |     |

### `nrows`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/structured/structured_tensor.py#L644-L660)

nrows()

The number of rows in this StructuredTensor (if rank>0).

This means the length of the outer-most dimension of the StructuredTensor.

Notice that if `self.rank > 1`, then this equals the number of rows of the first row partition. That is, `self.nrows() == self.row_partitions[0].nrows()`.

Otherwise `self.nrows()` will be the first dimension of the field values.

|     |
| --- |
| Returns |     |
| A scalar integer `Tensor` (or `None` if `self.rank == 0`). |     |

### `partition_outer_dimension`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/structured/structured_tensor.py#L1067-L1094)

partition_outer_dimension(
        row_partition
    )

Partitions the outer dimension of this StructuredTensor.

Returns a new `StructuredTensor` with the same values as `self`, where the outer dimension is partitioned into two (possibly ragged) dimensions. Requires that this StructuredTensor have an outer dimension (i.e., `self.shape.rank > 0`).

    st = tf.experimental.StructuredTensor.from_pyval(

|     |     |
| --- | --- |
| Args |     |
| `row_partition` | A `RowPartition`. |

|     |
| --- |
| Returns |     |
| A `StructuredTensor` with rank `values.rank + 1`. |     |

### `promote`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/structured/structured_tensor.py#L517-L555)

promote(
        source_path, new_name
    )

Promotes a field, merging dimensions between grandparent and parent.

    d = [\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `source_path` | the path of the field or substructure to promote; must have length at least 2. |\
| `new_name` | the name of the new field (must be a string). |\
\
|     |\
| --- |\
| Returns |     |\
| a modified structured tensor with the new field as a child of the grandparent of the source\_path. |     |\
\
|     |     |\
| --- | --- |\
| Raises |     |\
| `ValueError` | if source\_path is not a list or a tuple or has a length less than two, or new\_name is not a string, or the rank of source\_path is unknown and it is needed. |\
\
### `to_pyval`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/structured/structured_tensor.py#L820-L876)\
\
to_pyval()\
\
Returns this StructuredTensor as a nested Python dict or list of dicts.\
\
Converts this `StructuredTensor` to a nested python value:\
\
*   `StructTensors` with `rank=0` are converted into a dictionary, with an entry for each field. Field names are used as keys and field values are converted to python values. In particular:\
    \
    *   Scalar Tensor fields are converted to simple values (such as `int` or `float` or `string`)\
    *   Non-scalar Tensor fields and RaggedTensor fields are converted to nested lists of simple values.\
    *   StructuredTensor fields are converted recursively using `to_pyval`.\
*   `StructTensors` with `rank>0` are converted to nested python `list`s, containing one dictionary for each structure (where each structure's dictionary is defined as described above).\
    \
\
Requires that all fields are Eager tensors.\
\
    tf.experimental.StructuredTensor.from_fields(\
\
Note that `StructuredTensor.from_pyval(pyval).to_pyval() == pyval`.\
\
|     |\
| --- |\
| Returns |     |\
| A nested Python dict or list of dicts. |     |\
\
### `with_shape_dtype`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/structured/structured_tensor.py#L662-L667)\
\
with_shape_dtype(\
        dtype: dtypes.DType\
    ) -> 'StructuredTensor'\
\
### `with_updates`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/structured/structured_tensor.py#L317-L404)\
\
with_updates(\
        updates: Dict[FieldName, Union[_FieldValue, _FieldFn, None]],\
        validate: bool = False\
    ) -> 'StructuredTensor'\
\
Creates a new `StructuredTensor` with the updated fields.\
\
If this `StructuredTensor` is a scalar, and `k` is the `FieldName` being updated and `v` the new value, then:\
\
result[k] = v              # If (k, v) is in updates and v is a FieldValue\
    result[k] = f(self[k])     # If (k, f) is in updates and f is a FieldFn\
    result[k] = self[k]        # If k is in self.field_names but not in updates\
\
If this `StructuredTensor` has rank `N` and shape `[D1...DN]`, then each FieldValue `v` in `updates` must have shape `[D1...DN, ...]`, that is, prefixed with the same shape as the `StructuredTensor`. Then the resulting `StructuredTensor` will have:\
\
result[i1...iN][k] = v[i1...iN]                        # (k, v) in updates\
    result[i1...iN][k] = f(self.field_value(k))[i1...iN]   # (k, f) in updates\
    result[i1...iN][k] = self[i1...iN][k]                  # k not in updates\
\
Note that `result.shape` is always equal to `self.shape` (but the shapes of nested StructuredTensors may be changed if they are updated with new values).\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `updates` | A dictionary mapping `FieldName` to either a `FieldValue` to be used to update, or a `FieldFn` that will transform the value for the given `FieldName`. `FieldName` can be a string for a direct field, or a sequence of strings to refer to a nested sub-field. `FieldFn` is a function that takes a `FieldValue` as input and should return a `FieldValue`. All other fields are copied over to the new `StructuredTensor`. New `FieldName` can be given (to add new fields), but only to existing `StructuredTensor`, it won't automatically create new nested structures -- but one can create a whole `StructureTensor` sub-structure and set that into an existing structure. If the new value is set to `None`, it is removed. |\
| `validate` | If true, then add runtime validation ops that check that the field values all have compatible shapes in the outer `shape.rank` dimensions. |\
\
|     |\
| --- |\
| Returns |     |\
| A `StructuredTensor`. |     |\
\
|     |\
| --- |\
| Raises |     |\
| `ValueError`: If the any of the `FieldName` keys points to non-existent sub-structures, if parent and child nodes are updated, if shapes change, if a delete update is given for a non-existent field, or if a `FieldFn` transforming function is given for a `FieldName` that doesn't yet exist. |     |\
\
#### Examples:\
\
    shoes_us = tf.experimental.StructuredTensor.from_pyval([\
\
### `__eq__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/extension_type.py#L276-L305)\
\
__eq__(\
        other\
    )\
\
Return self==value.\
\
### `__getitem__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/structured/structured_tensor.py#L721-L764)\
\
__getitem__(\
        key\
    )\
\
Returns the specified piece of this StructuredTensor.\
\
*   If `struct_tensor` is scalar (i.e., a single structure), then `struct_tensor[f]` returns the value of field `f` (where `f` must be a string).\
    \
*   If `struct_tensor` is non-scalar (i.e., a vector or higher-dimensional tensor of structures), `struct_tensor[i]` selects an element or slice of the tensor using standard Python semantics (e.g., negative values index from the end). `i` may have any of the following types:\
    \
    *   `int` constant\
    *   `string` constant\
    *   scalar integer `Tensor`\
    *   `slice` containing integer constants and/or scalar integer `Tensor`s\
\
#### Multidimensional indexing\
\
`StructuredTensor` supports multidimensional indexing. I.e., `key` may be a `tuple` of values, indexing or slicing multiple dimensions at once. For example, if `people` is a vector of structures, each of which has a vector- valued `names` field, then `people[3, 'names', 0]` is equivalent to `people[3]['names'][0]`; and `people[:, 'names', :]` will return a (possibly ragged) matrix of names, with shape `[num_people, num_names_per_person]`.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `key` | Indicates which piece of the StructuredTensor to return. |\
\
|     |\
| --- |\
| Returns |     |\
| A `Tensor`, `StructuredTensor`, or `RaggedTensor`. |     |\
\
### `__ne__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/extension_type.py#L307-L312)\
\
__ne__(\
        other\
    )\
\
Return self!=value.\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.