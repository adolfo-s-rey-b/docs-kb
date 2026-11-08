[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagHolder#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagHolder)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagHolder?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagHolder#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagHolder#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagHolder#methods)
    *   [serialize](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagHolder#serialize)
        
    *   [\_\_bool\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagHolder#__bool__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagHolder#__eq__)
        
    *   [\_\_nonzero\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagHolder#__nonzero__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.flags.FlagHolder Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagHolder#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagHolder#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagHolder#methods)
    *   [serialize](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagHolder#serialize)
        
    *   [\_\_bool\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagHolder#__bool__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagHolder#__eq__)
        
    *   [\_\_nonzero\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagHolder#__nonzero__)
        

Holds a defined flag.

tf.compat.v1.flags.FlagHolder(
        flag_values: tf.compat.v1.flags.FlagValues,
        flag: Flag[_T_co],
        ensure_non_none_value: bool = False
    )

This facilitates a cleaner api around global state. Instead of::

flags.DEFINE_integer('foo', ...)
    flags.DEFINE_integer('bar', ...)
    
    def method():
      # prints parsed value of 'bar' flag
      print(flags.FLAGS.foo)
      # runtime error due to typo or possibly bad coding style.
      print(flags.FLAGS.baz)

it encourages code like::

_FOO_FLAG = flags.DEFINE_integer('foo', ...)
    _BAR_FLAG = flags.DEFINE_integer('bar', ...)
    
    def method():
      print(_FOO_FLAG.value)
      print(_BAR_FLAG.value)

since the name of the flag appears only once in the source code.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `flag_values` | The container the flag is registered to. |
| `flag` | The flag object for this flag. |
| `ensure_non_none_value` | Is the value of the flag allowed to be None. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `default` | Returns the default value of the flag. |
| `name` |     |
| `present` | Returns True if the flag was parsed from command-line flags. |
| `value` | Returns the value of the flag.<br><br>If `_ensure_non_none_value` is `True`, then return value is not `None`. |

Methods
-------

### `serialize`

serialize() -> str

Returns a serialized representation of the flag.

### `__bool__`

__bool__() -> NoReturn

### `__eq__`

__eq__(
        other
    ) -> NoReturn

Return self==value.

### `__nonzero__`

__nonzero__() -> NoReturn

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.