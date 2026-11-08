[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/DEFINE_multi_float#main-content)

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
    

tf.compat.v1.flags.DEFINE\_multi\_float Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

Registers a flag whose value can be a list of arbitrary floats.

tf.compat.v1.flags.DEFINE_multi_float(
        name,
        default,
        help,
        lower_bound=None,
        upper_bound=None,
        flag_values=_flagvalues.FLAGS,
        required=False,
        **args
    )

Use the flag on the command line multiple times to place multiple float values into the list. The 'default' may be a single float (which will be converted into a single-element list) or a list of floats.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `name` | str, the flag name. |
| `default` | Union\[Iterable\[float\], str, None\], the default value of the flag; see `DEFINE_multi`. |
| `help` | str, the help message. |
| `lower_bound` | float, min values of the flag. |
| `upper_bound` | float, max values of the flag. |
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

Last updated 2026-10-31 UTC.