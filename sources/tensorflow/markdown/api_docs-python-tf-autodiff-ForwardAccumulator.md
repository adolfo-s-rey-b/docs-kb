[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/autodiff/ForwardAccumulator#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/autodiff/ForwardAccumulator)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/autodiff/ForwardAccumulator?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/autodiff/ForwardAccumulator#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/autodiff/ForwardAccumulator#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/autodiff/ForwardAccumulator#methods)
    *   [jvp](https://www.tensorflow.org/api_docs/python/tf/autodiff/ForwardAccumulator#jvp)
        
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/autodiff/ForwardAccumulator#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/autodiff/ForwardAccumulator#__exit__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.autodiff.ForwardAccumulator Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/autodiff/ForwardAccumulator#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/autodiff/ForwardAccumulator#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/autodiff/ForwardAccumulator#methods)
    *   [jvp](https://www.tensorflow.org/api_docs/python/tf/autodiff/ForwardAccumulator#jvp)
        
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/autodiff/ForwardAccumulator#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/autodiff/ForwardAccumulator#__exit__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/eager/forwardprop.py#L229-L487)

Computes Jacobian-vector products ("JVP"s) using forward-mode autodiff.

tf.autodiff.ForwardAccumulator(
        primals, tangents
    )

Compare to [`tf.GradientTape`](https://www.tensorflow.org/api_docs/python/tf/GradientTape)
 which computes vector-Jacobian products ("VJP"s) using reverse-mode autodiff (backprop). Reverse mode is more attractive when computing gradients of a scalar-valued function with respect to many inputs (e.g. a neural network with many parameters and a scalar loss). Forward mode works best on functions with many outputs and few inputs. Since it does not hold on to intermediate activations, it is much more memory efficient than backprop where it is applicable.

Consider a simple linear regression:

    x = tf.constant([[2.0, 3.0], [1.0, 4.0]])

The example has two variables containing parameters, `dense.kernel` (2 parameters) and `dense.bias` (1 parameter). Considering the training data `x` as a constant, this means the Jacobian matrix for the function mapping from parameters to loss has one row and three columns.

With forwardprop, we specify a length-three vector in advance which multiplies the Jacobian. The `primals` constructor argument is the parameter (a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 or [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
) we're specifying a vector for, and the `tangents` argument is the "vector" in Jacobian-vector product. If our goal is to compute the entire Jacobian matrix, forwardprop computes one column at a time while backprop computes one row at a time. Since the Jacobian in the linear regression example has only one row, backprop requires fewer invocations:

    x = tf.constant([[2.0, 3.0], [1.0, 4.0]])

Implicit in the `tape.gradient` call is a length-one vector which left-multiplies the Jacobian, a vector-Jacobian product.

`ForwardAccumulator` maintains JVPs corresponding primal tensors it is watching, derived from the original `primals` specified in the constructor. As soon as a primal tensor is deleted, `ForwardAccumulator` deletes the corresponding JVP.

`acc.jvp(x)` retrieves `acc`'s JVP corresponding to the primal tensor `x`. It does not perform any computation. `acc.jvp` calls can be repeated as long as `acc` is accessible, whether the context manager is active or not. New JVPs are only computed while the context manager is active.

Note that `ForwardAccumulator`s are always applied in the order their context managers were entered, so inner accumulators will not see JVP computation from outer accumulators. Take higher-order JVPs from outer accumulators:

    primal = tf.constant(1.1)

Reversing the collection in the last line to instead retrieve `inner.jvp(outer.jvp(primal_out))` will not work.

Strict nesting also applies to combinations of `ForwardAccumulator` and [`tf.GradientTape`](https://www.tensorflow.org/api_docs/python/tf/GradientTape)
. More deeply nested `GradientTape` objects will ignore the products of outer `ForwardAccumulator` objects. This allows (for example) memory-efficient forward-over-backward computation of Hessian-vector products, where the inner `GradientTape` would otherwise hold on to all intermediate JVPs:

    v = tf.Variable([1., 2.])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `primals` | A tensor or nested structure of tensors to watch. |
| `tangents` | A tensor or nested structure of tensors, with the same nesting structure as `primals`, with each element being a vector with the same size as the corresponding primal element. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If the same tensor or variable is specified multiple times in `primals`. |

Methods
-------

### `jvp`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/eager/forwardprop.py#L425-L458)

jvp(
        primals,
        unconnected_gradients=tf.UnconnectedGradients.NONE
    )

Fetches the Jacobian-vector product computed for `primals`.

Note that this method performs no computation, and simply looks up a JVP that was already computed (unlike backprop using a [`tf.GradientTape`](https://www.tensorflow.org/api_docs/python/tf/GradientTape)
, where the computation happens on the call to `tape.gradient`).

|     |     |
| --- | --- |
| Args |     |
| `primals` | A watched Tensor or structure of Tensors to fetch the JVPs for. |
| `unconnected_gradients` | A value which can either hold 'none' or 'zero' and alters the value which will be returned if no JVP was computed for `primals`. The possible values and effects are detailed in 'tf.UnconnectedGradients' and it defaults to 'none'. |

|     |
| --- |
| Returns |     |
| Tensors with the same shapes and dtypes as `primals`, or None if no JVP is available. |     |

### `__enter__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/eager/forwardprop.py#L374-L376)

__enter__()

### `__exit__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/eager/forwardprop.py#L378-L380)

__exit__(
        typ, value, traceback
    )

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.