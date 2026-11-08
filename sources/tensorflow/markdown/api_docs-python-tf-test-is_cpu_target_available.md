[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/test/is_cpu_target_available#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/test/is_cpu_target_available)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/test/is_cpu_target_available?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/test/is_cpu_target_available#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/test/is_cpu_target_available#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.test.is\_cpu\_target\_available Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/test/is_cpu_target_available#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/test/is_cpu_target_available#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/platform/test.py#L194-L220)

Indicates whether TensorFlow was built with support for a given CPU target.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.test.is_cpu_target_available`](https://www.tensorflow.org/api_docs/python/tf/test/is_cpu_target_available)

tf.test.is_cpu_target_available(
        target
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `target` | The name of the CPU target whose support to check for. |

|     |
| --- |
| Returns<br>------- |     |
| A boolean indicating whether TensorFlow was built with support for the given CPU target. |     |

This method should only be used in tests written with [`tf.test.TestCase`](https://www.tensorflow.org/api_docs/python/tf/test/TestCase)
. A typical usage is to skip tests that should only run with a given target.

    class MyTest(tf.test.TestCase):

... @tf.function(jit\_compile=True) ... def add(x, y): ... return tf.math.add(x, y) ... ... self.assertEqual(add(tf.ones(()), tf.ones(())), 2.0)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.