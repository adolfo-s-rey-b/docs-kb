[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/leaky_relu#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/leaky_relu)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/leaky_relu?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/leaky_relu#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/leaky_relu#returns)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/leaky_relu#references)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.nn.leaky\_relu Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/leaky_relu#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/leaky_relu#returns)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/leaky_relu#references)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L3667-L3699)

Compute the Leaky ReLU activation function.

tf.compat.v1.nn.leaky_relu(
        features, alpha=0.2, name=None
    )

Source: [Rectifier Nonlinearities Improve Neural Network Acoustic Models. AL Maas, AY Hannun, AY Ng - Proc. ICML, 2013](https://ai.stanford.edu/%7Eamaas/papers/relu_hybrid_icml2013_final.pdf)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `features` | A `Tensor` representing preactivation values. Must be one of the following types: `float16`, `float32`, `float64`, `int32`, `int64`. |
| `alpha` | Slope of the activation function at x < 0. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| The activation value. |     |

|     |
| --- |
| References<br>---------- |     |
| Rectifier Nonlinearities Improve Neural Network Acoustic Models: [Maas et al., 2013](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.693.1422)<br> ([pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.693.1422&rep=rep1&type=pdf)<br>) |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.