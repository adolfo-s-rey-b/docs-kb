[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/load_file_system_library#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/load_file_system_library)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/load_file_system_library?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/load_file_system_library#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/load_file_system_library#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/load_file_system_library#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.load\_file\_system\_library Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/load_file_system_library#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/load_file_system_library#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/load_file_system_library#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/load_library.py#L77-L97)

Loads a TensorFlow plugin, containing file system implementation. (deprecated)

tf.compat.v1.load_file_system_library(
        library_filename
    )

Pass `library_filename` to a platform-specific mechanism for dynamically loading a library. The rules for determining the exact location of the library are platform-specific and are not documented here.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `library_filename` | Path to the plugin. Relative or absolute filesystem path to a dynamic library file. |

|     |
| --- |
| Returns<br>------- |     |
| None. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `RuntimeError` | when unable to load the library. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.