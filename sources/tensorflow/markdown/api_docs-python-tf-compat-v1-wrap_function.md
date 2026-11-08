[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/wrap_function#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/wrap_function)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/wrap_function?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/wrap_function#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/wrap_function#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/wrap_function#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.wrap\_function Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/wrap_function#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/wrap_function#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/wrap_function#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/eager/wrap_function.py#L598-L669)

Wraps the TF 1.x function fn into a graph function.

tf.compat.v1.wrap_function(
        fn, signature, name=None
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Migrate the SavedModel workflow](https://www.tensorflow.org/guide/migrate/saved_model) |

The python function `fn` will be called once with symbolic arguments specified in the `signature`, traced, and turned into a graph function. Any variables created by `fn` will be owned by the object returned by `wrap_function`. The resulting graph function can be called with tensors which match the signature.

def f(x, do_add):
      v = tf.Variable(5.0)
      if do_add:
        op = v.assign_add(x)
      else:
        op = v.assign_sub(x)
      with tf.control_dependencies([op]):
        return v.read_value()
    
    f_add = tf.compat.v1.wrap_function(f, [tf.TensorSpec((), tf.float32), True])
    
    assert float(f_add(1.0)) == 6.0
    assert float(f_add(1.0)) == 7.0
    
    # Can call tf.compat.v1.wrap_function again to get a new trace, a new set
    # of variables, and possibly different non-template arguments.
    f_sub= tf.compat.v1.wrap_function(f, [tf.TensorSpec((), tf.float32), False])
    
    assert float(f_sub(1.0)) == 4.0
    assert float(f_sub(1.0)) == 3.0

Both [`tf.compat.v1.wrap_function`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/wrap_function)
 and [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 create a callable TensorFlow graph. But while [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 runs all stateful operations (e.g. [`tf.print`](https://www.tensorflow.org/api_docs/python/tf/print)
) and sequences operations to provide the same semantics as eager execution, `wrap_function` is closer to the behavior of `session.run` in TensorFlow 1.x. It will not run any operations unless they are required to compute the function's outputs, either through a data dependency or a control dependency. Nor will it sequence operations.

Unlike [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
, `wrap_function` will only trace the Python function once. As with placeholders in TF 1.x, shapes and dtypes must be provided to `wrap_function`'s `signature` argument.

Since it is only traced once, variables and state may be created inside the function and owned by the function wrapper object.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `fn` | python function to be wrapped |
| `signature` | the placeholder and python arguments to be passed to the wrapped function |
| `name` | Optional. The name of the function. |

|     |
| --- |
| Returns<br>------- |     |
| the wrapped graph function. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.