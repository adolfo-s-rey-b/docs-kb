[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/sysconfig/get_compile_flags#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/sysconfig/get_compile_flags)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/sysconfig/get_compile_flags?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sysconfig/get_compile_flags#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.sysconfig.get\_compile\_flags Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sysconfig/get_compile_flags#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/platform/sysconfig.py#L56-L88)

Returns the compilation flags for compiling with TensorFlow.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.sysconfig.get_compile_flags`](https://www.tensorflow.org/api_docs/python/tf/sysconfig/get_compile_flags)

tf.sysconfig.get_compile_flags()

The returned list of arguments can be passed to the compiler for compiling against TensorFlow headers. The result is platform dependent.

For example, on a typical Linux system with Python 3.7 the following command prints `['-I/usr/local/lib/python3.7/dist-packages/tensorflow/include', '-D_GLIBCXX_USE_CXX11_ABI=1', '-DEIGEN_MAX_ALIGN_BYTES=64']`

    print(tf.sysconfig.get_compile_flags())

|     |
| --- |
| Returns<br>------- |     |
| A list of strings for the compiler flags. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.