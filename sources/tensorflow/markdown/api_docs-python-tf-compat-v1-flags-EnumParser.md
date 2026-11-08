[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumParser#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumParser)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumParser?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumParser#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumParser#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumParser#methods)
    *   [flag\_type](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumParser#flag_type)
        
    *   [parse](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumParser#parse)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumParser#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.flags.EnumParser Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumParser#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumParser#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumParser#methods)
    *   [flag\_type](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumParser#flag_type)
        
    *   [parse](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumParser#parse)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumParser#class-variables)
    

Parser of a string enum value (a string value from a given set).

Inherits From: [`ArgumentParser`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/ArgumentParser)

tf.compat.v1.flags.EnumParser(
        enum_values: Iterable[str], case_sensitive: bool = True
    ) -> None

|     |     |
| --- | --- |
| Args<br>---- |     |
| `enum_values` | \[str\], a non-empty list of string values in the enum. |
| `case_sensitive` | bool, whether or not the enum is to be case-sensitive. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | When enum\_values is empty. |

Methods
-------

### `flag_type`

flag_type() -> str

See base class.

### `parse`

parse(
        argument: str
    ) -> str

Determines validity of argument and returns the correct element of enum.

|     |     |
| --- | --- |
| Args |     |
| `argument` | str, the supplied flag value. |

|     |
| --- |
| Returns |     |
| The first matching element from enum\_values. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | Raised when argument didn't match anything in enum. |

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