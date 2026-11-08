[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fexperimental%2FDynamicRaggedShape%3Fversion%3Dstable&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape?version=stable#args_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape?version=stable#attributes_1)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape?version=stable#child_classes_2)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape?version=stable#methods_2)
    *   [from\_lengths](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape?version=stable#from_lengths)
        
    *   [from\_row\_partitions](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape?version=stable#from_row_partitions)
        
    *   [from\_tensor](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape?version=stable#from_tensor)
        
    *   [is\_uniform](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape?version=stable#is_uniform)
        
    *   [static\_lengths](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape?version=stable#static_lengths)
        
    *   [with\_dtype](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape?version=stable#with_dtype)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape?version=stable#__eq__)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape?version=stable#__getitem__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape?version=stable#__ne__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.DynamicRaggedShape Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape?version=stable#args_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape?version=stable#attributes_1)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape?version=stable#child_classes_2)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape?version=stable#methods_2)
    *   [from\_lengths](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape?version=stable#from_lengths)
        
    *   [from\_row\_partitions](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape?version=stable#from_row_partitions)
        
    *   [from\_tensor](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape?version=stable#from_tensor)
        
    *   [is\_uniform](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape?version=stable#is_uniform)
        
    *   [static\_lengths](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape?version=stable#static_lengths)
        
    *   [with\_dtype](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape?version=stable#with_dtype)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape?version=stable#__eq__)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape?version=stable#__getitem__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape?version=stable#__ne__)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/dynamic_ragged_shape.py#L167-L1588)

The shape of a ragged or dense tensor.

Inherits From: [`BatchableExtensionType`](https://www.tensorflow.org/api_docs/python/tf/experimental/BatchableExtensionType)
, [`ExtensionType`](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionType)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.experimental.DynamicRaggedShape`](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape)

tf.experimental.DynamicRaggedShape(
        row_partitions: Sequence[tf.experimental.RowPartition],
        inner_shape: tf.types.experimental.TensorLike,
        dtype: Optional[tf.dtypes.DType] = None,
        validate: bool = False,
        static_inner_shape: ... = None
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Ragged tensors](https://www.tensorflow.org/guide/ragged_tensor) |

Ragged shapes are encoded using two fields:

*   `inner_shape`: An integer vector giving the shape of a dense tensor.
*   `row_partitions`: A list of `RowPartition` objects, describing how that flat shape should be partitioned to add ragged axes.

If a DynamicRaggedShape is the shape of a RaggedTensor rt, then:

1.  row\_partitions = rt.\_nested\_row\_partitions (and thus len(row\_partitions) > 0)
2.  inner\_shape is the shape of rt.flat\_values

If a DynamicRaggedShape is the shape of a dense tensor t, then:

1.  row\_partitions = \[\]
2.  inner\_shape is the shape of t.

#### Examples:

The following table gives a few examples (where `RP(lengths)` is short for `RowPartition.from_lengths(lengths)`):

| Row Partitions | Inner Shape | Example Tensor |
| --- | --- | --- |
| \[\] | \[2, 3\] | `[[1, 2, 3], [4, 5, 6]]` |
| \[RP(\[2, 0, 3\])\] | \[5\] | `[[1, 2], [], [3, 4, 5]]` |
| \[RP(\[2, 1\])\] | \[3, 2\] | `[[[1, 2], [3, 4]], [[5, 6]]]` |
| \[RP(\[2, 1\]), RP(\[2, 1, 2\])\] | \[5\] | `[[[1, 2], [3]], [[4, 5]]]` |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `row_partitions` | the row\_partitions of the shape. |
| `inner_shape` | if len(row\_partitions) > 0, the shape of the flat\_values. Otherwise, the shape of the tensor. |
| `dtype` | tf.int64, tf.int32, or None representing the preferred dtype. |
| `validate` | if true, dynamic validation is applied to the shape. |
| `static_inner_shape` | if len(row\_partitions) > 0, the static shape of the flat\_values. Otherwise, the static shape of the tensor. Should be convertible to a TensorShape. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `dtype` | The dtype of the shape -- one of tf.int32 or tf.int64. |
| `inner_rank` | The rank of inner\_shape. |
| `inner_shape` | The inner dimension sizes for this shape. |
| `num_row_partitions` | The number of row\_partitions of the shape. |
| `rank` | The number of dimensions in this shape, or None if unknown. |
| `row_partitions` | The row\_partitions of the shape. |

Child Classes
-------------

[`class Spec`](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape/Spec)

Methods
-------

### `from_lengths`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/dynamic_ragged_shape.py#L308-L407)

@classmethod

Creates a shape with the given lengths and num\_row\_partitions.

The lengths can either be a nonnegative int or a list of nonnegative ints.

If num\_row\_partitions is None, then the minimal num\_row\_partitions is used.

For example, \[2, (3, 2)\] is the shape of \[\[0, 0, 0\], \[0, 0\]\], and \[2, 2\] is the shape of \[\[0, 0\], \[0, 0\]\]

This chooses the minimal num\_row\_partitions required (including zero).

The following table gives a few examples (where `RP(lengths)` is short for `RowPartition.from_lengths(lengths)`):

#### For example:

| from\_lengths | row\_partitions | inner\_shape |
| --- | --- | --- |
| \[\] | \[\] | \[\] |
| \[2, (3, 2)\] | \[RP(\[3, 2\])\] | \[5\] |
| \[2, 2\] | \[\] | \[2, 2\] |
| \[2, (3, 2), 7\] | \[RP(\[3, 2\])\] | \[5, 7\] |
| \[2, (2, 2), 3\] | \[RP(\[2, 2\])\] | \[4, 3\] |
| \[2, 2, 3\] | \[\] | \[2, 2, 3\] |
| \[2, (2, 1), (2, 0, 3)\] | \[RP(2, 1), RP(\[2, 0, 3\])\] | \[5\] |

If we want the row partitions to end with uniform row partitions, then we can set num\_row\_partitions.

For example, below URP(3, 12) is RowPartition.from\_uniform\_row\_length(3, 12)

| from\_lengths | num\_row\_partitions | row\_partitions | inner\_shape |
| --- | --- | --- | --- |
| \[2, (3, 2), 2\] | 2   | \[RP(\[3, 2\]), URP(2, 10)\] | \[10\] |
| \[2, 2\] | 1   | \[URP(2, 4)\] | \[4\] |
| \[2, 2, 3\] | 0   | \[\] | \[2, 2, 3\] |
| \[2, 2, 3\] | 1   | \[URP(2, 4)\] | \[4, 3\] |
| \[2, 2, 3\] | 2   | \[URP(2, 4), URP(3, 12)\] | \[12\] |

Representing the shapes from init():

| from\_lengths | Tensor Example |
| --- | --- |
| `[2, 3]` | `[[1, 2, 3], [4, 5, 6]]` |
| `[3, (2, 0, 3)]` | `[[1, 2], [], [3, 4, 5]]` |
| `[2, (2, 1), 2]` | `[[[1, 2], [3, 4]], [[5, 6]]]` |
| `[2, (2, 1), (2, 1, 2)]` | `[[[1, 2], [3]], [[4, 5]]]` |

|     |     |
| --- | --- |
| Args |     |
| `lengths` | the lengths of sublists along each axis. |
| `num_row_partitions` | the num\_row\_partitions of the result or None indicating the minimum number of row\_partitions. |
| `dtype` | the dtype of the shape (tf.int32 or tf.int64). |

|     |
| --- |
| Returns |     |
| a new DynamicRaggedShape |     |

### `from_row_partitions`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/dynamic_ragged_shape.py#L409-L423)

@classmethod

Create a shape from row\_partitions.

|     |     |
| --- | --- |
| Args |     |
| `row_partitions` | a nonempty list of RowPartition objects. |
| `dtype` | the dtype to use, or None to use the row\_partitions dtype. |

|     |
| --- |
| Returns |     |
| a DynamicRaggedShape with inner\_rank==1. |     |

### `from_tensor`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/dynamic_ragged_shape.py#L431-L439)

@classmethod

Constructs a ragged shape for a potentially ragged tensor.

### `is_uniform`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/dynamic_ragged_shape.py#L709-L720)

is_uniform(
        axis
    )

Returns true if the indicated dimension is uniform.

### `static_lengths`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/dynamic_ragged_shape.py#L465-L500)

static_lengths(
        ragged_lengths=True
    )

Returns a list of statically known axis lengths.

This represents what values are known. For each row partition, it presents either the uniform row length (if statically known), the list of row lengths, or none if it is not statically known. For the inner shape, if the rank is known, then each dimension is reported if known, and None otherwise. If the rank of the inner shape is not known, then the returned list ends with an ellipsis.

|     |     |
| --- | --- |
| Args |     |
| `ragged_lengths` | If false, returns None for all ragged dimensions. |

|     |
| --- |
| Returns |     |
| A Sequence\[Union\[Sequence\[int\],int, None\]\] of lengths, with a possible Ellipsis at the end. |     |

### `with_dtype`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/dynamic_ragged_shape.py#L984-L990)

with_dtype(
        dtype
    )

Change the dtype of the shape.

### `__eq__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/extension_type.py#L276-L305)

__eq__(
        other
    )

Return self==value.

### `__getitem__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/dynamic_ragged_shape.py#L615-L654)

__getitem__(
        index
    )

Returns a dimension or a slice of the shape.

Ragged shapes can have ragged dimensions that depend upon other dimensions. Therefore, if you ask for a dimension that is ragged, this function returns a ValueError. For similar reasons, if a slice is selected that includes a ragged dimension without including the zero dimension, then this fails.

Any slice that does not start at zero will return a shape with num\_row\_partitions == 0.

|     |     |
| --- | --- |
| Args |     |
| `index` | the index: can be an int or a slice. |

|     |     |
| --- | --- |
| Raises |     |
| `IndexError` | if the index is not in range. |
| `ValueError` | if the rank is unknown, or a ragged rank is requested incorrectly. |

### `__ne__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/extension_type.py#L307-L312)

__ne__(
        other
    )

Return self!=value.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.