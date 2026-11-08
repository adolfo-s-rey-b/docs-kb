[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/iinfo#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/iinfo)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/iinfo?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/iinfo#attributes)
    
*   [Parameters](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/iinfo#parameters)
    
*   [See Also](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/iinfo#see_also)
    
*   [Examples](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/iinfo#examples)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/iinfo#attributes_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.numpy.iinfo Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/iinfo#attributes)
    
*   [Parameters](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/iinfo#parameters)
    
*   [See Also](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/iinfo#see_also)
    
*   [Examples](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/iinfo#examples)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/iinfo#attributes_1)
    

iinfo(type)

tf.experimental.numpy.iinfo(
        int_type
    )

Machine limits for integer types.

Attributes
----------

bits : int The number of bits occupied by the type. dtype : dtype Returns the dtype for which `iinfo` returns information. min : int The smallest integer expressible by the type. max : int The largest integer expressible by the type.

Parameters
----------

int\_type : integer type, dtype, or instance The kind of integer data type to get information about.

See Also
--------

finfo : The equivalent for floating point data types.

Examples
--------

With types:

    import numpy as np

#### With instances:

    ii32 = np.iinfo(np.int32(10))

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `max` | Maximum value of given dtype. |
| `min` | Minimum value of given dtype. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.