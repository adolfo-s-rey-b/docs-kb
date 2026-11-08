[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/ArgumentParser#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/ArgumentParser)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/ArgumentParser?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/ArgumentParser#methods)
    *   [flag\_type](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/ArgumentParser#flag_type)
        
    *   [parse](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/ArgumentParser#parse)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/ArgumentParser#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.flags.ArgumentParser Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/ArgumentParser#methods)
    *   [flag\_type](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/ArgumentParser#flag_type)
        
    *   [parse](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/ArgumentParser#parse)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/ArgumentParser#class-variables)
    

Base class used to parse and convert arguments.

The :meth:`parse` method checks to make sure that the string argument is a legal value and convert it to a native type. If the value cannot be converted, it should throw a `ValueError` exception with a human readable explanation of why the value is illegal.

Subclasses should also define a syntactic\_help string which may be presented to the user to describe the form of the legal values.

Argument parser classes must be stateless, since instances are cached and shared between flags. Initializer arguments are allowed, but all member variables must be derived from initializer arguments only.

Methods
-------

### `flag_type`

flag_type() -> str

Returns a string representing the type of the flag.

### `parse`

parse(
        argument: str
    ) -> (_T | None)

Parses the string argument and returns the native value.

By default it returns its argument unmodified.

|     |     |
| --- | --- |
| Args |     |
| `argument` | string argument passed in the commandline. |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | Raised when it fails to parse the argument. |
| `TypeError` | Raised when the argument has the wrong type. |

|     |
| --- |
| Returns |     |
| The parsed value in native type. |     |

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| syntactic\_help | `''` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.