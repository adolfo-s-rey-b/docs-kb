[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/resource_loader/get_path_to_datafile#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/resource_loader/get_path_to_datafile)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/resource_loader/get_path_to_datafile?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/resource_loader/get_path_to_datafile#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/resource_loader/get_path_to_datafile#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/resource_loader/get_path_to_datafile#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.resource\_loader.get\_path\_to\_datafile Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/resource_loader/get_path_to_datafile#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/resource_loader/get_path_to_datafile#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/resource_loader/get_path_to_datafile#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/platform/resource_loader.py#L99-L126)

Get the path to the specified file in the data dependencies.

tf.compat.v1.resource_loader.get_path_to_datafile(
        path
    )

The path is relative to tensorflow/

|     |     |
| --- | --- |
| Args<br>---- |     |
| `path` | a string resource path relative to tensorflow/ |

|     |
| --- |
| Returns<br>------- |     |
| The path to the specified file present in the data attribute of py\_test or py\_binary. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `IOError` | If the path is not found, or the resource can't be opened. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.