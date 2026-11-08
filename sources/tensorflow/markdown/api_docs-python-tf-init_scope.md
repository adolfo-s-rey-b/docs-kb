[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/init_scope#main-content)

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
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.init\_scope Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/ops.py#L4758-L4860)

A context manager that lifts ops out of control-flow scopes and function-building graphs.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.init_scope`](https://www.tensorflow.org/api_docs/python/tf/init_scope)

@tf_contextlib.contextmanager

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Better performance with tf.function](https://www.tensorflow.org/guide/function) | *   [Preprocessing data with TensorFlow Transform](https://www.tensorflow.org/tfx/tutorials/transform/census)<br>    <br>*   [](https://www.tensorflow.org/tfx/transform/get_started) |

There is often a need to lift variable initialization ops out of control-flow scopes, function-building graphs, and gradient tapes. Entering an `init_scope` is a mechanism for satisfying these desiderata. In particular, entering an `init_scope` has three effects:

(1) All control dependencies are cleared the moment the scope is entered; this is equivalent to entering the context manager returned from `control_dependencies(None)`, which has the side-effect of exiting control-flow scopes like [`tf.cond`](https://www.tensorflow.org/api_docs/python/tf/cond)
 and [`tf.while_loop`](https://www.tensorflow.org/api_docs/python/tf/while_loop)
.

(2) All operations that are created while the scope is active are lifted into the lowest context on the `context_stack` that is not building a graph function. Here, a context is defined as either a graph or an eager context. Every context switch, i.e., every installation of a graph as the default graph and every switch into eager mode, is logged in a thread-local stack called `context_switches`; the log entry for a context switch is popped from the stack when the context is exited. Entering an `init_scope` is equivalent to crawling up `context_switches`, finding the first context that is not building a graph function, and entering it. A caveat is that if graph mode is enabled but the default graph stack is empty, then entering an `init_scope` will simply install a fresh graph as the default one.

(3) The gradient tape is paused while the scope is active.

When eager execution is enabled, code inside an init\_scope block runs with eager execution enabled even when tracing a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
. For example:

tf.compat.v1.enable_eager_execution()
    
    @tf.function
    def func():
      # A function constructs TensorFlow graphs,
      # it does not execute eagerly.
      assert not tf.executing_eagerly()
      with tf.init_scope():
        # Initialization runs with eager execution enabled
        assert tf.executing_eagerly()

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `RuntimeError` | if graph state is incompatible with this initialization. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.