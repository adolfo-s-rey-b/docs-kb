[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.RaggedTensor Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_tensor.py#L65-L2260)

Represents a ragged tensor.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Ragged tensors](https://www.tensorflow.org/guide/ragged_tensor)<br>    <br>*   [Unicode strings](https://www.tensorflow.org/text/guide/unicode) |

A `RaggedTensor` is a tensor with one or more _ragged dimensions_, which are dimensions whose slices may have different lengths. For example, the inner (column) dimension of `rt=[[3, 1, 4, 1], [], [5, 9, 2], [6], []]` is ragged, since the column slices (`rt[0, :]`, ..., `rt[4, :]`) have different lengths. Dimensions whose slices all have the same length are called _uniform dimensions_. The outermost dimension of a `RaggedTensor` is always uniform, since it consists of a single slice (and so there is no possibility for differing slice lengths).

The total number of dimensions in a `RaggedTensor` is called its _rank_, and the number of ragged dimensions in a `RaggedTensor` is called its _ragged-rank_. A `RaggedTensor`'s ragged-rank is fixed at graph creation time: it can't depend on the runtime values of `Tensor`s, and can't vary dynamically for different session runs.

Note that the `__init__` constructor is private. Please use one of the following methods to construct a `RaggedTensor`:

*   [`tf.RaggedTensor.from_row_lengths`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor#from_row_lengths)
    
*   [`tf.RaggedTensor.from_value_rowids`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor#from_value_rowids)
    
*   [`tf.RaggedTensor.from_row_splits`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor#from_row_splits)
    
*   [`tf.RaggedTensor.from_row_starts`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor#from_row_starts)
    
*   [`tf.RaggedTensor.from_row_limits`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor#from_row_limits)
    
*   [`tf.RaggedTensor.from_nested_row_splits`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor#from_nested_row_splits)
    
*   [`tf.RaggedTensor.from_nested_row_lengths`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor#from_nested_row_lengths)
    
*   [`tf.RaggedTensor.from_nested_value_rowids`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor#from_nested_value_rowids)
    

### Potentially Ragged Tensors

Many ops support both `Tensor`s and `RaggedTensor`s (see [tf.ragged](https://www.tensorflow.org/api_docs/python/tf/ragged)
 for a full listing). The term "potentially ragged tensor" may be used to refer to a tensor that might be either a `Tensor` or a `RaggedTensor`. The ragged-rank of a `Tensor` is zero.

### Documenting RaggedTensor Shapes

When documenting the shape of a RaggedTensor, ragged dimensions can be indicated by enclosing them in parentheses. For example, the shape of a 3-D `RaggedTensor` that stores the fixed-size word embedding for each word in a sentence, for each sentence in a batch, could be written as `[num_sentences, (num_words), embedding_size]`. The parentheses around `(num_words)` indicate that dimension is ragged, and that the length of each element list in that dimension may vary for each item.

### Component Tensors

Internally, a `RaggedTensor` consists of a concatenated list of values that are partitioned into variable-length rows. In particular, each `RaggedTensor` consists of:

*   A `values` tensor, which concatenates the variable-length rows into a flattened list. For example, the `values` tensor for `[[3, 1, 4, 1], [], [5, 9, 2], [6], []]` is `[3, 1, 4, 1, 5, 9, 2, 6]`.
    
*   A `row_splits` vector, which indicates how those flattened values are divided into rows. In particular, the values for row `rt[i]` are stored in the slice `rt.values[rt.row_splits[i]:rt.row_splits[i+1]]`.
    

#### Example:

    print(tf.RaggedTensor.from_row_splits(

### Alternative Row-Partitioning Schemes

In addition to `row_splits`, ragged tensors provide support for five other row-partitioning schemes:

*   `row_lengths`: a vector with shape `[nrows]`, which specifies the length of each row.
    
*   `value_rowids` and `nrows`: `value_rowids` is a vector with shape `[nvals]`, corresponding one-to-one with `values`, which specifies each value's row index. In particular, the row `rt[row]` consists of the values `rt.values[j]` where `value_rowids[j]==row`. `nrows` is an integer scalar that specifies the number of rows in the `RaggedTensor`. (`nrows` is used to indicate trailing empty rows.)
    
*   `row_starts`: a vector with shape `[nrows]`, which specifies the start offset of each row. Equivalent to `row_splits[:-1]`.
    
*   `row_limits`: a vector with shape `[nrows]`, which specifies the stop offset of each row. Equivalent to `row_splits[1:]`.
    
*   `uniform_row_length`: A scalar tensor, specifying the length of every row. This row-partitioning scheme may only be used if all rows have the same length.
    

Example: The following ragged tensors are equivalent, and all represent the nested list `[[3, 1, 4, 1], [], [5, 9, 2], [6], []]`.

    values = [3, 1, 4, 1, 5, 9, 2, 6]

### Multiple Ragged Dimensions

`RaggedTensor`s with multiple ragged dimensions can be defined by using a nested `RaggedTensor` for the `values` tensor. Each nested `RaggedTensor` adds a single ragged dimension.

    inner_rt = RaggedTensor.from_row_splits(  # =rt1 from above

The factory function [`RaggedTensor.from_nested_row_splits`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor#from_nested_row_splits)
 may be used to construct a `RaggedTensor` with multiple ragged dimensions directly, by providing a list of `row_splits` tensors:

    RaggedTensor.from_nested_row_splits(

### Uniform Inner Dimensions

`RaggedTensor`s with uniform inner dimensions can be defined by using a multidimensional `Tensor` for `values`.

    rt = RaggedTensor.from_row_splits(values=tf.ones([5, 3], tf.int32),

### Uniform Outer Dimensions

`RaggedTensor`s with uniform outer dimensions can be defined by using one or more `RaggedTensor` with a `uniform_row_length` row-partitioning tensor. For example, a `RaggedTensor` with shape `[2, 2, None]` can be constructed with this method from a `RaggedTensor` values with shape `[4, None]`:

    values = tf.ragged.constant([[1, 2, 3], [4], [5, 6], [7, 8, 9, 10]])

Note that `rt6` only contains one ragged dimension (the innermost dimension). In contrast, if `from_row_splits` is used to construct a similar `RaggedTensor`, then that `RaggedTensor` will have two ragged dimensions:

    rt7 = tf.RaggedTensor.from_row_splits(values, [0, 2, 4])

Uniform and ragged outer dimensions may be interleaved, meaning that a tensor with any combination of ragged and uniform dimensions may be created. For example, a RaggedTensor `t4` with shape `[3, None, 4, 8, None, 2]` could be constructed as follows:

t0 = tf.zeros([1000, 2])                           # Shape:         [1000, 2]
    t1 = RaggedTensor.from_row_lengths(t0, [...])      #           [160, None, 2]
    t2 = RaggedTensor.from_uniform_row_length(t1, 8)   #         [20, 8, None, 2]
    t3 = RaggedTensor.from_uniform_row_length(t2, 4)   #       [5, 4, 8, None, 2]
    t4 = RaggedTensor.from_row_lengths(t3, [...])      # [3, None, 4, 8, None, 2]

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `dtype` | The `DType` of values in this tensor. |
| `flat_values` | The innermost `values` tensor for this ragged tensor.<br><br>Concretely, if `rt.values` is a `Tensor`, then `rt.flat_values` is `rt.values`; otherwise, `rt.flat_values` is `rt.values.flat_values`.<br><br>Conceptually, `flat_values` is the tensor formed by flattening the outermost dimension and all of the ragged dimensions into a single dimension.<br><br>`rt.flat_values.shape = [nvals] + rt.shape[rt.ragged_rank + 1:]` (where `nvals` is the number of items in the flattened dimensions).<br><br>#### Example:<br><br>    rt = tf.ragged.constant([[[3, 1, 4, 1], [], [5, 9, 2]], [], [[6], []]]) |
| `nested_row_splits` | A tuple containing the row\_splits for all ragged dimensions.<br><br>`rt.nested_row_splits` is a tuple containing the `row_splits` tensors for all ragged dimensions in `rt`, ordered from outermost to innermost. In particular, `rt.nested_row_splits = (rt.row_splits,) + value_splits` where:<br><br>* `value_splits = ()` if `rt.values` is a `Tensor`.<br>    * `value_splits = rt.values.nested_row_splits` otherwise.<br><br>#### Example:<br><br>    rt = tf.ragged.constant( |
| `ragged_rank` | The number of times the RaggedTensor's flat\_values is partitioned.<br><br>    values = tf.ragged.constant([[1, 2, 3], [4], [5, 6], [7, 8, 9, 10]])<br><br>    rt = tf.RaggedTensor.from_uniform_row_length(values, 2) |
| `row_splits` | The row-split indices for this ragged tensor's `values`.<br><br>`rt.row_splits` specifies where the values for each row begin and end in `rt.values`. In particular, the values for row `rt[i]` are stored in the slice `rt.values[rt.row_splits[i]:rt.row_splits[i+1]]`.<br><br>#### Example:<br><br>    rt = tf.ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6], []]) |
| `shape` | The statically known shape of this ragged tensor.<br><br>    tf.ragged.constant([[0], [1, 2]]).shape<br><br>    tf.ragged.constant([[[0, 1]], [[1, 2], [3, 4]]], ragged_rank=1).shape |
| `uniform_row_length` | The length of each row in this ragged tensor, or None if rows are ragged.<br><br>    rt1 = tf.ragged.constant([[1, 2, 3], [4], [5, 6], [7, 8, 9, 10]])<br><br>    rt2 = tf.RaggedTensor.from_uniform_row_length(<br><br>A RaggedTensor's rows are only considered to be uniform (i.e. non-ragged) if it can be determined statically (at graph construction time) that the rows all have the same length. |
| `values` | The concatenated rows for this ragged tensor.<br><br>`rt.values` is a potentially ragged tensor formed by flattening the two outermost dimensions of `rt` into a single dimension.<br><br>`rt.values.shape = [nvals] + rt.shape[2:]` (where `nvals` is the number of items in the outer two dimensions of `rt`).<br><br>`rt.ragged_rank = self.ragged_rank - 1`<br><br>#### Example:<br><br>    rt = tf.ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6], []]) |

Methods
-------

### `bounding_shape`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_tensor.py#L1327-L1385)

bounding_shape(
        axis=None, name=None, out_type=None
    )

Returns the tight bounding box shape for this `RaggedTensor`.

|     |     |
| --- | --- |
| Args |     |
| `axis` | An integer scalar or vector indicating which axes to return the bounding box for. If not specified, then the full bounding box is returned. |
| `name` | A name prefix for the returned tensor (optional). |
| `out_type` | `dtype` for the returned tensor. Defaults to `self.row_splits.dtype`. |

|     |
| --- |
| Returns |     |
| An integer `Tensor` (`dtype=self.row_splits.dtype`). If `axis` is not specified, then `output` is a vector with `output.shape=[self.shape.ndims]`. If `axis` is a scalar, then the `output` is a scalar. If `axis` is a vector, then `output` is a vector, where `output[i]` is the bounding size for dimension `axis[i]`. |     |

#### Example:

    rt = tf.ragged.constant([[1, 2, 3, 4], [5], [], [6, 7, 8, 9], [10]])

### `consumers`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_tensor.py#L2256-L2257)

consumers()

### `from_nested_row_lengths`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_tensor.py#L773-L813)

@classmethod

Creates a `RaggedTensor` from a nested list of `row_lengths` tensors.

#### Equivalent to:

result = flat_values
    for row_lengths in reversed(nested_row_lengths):
      result = from_row_lengths(result, row_lengths)

|     |     |
| --- | --- |
| Args |     |
| `flat_values` | A potentially ragged tensor. |
| `nested_row_lengths` | A list of 1-D integer tensors. The `i`th tensor is used as the `row_lengths` for the `i`th ragged dimension. |
| `name` | A name prefix for the RaggedTensor (optional). |
| `validate` | If true, then use assertions to check that the arguments form a valid `RaggedTensor`. Note: these assertions incur a runtime cost, since they must be checked for each tensor value. |

|     |
| --- |
| Returns |     |
| A `RaggedTensor` (or `flat_values` if `nested_row_lengths` is empty). |     |

### `from_nested_row_splits`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_tensor.py#L731-L771)

@classmethod

Creates a `RaggedTensor` from a nested list of `row_splits` tensors.

#### Equivalent to:

result = flat_values
    for row_splits in reversed(nested_row_splits):
      result = from_row_splits(result, row_splits)

|     |     |
| --- | --- |
| Args |     |
| `flat_values` | A potentially ragged tensor. |
| `nested_row_splits` | A list of 1-D integer tensors. The `i`th tensor is used as the `row_splits` for the `i`th ragged dimension. |
| `name` | A name prefix for the RaggedTensor (optional). |
| `validate` | If true, then use assertions to check that the arguments form a valid `RaggedTensor`. Note: these assertions incur a runtime cost, since they must be checked for each tensor value. |

|     |
| --- |
| Returns |     |
| A `RaggedTensor` (or `flat_values` if `nested_row_splits` is empty). |     |

### `from_nested_value_rowids`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_tensor.py#L668-L729)

@classmethod

Creates a `RaggedTensor` from a nested list of `value_rowids` tensors.

#### Equivalent to:

result = flat_values
    for (rowids, nrows) in reversed(zip(nested_value_rowids, nested_nrows)):
      result = from_value_rowids(result, rowids, nrows)

|     |     |
| --- | --- |
| Args |     |
| `flat_values` | A potentially ragged tensor. |
| `nested_value_rowids` | A list of 1-D integer tensors. The `i`th tensor is used as the `value_rowids` for the `i`th ragged dimension. |
| `nested_nrows` | A list of integer scalars. The `i`th scalar is used as the `nrows` for the `i`th ragged dimension. |
| `name` | A name prefix for the RaggedTensor (optional). |
| `validate` | If true, then use assertions to check that the arguments form a valid `RaggedTensor`. Note: these assertions incur a runtime cost, since they must be checked for each tensor value. |

|     |
| --- |
| Returns |     |
| A `RaggedTensor` (or `flat_values` if `nested_value_rowids` is empty). |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If `len(nested_values_rowids) != len(nested_nrows)`. |

### `from_row_lengths`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_tensor.py#L468-L510)

@classmethod

Creates a `RaggedTensor` with rows partitioned by `row_lengths`.

The returned `RaggedTensor` corresponds with the python list defined by:

result = [[values.pop(0) for i in range(length)]\
              for length in row_lengths]

|     |     |
| --- | --- |
| Args |     |
| `values` | A potentially ragged tensor with shape `[nvals, ...]`. |
| `row_lengths` | A 1-D integer tensor with shape `[nrows]`. Must be nonnegative. `sum(row_lengths)` must be `nvals`. |
| `name` | A name prefix for the RaggedTensor (optional). |
| `validate` | If true, then use assertions to check that the arguments form a valid `RaggedTensor`. Note: these assertions incur a runtime cost, since they must be checked for each tensor value. |

|     |
| --- |
| Returns |     |
| A `RaggedTensor`. `result.rank = values.rank + 1`. `result.ragged_rank = values.ragged_rank + 1`. |     |

#### Example:

    print(tf.RaggedTensor.from_row_lengths(

### `from_row_limits`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_tensor.py#L553-L590)

@classmethod

Creates a `RaggedTensor` with rows partitioned by `row_limits`.

Equivalent to: `from_row_splits(values, concat([0, row_limits]))`.

|     |     |
| --- | --- |
| Args |     |
| `values` | A potentially ragged tensor with shape `[nvals, ...]`. |
| `row_limits` | A 1-D integer tensor with shape `[nrows]`. Must be sorted in ascending order. If `nrows>0`, then `row_limits[-1]` must be `nvals`. |
| `name` | A name prefix for the RaggedTensor (optional). |
| `validate` | If true, then use assertions to check that the arguments form a valid `RaggedTensor`. Note: these assertions incur a runtime cost, since they must be checked for each tensor value. |

|     |
| --- |
| Returns |     |
| A `RaggedTensor`. `result.rank = values.rank + 1`. `result.ragged_rank = values.ragged_rank + 1`. |     |

#### Example:

    print(tf.RaggedTensor.from_row_limits(

### `from_row_splits`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_tensor.py#L420-L466)

@classmethod

Creates a `RaggedTensor` with rows partitioned by `row_splits`.

The returned `RaggedTensor` corresponds with the python list defined by:

result = [values[row_splits[i]:row_splits[i + 1]]\
              for i in range(len(row_splits) - 1)]

|     |     |
| --- | --- |
| Args |     |
| `values` | A potentially ragged tensor with shape `[nvals, ...]`. |
| `row_splits` | A 1-D integer tensor with shape `[nrows+1]`. Must not be empty, and must be sorted in ascending order. `row_splits[0]` must be zero and `row_splits[-1]` must be `nvals`. |
| `name` | A name prefix for the RaggedTensor (optional). |
| `validate` | If true, then use assertions to check that the arguments form a valid `RaggedTensor`. Note: these assertions incur a runtime cost, since they must be checked for each tensor value. |

|     |
| --- |
| Returns |     |
| A `RaggedTensor`. `result.rank = values.rank + 1`. `result.ragged_rank = values.ragged_rank + 1`. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If `row_splits` is an empty list. |

#### Example:

    print(tf.RaggedTensor.from_row_splits(

### `from_row_starts`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_tensor.py#L512-L551)

@classmethod

Creates a `RaggedTensor` with rows partitioned by `row_starts`.

Equivalent to: `from_row_splits(values, concat([row_starts, nvals]))`.

|     |     |
| --- | --- |
| Args |     |
| `values` | A potentially ragged tensor with shape `[nvals, ...]`. |
| `row_starts` | A 1-D integer tensor with shape `[nrows]`. Must be nonnegative and sorted in ascending order. If `nrows>0`, then `row_starts[0]` must be zero. |
| `name` | A name prefix for the RaggedTensor (optional). |
| `validate` | If true, then use assertions to check that the arguments form a valid `RaggedTensor`. Note: these assertions incur a runtime cost, since they must be checked for each tensor value. |

|     |
| --- |
| Returns |     |
| A `RaggedTensor`. `result.rank = values.rank + 1`. `result.ragged_rank = values.ragged_rank + 1`. |     |

#### Example:

    print(tf.RaggedTensor.from_row_starts(

### `from_sparse`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_tensor.py#L1874-L1937)

@classmethod

Converts a 2D [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)
 to a `RaggedTensor`.

Each row of the `output` `RaggedTensor` will contain the explicit values from the same row in `st_input`. `st_input` must be ragged-right. If not it is not ragged-right, then an error will be generated.

#### Example:

    indices = [[0, 0], [0, 1], [0, 2], [1, 0], [3, 0]]

Currently, only two-dimensional `SparseTensors` are supported.

|     |     |
| --- | --- |
| Args |     |
| `st_input` | The sparse tensor to convert. Must have rank 2. |
| `name` | A name prefix for the returned tensors (optional). |
| `row_splits_dtype` | `dtype` for the returned `RaggedTensor`'s `row_splits` tensor. One of [`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)<br> or [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br>. |

|     |
| --- |
| Returns |     |
| A `RaggedTensor` with the same values as `st_input`. `output.ragged_rank = rank(st_input) - 1`. `output.shape = [st_input.dense_shape[0], None]`. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If the number of dimensions in `st_input` is not known statically, or is not two. |

### `from_tensor`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_tensor.py#L1582-L1796)

@classmethod

Converts a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 into a `RaggedTensor`.

The set of absent/default values may be specified using a vector of lengths or a padding value (but not both). If `lengths` is specified, then the output tensor will satisfy `output[row] = tensor[row][:lengths[row]]`. If 'lengths' is a list of lists or tuple of lists, those lists will be used as nested row lengths. If `padding` is specified, then any row _suffix_ consisting entirely of `padding` will be excluded from the returned `RaggedTensor`. If neither `lengths` nor `padding` is specified, then the returned `RaggedTensor` will have no absent/default values.

#### Examples:

    dt = tf.constant([[5, 7, 0], [0, 3, 0], [6, 0, 0]])

    tf.RaggedTensor.from_tensor(dt, padding=0)

    dt = tf.constant([[[5, 0], [7, 0], [0, 0]],\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `tensor` | The `Tensor` to convert. Must have rank `ragged_rank + 1` or higher. |\
| `lengths` | An optional set of row lengths, specified using a 1-D integer `Tensor` whose length is equal to `tensor.shape[0]` (the number of rows in `tensor`). If specified, then `output[row]` will contain `tensor[row][:lengths[row]]`. Negative lengths are treated as zero. You may optionally pass a list or tuple of lengths to this argument, which will be used as nested row lengths to construct a ragged tensor with multiple ragged dimensions. |\
| `padding` | An optional padding value. If specified, then any row suffix consisting entirely of `padding` will be excluded from the returned RaggedTensor. `padding` is a `Tensor` with the same dtype as `tensor` and with `shape=tensor.shape[ragged_rank + 1:]`. |\
| `ragged_rank` | Integer specifying the ragged rank for the returned `RaggedTensor`. Must be greater than zero. |\
| `name` | A name prefix for the returned tensors (optional). |\
| `row_splits_dtype` | `dtype` for the returned `RaggedTensor`'s `row_splits` tensor. One of [`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)<br> or [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br>. |\
\
|     |\
| --- |\
| Returns |     |\
| A `RaggedTensor` with the specified `ragged_rank`. The shape of the returned ragged tensor is compatible with the shape of `tensor`. |     |\
\
|     |     |\
| --- | --- |\
| Raises |     |\
| `ValueError` | If both `lengths` and `padding` are specified. |\
| `ValueError` | If the rank of `tensor` is 0 or 1. |\
\
### `from_uniform_row_length`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_tensor.py#L592-L666)\
\
@classmethod\
\
Creates a `RaggedTensor` with rows partitioned by `uniform_row_length`.\
\
This method can be used to create `RaggedTensor`s with multiple uniform outer dimensions. For example, a `RaggedTensor` with shape `[2, 2, None]` can be constructed with this method from a `RaggedTensor` values with shape `[4, None]`:\
\
    values = tf.ragged.constant([[1, 2, 3], [4], [5, 6], [7, 8, 9, 10]])\
\
Note that `rt1` only contains one ragged dimension (the innermost dimension). In contrast, if `from_row_splits` is used to construct a similar `RaggedTensor`, then that `RaggedTensor` will have two ragged dimensions:\
\
    rt2 = tf.RaggedTensor.from_row_splits(values, [0, 2, 4])\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `values` | A potentially ragged tensor with shape `[nvals, ...]`. |\
| `uniform_row_length` | A scalar integer tensor. Must be nonnegative. The size of the outer axis of `values` must be evenly divisible by `uniform_row_length`. |\
| `nrows` | The number of rows in the constructed RaggedTensor. If not specified, then it defaults to `nvals/uniform_row_length` (or `0` if `uniform_row_length==0`). `nrows` only needs to be specified if `uniform_row_length` might be zero. `uniform_row_length*nrows` must be `nvals`. |\
| `validate` | If true, then use assertions to check that the arguments form a valid `RaggedTensor`. Note: these assertions incur a runtime cost, since they must be checked for each tensor value. |\
| `name` | A name prefix for the RaggedTensor (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A `RaggedTensor` that corresponds with the python list defined by:<br><br>result = [[values.pop(0) for i in range(uniform_row_length)]<br>              for _ in range(nrows)]<br><br>`result.rank = values.rank + 1`. `result.ragged_rank = values.ragged_rank + 1`. |     |\
\
### `from_value_rowids`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_tensor.py#L360-L418)\
\
@classmethod\
\
Creates a `RaggedTensor` with rows partitioned by `value_rowids`.\
\
The returned `RaggedTensor` corresponds with the python list defined by:\
\
result = [[values[i] for i in range(len(values)) if value_rowids[i] == row]\
              for row in range(nrows)]\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `values` | A potentially ragged tensor with shape `[nvals, ...]`. |\
| `value_rowids` | A 1-D integer tensor with shape `[nvals]`, which corresponds one-to-one with `values`, and specifies each value's row index. Must be nonnegative, and must be sorted in ascending order. |\
| `nrows` | An integer scalar specifying the number of rows. This should be specified if the `RaggedTensor` may containing empty training rows. Must be greater than `value_rowids[-1]` (or zero if `value_rowids` is empty). Defaults to `value_rowids[-1] + 1` (or zero if `value_rowids` is empty). |\
| `name` | A name prefix for the RaggedTensor (optional). |\
| `validate` | If true, then use assertions to check that the arguments form a valid `RaggedTensor`. Note: these assertions incur a runtime cost, since they must be checked for each tensor value. |\
\
|     |\
| --- |\
| Returns |     |\
| A `RaggedTensor`. `result.rank = values.rank + 1`. `result.ragged_rank = values.ragged_rank + 1`. |     |\
\
|     |     |\
| --- | --- |\
| Raises |     |\
| `ValueError` | If `nrows` is incompatible with `value_rowids`. |\
\
#### Example:\
\
    print(tf.RaggedTensor.from_value_rowids(\
\
### `get_shape`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_tensor.py#L929-L948)\
\
get_shape() -> tf.TensorShape\
\
The statically known shape of this ragged tensor.\
\
|     |\
| --- |\
| Returns |     |\
| A `TensorShape` containing the statically known shape of this ragged tensor. Ragged dimensions have a size of `None`. |     |\
\
Alias for `shape` property.\
\
#### Examples:\
\
    tf.ragged.constant([[0], [1, 2]]).get_shape()\
\
    tf.ragged.constant(\
\
### `merge_dims`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_tensor.py#L1473-L1519)\
\
merge_dims(\
        outer_axis, inner_axis\
    )\
\
Merges outer\_axis...inner\_axis into a single dimension.\
\
Returns a copy of this RaggedTensor with the specified range of dimensions flattened into a single dimension, with elements in row-major order.\
\
#### Examples:\
\
    rt = tf.ragged.constant([[[1, 2], [3]], [[4, 5, 6]]])\
\
To mimic the behavior of `np.flatten` (which flattens all dimensions), use `rt.merge_dims(0, -1)`. To mimic the behavior of `tf.layers.Flatten` (which flattens all dimensions except the outermost batch dimension), use `rt.merge_dims(1, -1)`.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `outer_axis` | `int`: The first dimension in the range of dimensions to merge. May be negative if `self.shape.rank` is statically known. |\
| `inner_axis` | `int`: The last dimension in the range of dimensions to merge. May be negative if `self.shape.rank` is statically known. |\
\
|     |\
| --- |\
| Returns |     |\
| A copy of this tensor, with the specified dimensions merged into a single dimension. The shape of the returned tensor will be `self.shape[:outer_axis] + [N] + self.shape[inner_axis + 1:]`, where `N` is the total number of slices in the merged dimensions. |     |\
\
### `nested_row_lengths`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_tensor.py#L1306-L1325)\
\
nested_row_lengths(\
        name=None\
    )\
\
Returns a tuple containing the row\_lengths for all ragged dimensions.\
\
`rt.nested_row_lengths()` is a tuple containing the `row_lengths` tensors for all ragged dimensions in `rt`, ordered from outermost to innermost.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `name` | A name prefix for the returned tensors (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A `tuple` of 1-D integer `Tensors`. The length of the tuple is equal to `self.ragged_rank`. |     |\
\
### `nested_value_rowids`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_tensor.py#L1144-L1179)\
\
nested_value_rowids(\
        name=None\
    )\
\
Returns a tuple containing the value\_rowids for all ragged dimensions.\
\
`rt.nested_value_rowids` is a tuple containing the `value_rowids` tensors for all ragged dimensions in `rt`, ordered from outermost to innermost. In particular, `rt.nested_value_rowids = (rt.value_rowids(),) + value_ids` where:\
\
*   `value_ids = ()` if `rt.values` is a `Tensor`.\
*   `value_ids = rt.values.nested_value_rowids` otherwise.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `name` | A name prefix for the returned tensors (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A `tuple` of 1-D integer `Tensor`s. |     |\
\
#### Example:\
\
    rt = tf.ragged.constant(\
\
### `nrows`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_tensor.py#L1181-L1205)\
\
nrows(\
        out_type=None, name=None\
    )\
\
Returns the number of rows in this ragged tensor.\
\
I.e., the size of the outermost dimension of the tensor.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `out_type` | `dtype` for the returned tensor. Defaults to `self.row_splits.dtype`. |\
| `name` | A name prefix for the returned tensor (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A scalar `Tensor` with dtype `out_type`. |     |\
\
#### Example:\
\
    rt = tf.ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6], []])\
\
### `numpy`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_tensor.py#L2089-L2131)\
\
numpy()\
\
Returns a numpy `array` with the values for this `RaggedTensor`.\
\
Requires that this `RaggedTensor` was constructed in eager execution mode.\
\
Ragged dimensions are encoded using numpy `arrays` with `dtype=object` and `rank=1`, where each element is a single row.\
\
#### Examples\
\
In the following example, the value returned by [`RaggedTensor.numpy()`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor#numpy)\
 contains three numpy `array` objects: one for each row (with `rank=1` and `dtype=int64`), and one to combine them (with `rank=1` and `dtype=object`):\
\
    tf.ragged.constant([[1, 2, 3], [4, 5]], dtype=tf.int64).numpy()\
\
Uniform dimensions are encoded using multidimensional numpy `array`s. In the following example, the value returned by [`RaggedTensor.numpy()`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor#numpy)\
 contains a single numpy `array` object, with `rank=2` and `dtype=int64`:\
\
    tf.ragged.constant([[1, 2, 3], [4, 5, 6]], dtype=tf.int64).numpy()\
\
|     |\
| --- |\
| Returns |     |\
| A numpy `array`. |     |\
\
### `row_lengths`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_tensor.py#L1257-L1304)\
\
row_lengths(\
        axis=1, name=None\
    )\
\
Returns the lengths of the rows in this ragged tensor.\
\
`rt.row_lengths()[i]` indicates the number of values in the `i`th row of `rt`.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `axis` | An integer constant indicating the axis whose row lengths should be returned. |\
| `name` | A name prefix for the returned tensor (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A potentially ragged integer Tensor with shape `self.shape[:axis]`. |     |\
\
|     |     |\
| --- | --- |\
| Raises |     |\
| `ValueError` | If `axis` is out of bounds. |\
\
#### Example:\
\
    rt = tf.ragged.constant(\
\
### `row_limits`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_tensor.py#L1232-L1255)\
\
row_limits(\
        name=None\
    )\
\
Returns the limit indices for rows in this ragged tensor.\
\
These indices specify where the values for each row end in `self.values`. `rt.row_limits(self)` is equal to `rt.row_splits[:-1]`.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `name` | A name prefix for the returned tensor (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A 1-D integer Tensor with shape `[nrows]`. The returned tensor is nonnegative, and is sorted in ascending order. |     |\
\
#### Example:\
\
    rt = tf.ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6], []])\
\
### `row_starts`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_tensor.py#L1207-L1230)\
\
row_starts(\
        name=None\
    )\
\
Returns the start indices for rows in this ragged tensor.\
\
These indices specify where the values for each row begin in `self.values`. `rt.row_starts()` is equal to `rt.row_splits[:-1]`.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `name` | A name prefix for the returned tensor (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A 1-D integer Tensor with shape `[nrows]`. The returned tensor is nonnegative, and is sorted in ascending order. |     |\
\
#### Example:\
\
    rt = tf.ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6], []])\
\
### `to_list`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_tensor.py#L2133-L2163)\
\
to_list()\
\
Returns a nested Python `list` with the values for this `RaggedTensor`.\
\
Requires that `rt` was constructed in eager execution mode.\
\
|     |\
| --- |\
| Returns |     |\
| A nested Python `list`. |     |\
\
### `to_sparse`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_tensor.py#L1939-L1963)\
\
to_sparse(\
        name=None\
    )\
\
Converts this `RaggedTensor` into a [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)\
.\
\
#### Example:\
\
    rt = tf.ragged.constant([[1, 2, 3], [4], [], [5, 6]])\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `name` | A name prefix for the returned tensors (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A SparseTensor with the same values as `self`. |     |\
\
### `to_tensor`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_tensor.py#L1798-L1872)\
\
to_tensor(\
        default_value=None, name=None, shape=None\
    )\
\
Converts this `RaggedTensor` into a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)\
.\
\
If `shape` is specified, then the result is padded and/or truncated to the specified shape.\
\
#### Examples:\
\
    rt = tf.ragged.constant([[9, 8, 7], [], [6, 5], [4]])\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `default_value` | Value to set for indices not specified in `self`. Defaults to zero. `default_value` must be broadcastable to `self.shape[self.ragged_rank + 1:]`. |\
| `name` | A name prefix for the returned tensors (optional). |\
| `shape` | The shape of the resulting dense tensor. In particular, `result.shape[i]` is `shape[i]` (if `shape[i]` is not None), or `self.bounding_shape(i)` (otherwise).`shape.rank` must be `None` or equal to `self.rank`. |\
\
|     |\
| --- |\
| Returns |     |\
| A `Tensor` with shape `ragged.bounding_shape(self)` and the values specified by the non-empty values in `self`. Empty values are assigned `default_value`. |     |\
\
### `value_rowids`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_tensor.py#L1117-L1142)\
\
value_rowids(\
        name=None\
    )\
\
Returns the row indices for the `values` in this ragged tensor.\
\
`rt.value_rowids()` corresponds one-to-one with the outermost dimension of `rt.values`, and specifies the row containing each value. In particular, the row `rt[row]` consists of the values `rt.values[j]` where `rt.value_rowids()[j] == row`.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `name` | A name prefix for the returned tensor (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A 1-D integer `Tensor` with shape `self.values.shape[:1]`. The returned tensor is nonnegative, and is sorted in ascending order. |     |\
\
#### Example:\
\
    rt = tf.ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6], []])\
\
### `with_flat_values`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_tensor.py#L1420-L1440)\
\
with_flat_values(\
        new_values\
    )\
\
Returns a copy of `self` with `flat_values` replaced by `new_value`.\
\
Preserves cached row-partitioning tensors such as `self.cached_nrows` and `self.cached_value_rowids` if they have values.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `new_values` | Potentially ragged tensor that should replace `self.flat_values`. Must have `rank > 0`, and must have the same number of rows as `self.flat_values`. |\
\
|     |\
| --- |\
| Returns |     |\
| A `RaggedTensor`. `result.rank = self.ragged_rank + new_values.rank`. `result.ragged_rank = self.ragged_rank + new_values.ragged_rank`. |     |\
\
### `with_row_splits_dtype`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_tensor.py#L1442-L1471)\
\
with_row_splits_dtype(\
        dtype\
    )\
\
Returns a copy of this RaggedTensor with the given `row_splits` dtype.\
\
For RaggedTensors with multiple ragged dimensions, the `row_splits` for all nested `RaggedTensor` objects are cast to the given dtype.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `dtype` | The dtype for `row_splits`. One of [`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)<br> or [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br>. |\
\
|     |\
| --- |\
| Returns |     |\
| A copy of this RaggedTensor, with the `row_splits` cast to the given type. |     |\
\
### `with_values`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_tensor.py#L1391-L1418)\
\
with_values(\
        new_values\
    )\
\
Returns a copy of `self` with `values` replaced by `new_value`.\
\
Preserves cached row-partitioning tensors such as `self.cached_nrows` and `self.cached_value_rowids` if they have values.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `new_values` | Potentially ragged tensor to use as the `values` for the returned `RaggedTensor`. Must have `rank > 0`, and must have the same number of rows as `self.values`. |\
\
|     |\
| --- |\
| Returns |     |\
| A `RaggedTensor`. `result.rank = 1 + new_values.rank`. `result.ragged_rank = 1 + new_values.ragged_rank` |     |\
\
### `__abs__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_operators.py#L143-L177)\
\
__abs__(\
        name=None\
    )\
\
Computes the absolute value of a ragged tensor.\
\
Given a ragged tensor of integer or floating-point values, this operation returns a ragged tensor of the same type, where each element contains the absolute value of the corresponding element in the input.\
\
Given a ragged tensor `x` of complex numbers, this operation returns a tensor of type `float32` or `float64` that is the absolute value of each element in `x`. For a complex number \\(a + bj\\), its absolute value is computed as \\(\\sqrt{a^2 + b^2}\\).\
\
#### For example:\
\
    # real number\
\
    # complex number\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A `RaggedTensor` of the same size and type as `x`, with absolute values. Note, for `complex64` or `complex128` input, the returned `RaggedTensor` will be of type `float32` or `float64`, respectively. |     |\
\
### `__add__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L3916-L3994)\
\
__add__(\
        y, name=None\
    )\
\
Returns x + y element-wise.\
\
Example usages below.\
\
Add a scalar and a list:\
\
    x = [1, 2, 3, 4, 5]\
\
Note that binary `+` operator can be used instead:\
\
    x = tf.convert_to_tensor([1, 2, 3, 4, 5])\
\
Add a tensor and a list of same shape:\
\
    x = [1, 2, 3, 4, 5]\
\
For example,\
\
    x = tf.constant([1, 2], dtype=tf.int8)\
\
When adding two input values of different shapes, `Add` follows NumPy broadcasting rules. The two input array shapes are compared element-wise. Starting with the trailing dimensions, the two dimensions either have to be equal or one of them needs to be `1`.\
\
For example,\
\
    x = np.ones(6).reshape(1, 2, 1, 3)\
\
Another example with two arrays of different dimension.\
\
    x = np.ones([1, 2, 1, 4])\
\
The reduction version of this elementwise operation is [`tf.math.reduce_sum`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_sum)\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `x` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>. Must be one of the following types: bfloat16, half, float16, float32, float64, uint8, uint16, uint32, uint64, int8, int16, int32, int64, complex64, complex128, string. |\
| `y` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>. Must have the same type as x. |\
| `name` | A name for the operation (optional) |\
\
### `__and__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_operators.py#L181-L248)\
\
__and__(\
        y, name=None\
    )\
\
Returns the truth value of elementwise `x & y`.\
\
Logical AND function.\
\
Requires that `x` and `y` have the same shape or have [broadcast-compatible](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)\
 shapes. For example, `y` can be:\
\
*   A single Python boolean, where the result will be calculated by applying logical AND with the single element to each element in `x`.\
*   A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)\
     object of dtype [`tf.bool`](https://www.tensorflow.org/api_docs/python/tf#bool)\
     of the same shape or [broadcast-compatible](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)\
     shape. In this case, the result will be the element-wise logical AND of `x` and `y`.\
*   A [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)\
     object of dtype [`tf.bool`](https://www.tensorflow.org/api_docs/python/tf#bool)\
     of the same shape or [broadcast-compatible](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)\
     shape. In this case, the result will be the element-wise logical AND of `x` and `y`.\
\
#### For example:\
\
    # `y` is a Python boolean\
\
    # `y` is a tf.Tensor of the same shape.\
\
    # `y` is a tf.Tensor of a broadcast-compatible shape.\
\
    # `y` is a `tf.RaggedTensor` of the same shape.\
\
    # `y` is a `tf.RaggedTensor` of a broadcast-compatible shape.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `y` | A Python boolean or a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> or [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)<br> of dtype [`tf.bool`](https://www.tensorflow.org/api_docs/python/tf#bool)<br>. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)<br> of dtype [`tf.bool`](https://www.tensorflow.org/api_docs/python/tf#bool)<br> with the shape that `x` and `y` broadcast to. |     |\
\
### `__bool__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_operators.py#L316-L338)\
\
__bool__()\
\
Raises TypeError when a RaggedTensor is used as a Python bool.\
\
To prevent RaggedTensor from being used as a bool, this function always raise TypeError when being called.\
\
#### For example:\
\
    x = tf.ragged.constant([[1, 2], [3]])\
\
    x = tf.ragged.constant([[1]])\
\
### `__div__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L1564-L1593)\
\
__div__(\
        y, name=None\
    )\
\
Divides x / y elementwise (using Python 2 division operator semantics). (deprecated)\
\
This function divides `x` and `y`, forcing Python 2 semantics. That is, if `x` and `y` are both integers then the result will be an integer. This is in contrast to Python 3, where division with `/` is always a float while division with `//` is always an integer.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `x` | `Tensor` numerator of real numeric type. |\
| `y` | `Tensor` denominator of real numeric type. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| `x / y` returns the quotient of x and y. |     |\
\
#### Migrate to TF2\
\
This function is deprecated in TF2. Prefer using the Tensor division operator, [`tf.divide`](https://www.tensorflow.org/api_docs/python/tf/math/divide)\
, or [`tf.math.divide`](https://www.tensorflow.org/api_docs/python/tf/math/divide)\
, which obey the Python 3 division operator semantics.\
\
### `__eq__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_operators.py#L28-L72)\
\
__eq__(\
        other\
    )\
\
Returns result of elementwise `==` or False if not broadcast-compatible.\
\
Compares two ragged tensors elemewise for equality if they are broadcast-compatible; or returns False if they are not [broadcast-compatible](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)\
.\
\
Note that this behavior differs from [`tf.math.equal`](https://www.tensorflow.org/api_docs/python/tf/math/equal)\
, which raises an exception if the two ragged tensors are not broadcast-compatible.\
\
#### For example:\
\
    rt1 = tf.ragged.constant([[1, 2], [3]])\
\
    rt2 = tf.ragged.constant([[1, 2], [4]])\
\
    rt3 = tf.ragged.constant([[1, 2], [3, 4]])\
\
    # You can also compare a `tf.RaggedTensor` to a `tf.Tensor`.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `other` | The right-hand side of the `==` operator. |\
\
|     |\
| --- |\
| Returns |     |\
| The ragged tensor result of the elementwise `==` operation, or `False` if the arguments are not broadcast-compatible. |     |\
\
### `__floordiv__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L1704-L1731)\
\
__floordiv__(\
        y, name=None\
    )\
\
Divides `x / y` elementwise, rounding toward the most negative integer.\
\
Mathematically, this is equivalent to floor(x / y). For example: floor(8.4 / 4.0) = floor(2.1) = 2.0 floor(-8.4 / 4.0) = floor(-2.1) = -3.0 This is equivalent to the '//' operator in Python 3.0 and above.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `x` | `Tensor` numerator of real numeric type. |\
| `y` | `Tensor` denominator of real numeric type. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| `x / y` rounded toward -infinity. |     |\
\
|     |     |\
| --- | --- |\
| Raises |     |\
| `TypeError` | If the inputs are complex. |\
\
### `__ge__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_operators.py#L78-L132)\
\
__ge__(\
        other\
    )\
\
Elementwise `>=` comparison of two convertible-to-ragged-tensor values.\
\
Computes the elemewise `>=` comparison of two values that are convertible to ragged tenors, with [broadcasting](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)\
 support. Raises an exception if two values are not broadcast-compatible.\
\
#### For example:\
\
    rt1 = tf.ragged.constant([[1, 2], [3]])\
\
    rt2 = tf.ragged.constant([[2, 1], [3]])\
\
    rt3 = tf.ragged.constant([[1, 2], [3, 4]])\
\
    # You can also compare a `tf.RaggedTensor` to a `tf.Tensor`.\
\
    # Compares a `tf.RaggedTensor` to a `tf.Tensor` with broadcasting.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `other` | The right-hand side of the `>=` operator. |\
\
|     |\
| --- |\
| Returns |     |\
| A [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)<br> of dtype [`tf.bool`](https://www.tensorflow.org/api_docs/python/tf#bool)<br> with the shape that `self` and `other` broadcast to. |     |\
\
|     |     |\
| --- | --- |\
| Raises |     |\
| `InvalidArgumentError` | If `self` and `other` are not broadcast-compatible. |\
\
### `__getitem__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_getitem.py#L34-L106)\
\
__getitem__(\
        key\
    )\
\
Returns the specified piece of this RaggedTensor.\
\
Supports multidimensional indexing and slicing, with one restriction: indexing into a ragged inner dimension is not allowed. This case is problematic because the indicated value may exist in some rows but not others. In such cases, it's not obvious whether we should (1) report an IndexError; (2) use a default value; or (3) skip that value and return a tensor with fewer rows than we started with. Following the guiding principles of Python ("In the face of ambiguity, refuse the temptation to guess"), we simply disallow this operation.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `rt_input` | The RaggedTensor to slice. |\
| `key` | Indicates which piece of the RaggedTensor to return, using standard Python semantics (e.g., negative values index from the end). `key` may have any of the following types:<br><br>*   `int` constant<br>*   Scalar integer `Tensor`<br>*   `slice` containing integer constants and/or scalar integer `Tensor`s<br>    <br>*   `Ellipsis`<br>    <br>*   [`tf.newaxis`](https://www.tensorflow.org/api_docs/python/tf#newaxis)<br>    <br>*   `tuple` containing any of the above (for multidimensional indexing) |\
\
|     |\
| --- |\
| Returns |     |\
| A `Tensor` or `RaggedTensor` object. Values that include at least one ragged dimension are returned as `RaggedTensor`. Values that include no ragged dimensions are returned as `Tensor`. See above for examples of expressions that return `Tensor`s vs `RaggedTensor`s. |     |\
\
|     |     |\
| --- | --- |\
| Raises |     |\
| `ValueError` | If `key` is out of bounds. |\
| `ValueError` | If `key` is not supported. |\
| `TypeError` | If the indices in `key` have an unsupported type. |\
\
#### Examples:\
\
    # A 2-D ragged tensor with 1 ragged dimension.\
\
    # A 3-D ragged tensor with 2 ragged dimensions.\
\
### `__gt__`\
\
__gt__(\
        y: Annotated[Any, tf.raw_ops.Any],\
        name=None\
    ) -> Annotated[Any, tf.raw_ops.Any]\
\
Returns the truth value of (x > y) element-wise.\
\
#### Example:\
\
x = tf.constant([5, 4, 6])\
    y = tf.constant([5, 2, 5])\
    tf.math.greater(x, y) ==> [False, True, True]\
    \
    x = tf.constant([5, 4, 6])\
    y = tf.constant([5])\
    tf.math.greater(x, y) ==> [False, False, True]\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `x` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`. |\
| `y` | A `Tensor`. Must have the same type as `x`. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A `Tensor` of type `bool`. |     |\
\
### `__invert__`\
\
__invert__(\
        name=None\
    ) -> Annotated[Any, tf.raw_ops.Any]\
\
Returns the truth value of `NOT x` element-wise.\
\
#### Example:\
\
    tf.math.logical_not(tf.constant([True, False]))\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `x` | A `Tensor` of type `bool`. A `Tensor` of type `bool`. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A `Tensor` of type `bool`. |     |\
\
### `__le__`\
\
__le__(\
        y: Annotated[Any, tf.raw_ops.Any],\
        name=None\
    ) -> Annotated[Any, tf.raw_ops.Any]\
\
Returns the truth value of (x <= y) element-wise.\
\
#### Example:\
\
x = tf.constant([5, 4, 6])\
    y = tf.constant([5])\
    tf.math.less_equal(x, y) ==> [True, True, False]\
    \
    x = tf.constant([5, 4, 6])\
    y = tf.constant([5, 6, 6])\
    tf.math.less_equal(x, y) ==> [True, True, True]\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `x` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`. |\
| `y` | A `Tensor`. Must have the same type as `x`. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A `Tensor` of type `bool`. |     |\
\
### `__lt__`\
\
__lt__(\
        y: Annotated[Any, tf.raw_ops.Any],\
        name=None\
    ) -> Annotated[Any, tf.raw_ops.Any]\
\
Returns the truth value of (x < y) element-wise.\
\
#### Example:\
\
x = tf.constant([5, 4, 6])\
    y = tf.constant([5])\
    tf.math.less(x, y) ==> [False, True, False]\
    \
    x = tf.constant([5, 4, 6])\
    y = tf.constant([5, 6, 7])\
    tf.math.less(x, y) ==> [False, True, True]\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `x` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`. |\
| `y` | A `Tensor`. Must have the same type as `x`. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A `Tensor` of type `bool`. |     |\
\
### `__mod__`\
\
__mod__(\
        y: Annotated[Any, tf.raw_ops.Any],\
        name=None\
    ) -> Annotated[Any, tf.raw_ops.Any]\
\
Returns element-wise remainder of division.\
\
This follows Python semantics in that the result here is consistent with a flooring divide. E.g. `floor(x / y) * y + floormod(x, y) = x`, regardless of the signs of x and y.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `x` | A `Tensor`. Must be one of the following types: `int8`, `int16`, `int32`, `int64`, `uint8`, `uint16`, `uint32`, `uint64`, `bfloat16`, `half`, `float32`, `float64`. |\
| `y` | A `Tensor`. Must have the same type as `x`. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A `Tensor`. Has the same type as `x`. |     |\
\
### `__mul__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L505-L554)\
\
__mul__(\
        y, name=None\
    )\
\
Returns an element-wise x \* y.\
\
#### For example:\
\
    x = tf.constant(([1, 2, 3, 4]))\
\
Since [`tf.math.multiply`](https://www.tensorflow.org/api_docs/python/tf/math/multiply)\
 will convert its arguments to `Tensor`s, you can also pass in non-`Tensor` arguments:\
\
    tf.math.multiply(7,6)\
\
If `x.shape` is not the same as `y.shape`, they will be broadcast to a compatible shape. (More about broadcasting [here](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)\
.)\
\
#### For example:\
\
    x = tf.ones([1, 2]);\
\
The reduction version of this elementwise operation is [`tf.math.reduce_prod`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_prod)\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `x` | A Tensor. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `uint16`, `int16`, `int32`, `int64`, `complex64`, `complex128`. |\
| `y` | A `Tensor`. Must have the same type as `x`. |\
| `name` | A name for the operation (optional). |\
\
Returns\
\
A `Tensor`. Has the same type as `x`.\
\
|     |\
| --- |\
| Raises |     |\
| *   InvalidArgumentError: When `x` and `y` have incompatible shapes or types. |     |\
\
### `__ne__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L1976-L2013)\
\
__ne__(\
        other\
    )\
\
The operation invoked by the [`Tensor.**ne**`](https://www.tensorflow.org/api_docs/python/tf/Tensor#__ne__)\
 operator.\
\
Compares two tensors element-wise for inequality if they are broadcast-compatible; or returns True if they are not broadcast-compatible. (Note that this behavior differs from [`tf.math.not_equal`](https://www.tensorflow.org/api_docs/python/tf/math/not_equal)\
, which raises an exception if the two tensors are not broadcast-compatible.)\
\
|     |\
| --- |\
| Purpose in the API |     |\
| This method is exposed in TensorFlow's API so that library developers can register dispatching for [`Tensor.**ne**`](https://www.tensorflow.org/api_docs/python/tf/Tensor#__ne__)<br> to allow it to handle custom composite tensors & other custom objects.<br><br>The API symbol is not intended to be called by users directly and does appear in TensorFlow's generated documentation. |     |\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `self` | The left-hand side of the `!=` operator. |\
| `other` | The right-hand side of the `!=` operator. |\
\
|     |\
| --- |\
| Returns |     |\
| The result of the elementwise `!=` operation, or `True` if the arguments are not broadcast-compatible. |     |\
\
### `__neg__`\
\
__neg__(\
        name=None\
    ) -> Annotated[Any, tf.raw_ops.Any]\
\
Computes numerical negative value element-wise.\
\
I.e., \\(y = -x\\).\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int8`, `int16`, `int32`, `int64`, `complex64`, `complex128`. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A `Tensor`. Has the same type as `x`.<br><br>If `x` is a `SparseTensor`, returns `SparseTensor(x.indices, tf.math.negative(x.values, ...), x.dense_shape)` |     |\
\
### `__nonzero__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_operators.py#L316-L338)\
\
__nonzero__()\
\
Raises TypeError when a RaggedTensor is used as a Python bool.\
\
To prevent RaggedTensor from being used as a bool, this function always raise TypeError when being called.\
\
#### For example:\
\
    x = tf.ragged.constant([[1, 2], [3]])\
\
    x = tf.ragged.constant([[1]])\
\
### `__or__`\
\
__or__(\
        y: Annotated[Any, tf.raw_ops.Any],\
        name=None\
    ) -> Annotated[Any, tf.raw_ops.Any]\
\
Returns the truth value of x OR y element-wise.\
\
Logical OR function.\
\
Requires that `x` and `y` have the same shape or have [broadcast-compatible](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)\
 shapes. For example, `x` and `y` can be:\
\
*   Two single elements of type `bool`.\
*   One [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)\
     of type `bool` and one single `bool`, where the result will be calculated by applying logical OR with the single element to each element in the larger Tensor.\
*   Two [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)\
     objects of type `bool` of the same shape. In this case, the result will be the element-wise logical OR of the two input tensors.\
\
You can also use the `|` operator instead.\
\
|     |\
| --- |\
| Usage |     |\
| >>> a = tf.constant([True])<br>    >>> b = tf.constant([False])<br>    >>> tf.math.logical_or(a, b)<br>    <tf.Tensor: shape=(1,), dtype=bool, numpy=array([ True])><br>    >>> a \| b<br>    <tf.Tensor: shape=(1,), dtype=bool, numpy=array([ True])><br><br>    c = tf.constant([False])<br><br>    y = tf.constant([False, False, True, True])<br><br>This op also supports broadcasting<br><br>    tf.logical_or([[True, False]], [[True], [False]]) |     |\
\
The reduction version of this elementwise operation is [`tf.math.reduce_any`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_any)\
.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `x` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of type bool. |\
| `y` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of type bool. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of type bool with the shape that `x` and `y` broadcast to. |     |\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `x` | A `Tensor` of type `bool`. |\
| `y` | A `Tensor` of type `bool`. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A `Tensor` of type `bool`. |     |\
\
### `__pow__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L697-L723)\
\
__pow__(\
        y, name=None\
    )\
\
Computes the power of one value to another.\
\
Given a tensor `x` and a tensor `y`, this operation computes \\(x^y\\) for corresponding elements in `x` and `y`. For example:\
\
x = tf.constant([[2, 2], [3, 3]])\
    y = tf.constant([[8, 16], [2, 3]])\
    tf.pow(x, y)  # [[256, 65536], [9, 27]]\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `x` | A `Tensor` of type `float16`, `float32`, `float64`, `int32`, `int64`, `complex64`, or `complex128`. |\
| `y` | A `Tensor` of type `float16`, `float32`, `float64`, `int32`, `int64`, `complex64`, or `complex128`. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A `Tensor`. |     |\
\
### `__radd__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L3916-L3994)\
\
__radd__(\
        y, name=None\
    )\
\
Returns x + y element-wise.\
\
Example usages below.\
\
Add a scalar and a list:\
\
    x = [1, 2, 3, 4, 5]\
\
Note that binary `+` operator can be used instead:\
\
    x = tf.convert_to_tensor([1, 2, 3, 4, 5])\
\
Add a tensor and a list of same shape:\
\
    x = [1, 2, 3, 4, 5]\
\
For example,\
\
    x = tf.constant([1, 2], dtype=tf.int8)\
\
When adding two input values of different shapes, `Add` follows NumPy broadcasting rules. The two input array shapes are compared element-wise. Starting with the trailing dimensions, the two dimensions either have to be equal or one of them needs to be `1`.\
\
For example,\
\
    x = np.ones(6).reshape(1, 2, 1, 3)\
\
Another example with two arrays of different dimension.\
\
    x = np.ones([1, 2, 1, 4])\
\
The reduction version of this elementwise operation is [`tf.math.reduce_sum`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_sum)\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `x` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>. Must be one of the following types: bfloat16, half, float16, float32, float64, uint8, uint16, uint32, uint64, int8, int16, int32, int64, complex64, complex128, string. |\
| `y` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>. Must have the same type as x. |\
| `name` | A name for the operation (optional) |\
\
### `__rand__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_operators.py#L181-L248)\
\
__rand__(\
        y, name=None\
    )\
\
Returns the truth value of elementwise `x & y`.\
\
Logical AND function.\
\
Requires that `x` and `y` have the same shape or have [broadcast-compatible](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)\
 shapes. For example, `y` can be:\
\
*   A single Python boolean, where the result will be calculated by applying logical AND with the single element to each element in `x`.\
*   A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)\
     object of dtype [`tf.bool`](https://www.tensorflow.org/api_docs/python/tf#bool)\
     of the same shape or [broadcast-compatible](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)\
     shape. In this case, the result will be the element-wise logical AND of `x` and `y`.\
*   A [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)\
     object of dtype [`tf.bool`](https://www.tensorflow.org/api_docs/python/tf#bool)\
     of the same shape or [broadcast-compatible](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)\
     shape. In this case, the result will be the element-wise logical AND of `x` and `y`.\
\
#### For example:\
\
    # `y` is a Python boolean\
\
    # `y` is a tf.Tensor of the same shape.\
\
    # `y` is a tf.Tensor of a broadcast-compatible shape.\
\
    # `y` is a `tf.RaggedTensor` of the same shape.\
\
    # `y` is a `tf.RaggedTensor` of a broadcast-compatible shape.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `y` | A Python boolean or a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> or [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)<br> of dtype [`tf.bool`](https://www.tensorflow.org/api_docs/python/tf#bool)<br>. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)<br> of dtype [`tf.bool`](https://www.tensorflow.org/api_docs/python/tf#bool)<br> with the shape that `x` and `y` broadcast to. |     |\
\
### `__rdiv__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L1564-L1593)\
\
__rdiv__(\
        y, name=None\
    )\
\
Divides x / y elementwise (using Python 2 division operator semantics). (deprecated)\
\
This function divides `x` and `y`, forcing Python 2 semantics. That is, if `x` and `y` are both integers then the result will be an integer. This is in contrast to Python 3, where division with `/` is always a float while division with `//` is always an integer.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `x` | `Tensor` numerator of real numeric type. |\
| `y` | `Tensor` denominator of real numeric type. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| `x / y` returns the quotient of x and y. |     |\
\
#### Migrate to TF2\
\
This function is deprecated in TF2. Prefer using the Tensor division operator, [`tf.divide`](https://www.tensorflow.org/api_docs/python/tf/math/divide)\
, or [`tf.math.divide`](https://www.tensorflow.org/api_docs/python/tf/math/divide)\
, which obey the Python 3 division operator semantics.\
\
### `__rfloordiv__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L1704-L1731)\
\
__rfloordiv__(\
        y, name=None\
    )\
\
Divides `x / y` elementwise, rounding toward the most negative integer.\
\
Mathematically, this is equivalent to floor(x / y). For example: floor(8.4 / 4.0) = floor(2.1) = 2.0 floor(-8.4 / 4.0) = floor(-2.1) = -3.0 This is equivalent to the '//' operator in Python 3.0 and above.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `x` | `Tensor` numerator of real numeric type. |\
| `y` | `Tensor` denominator of real numeric type. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| `x / y` rounded toward -infinity. |     |\
\
|     |     |\
| --- | --- |\
| Raises |     |\
| `TypeError` | If the inputs are complex. |\
\
### `__rmod__`\
\
__rmod__(\
        y: Annotated[Any, tf.raw_ops.Any],\
        name=None\
    ) -> Annotated[Any, tf.raw_ops.Any]\
\
Returns element-wise remainder of division.\
\
This follows Python semantics in that the result here is consistent with a flooring divide. E.g. `floor(x / y) * y + floormod(x, y) = x`, regardless of the signs of x and y.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `x` | A `Tensor`. Must be one of the following types: `int8`, `int16`, `int32`, `int64`, `uint8`, `uint16`, `uint32`, `uint64`, `bfloat16`, `half`, `float32`, `float64`. |\
| `y` | A `Tensor`. Must have the same type as `x`. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A `Tensor`. Has the same type as `x`. |     |\
\
### `__rmul__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L505-L554)\
\
__rmul__(\
        y, name=None\
    )\
\
Returns an element-wise x \* y.\
\
#### For example:\
\
    x = tf.constant(([1, 2, 3, 4]))\
\
Since [`tf.math.multiply`](https://www.tensorflow.org/api_docs/python/tf/math/multiply)\
 will convert its arguments to `Tensor`s, you can also pass in non-`Tensor` arguments:\
\
    tf.math.multiply(7,6)\
\
If `x.shape` is not the same as `y.shape`, they will be broadcast to a compatible shape. (More about broadcasting [here](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)\
.)\
\
#### For example:\
\
    x = tf.ones([1, 2]);\
\
The reduction version of this elementwise operation is [`tf.math.reduce_prod`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_prod)\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `x` | A Tensor. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `uint16`, `int16`, `int32`, `int64`, `complex64`, `complex128`. |\
| `y` | A `Tensor`. Must have the same type as `x`. |\
| `name` | A name for the operation (optional). |\
\
Returns\
\
A `Tensor`. Has the same type as `x`.\
\
|     |\
| --- |\
| Raises |     |\
| *   InvalidArgumentError: When `x` and `y` have incompatible shapes or types. |     |\
\
### `__ror__`\
\
__ror__(\
        y: Annotated[Any, tf.raw_ops.Any],\
        name=None\
    ) -> Annotated[Any, tf.raw_ops.Any]\
\
Returns the truth value of x OR y element-wise.\
\
Logical OR function.\
\
Requires that `x` and `y` have the same shape or have [broadcast-compatible](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)\
 shapes. For example, `x` and `y` can be:\
\
*   Two single elements of type `bool`.\
*   One [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)\
     of type `bool` and one single `bool`, where the result will be calculated by applying logical OR with the single element to each element in the larger Tensor.\
*   Two [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)\
     objects of type `bool` of the same shape. In this case, the result will be the element-wise logical OR of the two input tensors.\
\
You can also use the `|` operator instead.\
\
|     |\
| --- |\
| Usage |     |\
| >>> a = tf.constant([True])<br>    >>> b = tf.constant([False])<br>    >>> tf.math.logical_or(a, b)<br>    <tf.Tensor: shape=(1,), dtype=bool, numpy=array([ True])><br>    >>> a \| b<br>    <tf.Tensor: shape=(1,), dtype=bool, numpy=array([ True])><br><br>    c = tf.constant([False])<br><br>    y = tf.constant([False, False, True, True])<br><br>This op also supports broadcasting<br><br>    tf.logical_or([[True, False]], [[True], [False]]) |     |\
\
The reduction version of this elementwise operation is [`tf.math.reduce_any`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_any)\
.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `x` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of type bool. |\
| `y` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of type bool. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of type bool with the shape that `x` and `y` broadcast to. |     |\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `x` | A `Tensor` of type `bool`. |\
| `y` | A `Tensor` of type `bool`. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A `Tensor` of type `bool`. |     |\
\
### `__rpow__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L697-L723)\
\
__rpow__(\
        y, name=None\
    )\
\
Computes the power of one value to another.\
\
Given a tensor `x` and a tensor `y`, this operation computes \\(x^y\\) for corresponding elements in `x` and `y`. For example:\
\
x = tf.constant([[2, 2], [3, 3]])\
    y = tf.constant([[8, 16], [2, 3]])\
    tf.pow(x, y)  # [[256, 65536], [9, 27]]\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `x` | A `Tensor` of type `float16`, `float32`, `float64`, `int32`, `int64`, `complex64`, or `complex128`. |\
| `y` | A `Tensor` of type `float16`, `float32`, `float64`, `int32`, `int64`, `complex64`, or `complex128`. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A `Tensor`. |     |\
\
### `__rsub__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L571-L575)\
\
__rsub__(\
        y, name=None\
    )\
\
Returns x - y element-wise.\
\
Both input and output have a range `(-inf, inf)`.\
\
Example usages below.\
\
Subtract operation between an array and a scalar:\
\
    x = [1, 2, 3, 4, 5]\
\
Note that binary `-` operator can be used instead:\
\
    x = tf.convert_to_tensor([1, 2, 3, 4, 5])\
\
Subtract operation between an array and a tensor of same shape:\
\
    x = [1, 2, 3, 4, 5]\
\
For example,\
\
    x = tf.constant([1, 2], dtype=tf.int8)\
\
When subtracting two input values of different shapes, [`tf.subtract`](https://www.tensorflow.org/api_docs/python/tf/math/subtract)\
 follows the [general broadcasting rules](https://numpy.org/doc/stable/user/basics.broadcasting.html#general-broadcasting-rules)\
 . The two input array shapes are compared element-wise. Starting with the trailing dimensions, the two dimensions either have to be equal or one of them needs to be `1`.\
\
For example,\
\
    x = np.ones(6).reshape(2, 3, 1)\
\
Example with inputs of different dimensions:\
\
    x = np.ones(6).reshape(2, 3, 1)\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `uint16`, `int16`, `int32`, `int64`, `complex64`, `complex128`, `uint32`, `uint64`. |\
| `y` | A `Tensor`. Must have the same type as `x`. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A `Tensor`. Has the same type as `x`. |     |\
\
### `__rtruediv__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L1509-L1561)\
\
__rtruediv__(\
        y, name=None\
    )\
\
Divides x / y elementwise (using Python 3 division operator semantics).\
\
This function forces Python 3 division operator semantics where all integer arguments are cast to floating types first. If you want integer division that rounds down, use `x // y` or `tf.math.floordiv`.\
\
`x` and `y` must have the same numeric type. If the inputs are floating point, the output will have the same type. If the inputs are integral, the inputs are cast to `float32` for `int8` and `int16` and `float64` for `int32` and `int64` (matching the behavior of Numpy).\
\
#### Example:\
\
    # Division with integer tensors (returns float)\
\
    # Division with different shaped tensors (broadcasting)\
\
Handling potential division by zero (returns inf)\
=================================================\
\
>>> x3 = tf.constant(5, dtype=tf.float32)\
    >>> y3 = tf.constant(0, dtype=tf.float32)\
    >>> result3 = tf.math.truediv(x3, y3)\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `x` | `Tensor` numerator of numeric type. |\
| `y` | `Tensor` denominator of numeric type. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| `x / y` evaluated in floating point. |     |\
\
|     |     |\
| --- | --- |\
| Raises |     |\
| `TypeError` | If `x` and `y` have different dtypes. |\
\
### `__rxor__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L1784-L1833)\
\
__rxor__(\
        y, name='LogicalXor'\
    )\
\
Logical XOR function.\
\
x ^ y = (x | y) & ~(x & y)\
\
Requires that `x` and `y` have the same shape or have [broadcast-compatible](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)\
 shapes. For example, `x` and `y` can be:\
\
*   Two single elements of type `bool`\
*   One [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)\
     of type `bool` and one single `bool`, where the result will be calculated by applying logical XOR with the single element to each element in the larger Tensor.\
*   Two [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)\
     objects of type `bool` of the same shape. In this case, the result will be the element-wise logical XOR of the two input tensors.\
\
#### Usage:\
\
    a = tf.constant([True])\
\
    c = tf.constant([True])\
\
    y = tf.constant([False, False, True, True])\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `x` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> type bool. |\
| `y` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of type bool. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of type bool with the same size as that of x or y. |     |\
\
### `__sub__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L571-L575)\
\
__sub__(\
        y, name=None\
    )\
\
Returns x - y element-wise.\
\
Both input and output have a range `(-inf, inf)`.\
\
Example usages below.\
\
Subtract operation between an array and a scalar:\
\
    x = [1, 2, 3, 4, 5]\
\
Note that binary `-` operator can be used instead:\
\
    x = tf.convert_to_tensor([1, 2, 3, 4, 5])\
\
Subtract operation between an array and a tensor of same shape:\
\
    x = [1, 2, 3, 4, 5]\
\
For example,\
\
    x = tf.constant([1, 2], dtype=tf.int8)\
\
When subtracting two input values of different shapes, [`tf.subtract`](https://www.tensorflow.org/api_docs/python/tf/math/subtract)\
 follows the [general broadcasting rules](https://numpy.org/doc/stable/user/basics.broadcasting.html#general-broadcasting-rules)\
 . The two input array shapes are compared element-wise. Starting with the trailing dimensions, the two dimensions either have to be equal or one of them needs to be `1`.\
\
For example,\
\
    x = np.ones(6).reshape(2, 3, 1)\
\
Example with inputs of different dimensions:\
\
    x = np.ones(6).reshape(2, 3, 1)\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `uint16`, `int16`, `int32`, `int64`, `complex64`, `complex128`, `uint32`, `uint64`. |\
| `y` | A `Tensor`. Must have the same type as `x`. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A `Tensor`. Has the same type as `x`. |     |\
\
### `__truediv__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L1509-L1561)\
\
__truediv__(\
        y, name=None\
    )\
\
Divides x / y elementwise (using Python 3 division operator semantics).\
\
This function forces Python 3 division operator semantics where all integer arguments are cast to floating types first. If you want integer division that rounds down, use `x // y` or `tf.math.floordiv`.\
\
`x` and `y` must have the same numeric type. If the inputs are floating point, the output will have the same type. If the inputs are integral, the inputs are cast to `float32` for `int8` and `int16` and `float64` for `int32` and `int64` (matching the behavior of Numpy).\
\
#### Example:\
\
    # Division with integer tensors (returns float)\
\
    # Division with different shaped tensors (broadcasting)\
\
Handling potential division by zero (returns inf)\
=================================================\
\
>>> x3 = tf.constant(5, dtype=tf.float32)\
    >>> y3 = tf.constant(0, dtype=tf.float32)\
    >>> result3 = tf.math.truediv(x3, y3)\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `x` | `Tensor` numerator of numeric type. |\
| `y` | `Tensor` denominator of numeric type. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| `x / y` evaluated in floating point. |     |\
\
|     |     |\
| --- | --- |\
| Raises |     |\
| `TypeError` | If `x` and `y` have different dtypes. |\
\
### `__xor__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L1784-L1833)\
\
__xor__(\
        y, name='LogicalXor'\
    )\
\
Logical XOR function.\
\
x ^ y = (x | y) & ~(x & y)\
\
Requires that `x` and `y` have the same shape or have [broadcast-compatible](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)\
 shapes. For example, `x` and `y` can be:\
\
*   Two single elements of type `bool`\
*   One [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)\
     of type `bool` and one single `bool`, where the result will be calculated by applying logical XOR with the single element to each element in the larger Tensor.\
*   Two [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)\
     objects of type `bool` of the same shape. In this case, the result will be the element-wise logical XOR of the two input tensors.\
\
#### Usage:\
\
    a = tf.constant([True])\
\
    c = tf.constant([True])\
\
    y = tf.constant([False, False, True, True])\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `x` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> type bool. |\
| `y` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of type bool. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of type bool with the same size as that of x or y. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-11-05 UTC.