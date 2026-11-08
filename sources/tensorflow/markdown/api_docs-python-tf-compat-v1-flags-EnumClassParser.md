[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumClassParser#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumClassParser)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumClassParser?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumClassParser#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumClassParser#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumClassParser#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumClassParser#methods)
    *   [flag\_type](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumClassParser#flag_type)
        
    *   [parse](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumClassParser#parse)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumClassParser#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.flags.EnumClassParser Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumClassParser#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumClassParser#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumClassParser#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumClassParser#methods)
    *   [flag\_type](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumClassParser#flag_type)
        
    *   [parse](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumClassParser#parse)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumClassParser#class-variables)
    

Parser of an Enum class member.

Inherits From: [`ArgumentParser`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/ArgumentParser)

tf.compat.v1.flags.EnumClassParser(
        enum_class: type[_ET], case_sensitive: bool = True
    ) -> None

|     |     |
| --- | --- |
| Args<br>---- |     |
| `enum_class` | class, the Enum class with all possible flag values. |
| `case_sensitive` | bool, whether or not the enum is to be case-sensitive. If False, all member names must be unique when case is ignored. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | When enum\_class is not a subclass of Enum. |
| `ValueError` | When enum\_class is empty. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `member_names` | The accepted enum names, in lowercase if not case sensitive. |

Methods
-------

### `flag_type`

flag_type() -> str

See base class.

### `parse`

parse(
        argument: (_ET | str)
    ) -> _ET

Determines validity of argument and returns the correct element of enum.

|     |     |
| --- | --- |
| Args |     |
| `argument` | str or Enum class member, the supplied flag value. |

|     |
| --- |
| Returns |     |
| The first matching Enum class member in Enum class. |     |

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