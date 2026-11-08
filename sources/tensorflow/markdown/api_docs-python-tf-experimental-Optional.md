[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fexperimental%2FOptional&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional#methods)
    *   [empty](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional#empty)
        
    *   [from\_value](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional#from_value)
        
    *   [get\_value](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional#get_value)
        
    *   [has\_value](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional#has_value)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.Optional Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional#methods)
    *   [empty](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional#empty)
        
    *   [from\_value](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional#from_value)
        
    *   [get\_value](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional#get_value)
        
    *   [has\_value](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional#has_value)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/optional_ops.py#L31-L159)

Represents a value that may or may not be present.

#### View aliases

**Main aliases**

[`tf.data.experimental.Optional`](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.Optional`](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional)
, [`tf.compat.v1.experimental.Optional`](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional)

A [`tf.experimental.Optional`](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional)
 can represent the result of an operation that may fail as a value, rather than raising an exception and halting execution. For example, [`tf.data.Iterator.get_next_as_optional()`](https://www.tensorflow.org/api_docs/python/tf/data/Iterator#get_next_as_optional)
 returns a [`tf.experimental.Optional`](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional)
 that either contains the next element of an iterator if one exists, or an "empty" value that indicates the end of the sequence has been reached.

[`tf.experimental.Optional`](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional)
 can only be used with values that are convertible to [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 or `tf.CompositeTensor`.

One can create a [`tf.experimental.Optional`](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional)
 from a value using the `from_value()` method:

    optional = tf.experimental.Optional.from_value(42)

or without a value using the `empty()` method:

    optional = tf.experimental.Optional.empty(

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `element_spec` | The type specification of an element of this optional.<br><br>    optional = tf.experimental.Optional.from_value(42) |

Methods
-------

### `empty`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/optional_ops.py#L113-L132)

@staticmethod

Returns an `Optional` that has no value.

    optional = tf.experimental.Optional.empty(

|     |     |
| --- | --- |
| Args |     |
| `element_spec` | A (nested) structure of [`tf.TypeSpec`](https://www.tensorflow.org/api_docs/python/tf/TypeSpec)<br> objects matching the structure of an element of this optional. |

|     |
| --- |
| Returns |     |
| A [`tf.experimental.Optional`](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional)<br> with no value. |     |

### `from_value`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/optional_ops.py#L134-L159)

@staticmethod

Returns a [`tf.experimental.Optional`](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional)
 that wraps the given value.

    optional = tf.experimental.Optional.from_value(42)

|     |     |
| --- | --- |
| Args |     |
| `value` | A value to wrap. The value must be convertible to [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> or `tf.CompositeTensor`. |

|     |
| --- |
| Returns |     |
| A [`tf.experimental.Optional`](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional)<br> that wraps `value`. |     |

### `get_value`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/optional_ops.py#L79-L97)

@abc.abstractmethod

Returns the value wrapped by this optional.

If this optional does not have a value (i.e. `self.has_value()` evaluates to `False`), this operation will raise [`tf.errors.InvalidArgumentError`](https://www.tensorflow.org/api_docs/python/tf/errors/InvalidArgumentError)
 at runtime.

    optional = tf.experimental.Optional.from_value(42)

|     |     |
| --- | --- |
| Args |     |
| `name` | (Optional.) A name for the created operation. |

|     |
| --- |
| Returns |     |
| The wrapped value. |     |

### `has_value`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/optional_ops.py#L63-L77)

@abc.abstractmethod

Returns a tensor that evaluates to `True` if this optional has a value.

    optional = tf.experimental.Optional.from_value(42)

|     |     |
| --- | --- |
| Args |     |
| `name` | (Optional.) A name for the created operation. |

|     |
| --- |
| Returns |     |
| A scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of type [`tf.bool`](https://www.tensorflow.org/api_docs/python/tf#bool)<br>. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.