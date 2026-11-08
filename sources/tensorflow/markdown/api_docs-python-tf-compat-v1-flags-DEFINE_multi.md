[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_multi#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.flags.DEFINE\_multi Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

Registers a generic MultiFlag that parses its args with a given parser.

tf.compat.v1.flags.DEFINE_multi(
        parser,
        serializer,
        name,
        default,
        help,
        flag_values=_flagvalues.FLAGS,
        module_name=None,
        required=False,
        **args
    )

Auxiliary function. Normal users should NOT use it directly.

Developers who need to create their own 'Parser' classes for options which can appear multiple times can call this module function to register their flags.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `parser` | ArgumentParser, used to parse the flag arguments. |
| `serializer` | ArgumentSerializer, the flag serializer instance. |
| `name` | str, the flag name. |
| `default` | Union\[Iterable\[T\], str, None\], the default value of the flag. If the value is text, it will be parsed as if it was provided from the command line. If the value is a non-string iterable, it will be iterated over to create a shallow copy of the values. If it is None, it is left as-is. |
| `help` | str, the help message. |
| `flag_values` | :class:`FlagValues`, the FlagValues instance with which the flag will be registered. This should almost never need to be overridden. |
| `module_name` | A string, the name of the Python module declaring this flag. If not provided, it will be computed using the stack trace of this call. |
| `required` | bool, is this a required flag. This must be used as a keyword argument. |
| `**args` | Dictionary with extra keyword args that are passed to the `Flag.__init__`. |

|     |
| --- |
| Returns<br>------- |     |
| a handle to defined flag. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.