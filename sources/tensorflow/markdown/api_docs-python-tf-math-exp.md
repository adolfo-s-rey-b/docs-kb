[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/exp#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/exp)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/exp?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/exp#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/exp#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/exp#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/math/exp#numpy-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.exp Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/exp#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/exp#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/exp#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/math/exp#numpy-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L5771-L5818)

Computes exponential of x element-wise. y\=ex.

#### View aliases

**Main aliases**

[`tf.exp`](https://www.tensorflow.org/api_docs/python/tf/math/exp)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.exp`](https://www.tensorflow.org/api_docs/python/tf/math/exp)

tf.math.exp(
        x, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Understanding masking & padding](https://www.tensorflow.org/guide/keras/understanding_masking_and_padding) | *   [Scalable model compression](https://www.tensorflow.org/tutorials/optimization/compression)<br>    <br>*   [Convolutional Variational Autoencoder](https://www.tensorflow.org/tutorials/generative/cvae)<br>    <br>*   [Learned data compression](https://www.tensorflow.org/tutorials/generative/data_compression)<br>    <br>*   [Multiple changepoint detection and Bayesian model selection](https://www.tensorflow.org/probability/examples/Multiple_changepoint_detection_and_Bayesian_model_selection)<br>    <br>*   [Modeling COVID-19 spread in Europe and the effect of interventions](https://www.tensorflow.org/probability/examples/Estimating_COVID_19_in_11_European_countries) |

This function computes the exponential of the input tensor element-wise. i.e. [`math.exp(x)`](https://www.tensorflow.org/api_docs/python/tf/math/exp)
 or ex, where `x` is the input tensor. e denotes Euler's number and is approximately equal to 2.718281. Output is positive for any real input.

    x = tf.constant(2.0)

    x = tf.constant([2.0, 8.0])

For complex numbers, the exponential value is calculated as

ex+iy\=exeiy\=ex(cos(y)+isin(y))

For `1+1j` the value would be computed as:

e1(cos(1)+isin(1))\=2.7182817×(0.5403023+0.84147096j)

    x = tf.constant(1 + 1j)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>. Has the same type as `x`. |     |

numpy compatibility
-------------------

Equivalent to np.exp

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.