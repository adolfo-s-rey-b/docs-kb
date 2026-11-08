[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/CsvListSerializer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/CsvListSerializer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/CsvListSerializer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fflags%2FCsvListSerializer&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/CsvListSerializer#methods)
    *   [serialize](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/CsvListSerializer#serialize)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.flags.CsvListSerializer Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/CsvListSerializer#methods)
    *   [serialize](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/CsvListSerializer#serialize)
        

Base class for generating string representations of a flag value.

Inherits From: [`ListSerializer`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/ListSerializer)
, [`ArgumentSerializer`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/ArgumentSerializer)

tf.compat.v1.flags.CsvListSerializer(
        list_sep: str
    ) -> None

Methods
-------

### `serialize`

serialize(
        value: list[str]
    ) -> str

Serializes a list as a CSV string or unicode.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.