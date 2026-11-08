[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BaseListParser#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BaseListParser)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BaseListParser?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fflags%2FBaseListParser&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BaseListParser#methods)
    *   [flag\_type](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BaseListParser#flag_type)
        
    *   [parse](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BaseListParser#parse)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BaseListParser#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.flags.BaseListParser Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BaseListParser#methods)
    *   [flag\_type](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BaseListParser#flag_type)
        
    *   [parse](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BaseListParser#parse)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/BaseListParser#class-variables)
    

Base class for a parser of lists of strings.

Inherits From: [`ArgumentParser`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/ArgumentParser)

tf.compat.v1.flags.BaseListParser(
        token: (str | None) = None, name: (str | None) = None
    ) -> None

To extend, inherit from this class; from the subclass `__init__`, call::

super().__init__(token, name)

where token is a character used to tokenize, and name is a description of the separator.

Methods
-------

### `flag_type`

flag_type() -> str

See base class.

### `parse`

parse(
        argument: str
    ) -> list[str]

See base class.

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| syntactic\_help | `''` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.