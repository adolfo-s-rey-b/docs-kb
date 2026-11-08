[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/load_library#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/load_library)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/load_library?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/load_library#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/load_library#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/load_library#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.load\_library Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/load_library#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/load_library#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/load_library#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/load_library.py#L120-L157)

Loads a TensorFlow plugin.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.load_library`](https://www.tensorflow.org/api_docs/python/tf/load_library)

tf.load_library(
        library_location
    )

"library\_location" can be a path to a specific shared object, or a folder. If it is a folder, all shared objects that are named "libtfkernel\*" will be loaded. When the library is loaded, kernels registered in the library via the `REGISTER_*` macros are made available in the TensorFlow process.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `library_location` | Path to the plugin or the folder of plugins. Relative or absolute filesystem path to a dynamic library file or folder. |

|     |
| --- |
| Returns<br>------- |     |
| None |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `OSError` | When the file to be loaded is not found. |
| `RuntimeError` | when unable to load the library. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.