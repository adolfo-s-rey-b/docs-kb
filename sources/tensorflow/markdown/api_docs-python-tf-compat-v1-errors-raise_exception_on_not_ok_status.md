[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/errors/raise_exception_on_not_ok_status#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/errors/raise_exception_on_not_ok_status)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/errors/raise_exception_on_not_ok_status?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/errors/raise_exception_on_not_ok_status#methods)
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/errors/raise_exception_on_not_ok_status#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/errors/raise_exception_on_not_ok_status#__exit__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.errors.raise\_exception\_on\_not\_ok\_status Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/errors/raise_exception_on_not_ok_status#methods)
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/errors/raise_exception_on_not_ok_status#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/errors/raise_exception_on_not_ok_status#__exit__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/errors_impl.py#L552-L571)

Context manager to check for C API status.

Methods
-------

### `__enter__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/errors_impl.py#L556-L558)

__enter__()

### `__exit__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/errors_impl.py#L560-L571)

__exit__(
        type_arg, value_arg, traceback_arg
    )

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.