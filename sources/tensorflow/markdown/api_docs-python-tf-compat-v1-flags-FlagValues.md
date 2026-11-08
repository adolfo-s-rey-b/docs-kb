[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#methods)
    *   [append\_flag\_values](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#append_flag_values)
        
    *   [append\_flags\_into\_file](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#append_flags_into_file)
        
    *   [find\_module\_defining\_flag](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#find_module_defining_flag)
        
    *   [find\_module\_id\_defining\_flag](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#find_module_id_defining_flag)
        
    *   [flag\_values\_dict](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#flag_values_dict)
        
    *   [flags\_by\_module\_dict](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#flags_by_module_dict)
        
    *   [flags\_by\_module\_id\_dict](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#flags_by_module_id_dict)
        
    *   [flags\_into\_string](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#flags_into_string)
        
    *   [get\_flag\_value](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#get_flag_value)
        
    *   [get\_flags\_for\_module](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#get_flags_for_module)
        
    *   [get\_help](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#get_help)
        
    *   [get\_key\_flags\_for\_module](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#get_key_flags_for_module)
        
    *   [is\_gnu\_getopt](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#is_gnu_getopt)
        
    *   [is\_parsed](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#is_parsed)
        
    *   [key\_flags\_by\_module\_dict](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#key_flags_by_module_dict)
        
    *   [main\_module\_help](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#main_module_help)
        
    *   [mark\_as\_parsed](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#mark_as_parsed)
        
    *   [module\_help](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#module_help)
        
    *   [read\_flags\_from\_files](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#read_flags_from_files)
        
    *   [register\_flag\_by\_module](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#register_flag_by_module)
        
    *   [register\_flag\_by\_module\_id](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#register_flag_by_module_id)
        
    *   [register\_key\_flag\_for\_module](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#register_key_flag_for_module)
        
    *   [remove\_flag\_values](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#remove_flag_values)
        
    *   [set\_default](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#set_default)
        
    *   [set\_gnu\_getopt](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#set_gnu_getopt)
        
    *   [unparse\_flags](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#unparse_flags)
        
    *   [validate\_all\_flags](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#validate_all_flags)
        
    *   [write\_help\_in\_xml\_format](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#write_help_in_xml_format)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#__call__)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#__contains__)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#__getitem__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#__iter__)
        
    *   [\_\_len\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#__len__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.flags.FlagValues Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#methods)
    *   [append\_flag\_values](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#append_flag_values)
        
    *   [append\_flags\_into\_file](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#append_flags_into_file)
        
    *   [find\_module\_defining\_flag](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#find_module_defining_flag)
        
    *   [find\_module\_id\_defining\_flag](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#find_module_id_defining_flag)
        
    *   [flag\_values\_dict](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#flag_values_dict)
        
    *   [flags\_by\_module\_dict](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#flags_by_module_dict)
        
    *   [flags\_by\_module\_id\_dict](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#flags_by_module_id_dict)
        
    *   [flags\_into\_string](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#flags_into_string)
        
    *   [get\_flag\_value](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#get_flag_value)
        
    *   [get\_flags\_for\_module](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#get_flags_for_module)
        
    *   [get\_help](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#get_help)
        
    *   [get\_key\_flags\_for\_module](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#get_key_flags_for_module)
        
    *   [is\_gnu\_getopt](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#is_gnu_getopt)
        
    *   [is\_parsed](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#is_parsed)
        
    *   [key\_flags\_by\_module\_dict](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#key_flags_by_module_dict)
        
    *   [main\_module\_help](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#main_module_help)
        
    *   [mark\_as\_parsed](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#mark_as_parsed)
        
    *   [module\_help](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#module_help)
        
    *   [read\_flags\_from\_files](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#read_flags_from_files)
        
    *   [register\_flag\_by\_module](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#register_flag_by_module)
        
    *   [register\_flag\_by\_module\_id](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#register_flag_by_module_id)
        
    *   [register\_key\_flag\_for\_module](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#register_key_flag_for_module)
        
    *   [remove\_flag\_values](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#remove_flag_values)
        
    *   [set\_default](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#set_default)
        
    *   [set\_gnu\_getopt](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#set_gnu_getopt)
        
    *   [unparse\_flags](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#unparse_flags)
        
    *   [validate\_all\_flags](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#validate_all_flags)
        
    *   [write\_help\_in\_xml\_format](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#write_help_in_xml_format)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#__call__)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#__contains__)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#__getitem__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#__iter__)
        
    *   [\_\_len\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues#__len__)
        

Registry of :class:`~absl.flags.Flag` objects.

tf.compat.v1.flags.FlagValues()

A :class:`FlagValues` can then scan command line arguments, passing flag arguments through to the 'Flag' objects that it owns. It also provides easy access to the flag values. Typically only one :class:`FlagValues` object is needed by an application: :const:`FLAGS`.

This class is heavily overloaded:

:class:`Flag` objects are registered via `__setitem__`::

 FLAGS['longname'] = x   # register a new flag

The `.value` attribute of the registered :class:`~absl.flags.Flag` objects can be accessed as attributes of this :class:`FlagValues` object, through `__getattr__`. Both the long and short name of the original :class:`~absl.flags.Flag` objects can be used to access its value::

 FLAGS.longname  # parsed flag value
     FLAGS.x  # parsed flag value (short name)

Command line arguments are scanned and passed to the registered :class:`~absl.flags.Flag` objects through the `__call__` method. Unparsed arguments, including `argv[0]` (e.g. the program name) are returned::

 argv = FLAGS(sys.argv)  # scan command line arguments

The original registered :class:`~absl.flags.Flag` objects can be retrieved through the use of the dictionary-like operator, `__getitem__`::

 x = FLAGS['longname']   # access the registered Flag object

The `str()` operator of a :class:`absl.flags.FlagValues` object provides help for all of the registered :class:`~absl.flags.Flag` objects.

Methods
-------

### `append_flag_values`

append_flag_values(
        flag_values: 'FlagValues'
    ) -> None

Appends flags registered in another FlagValues instance.

|     |     |
| --- | --- |
| Args |     |
| `flag_values` | FlagValues, the FlagValues instance from which to copy flags. |

### `append_flags_into_file`

append_flags_into_file(
        filename: str
    ) -> None

Appends all flags assignments from this FlagInfo object to a file.

Output will be in the format of a flagfile.

|     |     |
| --- | --- |
| Args |     |
| `filename` | str, name of the file. |

### `find_module_defining_flag`

find_module_defining_flag(
        flagname: str, default: (_T | None) = None
    ) -> (str | _T | None)

Return the name of the module defining this flag, or default.

|     |     |
| --- | --- |
| Args |     |
| `flagname` | str, name of the flag to lookup. |
| `default` | Value to return if flagname is not defined. Defaults to None. |

|     |
| --- |
| Returns |     |
| The name of the module which registered the flag with this name. If no such module exists (i.e. no flag with this name exists), we return default. |     |

### `find_module_id_defining_flag`

find_module_id_defining_flag(
        flagname: str, default: (_T | None) = None
    ) -> (int | _T | None)

Return the ID of the module defining this flag, or default.

|     |     |
| --- | --- |
| Args |     |
| `flagname` | str, name of the flag to lookup. |
| `default` | Value to return if flagname is not defined. Defaults to None. |

|     |
| --- |
| Returns |     |
| The ID of the module which registered the flag with this name. If no such module exists (i.e. no flag with this name exists), we return default. |     |

### `flag_values_dict`

flag_values_dict() -> dict[str, Any]

Returns a dictionary that maps flag names to flag values.

### `flags_by_module_dict`

flags_by_module_dict() -> dict[str, list[Flag]]

Returns the dictionary of module\_name -> list of defined flags.

|     |
| --- |
| Returns |     |
| A dictionary. Its keys are module names (strings). Its values are lists of Flag objects. |     |

### `flags_by_module_id_dict`

flags_by_module_id_dict() -> dict[int, list[Flag]]

Returns the dictionary of module\_id -> list of defined flags.

|     |
| --- |
| Returns |     |
| A dictionary. Its keys are module IDs (ints). Its values are lists of Flag objects. |     |

### `flags_into_string`

flags_into_string() -> str

Returns a string with the flags assignments from this FlagValues object.

This function ignores flags whose value is None. Each flag assignment is separated by a newline.

|     |
| --- |
| Returns |     |
| str, the string with the flags assignments from this FlagValues object. The flags are ordered by (module\_name, flag\_name). |     |

### `get_flag_value`

get_flag_value(
        name: str, default: Any
    ) -> Any

Returns the value of a flag (if not None) or a default value.

|     |     |
| --- | --- |
| Args |     |
| `name` | str, the name of a flag. |
| `default` | Default value to use if the flag value is None. |

|     |
| --- |
| Returns |     |
| Requested flag value or default. |     |

### `get_flags_for_module`

get_flags_for_module(
        module: (str | Any)
    ) -> list[Flag]

Returns the list of flags defined by a module.

|     |     |
| --- | --- |
| Args |     |
| `module` | module\|str, the module to get flags from. |

|     |     |
| --- | --- |
| Returns |     |
| \[Flag\], a new list of Flag instances. Caller may update this list as |     |
| `desired` | none of those changes will affect the internals of this FlagValue instance. |

### `get_help`

get_help(
        prefix: str = '', include_special_flags: bool = True
    ) -> str

Returns a help string for all known flags.

|     |     |
| --- | --- |
| Args |     |
| `prefix` | str, per-line output prefix. |
| `include_special_flags` | bool, whether to include description of SPECIAL\_FLAGS, i.e. --flagfile and --undefok. |

|     |
| --- |
| Returns |     |
| str, formatted help message. |     |

### `get_key_flags_for_module`

get_key_flags_for_module(
        module: (str | Any)
    ) -> list[Flag]

Returns the list of key flags for a module.

|     |     |
| --- | --- |
| Args |     |
| `module` | module\|str, the module to get key flags from. |

|     |     |
| --- | --- |
| Returns |     |
| \[Flag\], a new list of Flag instances. Caller may update this list as |     |
| `desired` | none of those changes will affect the internals of this FlagValue instance. |

### `is_gnu_getopt`

is_gnu_getopt() -> bool

### `is_parsed`

is_parsed() -> bool

Returns whether flags were parsed.

### `key_flags_by_module_dict`

key_flags_by_module_dict() -> dict[str, list[Flag]]

Returns the dictionary of module\_name -> list of key flags.

|     |
| --- |
| Returns |     |
| A dictionary. Its keys are module names (strings). Its values are lists of Flag objects. |     |

### `main_module_help`

main_module_help() -> str

Describes the key flags of the main module.

|     |
| --- |
| Returns |     |
| str, describing the key flags of the main module. |     |

### `mark_as_parsed`

mark_as_parsed() -> None

Explicitly marks flags as parsed.

Use this when the caller knows that this FlagValues has been parsed as if a `__call__()` invocation has happened. This is only a public method for use by things like appcommands which do additional command like parsing.

### `module_help`

module_help(
        module: Any
    ) -> str

Describes the key flags of a module.

|     |     |
| --- | --- |
| Args |     |
| `module` | module\|str, the module to describe the key flags for. |

|     |
| --- |
| Returns |     |
| str, describing the key flags of a module. |     |

### `read_flags_from_files`

read_flags_from_files(
        argv: Sequence[str], force_gnu: bool = True
    ) -> list[str]

Processes command line args, but also allow args to be read from file.

|     |     |
| --- | --- |
| Args |     |
| `argv` | \[str\], a list of strings, usually sys.argv\[1:\], which may contain one or more flagfile directives of the form --flagfile="./filename". Note that the name of the program (sys.argv\[0\]) should be omitted. |
| `force_gnu` | bool, if False, --flagfile parsing obeys the FLAGS.is\_gnu\_getopt() value. If True, ignore the value and always follow gnu\_getopt semantics. |

|     |
| --- |
| Returns |     |
| A new list which has the original list combined with what we read from any flagfile(s). |     |

|     |     |
| --- | --- |
| Raises |     |
| `IllegalFlagValueError` | Raised when --flagfile is provided with no argument. |

This function is called by FLAGS(argv). It scans the input list for a flag that looks like: --flagfile=. Then it opens , reads all valid key and value pairs and inserts them into the input list in exactly the place where the --flagfile arg is found.

Note that your application's flags are still defined the usual way using absl.flags DEFINE\_flag() type functions.

Notes (assuming we're getting a commandline of some sort as our input):

*   For duplicate flags, the last one we hit should "win".
*   Since flags that appear later win, a flagfile's settings can be "weak" if the --flagfile comes at the beginning of the argument sequence, and it can be "strong" if the --flagfile comes at the end.
*   A further "--flagfile=" CAN be nested in a flagfile. It will be expanded in exactly the spot where it is found.
*   In a flagfile, a line beginning with # or // is a comment.
*   Entirely blank lines _should_ be ignored.

### `register_flag_by_module`

register_flag_by_module(
        module_name: str,
        flag: tf.compat.v1.flags.Flag
    ) -> None

Records the module that defines a specific flag.

We keep track of which flag is defined by which module so that we can later sort the flags by module.

|     |     |
| --- | --- |
| Args |     |
| `module_name` | str, the name of a Python module. |
| `flag` | Flag, the Flag instance that is key to the module. |

### `register_flag_by_module_id`

register_flag_by_module_id(
        module_id: int,
        flag: tf.compat.v1.flags.Flag
    ) -> None

Records the module that defines a specific flag.

|     |     |
| --- | --- |
| Args |     |
| `module_id` | int, the ID of the Python module. |
| `flag` | Flag, the Flag instance that is key to the module. |

### `register_key_flag_for_module`

register_key_flag_for_module(
        module_name: str,
        flag: tf.compat.v1.flags.Flag
    ) -> None

Specifies that a flag is a key flag for a module.

|     |     |
| --- | --- |
| Args |     |
| `module_name` | str, the name of a Python module. |
| `flag` | Flag, the Flag instance that is key to the module. |

### `remove_flag_values`

remove_flag_values(
        flag_values: 'FlagValues | Iterable[str]'
    ) -> None

Remove flags that were previously appended from another FlagValues.

|     |     |
| --- | --- |
| Args |     |
| `flag_values` | FlagValues, the FlagValues instance containing flags to remove. |

### `set_default`

set_default(
        name: str, value: Any
    ) -> None

Changes the default value of the named flag object.

The flag's current value is also updated if the flag is currently using the default value, i.e. not specified in the command line, and not set by FLAGS.name = value.

|     |     |
| --- | --- |
| Args |     |
| `name` | str, the name of the flag to modify. |
| `value` | The new default value. |

|     |     |
| --- | --- |
| Raises |     |
| `UnrecognizedFlagError` | Raised when there is no registered flag named name. |
| `IllegalFlagValueError` | Raised when value is not valid. |

### `set_gnu_getopt`

set_gnu_getopt(
        gnu_getopt: bool = True
    ) -> None

Sets whether or not to use GNU style scanning.

GNU style allows mixing of flag and non-flag arguments. See [http://docs.python.org/library/getopt.html#getopt.gnu\_getopt](http://docs.python.org/library/getopt.html#getopt.gnu_getopt)

|     |     |
| --- | --- |
| Args |     |
| `gnu_getopt` | bool, whether or not to use GNU style scanning. |

### `unparse_flags`

unparse_flags() -> None

Unparses all flags to the point before any FLAGS(argv) was called.

### `validate_all_flags`

validate_all_flags() -> None

Verifies whether all flags pass validation.

|     |     |
| --- | --- |
| Raises |     |
| `AttributeError` | Raised if validators work with a non-existing flag. |
| `IllegalFlagValueError` | Raised if validation fails for at least one validator. |

### `write_help_in_xml_format`

write_help_in_xml_format(
        outfile: (TextIO | None) = None
    ) -> None

Outputs flag documentation in XML format.

|     |     |
| --- | --- |
| Args |     |
| `outfile` | File object we write to. Default None means sys.stdout. |

### `__call__`

__call__(
        argv: Sequence[str], known_only: bool = False
    ) -> list[str]

Parses flags from argv; stores parsed flags into this FlagValues object.

All unparsed arguments are returned.

|     |     |
| --- | --- |
| Args |     |
| `argv` | a tuple/list of strings. |
| `known_only` | bool, if True, parse and remove known flags; return the rest untouched. Unknown flags specified by --undefok are not returned. |

|     |
| --- |
| Returns |     |
| The list of arguments not parsed as options, including argv\[0\]. |     |

|     |     |
| --- | --- |
| Raises |     |
| `Error` | Raised on any parsing error. |
| `TypeError` | Raised on passing wrong type of arguments. |
| `ValueError` | Raised on flag value parsing error. |

### `__contains__`

__contains__(
        name: str
    ) -> bool

Returns True if name is a value (flag) in the dict.

### `__getitem__`

__getitem__(
        name: str
    ) -> tf.compat.v1.flags.Flag

Returns the Flag object for the flag --name.

### `__iter__`

__iter__() -> Iterator[str]

### `__len__`

__len__() -> int

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.