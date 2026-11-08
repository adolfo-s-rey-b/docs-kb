[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#methods)
    *   [reshape](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#reshape)
        
    *   [squeeze](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#squeeze)
        
    *   [\_\_abs\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__abs__)
        
    *   [\_\_add\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__add__)
        
    *   [\_\_and\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__and__)
        
    *   [\_\_array\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__array__)
        
    *   [\_\_bool\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__bool__)
        
    *   [\_\_div\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__div__)
        
    *   [\_\_floordiv\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__floordiv__)
        
    *   [\_\_ge\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__ge__)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__getitem__)
        
    *   [\_\_gt\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__gt__)
        
    *   [\_\_invert\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__invert__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__iter__)
        
    *   [\_\_le\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__le__)
        
    *   [\_\_lt\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__lt__)
        
    *   [\_\_matmul\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__matmul__)
        
    *   [\_\_mod\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__mod__)
        
    *   [\_\_mul\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__mul__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__ne__)
        
    *   [\_\_neg\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__neg__)
        
    *   [\_\_or\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__or__)
        
    *   [\_\_pow\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__pow__)
        
    *   [\_\_radd\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__radd__)
        
    *   [\_\_rand\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__rand__)
        
    *   [\_\_rdiv\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__rdiv__)
        
    *   [\_\_rfloordiv\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__rfloordiv__)
        
    *   [\_\_rmatmul\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__rmatmul__)
        
    *   [\_\_rmod\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__rmod__)
        
    *   [\_\_rmul\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__rmul__)
        
    *   [\_\_ror\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__ror__)
        
    *   [\_\_rpow\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__rpow__)
        
    *   [\_\_rsub\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__rsub__)
        
    *   [\_\_rtruediv\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__rtruediv__)
        
    *   [\_\_rxor\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__rxor__)
        
    *   [\_\_sub\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__sub__)
        
    *   [\_\_truediv\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__truediv__)
        
    *   [\_\_xor\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__xor__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.KerasTensor Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#methods)
    *   [reshape](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#reshape)
        
    *   [squeeze](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#squeeze)
        
    *   [\_\_abs\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__abs__)
        
    *   [\_\_add\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__add__)
        
    *   [\_\_and\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__and__)
        
    *   [\_\_array\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__array__)
        
    *   [\_\_bool\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__bool__)
        
    *   [\_\_div\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__div__)
        
    *   [\_\_floordiv\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__floordiv__)
        
    *   [\_\_ge\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__ge__)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__getitem__)
        
    *   [\_\_gt\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__gt__)
        
    *   [\_\_invert\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__invert__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__iter__)
        
    *   [\_\_le\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__le__)
        
    *   [\_\_lt\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__lt__)
        
    *   [\_\_matmul\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__matmul__)
        
    *   [\_\_mod\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__mod__)
        
    *   [\_\_mul\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__mul__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__ne__)
        
    *   [\_\_neg\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__neg__)
        
    *   [\_\_or\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__or__)
        
    *   [\_\_pow\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__pow__)
        
    *   [\_\_radd\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__radd__)
        
    *   [\_\_rand\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__rand__)
        
    *   [\_\_rdiv\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__rdiv__)
        
    *   [\_\_rfloordiv\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__rfloordiv__)
        
    *   [\_\_rmatmul\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__rmatmul__)
        
    *   [\_\_rmod\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__rmod__)
        
    *   [\_\_rmul\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__rmul__)
        
    *   [\_\_ror\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__ror__)
        
    *   [\_\_rpow\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__rpow__)
        
    *   [\_\_rsub\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__rsub__)
        
    *   [\_\_rtruediv\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__rtruediv__)
        
    *   [\_\_rxor\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__rxor__)
        
    *   [\_\_sub\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__sub__)
        
    *   [\_\_truediv\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__truediv__)
        
    *   [\_\_xor\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor#__xor__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L6-L399)

Symbolic tensor -- encapsulates a shape and a dtype.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.keras.KerasTensor`](https://www.tensorflow.org/api_docs/python/tf/keras/KerasTensor)

tf.keras.KerasTensor(
        shape,
        dtype='float32',
        sparse=False,
        ragged=False,
        record_history=True,
        name=None,
        **kwargs
    )

You can use `KerasTensor` instances to build computation graphs of Keras operations, such as [`keras.Function`](https://www.tensorflow.org/api_docs/python/tf/keras/Function)
 objects or Functional [`keras.models.Model`](https://www.tensorflow.org/api_docs/python/tf/keras/Model)
 objects.

#### Example:

    x = keras.KerasTensor(shape=(3, 4), dtype="float32")

Calling a Keras operation (including a layer or a model) on a `KerasTensor` instance will return another `KerasTensor` instance with the appropriate shape and dtype. This is called a "symbolic call" (since there is no actual data involved). The computation of the correct output shape and dtype is called "static shape inference".

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `dtype` |     |
| `ndim` |     |
| `ragged` |     |
| `ragged_rank` |     |
| `row_splits_dtype` |     |
| `shape` |     |
| `sparse` |     |

Methods
-------

### `reshape`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L139-L142)

reshape(
        newshape
    )

### `squeeze`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L144-L147)

squeeze(
        axis=None
    )

### `__abs__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L295-L298)

__abs__()

### `__add__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L230-L233)

__add__(
        other
    )

### `__and__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L355-L358)

__and__(
        other
    )

### `__array__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L163-L168)

__array__()

### `__bool__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L227-L228)

__bool__()

### `__div__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L270-L273)

__div__(
        other
    )

### `__floordiv__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L310-L313)

__floordiv__(
        other
    )

### `__ge__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L345-L348)

__ge__(
        other
    )

Return self>=value.

### `__getitem__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L390-L393)

__getitem__(
        key
    )

### `__gt__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L340-L343)

__gt__(
        other
    )

Return self>value.

### `__invert__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L375-L378)

__invert__()

### `__iter__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L222-L225)

__iter__()

### `__le__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L335-L338)

__le__(
        other
    )

Return self<=value.

### `__lt__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L330-L333)

__lt__(
        other
    )

Return self<value.

### `__matmul__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L260-L263)

__matmul__(
        other
    )

### `__mod__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L320-L323)

__mod__(
        other
    )

### `__mul__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L250-L253)

__mul__(
        other
    )

### `__ne__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L350-L353)

__ne__(
        other
    )

Return self!=value.

### `__neg__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L290-L293)

__neg__()

### `__or__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L365-L368)

__or__(
        other
    )

Return self|value.

### `__pow__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L300-L303)

__pow__(
        other
    )

### `__radd__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L235-L238)

__radd__(
        other
    )

### `__rand__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L360-L363)

__rand__(
        other
    )

### `__rdiv__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L275-L278)

__rdiv__(
        other
    )

### `__rfloordiv__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L315-L318)

__rfloordiv__(
        other
    )

### `__rmatmul__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L265-L268)

__rmatmul__(
        other
    )

### `__rmod__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L325-L328)

__rmod__(
        other
    )

### `__rmul__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L255-L258)

__rmul__(
        other
    )

### `__ror__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L370-L373)

__ror__(
        other
    )

Return value|self.

### `__rpow__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L305-L308)

__rpow__(
        other
    )

### `__rsub__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L245-L248)

__rsub__(
        other
    )

### `__rtruediv__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L285-L288)

__rtruediv__(
        other
    )

### `__rxor__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L385-L388)

__rxor__(
        other
    )

### `__sub__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L240-L243)

__sub__(
        other
    )

### `__truediv__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L280-L283)

__truediv__(
        other
    )

### `__xor__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L380-L383)

__xor__(
        other
    )

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.