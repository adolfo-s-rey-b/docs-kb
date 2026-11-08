[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/autograph/experimental/set_loop_options#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/autograph/experimental/set_loop_options)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/autograph/experimental/set_loop_options?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Usage](https://www.tensorflow.org/api_docs/python/tf/autograph/experimental/set_loop_options#usage)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/autograph/experimental/set_loop_options#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.autograph.experimental.set\_loop\_options Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================================

*   On this page
*   [Usage](https://www.tensorflow.org/api_docs/python/tf/autograph/experimental/set_loop_options#usage)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/autograph/experimental/set_loop_options#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/autograph/lang/directives.py#L45-L94)

Specifies additional arguments to be passed to the enclosing while\_loop.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.autograph.experimental.set_loop_options`](https://www.tensorflow.org/api_docs/python/tf/autograph/experimental/set_loop_options)

tf.autograph.experimental.set_loop_options(
        parallel_iterations=UNSPECIFIED,
        swap_memory=UNSPECIFIED,
        maximum_iterations=UNSPECIFIED,
        shape_invariants=UNSPECIFIED
    )

The parameters apply to and only to the immediately enclosing loop. It only has effect if the loop is staged as a TF while\_loop; otherwise the parameters have no effect.

|     |
| --- |
| Usage<br>----- |     |
| >>> @tf.function(autograph=True)<br>    ... def f():<br>    ...   n = 0<br>    ...   for i in tf.range(10):<br>    ...     tf.autograph.experimental.set_loop_options(maximum_iterations=3)<br>    ...     n += 1<br>    ...   return n<br><br>    @tf.function(autograph=True) |     |

Also see tf.while\_loop.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `parallel_iterations` | The maximum number of iterations allowed to run in parallel at any given time. Note that this does not guarantee parallel execution. |
| `swap_memory` | Whether to store intermediate values needed for gradients on the CPU instead of GPU. |
| `maximum_iterations` | Allows limiting the total number of iterations executed by the loop. |
| `shape_invariants` | Allows controlling the argument with the same name passed to tf.while\_loop. Unlike tf.while\_loop, this is a list of `(tensor, shape)` pairs. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.