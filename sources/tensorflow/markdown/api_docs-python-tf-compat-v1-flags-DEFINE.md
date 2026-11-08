[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.flags.DEFINE Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE#returns)
    

Registers a generic Flag object.

tf.compat.v1.flags.DEFINE(
        parser,
        name,
        default,
        help,
        flag_values=_flagvalues.FLAGS,
        serializer=None,
        module_name=None,
        required: bool = False,
        **args
    )

Auxiliary function: clients should use the specialized `DEFINE_<type>` function instead.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `parser` | :class:`ArgumentParser`, used to parse the flag arguments. |
| `name` | str, the flag name. |
| `default` | The default value of the flag. |
| `help` | str, the help message. |
| `flag_values` | :class:`FlagValues`, the FlagValues instance with which the flag will be registered. This should almost never need to be overridden. |
| `serializer` | :class:`ArgumentSerializer`, the flag serializer instance. |
| `module_name` | str, the name of the Python module declaring this flag. If not provided, it will be computed using the stack trace of this call. |
| `required` | bool, is this a required flag. This must be used as a keyword argument. |
| `**args` | dict, the extra keyword args that are passed to `Flag.__init__`. |

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