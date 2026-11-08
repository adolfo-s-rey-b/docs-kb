[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/Iterator#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/Iterator)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/Iterator?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/data/Iterator#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/data/Iterator#methods)
    *   [get\_next](https://www.tensorflow.org/api_docs/python/tf/data/Iterator#get_next)
        
    *   [get\_next\_as\_optional](https://www.tensorflow.org/api_docs/python/tf/data/Iterator#get_next_as_optional)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/data/Iterator#__iter__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.Iterator Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/data/Iterator#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/data/Iterator#methods)
    *   [get\_next](https://www.tensorflow.org/api_docs/python/tf/data/Iterator#get_next)
        
    *   [get\_next\_as\_optional](https://www.tensorflow.org/api_docs/python/tf/data/Iterator#get_next_as_optional)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/data/Iterator#__iter__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/iterator_ops.py#L560-L657)

Represents an iterator of a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
.

[`tf.data.Iterator`](https://www.tensorflow.org/api_docs/python/tf/data/Iterator)
 is the primary mechanism for enumerating elements of a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
. It supports the Python Iterator protocol, which means it can be iterated over using a for-loop:

    dataset = tf.data.Dataset.range(2)

or by fetching individual elements explicitly via `get_next()`:

    dataset = tf.data.Dataset.range(2)

In addition, non-raising iteration is supported via `get_next_as_optional()`, which returns the next element (if available) wrapped in a [`tf.experimental.Optional`](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional)
.

    dataset = tf.data.Dataset.from_tensors(42)

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `element_spec` | The type specification of an element of this iterator.<br><br>    dataset = tf.data.Dataset.from_tensors(42)<br><br>For more information, read [this guide](https://www.tensorflow.org/guide/data#dataset_structure)<br>. |

Methods
-------

### `get_next`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/iterator_ops.py#L619-L634)

@abc.abstractmethod

Returns the next element.

    dataset = tf.data.Dataset.from_tensors(42)

|     |
| --- |
| Returns |     |
| A (nested) structure of values matching [`tf.data.Iterator.element_spec`](https://www.tensorflow.org/api_docs/python/tf/data/Iterator#element_spec)<br>. |     |

|     |
| --- |
| Raises |     |
| [`tf.errors.OutOfRangeError`](https://www.tensorflow.org/api_docs/python/tf/errors/OutOfRangeError)<br>: If the end of the iterator has been reached. |     |

### `get_next_as_optional`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/iterator_ops.py#L636-L657)

@abc.abstractmethod

Returns the next element wrapped in [`tf.experimental.Optional`](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional)
.

If the iterator has reached the end of the sequence, the returned [`tf.experimental.Optional`](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional)
 will have no value.

    dataset = tf.data.Dataset.from_tensors(42)

|     |
| --- |
| Returns |     |
| A [`tf.experimental.Optional`](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional)<br> object representing the next element. |     |

### `__iter__`

__iter__()

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.