[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/gfile/join#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/gfile/join)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/gfile/join?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/gfile/join#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/gfile/join#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.gfile.join Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/gfile/join#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/gfile/join#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/lib/io/file_io.py#L781-L816)

Join one or more path components intelligently.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.io.gfile.join`](https://www.tensorflow.org/api_docs/python/tf/io/gfile/join)

tf.io.gfile.join(
        path, *paths
    )

TensorFlow specific filesystems will be joined like a url (using "/" as the path seperator) on all platforms:

On Windows or Linux/Unix-like:

>>> tf.io.gfile.join("gcs://folder", "file.py")
    'gcs://folder/file.py'

    tf.io.gfile.join("ram://folder", "file.py")

But the native filesystem is handled just like os.path.join:

    path = tf.io.gfile.join("folder", "file.py")

|     |     |
| --- | --- |
| Args<br>---- |     |
| `path` | string, path to a directory |
| `paths` | string, additional paths to concatenate |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `path` | the joined path. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.