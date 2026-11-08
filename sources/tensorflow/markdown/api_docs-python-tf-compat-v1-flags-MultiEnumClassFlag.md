[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/MultiEnumClassFlag#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/MultiEnumClassFlag)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/MultiEnumClassFlag?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/MultiEnumClassFlag#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/MultiEnumClassFlag#methods)
    *   [flag\_type](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/MultiEnumClassFlag#flag_type)
        
    *   [parse](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/MultiEnumClassFlag#parse)
        
    *   [serialize](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/MultiEnumClassFlag#serialize)
        
    *   [unparse](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/MultiEnumClassFlag#unparse)
        
    *   [\_\_bool\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/MultiEnumClassFlag#__bool__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/MultiEnumClassFlag#__eq__)
        
    *   [\_\_ge\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/MultiEnumClassFlag#__ge__)
        
    *   [\_\_gt\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/MultiEnumClassFlag#__gt__)
        
    *   [\_\_le\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/MultiEnumClassFlag#__le__)
        
    *   [\_\_lt\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/MultiEnumClassFlag#__lt__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.flags.MultiEnumClassFlag Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/MultiEnumClassFlag#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/MultiEnumClassFlag#methods)
    *   [flag\_type](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/MultiEnumClassFlag#flag_type)
        
    *   [parse](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/MultiEnumClassFlag#parse)
        
    *   [serialize](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/MultiEnumClassFlag#serialize)
        
    *   [unparse](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/MultiEnumClassFlag#unparse)
        
    *   [\_\_bool\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/MultiEnumClassFlag#__bool__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/MultiEnumClassFlag#__eq__)
        
    *   [\_\_ge\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/MultiEnumClassFlag#__ge__)
        
    *   [\_\_gt\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/MultiEnumClassFlag#__gt__)
        
    *   [\_\_le\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/MultiEnumClassFlag#__le__)
        
    *   [\_\_lt\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/MultiEnumClassFlag#__lt__)
        

A multi\_enum\_class flag.

Inherits From: [`MultiFlag`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/MultiFlag)
, [`Flag`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/Flag)

tf.compat.v1.flags.MultiEnumClassFlag(
        name: str,
        default: (None | Iterable[_ET] | _ET | Iterable[str] | str),
        help_string: str,
        enum_class: type[_ET],
        case_sensitive: bool = False,
        **args
    )

See the **doc** for MultiFlag for most behaviors of this class. In addition, this class knows how to handle enum.Enum instances as values for this flag type.

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `value` |     |

Methods
-------

### `flag_type`

flag_type()

See base class.

### `parse`

parse(
        arguments: (str | _T | Iterable[_T])
    )

Parses one or more arguments with the installed parser.

|     |     |
| --- | --- |
| Args |     |
| `arguments` | a single argument or a list of arguments (typically a list of default values); a single argument is converted internally into a list containing one item. |

### `serialize`

serialize() -> str

Serializes the flag.

### `unparse`

unparse() -> None

### `__bool__`

__bool__()

### `__eq__`

__eq__(
        other
    )

Return self==value.

### `__ge__`

__ge__(
        other
    )

Return a >= b. Computed by @total\_ordering from (not a < b).

### `__gt__`

__gt__(
        other
    )

Return a > b. Computed by @total\_ordering from (not a < b) and (a != b).

### `__le__`

__le__(
        other
    )

Return a <= b. Computed by @total\_ordering from (a < b) or (a == b).

### `__lt__`

__lt__(
        other
    )

Return self<value.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.