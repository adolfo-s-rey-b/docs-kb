[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/compat#modules)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tf/compat#other-members)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.compat Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/compat#modules)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tf/compat#other-members)
    

Public API for tf.\_api.v2.compat namespace

Modules
-------

[`v1`](https://www.tensorflow.org/api_docs/python/tf/compat/v1)
 module: Bring in all of the public TensorFlow interface into this module.

Functions
---------

[`as_bytes(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/as_bytes)
: Converts `bytearray`, `bytes`, or unicode python input types to `bytes`.

[`as_str(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/as_str)
: Acts as an alias for the `as_text` function..

[`as_str_any(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/as_str_any)
: Converts input to `str` type.

[`as_text(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/as_text)
: Converts any string-like python input types to unicode.

[`dimension_at_index(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/dimension_at_index)
: Compatibility utility required to allow for both V1 and V2 behavior in TF.

[`dimension_value(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/dimension_value)
: Compatibility utility required to allow for both V1 and V2 behavior in TF.

[`forward_compatibility_horizon(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/forward_compatibility_horizon)
: Context manager for testing forward compatibility of generated graphs.

[`forward_compatible(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/forward_compatible)
: Return true if the forward compatibility window has expired.

[`path_to_str(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/path_to_str)
: Converts input which is a `PathLike` object to `str` type.

|     |     |
| --- | --- |
| Other Members<br>------------- |     |
| bytes\_or\_text\_types | `(<class 'bytes'>, <class 'str'>)` |
| complex\_types | `(<class 'numbers.Complex'>, <class 'numpy.number'>)` |
| integral\_types | `(<class 'numbers.Integral'>, <class 'numpy.integer'>)` |
| real\_types | `(<class 'numbers.Real'>, <class 'numpy.integer'>, <class 'numpy.floating'>)` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.