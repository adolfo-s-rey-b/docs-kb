[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/py_func#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/py_func)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/py_func?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fpy_func&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/py_func#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/py_func#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/py_func#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/py_func#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/py_func#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.py\_func Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/py_func#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/py_func#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/py_func#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/py_func#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/py_func#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/script_ops.py#L785-L801)

Wraps a python function and uses it as a TensorFlow op.

tf.compat.v1.py_func(
        func, inp, Tout, stateful=True, name=None
    )

Migrate to TF2
--------------

This name was deprecated and removed in TF2, but [`tf.numpy_function`](https://www.tensorflow.org/api_docs/python/tf/numpy_function)
 is a near-exact replacement, just drop the `stateful` argument (all [`tf.numpy_function`](https://www.tensorflow.org/api_docs/python/tf/numpy_function)
 calls are considered stateful). It is compatible with eager execution and [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
.

[`tf.py_function`](https://www.tensorflow.org/api_docs/python/tf/py_function)
 is a close but not an exact replacement, passing TensorFlow tensors to the wrapped function instead of NumPy arrays, which provides gradients and can take advantage of accelerators.

Before:

    def fn_using_numpy(x):

After:

    tf.numpy_function(fn_using_numpy, inp=[tf.constant([1., 2.])],

Description
-----------

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [TensorFlow Probability Case Study: Covariance Estimation](https://www.tensorflow.org/probability/examples/TensorFlow_Probability_Case_Study_Covariance_Estimation) |

Given a python function `func`, which takes numpy arrays as its arguments and returns numpy arrays as its outputs, wrap this function as an operation in a TensorFlow graph. The following snippet constructs a simple TensorFlow graph that invokes the `np.sinh()` NumPy function as a operation in the graph:

def my_func(x):
      # x will be a numpy array with the contents of the placeholder below
      return np.sinh(x)
    input = tf.compat.v1.placeholder(tf.float32)
    y = tf.compat.v1.py_func(my_func, [input], tf.float32)

*   The body of the function (i.e. `func`) will not be serialized in a `GraphDef`. Therefore, you should not use this function if you need to serialize your model and restore it in a different environment.
    
*   The operation must run in the same address space as the Python program that calls [`tf.compat.v1.py_func()`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/py_func)
    . If you are using distributed TensorFlow, you must run a [`tf.distribute.Server`](https://www.tensorflow.org/api_docs/python/tf/distribute/Server)
     in the same process as the program that calls [`tf.compat.v1.py_func()`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/py_func)
     and you must pin the created operation to a device in that server (e.g. using `with tf.device():`).
    

E.g.

  import tensorflow as tf
      import numpy as np
    
      def make_synthetic_data(i):
          return np.cast[np.uint8](i) * np.ones([20,256,256,3],
                  dtype=np.float32) / 10.
    
      def preprocess_fn(i):
          ones = tf.py_function(make_synthetic_data,[i],tf.float32)
          ones.set_shape(tf.TensorShape([None, None, None, None]))
          ones = tf.image.resize(ones, [224,224])
          return ones
    
      ds = tf.data.Dataset.range(10)
      ds = ds.map(preprocess_fn)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `func` | A Python function, which accepts `ndarray` objects as arguments and returns a list of `ndarray` objects (or a single `ndarray`). This function must accept as many arguments as there are tensors in `inp`, and these argument types will match the corresponding [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> objects in `inp`. The returns `ndarray`s must match the number and types defined `Tout`. Important Note: Input and output numpy `ndarray`s of `func` are not guaranteed to be copies. In some cases their underlying memory will be shared with the corresponding TensorFlow tensors. In-place modification or storing `func` input or return values in python datastructures without explicit (np.)copy can have non-deterministic consequences. |
| `inp` | A list of `Tensor` objects. |
| `Tout` | A list or tuple of tensorflow data types or a single tensorflow data type if there is only one, indicating what `func` returns. |
| `stateful` | (Boolean.) If True, the function should be considered stateful. If a function is stateless, when given the same input it will return the same output and have no observable side effects. Optimizations such as common sub-expression elimination are only performed on stateless operations. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A list of `Tensor` or a single `Tensor` which `func` computes. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.