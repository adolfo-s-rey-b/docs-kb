[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/debugging/enable_check_numerics#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/debugging/enable_check_numerics)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/debugging/enable_check_numerics?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/debugging/enable_check_numerics#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.debugging.enable\_check\_numerics Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/debugging/enable_check_numerics#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/debug/lib/check_numerics_callback.py#L336-L442)

Enable tensor numerics checking in an eager/graph unified fashion.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.debugging.enable_check_numerics`](https://www.tensorflow.org/api_docs/python/tf/debugging/enable_check_numerics)

tf.debugging.enable_check_numerics(
        stack_height_limit=30, path_length_limit=50
    )

The numerics checking mechanism will cause any TensorFlow eager execution or graph execution to error out as soon as an op's output tensor contains infinity or NaN.

This method is idempotent. Calling it multiple times has the same effect as calling it once.

This method takes effect only on the thread in which it is called.

When a op's float-type output tensor contains any Infinity or NaN, an [`tf.errors.InvalidArgumentError`](https://www.tensorflow.org/api_docs/python/tf/errors/InvalidArgumentError)
 will be thrown, with an error message that reveals the following information:

*   The type of the op that generated the tensor with bad numerics.
*   Data type (dtype) of the tensor.
*   Shape of the tensor (to the extent known at the time of eager execution or graph construction).
*   Name of the containing graph (if available).
*   (Graph mode only): The stack trace of the intra-graph op's creation, with a stack-height limit and a path-length limit for visual clarity. The stack frames that belong to the user's code (as opposed to tensorflow's internal code) are highlighted with a text arrow ("->").
*   (Eager mode only): How many of the offending tensor's elements are `Infinity` and `NaN`, respectively.

Once enabled, the check-numerics mechanism can be disabled by using [`tf.debugging.disable_check_numerics()`](https://www.tensorflow.org/api_docs/python/tf/debugging/disable_check_numerics)
.

#### Example usage:

1.  Catching infinity during the execution of a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
     graph:
    
    import tensorflow as tf
        
        tf.debugging.enable_check_numerics()
        
        @tf.function
        def square_log_x_plus_1(x):
          v = tf.math.log(x + 1)
          return tf.math.square(v)
        
        x = -1.0
        
        # When the following line runs, a function graph will be compiled
        # from the Python function `square_log_x_plus_1()`. Due to the
        # `enable_check_numerics()` call above, the graph will contain
        # numerics checking ops that will run during the function graph's
        # execution. The function call generates an -infinity when the Log
        # (logarithm) op operates on the output tensor of the Add op.
        # The program errors out at this line, printing an error message.
        y = square_log_x_plus_1(x)
        z = -y
    
2.  Catching NaN during eager execution:
    
    import numpy as np
        import tensorflow as tf
        
        tf.debugging.enable_check_numerics()
        
        x = np.array([[0.0, -1.0], [4.0, 3.0]])
        
        # The following line executes the Sqrt op eagerly. Due to the negative
        # element in the input array, a NaN is generated. Due to the
        # `enable_check_numerics()` call above, the program errors immediately
        # at this line, printing an error message.
        y = tf.math.sqrt(x)
        z = tf.matmul(y, y)
    

tf.config.set_soft_device_placement(True)
    tf.debugging.enable_check_numerics()
    
    resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')
    strategy = tf.distribute.TPUStrategy(resolver)
    with strategy.scope():
      # ...

|     |     |
| --- | --- |
| Args<br>---- |     |
| `stack_height_limit` | Limit to the height of the printed stack trace. Applicable only to ops in [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br>s (graphs). |
| `path_length_limit` | Limit to the file path included in the printed stack trace. Applicable only to ops in [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br>s (graphs). |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.