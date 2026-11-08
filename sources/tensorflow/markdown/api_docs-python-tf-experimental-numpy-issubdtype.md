[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/issubdtype#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/issubdtype)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/issubdtype?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fexperimental%2Fnumpy%2Fissubdtype&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Parameters](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/issubdtype#parameters)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/issubdtype#returns)
    
*   [See Also](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/issubdtype#see_also)
    
*   [Examples](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/issubdtype#examples)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.numpy.issubdtype Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Parameters](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/issubdtype#parameters)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/issubdtype#returns)
    
*   [See Also](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/issubdtype#see_also)
    
*   [Examples](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/issubdtype#examples)
    

Returns True if first argument is a typecode lower/equal in type hierarchy.

tf.experimental.numpy.issubdtype(
        arg1, arg2
    )

This is like the builtin :func:`issubclass`, but for `dtype`\\ s.

Parameters
----------

arg1, arg2 : dtype\_like `dtype` or object coercible to one

Returns
-------

out : bool

See Also
--------

:ref:`arrays.scalars` : Overview of the numpy type hierarchy.

Examples
--------

`issubdtype` can be used to check the type of arrays:

    ints = np.array([1, 2, 3], dtype=np.int32)

    floats = np.array([1, 2, 3], dtype=np.float32)

Similar types of different sizes are not subdtypes of each other:

    np.issubdtype(np.float64, np.float32)

but both are subtypes of `floating`:

    np.issubdtype(np.float64, np.floating)

For convenience, dtype-like objects are allowed too:

    np.issubdtype('S1', np.bytes_)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.