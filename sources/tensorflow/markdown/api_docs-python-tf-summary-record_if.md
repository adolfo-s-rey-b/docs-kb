[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/summary/record_if#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/summary/record_if)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/summary/record_if?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/summary/record_if#args)
    
*   [Yields](https://www.tensorflow.org/api_docs/python/tf/summary/record_if#yields)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.summary.record\_if Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/summary/record_if#args)
    
*   [Yields](https://www.tensorflow.org/api_docs/python/tf/summary/record_if#yields)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/summary_ops_v2.py#L161-L188)

Sets summary recording on or off per the provided boolean value.

@tf_contextlib.contextmanager

The provided value can be a python boolean, a scalar boolean Tensor, or or a callable providing such a value; if a callable is passed it will be invoked on-demand to determine whether summary writing will occur. Note that when calling record\_if() in an eager mode context, if you intend to provide a varying condition like `step % 100 == 0`, you must wrap this in a callable to avoid immediate eager evaluation of the condition. In particular, using a callable is the only way to have your condition evaluated as part of the traced body of an @tf.function that is invoked from within the `record_if()` context.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `condition` | can be True, False, a bool Tensor, or a callable providing such. |

|     |
| --- |
| Yields<br>------ |     |
| Returns a context manager that sets this value on enter and restores the previous value on exit. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.