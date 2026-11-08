[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/log_poisson_loss#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/log_poisson_loss)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/log_poisson_loss?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/log_poisson_loss#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/log_poisson_loss#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nn/log_poisson_loss#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.log\_poisson\_loss Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/log_poisson_loss#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/log_poisson_loss#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nn/log_poisson_loss#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_impl.py#L44-L107)

Computes log Poisson loss given `log_input`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.nn.log_poisson_loss`](https://www.tensorflow.org/api_docs/python/tf/nn/log_poisson_loss)

tf.nn.log_poisson_loss(
        targets, log_input, compute_full_loss=False, name=None
    )

Gives the log-likelihood loss between the prediction and the target under the assumption that the target has a Poisson distribution. Caveat: By default, this is not the exact loss, but the loss minus a constant term \[log(z!)\]. That has no effect for optimization, but does not play well with relative loss comparisons. To compute an approximation of the log factorial term, specify compute\_full\_loss=True to enable Stirling's Approximation.

For brevity, let `c = log(x) = log_input`, `z = targets`. The log Poisson loss is

  -log(exp(-x) * (x^z) / z!)
    = -log(exp(-x) * (x^z)) + log(z!)
    ~ -log(exp(-x)) - log(x^z) [+ z * log(z) - z + 0.5 * log(2 * pi * z)]
        [ Note the second term is the Stirling's Approximation for log(z!).\
          It is invariant to x and does not affect optimization, though\
          important for correct relative loss comparisons. It is only\
          computed when compute_full_loss == True. ]
    = x - z * log(x) [+ z * log(z) - z + 0.5 * log(2 * pi * z)]
    = exp(c) - z * c [+ z * log(z) - z + 0.5 * log(2 * pi * z)]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `targets` | A `Tensor` of the same type and shape as `log_input`. |
| `log_input` | A `Tensor` of type `float32` or `float64`. |
| `compute_full_loss` | whether to compute the full loss. If false, a constant term is dropped in favor of more efficient optimization. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of the same shape as `log_input` with the componentwise logistic losses. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `log_input` and `targets` do not have the same shape. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.