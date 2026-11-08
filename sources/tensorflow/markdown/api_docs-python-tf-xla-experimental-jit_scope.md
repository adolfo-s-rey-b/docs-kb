[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/xla/experimental/jit_scope#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/xla/experimental/jit_scope)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/xla/experimental/jit_scope?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Example usage](https://www.tensorflow.org/api_docs/python/tf/xla/experimental/jit_scope#example-usage)
    
*   [For example](https://www.tensorflow.org/api_docs/python/tf/xla/experimental/jit_scope#for-example)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/xla/experimental/jit_scope#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/xla/experimental/jit_scope#raises)
    
*   [Yields](https://www.tensorflow.org/api_docs/python/tf/xla/experimental/jit_scope#yields)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.xla.experimental.jit\_scope Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Example usage](https://www.tensorflow.org/api_docs/python/tf/xla/experimental/jit_scope#example-usage)
    
*   [For example](https://www.tensorflow.org/api_docs/python/tf/xla/experimental/jit_scope#for-example)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/xla/experimental/jit_scope#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/xla/experimental/jit_scope#raises)
    
*   [Yields](https://www.tensorflow.org/api_docs/python/tf/xla/experimental/jit_scope#yields)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/compiler/xla/jit.py#L36-L156)

Enable or disable JIT compilation of operators within the scope.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.xla.experimental.jit_scope`](https://www.tensorflow.org/api_docs/python/tf/xla/experimental/jit_scope)

@contextlib.contextmanager

The compilation is a hint and only supported on a best-effort basis.

|     |
| --- |
| Example usage<br>------------- |     |
| with tf.xla.experimental.jit_scope():<br>      c = tf.matmul(a, b)  # compiled<br>    with tf.xla.experimental.jit_scope(compile_ops=False):<br>      d = tf.matmul(a, c)  # not compiled<br>    with tf.xla.experimental.jit_scope(<br>        compile_ops=lambda node_def: 'matmul' in node_def.op.lower()):<br>      e = tf.matmul(a, b) + d  # matmul is compiled, the addition is not. |     |

Example of `separate_compiled_gradients`:

  # In the example below, the computations for f, g and h will all be compiled
      # in separate scopes.
      with tf.xla.experimental.jit_scope(
          separate_compiled_gradients=True):
        f = tf.matmul(a, b)
      g = tf.gradients([f], [a, b], name='mygrads1')
      h = tf.gradients([f], [a, b], name='mygrads2')

Ops that are not in the scope may be clustered and compiled with ops in the scope with `compile_ops=True`, while the ops in the scope with `compile_ops=False` will never be compiled.

|     |
| --- |
| For example<br>----------- |     |
| # In the example below, x and loss may be clustered and compiled together,<br>    # while y will not be compiled.<br>    with tf.xla.experimental.jit_scope():<br>      x = tf.matmul(a, b)<br>    with tf.xla.experimental.jit_scope(compile_ops=False):<br>      y = tf.matmul(c, d)<br>    loss = x + y |     |

If you want to only compile the ops in the scope with `compile_ops=True`, consider adding an outer `jit_scope(compile_ops=False)`:

  # In the example below, only x will be compiled.
      with tf.xla.experimental.jit_scope(compile_ops=False):
        with tf.xla.experimental.jit_scope():
          x = tf.matmul(a, b)
        y = tf.matmul(c, d)
        loss = x + y

|     |     |
| --- | --- |
| Args<br>---- |     |
| `compile_ops` | Whether to enable or disable compilation in the scope. Either a Python bool, or a callable that accepts the parameter `node_def` and returns a python bool. |
| `separate_compiled_gradients` | If true put each gradient subgraph into a separate compilation scope. This gives fine-grained control over which portions of the graph will be compiled as a single unit. Compiling gradients separately may yield better performance for some graphs. The scope is named based on the scope of the forward computation as well as the name of the gradients. As a result, the gradients will be compiled in a scope that is separate from both the forward computation, and from other gradients. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `RuntimeError` | if called when eager execution is enabled. |

|     |
| --- |
| Yields<br>------ |     |
| The current scope, enabling or disabling compilation. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.