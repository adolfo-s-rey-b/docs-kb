[Skip to main content](https://www.tensorflow.org/api_docs/python/orbit/utils/LoopFnWithSummaries#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

orbit.utils.LoopFnWithSummaries Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/orbit/utils/loop_fns.py#L199-L212)

Implements a two-program approach for optimizing summaries on TPU.

Inherits From: [`OptionalSummariesFunction`](https://www.tensorflow.org/api_docs/python/orbit/utils/OptionalSummariesFunction)

orbit.utils.LoopFnWithSummaries(
        function, **tf_function_kwargs
    )

This version works with the result of `create_tf_while_loop_fn`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `function` | The underlying function to wrap. |
| `**tf_function_kwargs` | Additional arguments to pass to [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br>. |

Methods
-------

### `__call__`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/utils/loop_fns.py#L205-L212)

__call__(
        iterator, num_steps
    )

Call self as a function.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-02-13 UTC.