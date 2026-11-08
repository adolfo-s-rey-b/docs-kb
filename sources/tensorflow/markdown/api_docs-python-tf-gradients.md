[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/gradients#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/gradients)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/gradients?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/gradients#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/gradients#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/gradients#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/gradients#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.gradients Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/gradients#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/gradients#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/gradients#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/gradients#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/gradients_impl.py#L188-L331)

Constructs symbolic derivatives of sum of `ys` w.r.t. x in `xs`.

tf.gradients(
        ys,
        xs,
        grad_ys=None,
        name='gradients',
        gate_gradients=False,
        aggregation_method=None,
        stop_gradients=None,
        unconnected_gradients=tf.UnconnectedGradients.NONE
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Generalized Linear Models](https://www.tensorflow.org/probability/examples/Generalized_Linear_Models) |

[`tf.gradients`](https://www.tensorflow.org/api_docs/python/tf/gradients)
 is only valid in a graph context. In particular, it is valid in the context of a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 wrapper, where code is executing as a graph.

`ys` and `xs` are each a `Tensor` or a list of tensors. `grad_ys` is a list of `Tensor`, holding the gradients received by the `ys`. The list must be the same length as `ys`.

`gradients()` adds ops to the graph to output the derivatives of `ys` with respect to `xs`. It returns a list of `Tensor` of length `len(xs)` where each tensor is the `sum(dy/dx)` for y in `ys` and for x in `xs`.

`grad_ys` is a list of tensors of the same length as `ys` that holds the initial gradients for each y in `ys`. When `grad_ys` is None, we fill in a tensor of '1's of the shape of y for each y in `ys`. A user can provide their own initial `grad_ys` to compute the derivatives using a different initial gradient for each y (e.g., if one wanted to weight the gradient differently for each value in each y).

`stop_gradients` is a `Tensor` or a list of tensors to be considered constant with respect to all `xs`. These tensors will not be backpropagated through, as though they had been explicitly disconnected using `stop_gradient`. Among other things, this allows computation of partial derivatives as opposed to total derivatives. For example:

    @tf.function

Here the partial derivatives `g` evaluate to `[1.0, 1.0]`, compared to the total derivatives `tf.gradients(a + b, [a, b])`, which take into account the influence of `a` on `b` and evaluate to `[3.0, 1.0]`. Note that the above is equivalent to:

    @tf.function

`stop_gradients` provides a way of stopping gradient after the graph has already been constructed, as compared to [`tf.stop_gradient`](https://www.tensorflow.org/api_docs/python/tf/stop_gradient)
 which is used during graph construction. When the two approaches are combined, backpropagation stops at both [`tf.stop_gradient`](https://www.tensorflow.org/api_docs/python/tf/stop_gradient)
 nodes and nodes in `stop_gradients`, whichever is encountered first.

All integer tensors are considered constant with respect to all `xs`, as if they were included in `stop_gradients`.

`unconnected_gradients` determines the value returned for each x in xs if it is unconnected in the graph to ys. By default this is None to safeguard against errors. Mathematically these gradients are zero which can be requested using the `'zero'` option. `tf.UnconnectedGradients` provides the following options and behaviors:

    @tf.function

Let us take one practical example which comes during the back propogation phase. This function is used to evaluate the derivatives of the cost function with respect to Weights `Ws` and Biases `bs`. Below sample implementation provides the exaplantion of what it is actually used for :

    @tf.function

|     |     |
| --- | --- |
| Args<br>---- |     |
| `ys` | A `Tensor` or list of tensors to be differentiated. |
| `xs` | A `Tensor` or list of tensors to be used for differentiation. |
| `grad_ys` | Optional. A `Tensor` or list of tensors the same size as `ys` and holding the gradients computed for each y in `ys`. |
| `name` | Optional name to use for grouping all the gradient ops together. defaults to 'gradients'. |
| `gate_gradients` | If True, add a tuple around the gradients returned for an operations. This avoids some race conditions. |
| `aggregation_method` | Specifies the method used to combine gradient terms. Accepted values are constants defined in the class `AggregationMethod`. |
| `stop_gradients` | Optional. A `Tensor` or list of tensors not to differentiate through. |
| `unconnected_gradients` | Optional. Specifies the gradient value returned when the given input tensors are unconnected. Accepted values are constants defined in the class [`tf.UnconnectedGradients`](https://www.tensorflow.org/api_docs/python/tf/UnconnectedGradients)<br> and the default value is `none`. |

|     |
| --- |
| Returns<br>------- |     |
| A list of `Tensor` of length `len(xs)` where each tensor is the `sum(dy/dx)` for y in `ys` and for x in `xs`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `LookupError` | if one of the operations between `x` and `y` does not have a registered gradient function. |
| `ValueError` | if the arguments are invalid. |
| `RuntimeError` | if called in Eager mode. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.