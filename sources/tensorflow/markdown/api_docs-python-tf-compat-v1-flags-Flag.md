[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/Flag#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/Flag)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/Flag?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/Flag#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/Flag#methods)
    *   [flag\_type](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/Flag#flag_type)
        
    *   [parse](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/Flag#parse)
        
    *   [serialize](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/Flag#serialize)
        
    *   [unparse](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/Flag#unparse)
        
    *   [\_\_bool\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/Flag#__bool__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/Flag#__eq__)
        
    *   [\_\_ge\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/Flag#__ge__)
        
    *   [\_\_gt\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/Flag#__gt__)
        
    *   [\_\_le\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/Flag#__le__)
        
    *   [\_\_lt\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/Flag#__lt__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.flags.Flag Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/Flag#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/Flag#methods)
    *   [flag\_type](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/Flag#flag_type)
        
    *   [parse](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/Flag#parse)
        
    *   [serialize](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/Flag#serialize)
        
    *   [unparse](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/Flag#unparse)
        
    *   [\_\_bool\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/Flag#__bool__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/Flag#__eq__)
        
    *   [\_\_ge\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/Flag#__ge__)
        
    *   [\_\_gt\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/Flag#__gt__)
        
    *   [\_\_le\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/Flag#__le__)
        
    *   [\_\_lt\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/Flag#__lt__)
        

Information about a command-line flag.

tf.compat.v1.flags.Flag(
        parser: _argument_parser.ArgumentParser[_T],
        serializer: (_argument_parser.ArgumentSerializer[_T] | None),
        name: str,
        default: (_T | None | str),
        help_string: (str | None),
        short_name: (str | None) = None,
        boolean: bool = False,
        allow_override: bool = False,
        allow_override_cpp: bool = False,
        allow_hide_cpp: bool = False,
        allow_overwrite: bool = True,
        allow_using_method_names: bool = False
    ) -> None

The only public method of a `Flag` object is :meth:`parse`, but it is typically only called by a :class:`~absl.flags.FlagValues` object. The :meth:`parse` method is a thin wrapper around the :meth:`ArgumentParser.parse()<absl.flags.ArgumentParser.parse>` method. The parsed value is saved in `.value`, and the `.present` attribute is updated. If this flag was already present, an Error is raised.

:meth:`parse` is also called during `__init__` to parse the default value and initialize the `.value` attribute. This enables other python modules to safely use flags even if the `__main__` module neglects to parse the command line arguments. The `.present` attribute is cleared after `__init__` parsing. If the default value is set to `None`, then the `__init__` parsing step is skipped and the `.value` attribute is initialized to None.

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `name` | the name for this flag |
| `default` | the default value for this flag |
| `default_unparsed` | the unparsed default value for this flag. |
| `default_as_str` | default value as repr'd string, e.g., "'true'" (or None) |
| `value` | the most recent parsed value of this flag set by :meth:`parse` |
| `help` | a help string or None if no help is available |
| `short_name` | the single letter alias for this flag (or None) |
| `boolean` | if 'true', this flag does not accept arguments |
| `present` | true if this flag was parsed from command line flags |
| `parser` | an :class:`~absl.flags.ArgumentParser` object |
| `serializer` | an ArgumentSerializer object |
| `allow_override` | the flag may be redefined without raising an error, and newly defined flag overrides the old one. |
| `allow_override_cpp` | use the flag from C++ if available the flag definition is replaced by the C++ flag after init |
| `allow_hide_cpp` | use the Python flag despite having a C++ flag with the same name (ignore the C++ flag) |
| `using_default_value` | the flag value has not been set by user |
| `allow_overwrite` | the flag may be parsed more than once without raising an error, the last set value will be used |
| `allow_using_method_names` | whether this flag can be defined even if it has a name that conflicts with a FlagValues method. |
| `validators` | list of the flag validators. |

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