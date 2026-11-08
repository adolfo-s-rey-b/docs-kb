[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/DenseHashTable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/DenseHashTable)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/DenseHashTable?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/DenseHashTable#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/DenseHashTable#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/DenseHashTable#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/DenseHashTable#methods)
    *   [erase](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/DenseHashTable#erase)
        
    *   [export](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/DenseHashTable#export)
        
    *   [insert](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/DenseHashTable#insert)
        
    *   [insert\_or\_assign](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/DenseHashTable#insert_or_assign)
        
    *   [lookup](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/DenseHashTable#lookup)
        
    *   [remove](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/DenseHashTable#remove)
        
    *   [size](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/DenseHashTable#size)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/DenseHashTable#__getitem__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.lookup.experimental.DenseHashTable Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/DenseHashTable#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/DenseHashTable#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/DenseHashTable#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/DenseHashTable#methods)
    *   [erase](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/DenseHashTable#erase)
        
    *   [export](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/DenseHashTable#export)
        
    *   [insert](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/DenseHashTable#insert)
        
    *   [insert\_or\_assign](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/DenseHashTable#insert_or_assign)
        
    *   [lookup](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/DenseHashTable#lookup)
        
    *   [remove](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/DenseHashTable#remove)
        
    *   [size](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/DenseHashTable#size)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/DenseHashTable#__getitem__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/lookup_ops.py#L2110-L2462)

A mutable hash table with faster lookups and higher memory usage.

Inherits From: [`TrackableResource`](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/TrackableResource)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.lookup.experimental.DenseHashTable`](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/DenseHashTable)

tf.lookup.experimental.DenseHashTable(
        key_dtype,
        value_dtype,
        default_value,
        empty_key,
        deleted_key,
        initial_num_buckets=None,
        name='MutableDenseHashTable',
        checkpoint=True,
        experimental_is_anonymous=False
    )

Data can be inserted by calling the `insert` method and removed by calling the `remove` method. It does not support initialization via the init method.

Compared to `MutableHashTable`, `DenseHashTable` offers generally faster `insert`, `remove` and `lookup` operations, in exchange for a higher overall memory footprint.

It uses "open addressing" with quadratic reprobing to resolve collisions. This requires specifying two keys in the key space, `empty_key` and `deleted_key`, that can never inserted into the table.

Unlike `MutableHashTable`, `DenseHashTable` does not require additional memory for temporary tensors created during checkpointing and restore operations.

#### Example usage:

    table = tf.lookup.experimental.DenseHashTable(

|     |     |
| --- | --- |
| Args<br>---- |     |
| `key_dtype` | the type of the key tensors. |
| `value_dtype` | the type of the value tensors. |
| `default_value` | The value to use if a key is missing in the table. |
| `empty_key` | the key to use to represent empty buckets internally. Must not be used in insert, remove or lookup operations. |
| `deleted_key` | the key to use to represent deleted buckets internally. Must not be used in insert, remove or lookup operations and be different from the empty\_key. |
| `initial_num_buckets` | the initial number of buckets (optional, default to 2^17=131072). Note that the default value is relatively large (~1MB), so if you are going to create many tables (likely the case when `experimental_is_anonymous` is `True`), you should set `initial_num_buckets` to a smaller value to reduce memory usage. |
| `name` | A name for the operation (optional). |
| `checkpoint` | if True, the contents of the table are saved to and restored from checkpoints. If `shared_name` is empty for a checkpointed table, it is shared using the table node name. |
| `experimental_is_anonymous` | Whether to use anonymous mode for the table (default is False). In anonymous mode, the table resource can only be accessed via a resource handle. It can't be looked up by a name. When all resource handles pointing to that resource are gone, the resource will be deleted automatically. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If checkpoint is True and no name was specified. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `key_dtype` | The table key dtype. |
| `name` | The name of the table. |
| `resource_handle` | Returns the resource handle associated with this Resource. |
| `value_dtype` | The table value dtype. |

Methods
-------

### `erase`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/lookup_ops.py#L2344-L2369)

erase(
        keys, name=None
    )

Removes `keys` and its associated values from the table.

If a key is not present in the table, it is silently ignored.

|     |     |
| --- | --- |
| Args |     |
| `keys` | Keys to remove. Can be a tensor of any shape. Must match the table's key type. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns |     |
| The created Operation. |     |

|     |     |
| --- | --- |
| Raises |     |
| `TypeError` | when `keys` do not match the table data types. |

### `export`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/lookup_ops.py#L2389-L2405)

export(
        name=None
    )

Returns tensors of all keys and values in the table.

|     |     |
| --- | --- |
| Args |     |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns |     |
| A pair of tensors with the first tensor containing all keys and the second tensors containing all values in the table. |     |

### `insert`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/lookup_ops.py#L2325-L2342)

insert(
        keys, values, name=None
    )

Associates `keys` with `values`.

|     |     |
| --- | --- |
| Args |     |
| `keys` | Keys to insert. Can be a tensor of any shape. Must match the table's key type. |
| `values` | Values to be associated with keys. Must be a tensor of the same shape as `keys` and match the table's value type. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns |     |
| The created Operation. |     |

|     |     |
| --- | --- |
| Raises |     |
| `TypeError` | when `keys` or `values` doesn't match the table data types. |

### `insert_or_assign`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/lookup_ops.py#L2298-L2323)

insert_or_assign(
        keys, values, name=None
    )

Associates `keys` with `values`.

|     |     |
| --- | --- |
| Args |     |
| `keys` | Keys to insert. Can be a tensor of any shape. Must match the table's key type. |
| `values` | Values to be associated with keys. Must be a tensor of the same shape as `keys` and match the table's value type. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns |     |
| The created Operation. |     |

|     |     |
| --- | --- |
| Raises |     |
| `TypeError` | when `keys` or `values` doesn't match the table data types. |

### `lookup`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/lookup_ops.py#L2272-L2296)

lookup(
        keys, name=None
    )

Looks up `keys` in a table, outputs the corresponding values.

The `default_value` is used for keys not present in the table.

|     |     |
| --- | --- |
| Args |     |
| `keys` | Keys to look up. Can be a tensor of any shape. Must match the table's key\_dtype. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns |     |
| A tensor containing the values in the same shape as `keys` using the table's value type. |     |

|     |     |
| --- | --- |
| Raises |     |
| `TypeError` | when `keys` do not match the table data types. |

### `remove`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/lookup_ops.py#L2371-L2387)

remove(
        keys, name=None
    )

Removes `keys` and its associated values from the table.

If a key is not present in the table, it is silently ignored.

|     |     |
| --- | --- |
| Args |     |
| `keys` | Keys to remove. Can be a tensor of any shape. Must match the table's key type. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns |     |
| The created Operation. |     |

|     |     |
| --- | --- |
| Raises |     |
| `TypeError` | when `keys` do not match the table data types. |

### `size`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/lookup_ops.py#L2259-L2270)

size(
        name=None
    )

Compute the number of elements in this table.

|     |     |
| --- | --- |
| Args |     |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns |     |
| A scalar tensor containing the number of elements in this table. |     |

### `__getitem__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/lookup_ops.py#L171-L173)

__getitem__(
        keys
    )

Looks up `keys` in a table, outputs the corresponding values.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.