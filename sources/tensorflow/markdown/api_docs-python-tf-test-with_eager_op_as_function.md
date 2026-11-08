[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/test/with_eager_op_as_function#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/test/with_eager_op_as_function)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/test/with_eager_op_as_function?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/test/with_eager_op_as_function#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/test/with_eager_op_as_function#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.test.with\_eager\_op\_as\_function Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/test/with_eager_op_as_function#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/test/with_eager_op_as_function#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L1304-L1325)

Returns the same class. This will be removed once all usages are removed.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.test.with_eager_op_as_function`](https://www.tensorflow.org/api_docs/python/tf/test/with_eager_op_as_function)

tf.test.with_eager_op_as_function(
        cls: Optional[type[_T]] = None, only_as_function: bool = False
    ) -> Union[Callable[[type[_T]], type[_T]], type[_T]]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `cls` | class to decorate. |
| `only_as_function` | unused argument. |

|     |
| --- |
| Returns<br>------- |     |
| cls |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.