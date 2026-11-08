[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/UnconnectedGradients#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/UnconnectedGradients)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/UnconnectedGradients?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2FUnconnectedGradients&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/UnconnectedGradients#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.UnconnectedGradients Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/UnconnectedGradients#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/unconnected_gradients.py#L22-L39)

Controls how gradient computation behaves when y does not depend on x.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.UnconnectedGradients`](https://www.tensorflow.org/api_docs/python/tf/UnconnectedGradients)

The gradient of y with respect to x can be zero in two different ways: there could be no differentiable path in the graph connecting x to y (and so we can statically prove that the gradient is zero) or it could be that runtime values of tensors in a particular execution lead to a gradient of zero (say, if a relu unit happens to not be activated). To allow you to distinguish between these two cases you can choose what value gets returned for the gradient when there is no path in the graph from x to y:

*   `NONE`: Indicates that \[None\] will be returned if there is no path from x to y
*   `ZERO`: Indicates that a zero tensor will be returned in the shape of x.

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| NONE | `<UnconnectedGradients.NONE: 'none'>` |
| ZERO | `<UnconnectedGradients.ZERO: 'zero'>` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.