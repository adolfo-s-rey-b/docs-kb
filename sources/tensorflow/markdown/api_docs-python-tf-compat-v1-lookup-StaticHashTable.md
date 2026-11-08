[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/lookup/StaticHashTable#main-content)

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
    

tf.compat.v1.lookup.StaticHashTable Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/lookup_ops.py#L416-L471)

A generic hash table that is immutable once initialized.

Inherits From: [`StaticHashTable`](https://www.tensorflow.org/api_docs/python/tf/lookup/StaticHashTable)
, [`TrackableResource`](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/TrackableResource)

tf.compat.v1.lookup.StaticHashTable(
        initializer, default_value, name=None, experimental_is_anonymous=False
    )

When running in graph mode, you must evaluate the tensor returned by `tf.tables_initializer()` before evaluating the tensor returned by this class's `lookup()` method. Example usage in graph mode:

keys_tensor = tf.constant([1, 2])
    vals_tensor = tf.constant([3, 4])
    input_tensor = tf.constant([1, 5])
    table = tf.lookup.StaticHashTable(
        tf.lookup.KeyValueTensorInitializer(keys_tensor, vals_tensor), -1)
    out = table.lookup(input_tensor)
    with tf.Session() as sess:
        sess.run(tf.tables_initializer())
        print(sess.run(out))

Note that in graph mode if you set `experimental_is_anonymous` to `True`, you should only call `Session.run` once, otherwise each `Session.run` will create (and destroy) a new table unrelated to each other, leading to errors such as "Table not initialized". You can do so like this:

keys_tensor = tf.constant([1, 2])
    vals_tensor = tf.constant([3, 4])
    input_tensor = tf.constant([1, 5])
    table = tf.lookup.StaticHashTable(
        tf.lookup.KeyValueTensorInitializer(keys_tensor, vals_tensor), -1,
        experimental_is_anonymous=True)
    with tf.control_dependencies([tf.tables_initializer()]):
      out = table.lookup(input_tensor)
    with tf.Session() as sess:
      print(sess.run(out))

In eager mode, no special code is needed to initialize the table. Example usage in eager mode:

tf.enable_eager_execution()
    keys_tensor = tf.constant([1, 2])
    vals_tensor = tf.constant([3, 4])
    input_tensor = tf.constant([1, 5])
    table = tf.lookup.StaticHashTable(
        tf.lookup.KeyValueTensorInitializer(keys_tensor, vals_tensor), -1)
    print(table.lookup(input_tensor))

|     |     |
| --- | --- |
| Args<br>---- |     |
| `initializer` | The table initializer to use. See `HashTable` kernel for supported key and value types. |
| `default_value` | The value to use if a key is missing in the table. |
| `name` | A name for the operation (optional). |
| `experimental_is_anonymous` | Whether to use anonymous mode for the table (default is False). In anonymous mode, the table resource can only be accessed via a resource handle. It can't be looked up by a name. When all resource handles pointing to that resource are gone, the resource will be deleted automatically. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `default_value` | The default value of the table. |
| `initializer` |     |
| `key_dtype` | The table key dtype. |
| `name` | The name of the table. |
| `resource_handle` | Returns the resource handle associated with this Resource. |
| `value_dtype` | The table value dtype. |

Methods
-------

### `export`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/lookup_ops.py#L378-L394)

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

### `lookup`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/lookup_ops.py#L229-L271)

lookup(
        keys, name=None
    )

Looks up `keys` in a table, outputs the corresponding values.

The `default_value` is used for keys not present in the table.

|     |     |
| --- | --- |
| Args |     |
| `keys` | Keys to look up. May be either a `SparseTensor` or dense `Tensor`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns |     |
| A `SparseTensor` if keys are sparse, a `RaggedTensor` if keys are ragged, otherwise a dense `Tensor`. |     |

|     |     |
| --- | --- |
| Raises |     |
| `TypeError` | when `keys` or `default_value` doesn't match the table data types. |

### `size`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/lookup_ops.py#L217-L227)

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