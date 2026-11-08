[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FloatParser#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FloatParser)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FloatParser?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FloatParser#methods)
    *   [convert](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FloatParser#convert)
        
    *   [flag\_type](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FloatParser#flag_type)
        
    *   [is\_outside\_bounds](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FloatParser#is_outside_bounds)
        
    *   [parse](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FloatParser#parse)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FloatParser#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.flags.FloatParser Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FloatParser#methods)
    *   [convert](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FloatParser#convert)
        
    *   [flag\_type](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FloatParser#flag_type)
        
    *   [is\_outside\_bounds](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FloatParser#is_outside_bounds)
        
    *   [parse](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FloatParser#parse)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FloatParser#class-variables)
    

Parser of floating point values.

Inherits From: [`ArgumentParser`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/ArgumentParser)

tf.compat.v1.flags.FloatParser(
        lower_bound: (float | None) = None, upper_bound: (float | None) = None
    ) -> None

Parsed value may be bounded to a given upper and lower bound.

Methods
-------

### `convert`

convert(
        argument: (int | float | str)
    ) -> float

Returns the float value of argument.

### `flag_type`

flag_type() -> str

See base class.

### `is_outside_bounds`

is_outside_bounds(
        val: _N
    ) -> bool

Returns whether the value is outside the bounds or not.

### `parse`

parse(
        argument: (str | _N)
    ) -> _N

See base class.

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| number\_article | `'a'` |
| number\_name | `'number'` |
| syntactic\_help | `'a number'` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.