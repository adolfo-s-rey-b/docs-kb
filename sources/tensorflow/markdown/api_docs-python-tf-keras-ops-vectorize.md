[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/vectorize#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/vectorize)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/vectorize?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/vectorize#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/vectorize#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.vectorize Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/vectorize#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/vectorize#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L8421-L8460)

Turn a function into a vectorized function.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.vectorize`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/vectorize)

tf.keras.ops.vectorize(
        pyfunc, *, excluded=None, signature=None
    )

#### Example:

def myfunc(a, b):
        return a + b
    
    vfunc = keras.ops.vectorize(myfunc)
    y = vfunc([1, 2, 3, 4], 2)  # Returns Tensor([3, 4, 5, 6])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `pyfunc` | Callable of a single tensor argument. |
| `excluded` | Optional set of integers representing positional arguments for which the function will not be vectorized. These will be passed directly to `pyfunc` unmodified. |
| `signature` | Optional generalized universal function signature, e.g., `"(m,n),(n)->(m)"` for vectorized matrix-vector multiplication. If provided, `pyfunc` will be called with (and expected to return) arrays with shapes given by the size of corresponding core dimensions. By default, `pyfunc` is assumed to take scalars tensors as input and output. |

|     |
| --- |
| Returns<br>------- |     |
| A new function that applies `pyfunc` to every element of its input along axis 0 (the batch axis). |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.