[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/test/is_built_with_rocm#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/test/is_built_with_rocm)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/test/is_built_with_rocm?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.test.is\_built\_with\_rocm Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/platform/test.py#L110-L128)

Returns whether TensorFlow was built with ROCm (GPU) support.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.test.is_built_with_rocm`](https://www.tensorflow.org/api_docs/python/tf/test/is_built_with_rocm)

tf.test.is_built_with_rocm()

This method should only be used in tests written with [`tf.test.TestCase`](https://www.tensorflow.org/api_docs/python/tf/test/TestCase)
. A typical usage is to skip tests that should only run with ROCm (GPU).

    class MyTest(tf.test.TestCase):

TensorFlow official binary is NOT built with ROCm.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.