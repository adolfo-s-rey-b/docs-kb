[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FLAGS#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FLAGS)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/FLAGS?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.flags.FLAGS Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

Registry of :class:`~absl.flags.Flag` objects.

tf.compat.v1.flags.FLAGS(
        *args, **kwargs
    )

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

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.