[Skip to main content](https://www.tensorflow.org/api_docs/python/tfc/layers#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfc/layers)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfc/layers?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfc%2Flayers&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfc/layers#classes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfc.layers Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfc/layers#classes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/layers/__init__.py)

Layers, based on [`tf.keras.layers.Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
.

Classes
-------

[`class GDN`](https://www.tensorflow.org/api_docs/python/tfc/layers/GDN)
: Generalized divisive normalization layer.

[`class GDNParameter`](https://www.tensorflow.org/api_docs/python/tfc/layers/GDNParameter)
: Nonnegative parameterization as needed for GDN parameters.

[`class IdentityInitializer`](https://www.tensorflow.org/api_docs/python/tfc/layers/IdentityInitializer)
: Initialize to the identity kernel with the given shape.

[`class Parameter`](https://www.tensorflow.org/api_docs/python/tfc/layers/Parameter)
: Reparameterized `Layer` variable.

[`class RDFTParameter`](https://www.tensorflow.org/api_docs/python/tfc/layers/RDFTParameter)
: RDFT reparameterization of a convolution kernel.

[`class SignalConv1D`](https://www.tensorflow.org/api_docs/python/tfc/layers/SignalConv1D)
: 1D convolution layer.

[`class SignalConv2D`](https://www.tensorflow.org/api_docs/python/tfc/layers/SignalConv2D)
: 2D convolution layer.

[`class SignalConv3D`](https://www.tensorflow.org/api_docs/python/tfc/layers/SignalConv3D)
: 3D convolution layer.

[`class SoftRound`](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound)
: Applies a differentiable approximation of rounding.

[`class SoftRoundConditionalMean`](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRoundConditionalMean)
: Conditional mean of inputs given noisy soft rounded values.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.