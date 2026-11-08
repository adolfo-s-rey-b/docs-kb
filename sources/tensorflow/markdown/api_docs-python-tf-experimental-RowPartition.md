[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#used-in-the-notebooks)
    
*   [Precomputed Encodings](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#precomputed_encodings)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#methods)
    *   [from\_row\_lengths](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#from_row_lengths)
        
    *   [from\_row\_limits](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#from_row_limits)
        
    *   [from\_row\_splits](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#from_row_splits)
        
    *   [from\_row\_starts](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#from_row_starts)
        
    *   [from\_uniform\_row\_length](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#from_uniform_row_length)
        
    *   [from\_value\_rowids](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#from_value_rowids)
        
    *   [is\_uniform](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#is_uniform)
        
    *   [nrows](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#nrows)
        
    *   [nvals](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#nvals)
        
    *   [offsets\_in\_rows](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#offsets_in_rows)
        
    *   [row\_lengths](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#row_lengths)
        
    *   [row\_limits](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#row_limits)
        
    *   [row\_splits](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#row_splits)
        
    *   [row\_starts](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#row_starts)
        
    *   [uniform\_row\_length](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#uniform_row_length)
        
    *   [value\_rowids](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#value_rowids)
        
    *   [with\_dtype](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#with_dtype)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.RowPartition Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#used-in-the-notebooks)
    
*   [Precomputed Encodings](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#precomputed_encodings)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#methods)
    *   [from\_row\_lengths](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#from_row_lengths)
        
    *   [from\_row\_limits](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#from_row_limits)
        
    *   [from\_row\_splits](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#from_row_splits)
        
    *   [from\_row\_starts](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#from_row_starts)
        
    *   [from\_uniform\_row\_length](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#from_uniform_row_length)
        
    *   [from\_value\_rowids](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#from_value_rowids)
        
    *   [is\_uniform](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#is_uniform)
        
    *   [nrows](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#nrows)
        
    *   [nvals](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#nvals)
        
    *   [offsets\_in\_rows](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#offsets_in_rows)
        
    *   [row\_lengths](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#row_lengths)
        
    *   [row\_limits](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#row_limits)
        
    *   [row\_splits](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#row_splits)
        
    *   [row\_starts](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#row_starts)
        
    *   [uniform\_row\_length](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#uniform_row_length)
        
    *   [value\_rowids](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#value_rowids)
        
    *   [with\_dtype](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition#with_dtype)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/row_partition.py#L56-L1203)

Partitioning of a sequence of values into contiguous subsequences ("rows").

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.experimental.RowPartition`](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition)

tf.experimental.RowPartition(
        row_splits,
        row_lengths=None,
        value_rowids=None,
        nrows=None,
        uniform_row_length=None,
        nvals=None,
        internal=False
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Ragged tensors](https://www.tensorflow.org/guide/ragged_tensor) |

A `RowPartition` describes how a sequence with `nvals` items should be divided into `nrows` contiguous subsequences ("rows"). For example, a `RowPartition` could be used to partition the vector `[1, 2, 3, 4, 5]` into subsequences `[[1, 2], [3], [], [4, 5]]`. Note that `RowPartition` stores information about how values are partitioned, but does not include the partitioned values themselves. [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
 is used to pair a `values` tensor with one or more `RowPartition`s, providing a complete encoding for a ragged tensor (i.e. a tensor with variable-length dimensions).

`RowPartition`s may be defined using several different schemes:

*   `row_lengths`: an integer vector with shape `[nrows]`, which specifies the length of each row.
    
*   `row_splits`: an integer vector with shape `[nrows+1]`, specifying the "split points" between each row.
    
*   `row_starts`: an integer vector with shape `[nrows]`, which specifies the start offset for each row. Equivalent to `row_splits[:-1]`.
    
*   `row_limits`: an integer vector with shape `[nrows]`, which specifies the stop offset for each row. Equivalent to `row_splits[1:]`.
    
*   `value_rowids` is an integer vector with shape `[nvals]`, corresponding one-to-one with sequence values, which specifies the row that each value belongs to. If the partition has empty trailing rows, then `nrows` must also be specified.
    
*   `uniform_row_length` is an integer scalar, specifying the length of every row. This scheme may only be used if all rows have the same length.
    

For example, the following `RowPartition`s all represent the partitioning of 8 values into 5 sublists as follows: `[[*, *, *, *], [], [*, *, *], [*], []]`.

    p1 = RowPartition.from_row_lengths([4, 0, 3, 1, 0])

For more information about each scheme, see the documentation for the its factory method. For additional examples, see the documentation on [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
.

### Precomputed Encodings

`RowPartition` always stores at least one encoding of the partitioning, but it can be configured to cache additional encodings as well. This can avoid unnecessary recomputation in eager mode. (In graph mode, optimizations such as common subexpression elimination will typically prevent these unnecessary recomputations.) To check which encodings are precomputed, use `RowPartition.has_precomputed_<encoding>`. To cache an additional encoding, use `RowPartition.with_precomputed_<encoding>`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `row_splits` | A 1-D integer tensor with shape `[nrows+1]`. |
| `row_lengths` | A 1-D integer tensor with shape `[nrows]` |
| `value_rowids` | A 1-D integer tensor with shape `[nvals]`. |
| `nrows` | A 1-D integer scalar tensor. |
| `uniform_row_length` | A scalar tensor. |
| `nvals` | A scalar tensor. |
| `internal` | Private key value, required to ensure that this private constructor is _only_ called from the factory methods. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If a row partitioning tensor has an inappropriate dtype. |
| `TypeError` | If exactly one row partitioning argument was not specified. |
| `ValueError` | If a row partitioning tensor has an inappropriate shape. |
| `ValueError` | If multiple partitioning arguments are specified. |
| `ValueError` | If nrows is specified but value\_rowids is not None. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `dtype` | The `DType` used to encode the row partition (either int32 or int64). |
| `static_nrows` | The number of rows in this partition, if statically known.<br><br>self.row_lengths().shape == [self.static_nrows]<br>    self.row_starts().shape == [self.static_nrows]<br>    self.row_limits().shape == [self.static_nrows]<br>    self.row_splits().shape == [self.static_nrows + 1] |
| `static_nvals` | The number of values in this partition, if statically known.<br><br>self.value_rowids().shape == [self.static_vals] |
| `static_uniform_row_length` | The number of values in each row of this partition, if statically known. |

Methods
-------

### `from_row_lengths`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/row_partition.py#L378-L431)

@classmethod

Creates a `RowPartition` with rows partitioned by `row_lengths`.

This `RowPartition` divides a sequence `values` into rows by indicating the length of each row:

partitioned_rows = [[values.pop(0) for _ in range(length)]\
                        for length in row_lengths]

|     |     |
| --- | --- |
| Args |     |
| `row_lengths` | A 1-D integer tensor with shape `[nrows]`. Must be nonnegative. |
| `validate` | If true, then use assertions to check that the arguments form a valid `RowPartition`. |
| `dtype` | Optional dtype for the RowPartition. If missing, the type is inferred from the type of `row_lengths`, dtype\_hint, or tf.int64. |
| `dtype_hint` | Optional dtype for the RowPartition, used when dtype is None. In some cases, a caller may not have a dtype in mind when converting to a tensor, so dtype\_hint can be used as a soft preference. If the conversion to `dtype_hint` is not possible, this argument has no effect. |

|     |
| --- |
| Returns |     |
| A `RowPartition`. |     |

### `from_row_limits`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/row_partition.py#L485-L529)

@classmethod

Creates a `RowPartition` with rows partitioned by `row_limits`.

Equivalent to: `from_row_splits(values, concat([0, row_limits], axis=0))`.

|     |     |
| --- | --- |
| Args |     |
| `row_limits` | A 1-D integer tensor with shape `[nrows]`. Must be sorted in ascending order. |
| `validate` | If true, then use assertions to check that the arguments form a valid `RowPartition`. |
| `dtype` | Optional dtype for the RowPartition. If missing, the type is inferred from the type of `row_limits`, dtype\_hint, or tf.int64. |
| `dtype_hint` | Optional dtype for the RowPartition, used when dtype is None. In some cases, a caller may not have a dtype in mind when converting to a tensor, so dtype\_hint can be used as a soft preference. If the conversion to `dtype_hint` is not possible, this argument has no effect. |

|     |
| --- |
| Returns |     |
| A `RowPartition`. |     |

### `from_row_splits`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/row_partition.py#L315-L376)

@classmethod

Creates a `RowPartition` with rows partitioned by `row_splits`.

This `RowPartition` divides a sequence `values` into rows by indicating where each row begins and ends:

partitioned_rows = []
    for i in range(len(row_splits) - 1):
      row_start = row_splits[i]
      row_end = row_splits[i + 1]
      partitioned_rows.append(values[row_start:row_end])

|     |     |
| --- | --- |
| Args |     |
| `row_splits` | A 1-D integer tensor with shape `[nrows+1]`. Must not be empty, and must be sorted in ascending order. `row_splits[0]` must be zero. |
| `validate` | If true, then use assertions to check that the arguments form a valid `RowPartition`. |
| `dtype` | Optional dtype for the RowPartition. If missing, the type is inferred from the type of `row_splits`, dtype\_hint, or tf.int64. |
| `dtype_hint` | Optional dtype for the RowPartition, used when dtype is None. In some cases, a caller may not have a dtype in mind when converting to a tensor, so dtype\_hint can be used as a soft preference. If the conversion to `dtype_hint` is not possible, this argument has no effect. |

|     |
| --- |
| Returns |     |
| A `RowPartition`. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If `row_splits` is an empty list. |

### `from_row_starts`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/row_partition.py#L433-L483)

@classmethod

Creates a `RowPartition` with rows partitioned by `row_starts`.

Equivalent to: `from_row_splits(concat([row_starts, nvals], axis=0))`.

|     |     |
| --- | --- |
| Args |     |
| `row_starts` | A 1-D integer tensor with shape `[nrows]`. Must be nonnegative and sorted in ascending order. If `nrows>0`, then `row_starts[0]` must be zero. |
| `nvals` | A scalar tensor indicating the number of values. |
| `validate` | If true, then use assertions to check that the arguments form a valid `RowPartition`. |
| `dtype` | Optional dtype for the RowPartition. If missing, the type is inferred from the type of `row_starts`, dtype\_hint, or tf.int64. |
| `dtype_hint` | Optional dtype for the RowPartition, used when dtype is None. In some cases, a caller may not have a dtype in mind when converting to a tensor, so dtype\_hint can be used as a soft preference. If the conversion to `dtype_hint` is not possible, this argument has no effect. |

|     |
| --- |
| Returns |     |
| A `RowPartition`. |     |

### `from_uniform_row_length`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/row_partition.py#L531-L667)

@classmethod

Creates a `RowPartition` with rows partitioned by `uniform_row_length`.

This `RowPartition` divides a sequence `values` into rows that all have the same length:

partitioned_rows = [[values.pop(0) for _ in range(uniform_row_length)]\
             for _ in range(nrows)]

Note that either or both of nvals and nrows must be specified.

|     |     |
| --- | --- |
| Args |     |
| `uniform_row_length` | A scalar integer tensor. Must be nonnegative. The size of the outer axis of `values` must be evenly divisible by `uniform_row_length`. |
| `nvals` | a non-negative scalar integer tensor for the number of values. Must be specified if nrows is not specified. If not specified, defaults to uniform\_row\_length\*nrows |
| `nrows` | The number of rows in the constructed RowPartition. If not specified, then it defaults to `nvals/uniform_row_length` (or `0` if `uniform_row_length==0`). `nrows` only needs to be specified if `uniform_row_length` might be zero. `uniform_row_length*nrows` must be `nvals`. |
| `validate` | If true, then use assertions to check that the arguments form a valid `RowPartition`. |
| `dtype` | Optional dtype for the RowPartition. If missing, the type is inferred from the type of `uniform_row_length`, dtype\_hint, or tf.int64. |
| `dtype_hint` | Optional dtype for the RowPartition, used when dtype is None. In some cases, a caller may not have a dtype in mind when converting to a tensor, so dtype\_hint can be used as a soft preference. If the conversion to `dtype_hint` is not possible, this argument has no effect. |

|     |
| --- |
| Returns |     |
| A `RowPartition`. |     |

### `from_value_rowids`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/row_partition.py#L195-L313)

@classmethod

Creates a `RowPartition` with rows partitioned by `value_rowids`.

This `RowPartition` divides a sequence `values` into rows by specifying which row each value should be added to:

partitioned_rows = [[] for _ in nrows]
    for (value, rowid) in zip(values, value_rowids):
      partitioned_rows[rowid].append(value)

|     |     |
| --- | --- |
| Args |     |
| `value_rowids` | A 1-D integer tensor with shape `[nvals]`, which corresponds one-to-one with `values`, and specifies each value's row index. Must be nonnegative, and must be sorted in ascending order. |
| `nrows` | An integer scalar specifying the number of rows. This should be specified if the `RowPartition` may containing empty training rows. Must be greater than `value_rowids[-1]` (or greater than or equal to zero if `value_rowids` is empty). Defaults to `value_rowids[-1] + 1` (or zero if `value_rowids` is empty). |
| `validate` | If true, then use assertions to check that the arguments form a valid `RowPartition`. |
| `dtype` | Optional dtype for the RowPartition. If missing, the type is inferred from the type of `value_rowids`, dtype\_hint, or tf.int64. |
| `dtype_hint` | Optional dtype for the RowPartition, used when dtype is None. In some cases, a caller may not have a dtype in mind when converting to a tensor, so dtype\_hint can be used as a soft preference. If the conversion to `dtype_hint` is not possible, this argument has no effect. |

|     |
| --- |
| Returns |     |
| A `RowPartition`. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If `nrows` is incompatible with `value_rowids`. |

#### Example:

    print(RowPartition.from_value_rowids(

### `is_uniform`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/row_partition.py#L926-L937)

is_uniform()

Returns true if the partition is known to be uniform statically.

This is based upon the existence of self.\_uniform\_row\_length. For example: RowPartition.from\_row\_lengths(\[3,3,3\]).is\_uniform()false RowPartition.from\_uniform\_row\_length(5, nvals=20).is\_uniform()true RowPartition.from\_row\_lengths(\[2,0,2\]).is\_uniform()==false

|     |
| --- |
| Returns |     |
| Whether a RowPartition is known to be uniform statically. |     |

### `nrows`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/row_partition.py#L782-L794)

nrows()

Returns the number of rows created by this `RowPartition`.

|     |
| --- |
| Returns |     |
| scalar integer Tensor |     |

### `nvals`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/row_partition.py#L767-L780)

nvals()

Returns the number of values partitioned by this `RowPartition`.

If the sequence partitioned by this `RowPartition` is a tensor, then `nvals` is the size of that tensor's outermost dimension -- i.e., `nvals == values.shape[0]`.

|     |
| --- |
| Returns |     |
| scalar integer Tensor |     |

### `offsets_in_rows`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/row_partition.py#L908-L924)

offsets_in_rows()

Return the offset of each value.

RowPartition takes an array x and converts it into sublists. offsets\[i\] is the index of x\[i\] in its sublist. Given a shape, such as: \[_,_,_\],\[_,_\],\[\],\[_,\*\] This returns: 0,1,2,0,1,0,1

|     |
| --- |
| Returns |     |
| an offset for every value. |     |

### `row_lengths`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/row_partition.py#L834-L845)

row_lengths()

Returns the lengths of rows in this `RowPartition`.

|     |
| --- |
| Returns |     |
| A 1-D integer Tensor with shape `[self.nrows]`. The returned tensor is nonnegative. `tf.reduce_sum(self.row_lengths) == self.nvals()`. |     |

### `row_limits`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/row_partition.py#L821-L832)

row_limits()

Returns the limit indices for rows in this row partition.

These indices specify where the values for each row end. `partition.row_limits()` is equal to `partition.row_splits()[:-1]`.

|     |
| --- |
| Returns |     |
| A 1-D integer Tensor with shape `[self.nrows]`. The returned tensor is nonnegative, and is sorted in ascending order. `self.row_limits()[-1] == self.nvals()`. |     |

### `row_splits`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/row_partition.py#L738-L751)

row_splits()

Returns the row-split indices for this row partition.

`row_splits` specifies where the values for each row begin and end. In particular, the values for row `i` are stored in the slice `values[row_splits[i]:row_splits[i+1]]`.

|     |
| --- |
| Returns |     |
| A 1-D integer `Tensor` with shape `[self.nrows+1]`. The returned tensor is non-empty, and is sorted in ascending order. `self.row_splits()[0] == 0`. `self.row_splits()[-1] == self.nvals()`. |     |

### `row_starts`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/row_partition.py#L807-L819)

row_starts()

Returns the start indices for rows in this row partition.

These indices specify where the values for each row begin. `partition.row_starts()` is equal to `partition.row_splits()[:-1]`.

|     |
| --- |
| Returns |     |
| A 1-D integer Tensor with shape `[self.nrows()]`. The returned tensor is nonnegative, and is sorted in ascending order. `self.row_starts()[0] == 0`. `self.row_starts()[-1] <= self.nvals()`. |     |

### `uniform_row_length`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/row_partition.py#L796-L805)

uniform_row_length()

Returns the length of each row in this partition, if rows are uniform.

If all rows in this `RowPartition` have the same length, then this returns that length as a scalar integer `Tensor`. Otherwise, it returns `None`.

|     |
| --- |
| Returns |     |
| scalar Tensor with `type=self.dtype`, or `None`. |     |

### `value_rowids`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/row_partition.py#L753-L765)

value_rowids()

Returns the row indices for this row partition.

`value_rowids` specifies the row index for each value. In particular, `value_rowids[i]` is the row index for `values[i]`.

|     |
| --- |
| Returns |     |
| A 1-D integer `Tensor` with shape `[self.nvals()]`. The returned tensor is nonnegative, and is sorted in ascending order. |     |

### `with_dtype`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/row_partition.py#L968-L991)

with_dtype(
        dtype
    )

Returns a copy of this RowPartition with the given encoding dtype.

|     |     |
| --- | --- |
| Args |     |
| `dtype` | The dtype for encoding tensors, such as `row_splits` and `nrows`. One of [`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)<br> or [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br>. |

|     |
| --- |
| Returns |     |
| A copy of this RowPartition, with the encoding tensors cast to the given type. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.