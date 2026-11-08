[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/py_function#main-content)

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
    

tf.py\_function Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/script_ops.py#L460-L645)

Wraps a python function into a TensorFlow op that executes it eagerly.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.py_function`](https://www.tensorflow.org/api_docs/python/tf/py_function)

tf.py_function(
        func=None, inp=None, Tout=None, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Better performance with the tf.data API](https://www.tensorflow.org/guide/data_performance)<br>    <br>*   [tf.data: Build TensorFlow input pipelines](https://www.tensorflow.org/guide/data)<br>    <br>*   [Better performance with tf.function](https://www.tensorflow.org/guide/function) | *   [TFRecord and tf.train.Example](https://www.tensorflow.org/tutorials/load_data/tfrecord) |

Using [`tf.py_function`](https://www.tensorflow.org/api_docs/python/tf/py_function)
 inside a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 allows you to run a python function using eager execution, inside the [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
's graph. This has two main effects:

1.  This allows you to use nofunc=None, inp=None, Tout=None tensorflow code inside your [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
    .
2.  It allows you to run python control logic in a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
     without relying on [`tf.autograph`](https://www.tensorflow.org/api_docs/python/tf/autograph)
     to convert the code to use tensorflow control logic (tf.cond, tf.while\_loop).

Both of these features can be useful for debugging.

Since [`tf.py_function`](https://www.tensorflow.org/api_docs/python/tf/py_function)
 operates on `Tensor`s it is still differentiable (once).

There are two ways to use this function:

### As a decorator

Use [`tf.py_function`](https://www.tensorflow.org/api_docs/python/tf/py_function)
 as a decorator to ensure the function always runs eagerly.

When using [`tf.py_function`](https://www.tensorflow.org/api_docs/python/tf/py_function)
 as a decorator:

*   you must set `Tout`
*   you may set `name`
*   you must not set `func` or `inp`

For example, you might use [`tf.py_function`](https://www.tensorflow.org/api_docs/python/tf/py_function)
 to implement the log huber function.

    @tf.py_function(Tout=tf.float32)

Under eager execution the function operates normally:

    x = tf.constant(1.0)

Inside a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 the [`tf.py_function`](https://www.tensorflow.org/api_docs/python/tf/py_function)
 is not converted to a [`tf.Graph`](https://www.tensorflow.org/api_docs/python/tf/Graph)
.:

    @tf.function

The [`tf.py_function`](https://www.tensorflow.org/api_docs/python/tf/py_function)
 only executes eagerly, and only when the [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 is called:

    print(tf_wrapper(x).numpy())

Gradients work as expected:

    with tf.GradientTape() as t:

### Inplace

You can also skip the decorator and use [`tf.py_function`](https://www.tensorflow.org/api_docs/python/tf/py_function)
 in-place. This form is a useful shortcut if you don't control the function's source, but it is harder to read.

    # No decorator

### More info

You can also use [`tf.py_function`](https://www.tensorflow.org/api_docs/python/tf/py_function)
 to debug your models at runtime using Python tools, i.e., you can isolate portions of your code that you want to debug, wrap them in Python functions and insert `pdb` tracepoints or print statements as desired, and wrap those functions in [`tf.py_function`](https://www.tensorflow.org/api_docs/python/tf/py_function)
.

For more information on eager execution, see the [Eager guide](https://tensorflow.org/guide/eager)
.

[`tf.py_function`](https://www.tensorflow.org/api_docs/python/tf/py_function)
 is similar in spirit to [`tf.numpy_function`](https://www.tensorflow.org/api_docs/python/tf/numpy_function)
, but unlike the latter, the former lets you use TensorFlow operations in the wrapped Python function. In particular, while [`tf.compat.v1.py_func`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/py_func)
 only runs on CPUs and wraps functions that take NumPy arrays as inputs and return NumPy arrays as outputs, [`tf.py_function`](https://www.tensorflow.org/api_docs/python/tf/py_function)
 can be placed on GPUs and wraps functions that take Tensors as inputs, execute TensorFlow operations in their bodies, and return Tensors as outputs.

*   Calling [`tf.py_function`](https://www.tensorflow.org/api_docs/python/tf/py_function)
     will acquire the Python Global Interpreter Lock (GIL) that allows only one thread to run at any point in time. This will preclude efficient parallelization and distribution of the execution of the program.
    
*   The body of the function (i.e. `func`) will not be serialized in a `GraphDef`. Therefore, you should not use this function if you need to serialize your model and restore it in a different environment.
    
*   The operation must run in the same address space as the Python program that calls [`tf.py_function()`](https://www.tensorflow.org/api_docs/python/tf/py_function)
    . If you are using distributed TensorFlow, you must run a [`tf.distribute.Server`](https://www.tensorflow.org/api_docs/python/tf/distribute/Server)
     in the same process as the program that calls [`tf.py_function()`](https://www.tensorflow.org/api_docs/python/tf/py_function)
     and you must pin the created operation to a device in that server (e.g. using `with tf.device():`).
    
*   Currently [`tf.py_function`](https://www.tensorflow.org/api_docs/python/tf/py_function)
     is not compatible with XLA. Calling [`tf.py_function`](https://www.tensorflow.org/api_docs/python/tf/py_function)
     inside [`tf.function(jit_compile=True)`](https://www.tensorflow.org/api_docs/python/tf/function)
     will raise an error.
    

|     |     |
| --- | --- |
| Args<br>---- |     |
| `func` | A Python function that accepts `inp` as arguments, and returns a value (or list of values) whose type is described by `Tout`. Do not set `func` when using [`tf.py_function`](https://www.tensorflow.org/api_docs/python/tf/py_function)<br> as a decorator. |
| `inp` | Input arguments for `func`. A list whose elements are `Tensor`s or `CompositeTensors` (such as [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)<br>); or a single `Tensor` or `CompositeTensor`. Do not set `inp` when using [`tf.py_function`](https://www.tensorflow.org/api_docs/python/tf/py_function)<br> as a decorator. |
| `Tout` | The type(s) of the value(s) returned by `func`. One of the following:<br><br>*   If `func` returns a `Tensor` (or a value that can be converted to a Tensor): the [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br>     for that value.<br>*   If `func` returns a `CompositeTensor`: The [`tf.TypeSpec`](https://www.tensorflow.org/api_docs/python/tf/TypeSpec)<br>     for that value.<br>*   If `func` returns `None`: the empty list (`[]`).<br>*   If `func` returns a list of `Tensor` and `CompositeTensor` values: a corresponding list of [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br>    s and [`tf.TypeSpec`](https://www.tensorflow.org/api_docs/python/tf/TypeSpec)<br>    s for each value. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| *   If `func` is `None` this returns a decorator that will ensure the decorated function will always run with eager execution even if called from a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br>    /[`tf.Graph`](https://www.tensorflow.org/api_docs/python/tf/Graph)<br>    .<br>*   If used `func` is not `None` this executes `func` with eager execution and returns the result: a `Tensor`, `CompositeTensor`, or list of `Tensor` and `CompositeTensor`; or an empty list if `func` returns `None`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.