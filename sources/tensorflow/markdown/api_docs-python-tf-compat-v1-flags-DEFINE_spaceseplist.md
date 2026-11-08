[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_spaceseplist#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_spaceseplist)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_spaceseplist?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_spaceseplist#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_spaceseplist#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.flags.DEFINE\_spaceseplist Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_spaceseplist#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_spaceseplist#returns)
    

Registers a flag whose value is a whitespace-separated list of strings.

tf.compat.v1.flags.DEFINE_spaceseplist(
        name,
        default,
        help,
        comma_compat=False,
        flag_values=_flagvalues.FLAGS,
        required=False,
        **args
    )

Any whitespace can be used as a separator.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `name` | str, the flag name. |
| `default` | list\|str\|None, the default value of the flag. |
| `help` | str, the help message. |
| `comma_compat` | bool - Whether to support comma as an additional separator. If false then only whitespace is supported. This is intended only for backwards compatibility with flags that used to be comma-separated. |
| `flag_values` | :class:`FlagValues`, the FlagValues instance with which the flag will be registered. This should almost never need to be overridden. |
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

Last updated 2024-04-26 UTC.