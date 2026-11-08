[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/sysconfig/get_build_info#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/sysconfig/get_build_info)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/sysconfig/get_build_info?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fsysconfig%2Fget_build_info&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sysconfig/get_build_info#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.sysconfig.get\_build\_info Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sysconfig/get_build_info#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/platform/sysconfig.py#L119-L141)

Get a dictionary describing TensorFlow's build environment.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.sysconfig.get_build_info`](https://www.tensorflow.org/api_docs/python/tf/sysconfig/get_build_info)

tf.sysconfig.get_build_info()

Values are generated when TensorFlow is compiled, and are static for each TensorFlow package. The return value is a dictionary with string keys such as:

*   cuda\_version
*   cudnn\_version
*   is\_cuda\_build
*   is\_rocm\_build
*   msvcp\_dll\_names
*   nvcuda\_dll\_name
*   cudart\_dll\_name
*   cudnn\_dll\_name

Note that the actual keys and values returned by this function is subject to change across different versions of TensorFlow or across platforms.

|     |
| --- |
| Returns<br>------- |     |
| A Dictionary describing TensorFlow's build environment. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.