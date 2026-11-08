[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fflags&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.compat.v1.flags Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags#functions)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/platform/flags.py)

Import router for absl.flags. See [https://github.com/abseil/abseil-py](https://github.com/abseil/abseil-py)

Classes
-------

[`class ArgumentParser`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/ArgumentParser)
: Base class used to parse and convert arguments.

[`class ArgumentSerializer`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/ArgumentSerializer)
: Base class for generating string representations of a flag value.

[`class BaseListParser`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BaseListParser)
: Base class for a parser of lists of strings.

[`class BooleanFlag`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BooleanFlag)
: Basic boolean flag.

[`class BooleanParser`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BooleanParser)
: Parser of boolean values.

[`class CantOpenFlagFileError`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/CantOpenFlagFileError)
: Raised when flagfile fails to open.

[`class CsvListSerializer`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/CsvListSerializer)
: Base class for generating string representations of a flag value.

[`class DuplicateFlagError`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DuplicateFlagError)
: Raised if there is a flag naming conflict.

[`class EnumClassFlag`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumClassFlag)
: Basic enum flag; its value is an enum class's member.

[`class EnumClassListSerializer`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumClassListSerializer)
: A serializer for :class:`MultiEnumClass` flags.

[`class EnumClassParser`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumClassParser)
: Parser of an Enum class member.

[`class EnumClassSerializer`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumClassSerializer)
: Class for generating string representations of an enum class flag value.

[`class EnumFlag`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumFlag)
: Basic enum flag; its value can be any string from list of enum\_values.

[`class EnumParser`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumParser)
: Parser of a string enum value (a string value from a given set).

[`class Error`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/Error)
: The base class for all flags errors.

[`class Flag`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/Flag)
: Information about a command-line flag.

[`class FlagHolder`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagHolder)
: Holds a defined flag.

[`class FlagNameConflictsWithMethodError`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagNameConflictsWithMethodError)
: Raised when a flag name conflicts with :class:`FlagValues` methods.

[`class FlagValues`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FlagValues)
: Registry of :class:`~absl.flags.Flag` objects.

[`class FloatParser`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FloatParser)
: Parser of floating point values.

[`class IllegalFlagValueError`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/IllegalFlagValueError)
: Raised when the flag command line argument is illegal.

[`class IntegerParser`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/IntegerParser)
: Parser of an integer value.

[`class ListParser`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/ListParser)
: Parser for a comma-separated list of strings.

[`class ListSerializer`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/ListSerializer)
: Base class for generating string representations of a flag value.

[`class MultiEnumClassFlag`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/MultiEnumClassFlag)
: A multi\_enum\_class flag.

[`class MultiFlag`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/MultiFlag)
: A flag that can appear multiple time on the command-line.

[`class UnparsedFlagAccessError`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/UnparsedFlagAccessError)
: Raised when accessing the flag value from unparsed :class:`FlagValues`.

[`class UnrecognizedFlagError`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/UnrecognizedFlagError)
: Raised when a flag is unrecognized.

[`class ValidationError`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/ValidationError)
: Raised when flag validator constraint is not satisfied.

[`class WhitespaceSeparatedListParser`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/WhitespaceSeparatedListParser)
: Parser for a whitespace-separated list of strings.

Functions
---------

[`DEFINE(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE)
: Registers a generic Flag object.

[`DEFINE_alias(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_alias)
: Defines an alias flag for an existing one.

[`DEFINE_bool(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_bool)
: Registers a boolean flag.

[`DEFINE_boolean(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_bool)
: Registers a boolean flag.

[`DEFINE_enum(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_enum)
: Registers a flag whose value can be any string from enum\_values.

[`DEFINE_enum_class(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_enum_class)
: Registers a flag whose value can be the name of enum members.

[`DEFINE_flag(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_flag)
: Registers a :class:`Flag` object with a :class:`FlagValues` object.

[`DEFINE_float(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_float)
: Registers a flag whose value must be a float.

[`DEFINE_integer(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_integer)
: Registers a flag whose value must be an integer.

[`DEFINE_list(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_list)
: Registers a flag whose value is a comma-separated list of strings.

[`DEFINE_multi(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_multi)
: Registers a generic MultiFlag that parses its args with a given parser.

[`DEFINE_multi_enum(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_multi_enum)
: Registers a flag whose value can be a list strings from enum\_values.

[`DEFINE_multi_enum_class(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_multi_enum_class)
: Registers a flag whose value can be a list of enum members.

[`DEFINE_multi_float(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_multi_float)
: Registers a flag whose value can be a list of arbitrary floats.

[`DEFINE_multi_integer(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_multi_integer)
: Registers a flag whose value can be a list of arbitrary integers.

[`DEFINE_multi_string(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_multi_string)
: Registers a flag whose value can be a list of any strings.

[`DEFINE_spaceseplist(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_spaceseplist)
: Registers a flag whose value is a whitespace-separated list of strings.

[`DEFINE_string(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_string)
: Registers a flag whose value can be any string.

[`FLAGS(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FLAGS)
: Registry of :class:`~absl.flags.Flag` objects.

[`adopt_module_key_flags(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/adopt_module_key_flags)
: Declares that all flags key to a module are key to the current module.

[`declare_key_flag(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/declare_key_flag)
: Declares one flag as key to the current module.

[`disclaim_key_flags(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/disclaim_key_flags)
: Declares that the current module will not define any more key flags.

[`doc_to_help(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/doc_to_help)
: Takes a **doc** string and reformats it as help.

[`flag_dict_to_args(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/flag_dict_to_args)
: Convert a dict of values into process call parameters.

[`get_help_width(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/get_help_width)
: Returns the integer width of help lines that is used in TextWrap.

[`mark_bool_flags_as_mutual_exclusive(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/mark_bool_flags_as_mutual_exclusive)
: Ensures that only one flag among flag\_names is True.

[`mark_flag_as_required(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/mark_flag_as_required)
: Ensures that flag is not None during program execution.

[`mark_flags_as_mutual_exclusive(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/mark_flags_as_mutual_exclusive)
: Ensures that only one flag among flag\_names is not None.

[`mark_flags_as_required(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/mark_flags_as_required)
: Ensures that flags are not None during program execution.

[`multi_flags_validator(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/multi_flags_validator)
: A function decorator for defining a multi-flag validator.

[`override_value(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/override_value)
: Overrides the value of the provided flag.

[`register_multi_flags_validator(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/register_multi_flags_validator)
: Adds a constraint to multiple flags.

[`register_validator(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/register_validator)
: Adds a constraint, which will be enforced during program execution.

[`set_default(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/set_default)
: Changes the default value of the provided flag object.

[`text_wrap(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/text_wrap)
: Wraps a given text to a maximum line length and returns it.

[`validator(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/validator)
: A function decorator for defining a flag validator.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.