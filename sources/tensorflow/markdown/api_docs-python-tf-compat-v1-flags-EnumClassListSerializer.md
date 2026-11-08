[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/EnumClassListSerializer#main-content)

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
    

tf.compat.v1.flags.EnumClassListSerializer Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

A serializer for :class:`MultiEnumClass` flags.

Inherits From: [`ListSerializer`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/ListSerializer)
, [`ArgumentSerializer`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/ArgumentSerializer)

tf.compat.v1.flags.EnumClassListSerializer(
        list_sep: str, **kwargs
    ) -> None

This serializer simply joins the output of `EnumClassSerializer` using a provided separator.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `list_sep` | String to be used as a separator when serializing |
| `**kwargs` | Keyword arguments to the `EnumClassSerializer` used to serialize individual values. |

Methods
-------

### `serialize`

serialize(
        value: (_ET | list[_ET])
    ) -> str

See base class.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.