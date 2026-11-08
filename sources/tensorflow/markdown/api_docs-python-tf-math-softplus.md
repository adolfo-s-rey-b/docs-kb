[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/softplus#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/softplus)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/softplus?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fmath%2Fsoftplus&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/softplus#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/softplus#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/softplus#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.softplus Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/softplus#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/softplus#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/softplus#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L662-L685)

Computes elementwise softplus: `softplus(x) = log(exp(x) + 1)`.

#### View aliases

**Main aliases**

[`tf.nn.softplus`](https://www.tensorflow.org/api_docs/python/tf/math/softplus)

tf.math.softplus(
        features, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Introduction to gradients and automatic differentiation](https://www.tensorflow.org/guide/autodiff) | *   [TFP Probabilistic Layers: Regression](https://www.tensorflow.org/probability/examples/Probabilistic_Layers_Regression)<br>    <br>*   [Gaussian Process Latent Variable Models](https://www.tensorflow.org/probability/examples/Gaussian_Process_Latent_Variable_Model)<br>    <br>*   [Bayesian Modeling with Joint Distribution](https://www.tensorflow.org/probability/examples/Modeling_with_JointDistribution) |

`softplus` is a smooth approximation of `relu`. Like `relu`, `softplus` always takes on positive values.

![](https://www.tensorflow.org/images/softplus.png)

#### Example:

    import tensorflow as tf

|     |     |
| --- | --- |
| Args<br>---- |     |
| `features` | `Tensor` |
| `name` | Optional: name to associate with this operation. |

|     |
| --- |
| Returns<br>------- |     |
| `Tensor` |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.