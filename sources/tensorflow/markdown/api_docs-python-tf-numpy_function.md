[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/numpy_function#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/numpy_function)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/numpy_function?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/numpy_function#used-in-the-notebooks)
    
*   [As a decorator](https://www.tensorflow.org/api_docs/python/tf/numpy_function#as_a_decorator)
    
*   [Inplace](https://www.tensorflow.org/api_docs/python/tf/numpy_function#inplace)
    
*   [More info](https://www.tensorflow.org/api_docs/python/tf/numpy_function#more_info)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/numpy_function#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/numpy_function#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.numpy\_function Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/numpy_function#used-in-the-notebooks)
    
*   [As a decorator](https://www.tensorflow.org/api_docs/python/tf/numpy_function#as_a_decorator)
    
*   [Inplace](https://www.tensorflow.org/api_docs/python/tf/numpy_function#inplace)
    
*   [More info](https://www.tensorflow.org/api_docs/python/tf/numpy_function#more_info)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/numpy_function#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/numpy_function#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/script_ops.py#L807-L948)

Wraps a python function and uses it as a TensorFlow op.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.numpy_function`](https://www.tensorflow.org/api_docs/python/tf/numpy_function)

tf.numpy_function(
        func=None, inp=None, Tout=None, stateful=True, name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Playing CartPole with the Actor-Critic method](https://www.tensorflow.org/tutorials/reinforcement_learning/actor_critic) |

Given a python function `func` wrap this function as an operation in a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
. `func` must take numpy arrays as its arguments and return numpy arrays as its outputs.

There are two ways to use [`tf.numpy_function`](https://www.tensorflow.org/api_docs/python/tf/numpy_function)
.

### As a decorator

When using [`tf.numpy_function`](https://www.tensorflow.org/api_docs/python/tf/numpy_function)
 as a decorator:

*   you must set `Tout`
*   you may set `name`
*   you must not set `func` or `inp`

    @tf.numpy_function(Tout=tf.float32)

The function runs eagerly:

    my_numpy_func(1.0).numpy()

The behavior doesn't change inside a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
:

    @tf.function(input_signature=[tf.TensorSpec(None, tf.float32)])

### Inplace

This form can be useful if you don't control the function's source, but it is harder to read.

Here is the same function with no decorator:

    def my_func(x):

To run [`tf.numpy_function`](https://www.tensorflow.org/api_docs/python/tf/numpy_function)
 in-place, pass the function, its inputs, and the output type in a single call to [`tf.numpy_function`](https://www.tensorflow.org/api_docs/python/tf/numpy_function)
:

    tf.numpy_function(my_func, [tf.constant(1.0)], tf.float32)

### More info

Comparison to [`tf.py_function`](https://www.tensorflow.org/api_docs/python/tf/py_function)
: [`tf.py_function`](https://www.tensorflow.org/api_docs/python/tf/py_function)
 and [`tf.numpy_function`](https://www.tensorflow.org/api_docs/python/tf/numpy_function)
 are very similar, except that [`tf.numpy_function`](https://www.tensorflow.org/api_docs/python/tf/numpy_function)
 takes numpy arrays, and not [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
s. If you want the function to contain `tf.Tensors`, and have any TensorFlow operations executed in the function be differentiable, please use [`tf.py_function`](https://www.tensorflow.org/api_docs/python/tf/py_function)
.

*   Calling [`tf.numpy_function`](https://www.tensorflow.org/api_docs/python/tf/numpy_function)
     will acquire the Python Global Interpreter Lock (GIL) that allows only one thread to run at any point in time. This will preclude efficient parallelization and distribution of the execution of the program. Therefore, you are discouraged to use [`tf.numpy_function`](https://www.tensorflow.org/api_docs/python/tf/numpy_function)
     outside of prototyping and experimentation.
    
*   The body of the function (i.e. `func`) will not be serialized in a `tf.SavedModel`. Therefore, you should not use this function if you need to serialize your model and restore it in a different environment.
    
*   The operation must run in the same address space as the Python program that calls [`tf.numpy_function()`](https://www.tensorflow.org/api_docs/python/tf/numpy_function)
    . If you are using distributed TensorFlow, you must run a [`tf.distribute.Server`](https://www.tensorflow.org/api_docs/python/tf/distribute/Server)
     in the same process as the program that calls [`tf.numpy_function`](https://www.tensorflow.org/api_docs/python/tf/numpy_function)
     you must pin the created operation to a device in that server (e.g. using `with tf.device():`).
    
*   Currently [`tf.numpy_function`](https://www.tensorflow.org/api_docs/python/tf/numpy_function)
     is not compatible with XLA. Calling [`tf.numpy_function`](https://www.tensorflow.org/api_docs/python/tf/numpy_function)
     inside [`tf.function(jit_compile=True)`](https://www.tensorflow.org/api_docs/python/tf/function)
     will raise an error.
    
*   Since the function takes numpy arrays, you cannot take gradients through a numpy\_function. If you require something that is differentiable, please consider using tf.py\_function.
    

|     |     |
| --- | --- |
| Args<br>---- |     |
| `func` | A Python function, which accepts `numpy.ndarray` objects as arguments and returns a list of `numpy.ndarray` objects (or a single `numpy.ndarray`). This function must accept as many arguments as there are tensors in `inp`, and these argument types will match the corresponding [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> objects in `inp`. The returns `numpy.ndarray`s must match the number and types defined `Tout`. Important Note: Input and output `numpy.ndarray`s of `func` are not guaranteed to be copies. In some cases their underlying memory will be shared with the corresponding TensorFlow tensors. In-place modification or storing `func` input or return values in python datastructures without explicit (np.)copy can have non-deterministic consequences. |
| `inp` | A list of [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> objects. |
| `Tout` | A list or tuple of tensorflow data types or a single tensorflow data type if there is only one, indicating what `func` returns. |
| `stateful` | (Boolean.) Setting this argument to False tells the runtime to treat the function as stateless, which enables certain optimizations. A function is stateless when given the same input it will return the same output and have no side effects; its only purpose is to have a return value. The behavior for a stateful function with the `stateful` argument False is undefined. In particular, caution should be taken when mutating the input arguments as this is a stateful operation. |
| `name` | (Optional) A name for the operation. |

|     |
| --- |
| Returns<br>------- |     |
| *   If `func` is `None` this returns a decorator that will ensure the decorated function will always run with eager execution even if called from a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br>    /[`tf.Graph`](https://www.tensorflow.org/api_docs/python/tf/Graph)<br>    .<br>*   If used `func` is not `None` this executes `func` with eager execution and returns the result: A single or list of [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>     which `func` computes. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.