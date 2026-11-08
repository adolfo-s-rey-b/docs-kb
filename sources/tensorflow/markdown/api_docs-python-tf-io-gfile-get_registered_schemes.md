[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/gfile/get_registered_schemes#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/gfile/get_registered_schemes)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/gfile/get_registered_schemes?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/gfile/get_registered_schemes#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/io/gfile/get_registered_schemes#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.gfile.get\_registered\_schemes Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/gfile/get_registered_schemes#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/io/gfile/get_registered_schemes#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/lib/io/file_io.py#L980-L1004)

Returns the currently registered filesystem schemes.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.io.gfile.get_registered_schemes`](https://www.tensorflow.org/api_docs/python/tf/io/gfile/get_registered_schemes)

tf.io.gfile.get_registered_schemes()

The [`tf.io.gfile`](https://www.tensorflow.org/api_docs/python/tf/io/gfile)
 APIs, in addition to accepting traditional filesystem paths, also accept file URIs that begin with a scheme. For example, the local filesystem path `/tmp/tf` can also be addressed as `file:///tmp/tf`. In this case, the scheme is `file`, followed by `://` and then the path, according to [URI syntax](https://datatracker.ietf.org/doc/html/rfc3986#section-3)
.

This function returns the currently registered schemes that will be recognized by [`tf.io.gfile`](https://www.tensorflow.org/api_docs/python/tf/io/gfile)
 APIs. This includes both built-in schemes and those registered by other TensorFlow filesystem implementations, for example those provided by [TensorFlow I/O](https://github.com/tensorflow/io)
.

The empty string is always included, and represents the "scheme" for regular local filesystem paths.

|     |
| --- |
| Returns<br>------- |     |
| List of string schemes, e.g. `['', 'file', 'ram']`, in arbitrary order. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| [`errors.OpError`](https://www.tensorflow.org/api_docs/python/tf/errors/OpError) | If the operation fails. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.