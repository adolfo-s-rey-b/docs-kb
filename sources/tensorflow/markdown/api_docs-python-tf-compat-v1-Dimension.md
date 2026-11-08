[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2FDimension&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#description)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#methods)
    *   [assert\_is\_compatible\_with](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#assert_is_compatible_with)
        
    *   [is\_compatible\_with](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#is_compatible_with)
        
    *   [merge\_with](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#merge_with)
        
    *   [\_\_add\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__add__)
        
    *   [\_\_bool\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__bool__)
        
    *   [\_\_div\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__div__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__eq__)
        
    *   [\_\_floordiv\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__floordiv__)
        
    *   [\_\_ge\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__ge__)
        
    *   [\_\_gt\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__gt__)
        
    *   [\_\_le\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__le__)
        
    *   [\_\_lt\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__lt__)
        
    *   [\_\_mod\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__mod__)
        
    *   [\_\_mul\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__mul__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__ne__)
        
    *   [\_\_radd\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__radd__)
        
    *   [\_\_rdiv\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__rdiv__)
        
    *   [\_\_rfloordiv\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__rfloordiv__)
        
    *   [\_\_rmod\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__rmod__)
        
    *   [\_\_rmul\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__rmul__)
        
    *   [\_\_rsub\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__rsub__)
        
    *   [\_\_rtruediv\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__rtruediv__)
        
    *   [\_\_sub\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__sub__)
        
    *   [\_\_truediv\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__truediv__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.Dimension Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#description)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#methods)
    *   [assert\_is\_compatible\_with](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#assert_is_compatible_with)
        
    *   [is\_compatible\_with](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#is_compatible_with)
        
    *   [merge\_with](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#merge_with)
        
    *   [\_\_add\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__add__)
        
    *   [\_\_bool\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__bool__)
        
    *   [\_\_div\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__div__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__eq__)
        
    *   [\_\_floordiv\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__floordiv__)
        
    *   [\_\_ge\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__ge__)
        
    *   [\_\_gt\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__gt__)
        
    *   [\_\_le\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__le__)
        
    *   [\_\_lt\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__lt__)
        
    *   [\_\_mod\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__mod__)
        
    *   [\_\_mul\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__mul__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__ne__)
        
    *   [\_\_radd\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__radd__)
        
    *   [\_\_rdiv\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__rdiv__)
        
    *   [\_\_rfloordiv\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__rfloordiv__)
        
    *   [\_\_rmod\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__rmod__)
        
    *   [\_\_rmul\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__rmul__)
        
    *   [\_\_rsub\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__rsub__)
        
    *   [\_\_rtruediv\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__rtruediv__)
        
    *   [\_\_sub\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__sub__)
        
    *   [\_\_truediv\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Dimension#__truediv__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L188-L725)

Represents the value of one dimension in a TensorShape.

tf.compat.v1.Dimension(
        value
    )

Migrate to TF2
--------------

In TF2, members of a `TensorShape` object are integers. The `Dimension` class is not part of TF2's data model.

Please refer to the [TensorShape section of the migration guide](https://www.tensorflow.org/guide/migrate/index#tensorshape)
 on common code patterns adapting Dimension objects to a TF2 syntax.

Description
-----------

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `value` | The value of this dimension, or None if it is unknown. |

Methods
-------

### `assert_is_compatible_with`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L292-L304)

assert_is_compatible_with(
        other
    )

Raises an exception if `other` is not compatible with this Dimension.

|     |     |
| --- | --- |
| Args |     |
| `other` | Another Dimension. |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If `self` and `other` are not compatible (see is\_compatible\_with). |

### `is_compatible_with`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L276-L290)

is_compatible_with(
        other
    )

Returns true if `other` is compatible with this Dimension.

Two known Dimensions are compatible if they have the same value. An unknown Dimension is compatible with all other Dimensions.

|     |     |
| --- | --- |
| Args |     |
| `other` | Another Dimension. |

|     |
| --- |
| Returns |     |
| True if this Dimension and `other` are compatible. |     |

### `merge_with`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L306-L341)

merge_with(
        other
    )

Returns a Dimension that combines the information in `self` and `other`.

Dimensions are combined as follows:

tf.compat.v1.Dimension(n)   .merge_with(tf.compat.v1.Dimension(n))     ==
    tf.compat.v1.Dimension(n)
    tf.compat.v1.Dimension(n)   .merge_with(tf.compat.v1.Dimension(None))  ==
    tf.compat.v1.Dimension(n)
    tf.compat.v1.Dimension(None).merge_with(tf.compat.v1.Dimension(n))     ==
    tf.compat.v1.Dimension(n)
    # equivalent to tf.compat.v1.Dimension(None)
    tf.compat.v1.Dimension(None).merge_with(tf.compat.v1.Dimension(None))
    
    # raises ValueError for n != m
    tf.compat.v1.Dimension(n)   .merge_with(tf.compat.v1.Dimension(m))

|     |     |
| --- | --- |
| Args |     |
| `other` | Another Dimension. |

|     |
| --- |
| Returns |     |
| A Dimension containing the combined information of `self` and `other`. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If `self` and `other` are not compatible (see is\_compatible\_with). |

### `__add__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L343-L372)

__add__(
        other
    )

Returns the sum of `self` and `other`.

Dimensions are summed as follows:

tf.compat.v1.Dimension(m)    + tf.compat.v1.Dimension(n)     ==
    tf.compat.v1.Dimension(m + n)
    tf.compat.v1.Dimension(m)    + tf.compat.v1.Dimension(None)  # equiv. to
    tf.compat.v1.Dimension(None)
    tf.compat.v1.Dimension(None) + tf.compat.v1.Dimension(n)     # equiv. to
    tf.compat.v1.Dimension(None)
    tf.compat.v1.Dimension(None) + tf.compat.v1.Dimension(None)  # equiv. to
    tf.compat.v1.Dimension(None)

|     |     |
| --- | --- |
| Args |     |
| `other` | Another Dimension, or a value accepted by `as_dimension`. |

|     |
| --- |
| Returns |     |
| A Dimension whose value is the sum of `self` and `other`. |     |

### `__bool__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L254-L256)

__bool__()

Equivalent to `bool(self.value)`.

### `__div__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L520-L534)

__div__(
        other
    )

This function exists only for backwards compatibility purposes; new code should use `__floordiv__` via the syntax `x // y`. Using `x // y` communicates clearly that the result rounds down, and is forward compatible to Python 3.

|     |     |
| --- | --- |
| Args |     |
| `other` | Another `Dimension`. |

|     |
| --- |
| Returns |     |
| A `Dimension` whose value is the integer quotient of `self` and `other`. |     |

### `__eq__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L234-L242)

__eq__(
        other
    )

Returns true if `other` has the same known value as this Dimension.

### `__floordiv__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L474-L503)

__floordiv__(
        other
    )

Returns the quotient of `self` and `other` rounded down.

Dimensions are divided as follows:

tf.compat.v1.Dimension(m)    // tf.compat.v1.Dimension(n)     ==
    tf.compat.v1.Dimension(m // n)
    tf.compat.v1.Dimension(m)    // tf.compat.v1.Dimension(None)  # equiv. to
    tf.compat.v1.Dimension(None)
    tf.compat.v1.Dimension(None) // tf.compat.v1.Dimension(n)     # equiv. to
    tf.compat.v1.Dimension(None)
    tf.compat.v1.Dimension(None) // tf.compat.v1.Dimension(None)  # equiv. to
    tf.compat.v1.Dimension(None)

|     |     |
| --- | --- |
| Args |     |
| `other` | Another Dimension, or a value accepted by `as_dimension`. |

|     |
| --- |
| Returns |     |
| A `Dimension` whose value is the integer quotient of `self` and `other`. |     |

### `__ge__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L699-L722)

__ge__(
        other
    )

Returns True if `self` is known to be greater than or equal to `other`.

Dimensions are compared as follows:

(tf.compat.v1.Dimension(m)    >= tf.compat.v1.Dimension(n))    == (m >= n)
    (tf.compat.v1.Dimension(m)    >= tf.compat.v1.Dimension(None)) == None
    (tf.compat.v1.Dimension(None) >= tf.compat.v1.Dimension(n))    == None
    (tf.compat.v1.Dimension(None) >= tf.compat.v1.Dimension(None)) == None

|     |     |
| --- | --- |
| Args |     |
| `other` | Another Dimension. |

|     |
| --- |
| Returns |     |
| The value of `self.value >= other.value` if both are known, otherwise None. |     |

### `__gt__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L674-L697)

__gt__(
        other
    )

Returns True if `self` is known to be greater than `other`.

Dimensions are compared as follows:

(tf.compat.v1.Dimension(m)    > tf.compat.v1.Dimension(n))    == (m > n)
    (tf.compat.v1.Dimension(m)    > tf.compat.v1.Dimension(None)) == None
    (tf.compat.v1.Dimension(None) > tf.compat.v1.Dimension(n))    == None
    (tf.compat.v1.Dimension(None) > tf.compat.v1.Dimension(None)) == None

|     |     |
| --- | --- |
| Args |     |
| `other` | Another Dimension. |

|     |
| --- |
| Returns |     |
| The value of `self.value > other.value` if both are known, otherwise None. |     |

### `__le__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L649-L672)

__le__(
        other
    )

Returns True if `self` is known to be less than or equal to `other`.

Dimensions are compared as follows:

(tf.compat.v1.Dimension(m)    <= tf.compat.v1.Dimension(n))    == (m <= n)
    (tf.compat.v1.Dimension(m)    <= tf.compat.v1.Dimension(None)) == None
    (tf.compat.v1.Dimension(None) <= tf.compat.v1.Dimension(n))    == None
    (tf.compat.v1.Dimension(None) <= tf.compat.v1.Dimension(None)) == None

|     |     |
| --- | --- |
| Args |     |
| `other` | Another Dimension. |

|     |
| --- |
| Returns |     |
| The value of `self.value <= other.value` if both are known, otherwise None. |     |

### `__lt__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L624-L647)

__lt__(
        other
    )

Returns True if `self` is known to be less than `other`.

Dimensions are compared as follows:

(tf.compat.v1.Dimension(m)    < tf.compat.v1.Dimension(n))    == (m < n)
    (tf.compat.v1.Dimension(m)    < tf.compat.v1.Dimension(None)) == None
    (tf.compat.v1.Dimension(None) < tf.compat.v1.Dimension(n))    == None
    (tf.compat.v1.Dimension(None) < tf.compat.v1.Dimension(None)) == None

|     |     |
| --- | --- |
| Args |     |
| `other` | Another Dimension. |

|     |
| --- |
| Returns |     |
| The value of `self.value < other.value` if both are known, otherwise None. |     |

### `__mod__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L584-L610)

__mod__(
        other
    )

Returns `self` modulo `other`.

Dimension modulo are computed as follows:

tf.compat.v1.Dimension(m)    % tf.compat.v1.Dimension(n)     ==
    tf.compat.v1.Dimension(m % n)
    tf.compat.v1.Dimension(m)    % tf.compat.v1.Dimension(None)  # equiv. to
    tf.compat.v1.Dimension(None)
    tf.compat.v1.Dimension(None) % tf.compat.v1.Dimension(n)     # equiv. to
    tf.compat.v1.Dimension(None)
    tf.compat.v1.Dimension(None) % tf.compat.v1.Dimension(None)  # equiv. to
    tf.compat.v1.Dimension(None)

|     |     |
| --- | --- |
| Args |     |
| `other` | Another Dimension, or a value accepted by `as_dimension`. |

|     |
| --- |
| Returns |     |
| A Dimension whose value is `self` modulo `other`. |     |

### `__mul__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L431-L461)

__mul__(
        other
    )

Returns the product of `self` and `other`.

Dimensions are summed as follows:

tf.compat.v1.Dimension(m)    * tf.compat.v1.Dimension(n)     ==
    tf.compat.v1.Dimension(m * n)
    tf.compat.v1.Dimension(m)    * tf.compat.v1.Dimension(None)  # equiv. to
    tf.compat.v1.Dimension(None)
    tf.compat.v1.Dimension(None) * tf.compat.v1.Dimension(n)     # equiv. to
    tf.compat.v1.Dimension(None)
    tf.compat.v1.Dimension(None) * tf.compat.v1.Dimension(None)  # equiv. to
    tf.compat.v1.Dimension(None)

|     |     |
| --- | --- |
| Args |     |
| `other` | Another Dimension, or a value accepted by `as_dimension`. |

|     |
| --- |
| Returns |     |
| A Dimension whose value is the product of `self` and `other`. |     |

### `__ne__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L244-L252)

__ne__(
        other
    )

Returns true if `other` has a different known value from `self`.

### `__radd__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L374-L383)

__radd__(
        other
    )

Returns the sum of `other` and `self`.

|     |     |
| --- | --- |
| Args |     |
| `other` | Another Dimension, or a value accepted by `as_dimension`. |

|     |
| --- |
| Returns |     |
| A Dimension whose value is the sum of `self` and `other`. |     |

### `__rdiv__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L536-L550)

__rdiv__(
        other
    )

Use `__floordiv__` via `x // y` instead.

This function exists only to have a better error message. Instead of: `TypeError: unsupported operand type(s) for /: 'int' and 'Dimension'`, this function will explicitly call for usage of `//` instead.

|     |     |
| --- | --- |
| Args |     |
| `other` | Another `Dimension`. |

|     |
| --- |
| Raises |     |
| TypeError. |     |

### `__rfloordiv__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L505-L518)

__rfloordiv__(
        other
    )

Returns the quotient of `other` and `self` rounded down.

|     |     |
| --- | --- |
| Args |     |
| `other` | Another Dimension, or a value accepted by `as_dimension`. |

|     |
| --- |
| Returns |     |
| A `Dimension` whose value is the integer quotient of `self` and `other`. |     |

### `__rmod__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L612-L622)

__rmod__(
        other
    )

Returns `other` modulo `self`.

|     |     |
| --- | --- |
| Args |     |
| `other` | Another Dimension, or a value accepted by `as_dimension`. |

|     |
| --- |
| Returns |     |
| A Dimension whose value is `other` modulo `self`. |     |

### `__rmul__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L463-L472)

__rmul__(
        other
    )

Returns the product of `self` and `other`.

|     |     |
| --- | --- |
| Args |     |
| `other` | Another Dimension, or a value accepted by `as_dimension`. |

|     |
| --- |
| Returns |     |
| A Dimension whose value is the product of `self` and `other`. |     |

### `__rsub__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L416-L429)

__rsub__(
        other
    )

Returns the subtraction of `self` from `other`.

|     |     |
| --- | --- |
| Args |     |
| `other` | Another Dimension, or a value accepted by `as_dimension`. |

|     |
| --- |
| Returns |     |
| A Dimension whose value is the subtraction of `self` from `other`. |     |

### `__rtruediv__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L568-L582)

__rtruediv__(
        other
    )

Use `__floordiv__` via `x // y` instead.

This function exists only to have a better error message. Instead of: `TypeError: unsupported operand type(s) for /: 'int' and 'Dimension'`, this function will explicitly call for usage of `//` instead.

|     |     |
| --- | --- |
| Args |     |
| `other` | Another `Dimension`. |

|     |
| --- |
| Raises |     |
| TypeError. |     |

### `__sub__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L385-L414)

__sub__(
        other
    )

Returns the subtraction of `other` from `self`.

Dimensions are subtracted as follows:

tf.compat.v1.Dimension(m)    - tf.compat.v1.Dimension(n)     ==
    tf.compat.v1.Dimension(m - n)
    tf.compat.v1.Dimension(m)    - tf.compat.v1.Dimension(None)  # equiv. to
    tf.compat.v1.Dimension(None)
    tf.compat.v1.Dimension(None) - tf.compat.v1.Dimension(n)     # equiv. to
    tf.compat.v1.Dimension(None)
    tf.compat.v1.Dimension(None) - tf.compat.v1.Dimension(None)  # equiv. to
    tf.compat.v1.Dimension(None)

|     |     |
| --- | --- |
| Args |     |
| `other` | Another Dimension, or a value accepted by `as_dimension`. |

|     |
| --- |
| Returns |     |
| A Dimension whose value is the subtraction of `other` from `self`. |     |

### `__truediv__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L552-L566)

__truediv__(
        other
    )

Use `__floordiv__` via `x // y` instead.

This function exists only to have a better error message. Instead of: `TypeError: unsupported operand type(s) for /: 'Dimension' and 'int'`, this function will explicitly call for usage of `//` instead.

|     |     |
| --- | --- |
| Args |     |
| `other` | Another `Dimension`. |

|     |
| --- |
| Raises |     |
| TypeError. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.