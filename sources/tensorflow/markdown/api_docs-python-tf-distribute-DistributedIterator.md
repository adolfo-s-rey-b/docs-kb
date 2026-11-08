[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedIterator#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedIterator)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedIterator?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedIterator#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedIterator#methods)
    *   [get\_next](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedIterator#get_next)
        
    *   [get\_next\_as\_optional](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedIterator#get_next_as_optional)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedIterator#__iter__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.DistributedIterator Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedIterator#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedIterator#methods)
    *   [get\_next](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedIterator#get_next)
        
    *   [get\_next\_as\_optional](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedIterator#get_next_as_optional)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedIterator#__iter__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/types/distribute.py#L196-L304)

An iterator over [`tf.distribute.DistributedDataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset)
.

[`tf.distribute.DistributedIterator`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedIterator)
 is the primary mechanism for enumerating elements of a [`tf.distribute.DistributedDataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset)
. It supports the Python Iterator protocol, which means it can be iterated over using a for-loop or by fetching individual elements explicitly via `get_next()`.

You can create a [`tf.distribute.DistributedIterator`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedIterator)
 by calling `iter` on a [`tf.distribute.DistributedDataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset)
 or creating a python loop over a [`tf.distribute.DistributedDataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset)
.

Visit the [tutorial](https://www.tensorflow.org/tutorials/distribute/input)
 on distributed input for more examples and caveats.

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `element_spec` | The type specification of an element of [`tf.distribute.DistributedIterator`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedIterator)<br>.<br><br>    global_batch_size = 16 |

Methods
-------

### `get_next`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/types/distribute.py#L213-L240)

get_next()

Returns the next input from the iterator for all replicas.

#### Example use:

    strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])

|     |
| --- |
| Returns |     |
| A single [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> or a [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)<br> which contains the next input for all replicas. |     |

|     |
| --- |
| Raises |     |
| [`tf.errors.OutOfRangeError`](https://www.tensorflow.org/api_docs/python/tf/errors/OutOfRangeError)<br>: If the end of the iterator has been reached. |     |

### `get_next_as_optional`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/types/distribute.py#L268-L304)

get_next_as_optional()

Returns a [`tf.experimental.Optional`](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional)
 that contains the next value for all replicas.

If the [`tf.distribute.DistributedIterator`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedIterator)
 has reached the end of the sequence, the returned [`tf.experimental.Optional`](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional)
 will have no value.

#### Example usage:

    strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])

|     |
| --- |
| Returns |     |
| An [`tf.experimental.Optional`](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional)<br> object representing the next value from the [`tf.distribute.DistributedIterator`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedIterator)<br> (if it has one) or no value. |     |

### `__iter__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/types/distribute.py#L58-L59)

__iter__()

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.