[Skip to main content](https://www.tensorflow.org/api_docs/python/orbit/utils/create_loop_fn#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/orbit/utils/create_loop_fn)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/orbit/utils/create_loop_fn?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/orbit/utils/create_loop_fn#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/orbit/utils/create_loop_fn#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

orbit.utils.create\_loop\_fn Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/orbit/utils/create_loop_fn#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/orbit/utils/create_loop_fn#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/orbit/utils/loop_fns.py#L27-L89)

Creates a loop function driven by a Python `while` loop.

orbit.utils.create_loop_fn(
        step_fn
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `step_fn` | A function taking a nested structure of [`tf.data.Iterator`](https://www.tensorflow.org/api_docs/python/tf/data/Iterator)<br> or `DistributedIterator`. There are no constraints on the return value of the function (except that it must be compatible with any `reduce_fn` provided to the returned `loop_fn`). |

|     |
| --- |
| Returns<br>------- |     |
| A loop function taking required `iterator` and `num_steps` parameters, as well as optional `state` and `reduce_fn` parameters for accumulating state over multiple iterations of the loop. See the `loop_fn` definition below for additional details. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-02-13 UTC.