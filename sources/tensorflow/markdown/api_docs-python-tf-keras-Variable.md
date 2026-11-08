[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/Variable#main-content)

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
    

tf.keras.Variable Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/__init__.py#L62-L64)

Represents a backend-agnostic variable in Keras.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.keras.Variable`](https://www.tensorflow.org/api_docs/python/tf/keras/Variable)

tf.keras.Variable(
        initializer,
        shape=None,
        dtype=None,
        trainable=True,
        autocast=True,
        aggregation='none',
        synchronization='auto',
        name=None,
        layout=None,
        **kwargs
    )

A `Variable` acts as a container for state. It holds a tensor value and can be updated. With the JAX backend, variables are used to implement "functionalization", the pattern of lifting stateful operations out of a piece of computation to turn it into a stateless function.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `initializer` | Initial value or callable for initialization. If a callable is used, it should take the arguments `shape` and `dtype`. |
| `shape` | Optional. Tuple for the variable's shape. Required if `initializer` is a callable. |
| `dtype` | Optional. Data type of the variable. Defaults to the global float dtype type (`"float32"` if never configured). |
| `trainable` | Optional. Boolean indicating if variable is trainable. Defaults to `True`. |
| `autocast` | Optional. Boolean indicating whether the variable supports autocasting. If `True`, the layer may first convert the variable to the compute data type when accessed. Defaults to `True`. |
| `aggregation` | Optional string, one of `None`, `"none"`, `"mean"`, `"sum"` or `"only_first_replica"` specifying how a distributed variable will be aggregated. This serves as a semantic annotation, to be taken into account by downstream backends or users. Defaults to `"none"`. |
| `name` | Optional. A unique name for the variable. Automatically generated if not set. |
| `layout` | Optional. Sharding layout for the variable. Can be a [`keras.distribution.TensorLayout`](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/TensorLayout)<br> or a backend-specific layout. |
| `kwargs` | Additional backend-specific keyword arguments. |

#### Examples:

**Initializing a `Variable` with a NumPy array:**

import numpy as np
    import keras
    initial_array = np.ones((3, 3))
    variable_from_array = keras.Variable(initializer=initial_array)

**Using a Keras initializer to create a `Variable`:**

from keras.src.initializers import Ones
    variable_from_initializer = keras.Variable(
        initializer=Ones(), shape=(3, 3), dtype="float32"
    )

**Updating the value of a `Variable`:**

new_value = np.zeros((3, 3), dtype="float32")
    variable_from_array.assign(new_value)

**Marking a `Variable` as non-trainable:**

non_trainable_variable = keras.Variable(
        initializer=np.ones((3, 3), dtype="float32"), trainable=False
    )

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `shape` | The shape of the variable (tuple of integers). |
| `ndim` | The number of dimensions of the variable (integer). |
| `dtype` | The data type of the variable (string). |
| `trainable` | Whether the variable is trainable (boolean). |
| `autocast` | Whether the variable supports autocasting (boolean). |
| `aggregation` | How a distributed variable will be aggregated (string). |
| `value` | The current value of the variable (NumPy array or tensor). |
| `name` | The name of the variable (string). |
| `path` | The path of the variable within the Keras model or layer (string). |
| `constraint` |     |
| `handle` |     |
| `overwrite_with_gradient` | Whether this variable should be overwritten by the gradient.<br><br>This property is designed for a special case where we want to overwrite the variable directly with its computed gradient. For example, in float8 training, new `scale` and `amax_history` are computed as gradients, and we want to overwrite them directly instead of following the typical procedure such as gradient descent with a learning rate, gradient clipping and weight decaying. |
| `regularizer` |     |
| `synchronization` | The strategy for synchronizing this variable. |

Methods
-------

### `assign`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L282-L298)

assign(
        value
    )

### `assign_add`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L300-L301)

assign_add(
        value
    )

### `assign_sub`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L303-L304)

assign_sub(
        value
    )

### `numpy`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/core.py#L76-L77)

numpy()

### `__abs__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L460-L461)

__abs__()

### `__add__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L484-L485)

__add__(
        other
    )

### `__and__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L532-L533)

__and__(
        other
    )

### `__array__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L444-L449)

__array__(
        dtype=None
    )

### `__bool__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L451-L452)

__bool__()

### `__eq__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L466-L467)

__eq__(
        other
    )

Return self==value.

### `__floordiv__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L508-L509)

__floordiv__(
        other
    )

### `__ge__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L481-L482)

__ge__(
        other
    )

Return self>=value.

### `__getitem__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L425-L426)

__getitem__(
        idx
    )

### `__gt__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L478-L479)

__gt__(
        other
    )

Return self>value.

### `__invert__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L463-L464)

__invert__()

### `__le__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L475-L476)

__le__(
        other
    )

Return self<=value.

### `__lt__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L472-L473)

__lt__(
        other
    )

Return self<value.

### `__matmul__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L526-L527)

__matmul__(
        other
    )

### `__mod__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L514-L515)

__mod__(
        other
    )

### `__mul__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L496-L497)

__mul__(
        other
    )

### `__ne__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L469-L470)

__ne__(
        other
    )

Return self!=value.

### `__neg__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L454-L455)

__neg__()

### `__or__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L538-L539)

__or__(
        other
    )

Return self|value.

### `__pos__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L457-L458)

__pos__()

### `__pow__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L520-L521)

__pow__(
        other
    )

### `__radd__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L487-L488)

__radd__(
        other
    )

### `__rand__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L535-L536)

__rand__(
        other
    )

### `__rfloordiv__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L511-L512)

__rfloordiv__(
        other
    )

### `__rmatmul__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L529-L530)

__rmatmul__(
        other
    )

### `__rmod__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L517-L518)

__rmod__(
        other
    )

### `__rmul__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L499-L500)

__rmul__(
        other
    )

### `__ror__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L541-L542)

__ror__(
        other
    )

Return value|self.

### `__rpow__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L523-L524)

__rpow__(
        other
    )

### `__rsub__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L493-L494)

__rsub__(
        other
    )

### `__rtruediv__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L505-L506)

__rtruediv__(
        other
    )

### `__rxor__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L547-L548)

__rxor__(
        other
    )

### `__sub__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L490-L491)

__sub__(
        other
    )

### `__truediv__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L502-L503)

__truediv__(
        other
    )

### `__xor__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L544-L545)

__xor__(
        other
    )

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.