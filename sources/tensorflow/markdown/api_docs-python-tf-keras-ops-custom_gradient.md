[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/custom_gradient#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/custom_gradient)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/custom_gradient?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fops%2Fcustom_gradient&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/custom_gradient#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/custom_gradient#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.custom\_gradient Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/custom_gradient#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/custom_gradient#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/core.py#L1222-L1303)

Decorator to define a function with a custom gradient.

tf.keras.ops.custom_gradient(
        f
    )

This decorator allows fine grained control over the gradients of a sequence for operations. This may be useful for multiple reasons, including providing a more efficient or numerically stable gradient for a sequence of operations.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `f` | Function `f(*args)` that returns a tuple `(output, grad_fn)`, where:<br><br>*   `args` is a sequence of (nested structures of) tensor inputs to the function.<br>*   `output` is a (nested structure of) tensor outputs of applying operations in `forward_fn` to `args`.<br>*   `grad_fn` is a function with the signature `grad_fn(*args, upstream)` which returns a tuple of tensors the same size as (flattened) `args`: the derivatives of tensors in `output` with respect to the tensors in `args`. `upstream` is a tensor or sequence of tensors holding the initial value gradients for each tensor in `output`. |

|     |
| --- |
| Returns<br>------- |     |
| A function `h(*args)` which returns the same value as `f(*args)[0]` and whose gradient is determined by `f(*args)[1]`. |     |

#### Examples:

1.  Backend-agnostic example.

@ops.custom_gradient
    def log1pexp(x):
        e = ops.exp(x)
    
        def grad(*args, upstream=None):
            if upstream is None:
                (upstream,) = args
            return ops.multiply(upstream, 1.0 - 1.0 / ops.add(1, e))
    
        return ops.log(1 + e), grad

Note that the grad function that returns gradient computation requires `args` as well as an `upstream` keyword argument, depending on the backend being set. With the JAX and TensorFlow backends, it requires only one argument, whereas it might use the `upstream` argument in the case of the PyTorch backend.

When working with TensorFlow/JAX backend, `grad(upstream)` is sufficient. With PyTorch, the `grad` function requires `*args` as well as `upstream`, e.g. `def grad(*args, upstream)`. Follow the previous example to use [`@ops.custom_gradient`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/custom_gradient)
 in a way that is compatible with all backends.

1.  Here's JAX & TensorFlow-specific example:

@ops.custom_gradient
    def log1pexp(x):
        e = ops.exp(x)
        def grad(upstream):
            return ops.multiply(upstream, 1.0 - 1.0 / ops.add(1, e))
        return ops.log(1 + e), grad

1.  Lastly, here's a PyTorch-specific example, using `*args` & `upstream`:

@ops.custom_gradient
    def log1pexp(x):
        e = ops.exp(x)
        def grad(*args, upstream):
            return ops.multiply(upstream, 1.0 - 1.0 / ops.add(1, e))
        return ops.log(1 + e), grad

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.