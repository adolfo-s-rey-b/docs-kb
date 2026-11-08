[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/MutableHashTable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/MutableHashTable)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/MutableHashTable?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/MutableHashTable#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/MutableHashTable#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/MutableHashTable#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/MutableHashTable#methods)
    *   [export](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/MutableHashTable#export)
        
    *   [insert](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/MutableHashTable#insert)
        
    *   [lookup](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/MutableHashTable#lookup)
        
    *   [remove](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/MutableHashTable#remove)
        
    *   [size](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/MutableHashTable#size)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/MutableHashTable#__getitem__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.lookup.experimental.MutableHashTable Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/MutableHashTable#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/MutableHashTable#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/MutableHashTable#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/MutableHashTable#methods)
    *   [export](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/MutableHashTable#export)
        
    *   [insert](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/MutableHashTable#insert)
        
    *   [lookup](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/MutableHashTable#lookup)
        
    *   [remove](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/MutableHashTable#remove)
        
    *   [size](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/MutableHashTable#size)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/MutableHashTable#__getitem__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/lookup_ops.py#L1798-L2107)

A generic mutable hash table implementation.

Inherits From: [`TrackableResource`](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/TrackableResource)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.lookup.experimental.MutableHashTable`](https://www.tensorflow.org/api_docs/python/tf/lookup/experimental/MutableHashTable)

tf.lookup.experimental.MutableHashTable(
        key_dtype,
        value_dtype,
        default_value,
        name='MutableHashTable',
        checkpoint=True,
        experimental_is_anonymous=False
    )

Data can be inserted by calling the `insert` method and removed by calling the `remove` method. It does not support initialization via the init method.

`MutableHashTable` requires additional memory during checkpointing and restore operations to create temporary key and value tensors.

#### Example usage:

    table = tf.lookup.experimental.MutableHashTable(key_dtype=tf.string,

|     |     |
| --- | --- |
| Args<br>---- |     |
| `key_dtype` | the type of the key tensors. |
| `value_dtype` | the type of the value tensors. |
| `default_value` | The value to use if a key is missing in the table. |
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

### `export`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/lookup_ops.py#L2038-L2053)

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/lookup_ops.py#L2011-L2036)

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

### `lookup`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/lookup_ops.py#L1968-L2009)

lookup(
        keys, dynamic_default_values=None, name=None
    )

Looks up `keys` in a table, outputs the corresponding values.

The `default_value` is used for keys not present in the table.

|     |     |
| --- | --- |
| Args |     |
| `keys` | Keys to look up. Can be a tensor of any shape. Must match the table's key\_dtype. |
| `dynamic_default_values` | The values to use if a key is missing in the table. If None (by default), the `table.default_value` will be used. Shape of `dynamic_default_values` must be same with `table.default_value` or the lookup result tensor. In the latter case, each key will have a different default value.<br><br>For example:<br><br>  keys = [0, 1, 3]<br>      dynamic_default_values = [[1, 3, 4], [2, 3, 9], [8, 3, 0]]<br>    <br>      # The key '0' will use [1, 3, 4] as default value.<br>      # The key '1' will use [2, 3, 9] as default value.<br>      # The key '3' will use [8, 3, 0] as default value. |
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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/lookup_ops.py#L1942-L1966)

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/lookup_ops.py#L1929-L1940)

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