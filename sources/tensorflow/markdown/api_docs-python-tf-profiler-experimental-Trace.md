[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/Trace#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/Trace)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/Trace?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/Trace#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/Trace#methods)
    *   [set\_metadata](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/Trace#set_metadata)
        
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/Trace#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/Trace#__exit__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.profiler.experimental.Trace Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/Trace#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/Trace#methods)
    *   [set\_metadata](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/Trace#set_metadata)
        
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/Trace#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/Trace#__exit__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/trace.py#L27-L123)

Context manager that generates a trace event in the profiler.

tf.profiler.experimental.Trace(
        name, **kwargs
    )

A trace event will start when entering the context, and stop and save the result to the profiler when exiting the context. Open TensorBoard Profile tab and choose trace viewer to view the trace event in the timeline.

Trace events are created only when the profiler is enabled. More information on how to use the profiler can be found at [https://tensorflow.org/guide/profiler](https://tensorflow.org/guide/profiler)

#### Example usage:

tf.profiler.experimental.start('logdir')
    for step in range(num_steps):
      # Creates a trace event for each training step with the step number.
      with tf.profiler.experimental.Trace("Train", step_num=step, _r=1):
        train_fn()
    tf.profiler.experimental.stop()

|     |     |
| --- | --- |
| Args<br>---- |     |
| `name` | The name of the trace event. |
| `**kwargs` | Keyword arguments added to the trace event. Both the key and value are of types that can be converted to strings, which will be interpreted by the profiler according to the traceme name.<br><br>Example usage:<br><br>  tf.profiler.experimental.start('logdir')<br>      for step in range(num_steps):<br>        # Creates a trace event for each training step with the<br>        # step number.<br>        with tf.profiler.experimental.Trace("Train", step_num=step):<br>          train_fn()<br>      tf.profiler.experimental.stop()<br><br>The example above uses the keyword argument "step\_num" to specify the training step being traced. |

Methods
-------

### `set_metadata`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/trace.py#L87-L119)

set_metadata(
        **kwargs
    )

Sets metadata in this trace event.

|     |     |
| --- | --- |
| Args |     |
| `**kwargs` | metadata in key-value pairs. |

This method enables setting metadata in a trace event after it is created.

#### Example usage:

  def call(function):
        with tf.profiler.experimental.Trace("call",
             function_name=function.name) as tm:
          binary, in_cache = jit_compile(function)
          tm.set_metadata(in_cache=in_cache)
          execute(binary)

In this example, we want to trace how much time spent on calling a function, which includes compilation and execution. The compilation can be either getting a cached copy of the binary or actually generating the binary, which is indicated by the boolean "in\_cache" returned by jit\_compile(). We need to use set\_metadata() to pass in\_cache because we did not know the in\_cache value when the trace was created (and we cannot create the trace after jit\_compile(), because we want to measure the entire duration of call()).

### `__enter__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/trace.py#L83-L85)

__enter__()

### `__exit__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/trace.py#L121-L123)

__exit__(
        exc_type, exc_val, exc_tb
    )

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.