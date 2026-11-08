[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/grad#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/grad)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/grad?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fops%2Fgrad&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/grad#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/grad#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.grad Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/grad#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/grad#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/master/keras/src/ops/core.py#L1231-L1267)

Return a function that computes the gradient of `f`.

tf.keras.ops.grad(
        f, argnums=0
    )

Experimental. This works on concrete tensors only, not symbolic ones, and raises `NotImplementedError` on backends without automatic differentiation. A non-scalar output is summed before differentiating, the same as a gradient tape would.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `f` | A function returning a tensor. The arguments at `argnums` may be tensors, variables or nested structures of them. |
| `argnums` | An integer or a tuple of integers, the positions of the arguments to differentiate with respect to. Defaults to `0`. |

|     |
| --- |
| Returns<br>------- |     |
| A function with the signature of `f` that returns the gradient for each position in `argnums`, a single value for an integer and a tuple for a tuple. Arguments that do not affect the output get zeros. |     |

#### Example:

def f(x, y):
        return x * y
    
    x = ops.array([1.0, 2.0])
    y = ops.array([3.0, 4.0])
    dx = ops.grad(f)(x, y)
    # dx is [3.0, 4.0]
    dx, dy = ops.grad(f, argnums=(0, 1))(x, y)
    # dy is [1.0, 2.0]
    ops.grad(ops.tanh)(x)
    # the elementwise derivative of tanh at x

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.