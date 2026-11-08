[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/stop_gradient#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/stop_gradient)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/stop_gradient?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/stop_gradient#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/stop_gradient#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/stop_gradient#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.stop\_gradient Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/stop_gradient#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/stop_gradient#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/stop_gradient#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L6772-L6802)

Stops gradient computation.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.stop_gradient`](https://www.tensorflow.org/api_docs/python/tf/stop_gradient)

tf.stop_gradient(
        input, name=None
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Advanced automatic differentiation](https://www.tensorflow.org/guide/advanced_autodiff) |

When executed in a graph, this op outputs its input tensor as-is.

When building ops to compute gradients, this op prevents the contribution of its inputs to be taken into account. Normally, the gradient generator adds ops to a graph to compute the derivatives of a specified 'loss' by recursively finding out inputs that contributed to its computation. If you insert this op in the graph it inputs are masked from the gradient generator. They are not taken into account for computing gradients.

This is useful any time you want to compute a value with TensorFlow but need to pretend that the value was a constant. For example, the softmax function for a vector x can be written as

  def softmax(x):
        numerator = tf.exp(x)
        denominator = tf.reduce_sum(numerator)
        return numerator / denominator

This however is susceptible to overflow if the values in x are large. An alternative more stable way is to subtract the maximum of x from each of the values.

  def stable_softmax(x):
        z = x - tf.reduce_max(x)
        numerator = tf.exp(z)
        denominator = tf.reduce_sum(numerator)
        return numerator / denominator

However, when we backprop through the softmax to x, we dont want to backprop through the [`tf.reduce_max(x)`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_max)
 (if the max values are not unique then the gradient could flow to the wrong input) calculation and treat that as a constant. Therefore, we should write this out as

  def stable_softmax(x):
        z = x - tf.stop_gradient(tf.reduce_max(x))
        numerator = tf.exp(z)
        denominator = tf.reduce_sum(numerator)
        return numerator / denominator

Some other examples include:

*   The _EM_ algorithm where the _M-step_ should not involve backpropagation through the output of the _E-step_.
*   Contrastive divergence training of Boltzmann machines where, when differentiating the energy function, the training must not backpropagate through the graph that generated the samples from the model.
*   Adversarial training, where no backprop should happen through the adversarial example generation process.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `input`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.