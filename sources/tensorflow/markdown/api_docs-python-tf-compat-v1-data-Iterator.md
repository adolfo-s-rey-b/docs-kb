[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/Iterator#main-content)

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
    

tf.compat.v1.data.Iterator Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/iterator_ops.py#L94-L545)

Represents the state of iterating through a `Dataset`.

tf.compat.v1.data.Iterator(
        iterator_resource, initializer, output_types, output_shapes, output_classes
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `iterator_resource` | A [`tf.resource`](https://www.tensorflow.org/api_docs/python/tf#resource)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> representing the iterator. |
| `initializer` | A [`tf.Operation`](https://www.tensorflow.org/api_docs/python/tf/Operation)<br> that should be run to initialize this iterator. |
| `output_types` | A (nested) structure of [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br> objects corresponding to each component of an element of this iterator. |
| `output_shapes` | A (nested) structure of [`tf.TensorShape`](https://www.tensorflow.org/api_docs/python/tf/TensorShape)<br> objects corresponding to each component of an element of this iterator. |
| `output_classes` | A (nested) structure of Python `type` objects corresponding to each component of an element of this iterator. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If `output_types`, `output_shapes`, or `output_classes` is not specified. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `element_spec` | The type specification of an element of this iterator.<br><br>For more information, read [this guide](https://www.tensorflow.org/guide/data#dataset_structure)<br>. |
| `initializer` | A [`tf.Operation`](https://www.tensorflow.org/api_docs/python/tf/Operation)<br> that should be run to initialize this iterator. |
| `output_classes` | Returns the class of each component of an element of this iterator. (deprecated)<br><br>The expected values are [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> and [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)<br>. |
| `output_shapes` | Returns the shape of each component of an element of this iterator. (deprecated) |
| `output_types` | Returns the type of each component of an element of this iterator. (deprecated) |

Methods
-------

### `from_string_handle`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/iterator_ops.py#L240-L309)

@staticmethod

Creates a new, uninitialized `Iterator` based on the given handle.

This method allows you to define a "feedable" iterator where you can choose between concrete iterators by feeding a value in a `tf.Session.run` call. In that case, `string_handle` would be a [`tf.compat.v1.placeholder`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/placeholder)
, and you would feed it with the value of `tf.data.Iterator.string_handle` in each step.

For example, if you had two iterators that marked the current position in a training dataset and a test dataset, you could choose which to use in each step as follows:

train_iterator = tf.data.Dataset(...).make_one_shot_iterator()
    train_iterator_handle = sess.run(train_iterator.string_handle())
    
    test_iterator = tf.data.Dataset(...).make_one_shot_iterator()
    test_iterator_handle = sess.run(test_iterator.string_handle())
    
    handle = tf.compat.v1.placeholder(tf.string, shape=[])
    iterator = tf.data.Iterator.from_string_handle(
        handle, train_iterator.output_types)
    
    next_element = iterator.get_next()
    loss = f(next_element)
    
    train_loss = sess.run(loss, feed_dict={handle: train_iterator_handle})
    test_loss = sess.run(loss, feed_dict={handle: test_iterator_handle})

|     |     |
| --- | --- |
| Args |     |
| `string_handle` | A scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of type [`tf.string`](https://www.tensorflow.org/api_docs/python/tf#string)<br> that evaluates to a handle produced by the `Iterator.string_handle()` method. |
| `output_types` | A (nested) structure of [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br> objects corresponding to each component of an element of this dataset. |
| `output_shapes` | (Optional.) A (nested) structure of [`tf.TensorShape`](https://www.tensorflow.org/api_docs/python/tf/TensorShape)<br> objects corresponding to each component of an element of this dataset. If omitted, each component will have an unconstrainted shape. |
| `output_classes` | (Optional.) A (nested) structure of Python `type` objects corresponding to each component of an element of this iterator. If omitted, each component is assumed to be of type [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>. |

|     |
| --- |
| Returns |     |
| An `Iterator`. |     |

### `from_structure`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/iterator_ops.py#L146-L238)

@staticmethod

Creates a new, uninitialized `Iterator` with the given structure.

This iterator-constructing method can be used to create an iterator that is reusable with many different datasets.

The returned iterator is not bound to a particular dataset, and it has no `initializer`. To initialize the iterator, run the operation returned by `Iterator.make_initializer(dataset)`.

The following is an example

iterator = Iterator.from_structure(tf.int64, tf.TensorShape([]))
    
    dataset_range = Dataset.range(10)
    range_initializer = iterator.make_initializer(dataset_range)
    
    dataset_evens = dataset_range.filter(lambda x: x % 2 == 0)
    evens_initializer = iterator.make_initializer(dataset_evens)
    
    # Define a model based on the iterator; in this example, the model_fn
    # is expected to take scalar tf.int64 Tensors as input (see
    # the definition of 'iterator' above).
    prediction, loss = model_fn(iterator.get_next())
    
    # Train for `num_epochs`, where for each epoch, we first iterate over
    # dataset_range, and then iterate over dataset_evens.
    for _ in range(num_epochs):
      # Initialize the iterator to `dataset_range`
      sess.run(range_initializer)
      while True:
        try:
          pred, loss_val = sess.run([prediction, loss])
        except tf.errors.OutOfRangeError:
          break
    
      # Initialize the iterator to `dataset_evens`
      sess.run(evens_initializer)
      while True:
        try:
          pred, loss_val = sess.run([prediction, loss])
        except tf.errors.OutOfRangeError:
          break

|     |     |
| --- | --- |
| Args |     |
| `output_types` | A (nested) structure of [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br> objects corresponding to each component of an element of this dataset. |
| `output_shapes` | (Optional.) A (nested) structure of [`tf.TensorShape`](https://www.tensorflow.org/api_docs/python/tf/TensorShape)<br> objects corresponding to each component of an element of this dataset. If omitted, each component will have an unconstrainted shape. |
| `shared_name` | (Optional.) If non-empty, this iterator will be shared under the given name across multiple sessions that share the same devices (e.g. when using a remote server). |
| `output_classes` | (Optional.) A (nested) structure of Python `type` objects corresponding to each component of an element of this iterator. If omitted, each component is assumed to be of type [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>. |

|     |
| --- |
| Returns |     |
| An `Iterator`. |     |

|     |     |
| --- | --- |
| Raises |     |
| `TypeError` | If the structures of `output_shapes` and `output_types` are not the same. |

### `get_next`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/iterator_ops.py#L392-L448)

get_next(
        name=None
    )

Returns the next element.

In graph mode, you should typically call this method _once_ and use its result as the input to another computation. A typical loop will then call `tf.Session.run` on the result of that computation. The loop will terminate when the [`Iterator.get_next()`](https://www.tensorflow.org/api_docs/python/tf/data/Iterator#get_next)
 operation raises [`tf.errors.OutOfRangeError`](https://www.tensorflow.org/api_docs/python/tf/errors/OutOfRangeError)
. The following skeleton shows how to use this method when building a training loop:

dataset = ...  # A `tf.data.Dataset` object.
    iterator = dataset.make_initializable_iterator()
    next_element = iterator.get_next()
    
    # Build a TensorFlow graph that does something with each element.
    loss = model_function(next_element)
    optimizer = ...  # A `tf.compat.v1.train.Optimizer` object.
    train_op = optimizer.minimize(loss)
    
    with tf.compat.v1.Session() as sess:
      try:
        while True:
          sess.run(train_op)
      except tf.errors.OutOfRangeError:
        pass

|     |     |
| --- | --- |
| Args |     |
| `name` | (Optional.) A name for the created operation. |

|     |
| --- |
| Returns |     |
| A (nested) structure of values matching [`tf.data.Iterator.element_spec`](https://www.tensorflow.org/api_docs/python/tf/data/Iterator#element_spec)<br>. |     |

### `get_next_as_optional`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/iterator_ops.py#L450-L459)

get_next_as_optional()

### `make_initializer`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/iterator_ops.py#L332-L390)

make_initializer(
        dataset, name=None
    )

Returns a [`tf.Operation`](https://www.tensorflow.org/api_docs/python/tf/Operation)
 that initializes this iterator on `dataset`.

|     |     |
| --- | --- |
| Args |     |
| `dataset` | A `Dataset` whose `element_spec` if compatible with this iterator. |
| `name` | (Optional.) A name for the created operation. |

|     |
| --- |
| Returns |     |
| A [`tf.Operation`](https://www.tensorflow.org/api_docs/python/tf/Operation)<br> that can be run to initialize this iterator on the given `dataset`. |     |

|     |     |
| --- | --- |
| Raises |     |
| `TypeError` | If `dataset` and this iterator do not have a compatible `element_spec`. |

### `string_handle`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/iterator_ops.py#L461-L474)

string_handle(
        name=None
    )

Returns a string-valued [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 that represents this iterator.

|     |     |
| --- | --- |
| Args |     |
| `name` | (Optional.) A name for the created operation. |

|     |
| --- |
| Returns |     |
| A scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of type [`tf.string`](https://www.tensorflow.org/api_docs/python/tf#string)<br>. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.