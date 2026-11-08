[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BooleanFlag#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BooleanFlag)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BooleanFlag?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BooleanFlag#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BooleanFlag#methods)
    *   [flag\_type](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BooleanFlag#flag_type)
        
    *   [parse](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BooleanFlag#parse)
        
    *   [serialize](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BooleanFlag#serialize)
        
    *   [unparse](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BooleanFlag#unparse)
        
    *   [\_\_bool\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BooleanFlag#__bool__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BooleanFlag#__eq__)
        
    *   [\_\_ge\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BooleanFlag#__ge__)
        
    *   [\_\_gt\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BooleanFlag#__gt__)
        
    *   [\_\_le\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BooleanFlag#__le__)
        
    *   [\_\_lt\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BooleanFlag#__lt__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.flags.BooleanFlag Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BooleanFlag#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BooleanFlag#methods)
    *   [flag\_type](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BooleanFlag#flag_type)
        
    *   [parse](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BooleanFlag#parse)
        
    *   [serialize](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BooleanFlag#serialize)
        
    *   [unparse](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BooleanFlag#unparse)
        
    *   [\_\_bool\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BooleanFlag#__bool__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BooleanFlag#__eq__)
        
    *   [\_\_ge\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BooleanFlag#__ge__)
        
    *   [\_\_gt\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BooleanFlag#__gt__)
        
    *   [\_\_le\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BooleanFlag#__le__)
        
    *   [\_\_lt\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BooleanFlag#__lt__)
        

Basic boolean flag.

Inherits From: [`Flag`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/Flag)

tf.compat.v1.flags.BooleanFlag(
        name: str,
        default: (bool | None | str),
        help: (str | None),
        short_name: (str | None) = None,
        **args
    ) -> None

Boolean flags do not take any arguments, and their value is either `True` (1) or `False` (0). The false value is specified on the command line by prepending the word `'no'` to either the long or the short flag name.

For example, if a Boolean flag was created whose long name was `'update'` and whose short name was `'x'`, then this flag could be explicitly unset through either `--noupdate` or `--nox`.

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `value` |     |

Methods
-------

### `flag_type`

flag_type() -> str

Returns a str that describes the type of the flag.

### `parse`

parse(
        argument: (str | _T)
    ) -> None

Parses string and sets flag value.

|     |     |
| --- | --- |
| Args |     |
| `argument` | str or the correct flag value type, argument to be parsed. |

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