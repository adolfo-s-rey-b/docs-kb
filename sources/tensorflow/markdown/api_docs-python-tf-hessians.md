[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/hessians#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/hessians)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/hessians?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/hessians#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/hessians#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/hessians#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/hessians#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.hessians Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/hessians#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/hessians#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/hessians#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/hessians#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/gradients_impl.py#L455-L491)

Constructs the Hessian of sum of `ys` with respect to `x` in `xs`.

tf.hessians(
        ys,
        xs,
        gate_gradients=False,
        aggregation_method=None,
        name='hessians'
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Generalized Linear Models](https://www.tensorflow.org/probability/examples/Generalized_Linear_Models) |

`hessians()` adds ops to the graph to output the Hessian matrix of `ys` with respect to `xs`. It returns a list of `Tensor` of length `len(xs)` where each tensor is the Hessian of `sum(ys)`.

The Hessian is a matrix of second-order partial derivatives of a scalar tensor (see [https://en.wikipedia.org/wiki/Hessian\_matrix](https://en.wikipedia.org/wiki/Hessian_matrix)
 for more details).

|     |     |
| --- | --- |
| Args<br>---- |     |
| `ys` | A `Tensor` or list of tensors to be differentiated. |
| `xs` | A `Tensor` or list of tensors to be used for differentiation. |
| `gate_gradients` | See `gradients()` documentation for details. |
| `aggregation_method` | See `gradients()` documentation for details. |
| `name` | Optional name to use for grouping all the gradient ops together. defaults to 'hessians'. |

|     |
| --- |
| Returns<br>------- |     |
| A list of Hessian matrices of `sum(ys)` for each `x` in `xs`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `LookupError` | if one of the operations between `xs` and `ys` does not have a registered gradient function. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.