[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/resource_loader/get_root_dir_with_all_resources#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/resource_loader/get_root_dir_with_all_resources)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/resource_loader/get_root_dir_with_all_resources?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/resource_loader/get_root_dir_with_all_resources#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.resource\_loader.get\_root\_dir\_with\_all\_resources Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================================================

*   On this page
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/resource_loader/get_root_dir_with_all_resources#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/platform/resource_loader.py#L59-L96)

Get a root directory containing all the data attributes in the build rule.

tf.compat.v1.resource_loader.get_root_dir_with_all_resources()

|     |
| --- |
| Returns<br>------- |     |
| The path to the specified file present in the data attribute of py\_test or py\_binary. Falls back to returning the same as get\_data\_files\_path if it fails to detect a bazel runfiles directory. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.