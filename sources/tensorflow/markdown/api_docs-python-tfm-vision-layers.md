[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/layers#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/layers)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/layers?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/vision/layers#classes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfm.vision.layers Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/vision/layers#classes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/layers/__init__.py)

Layers package definition.

Classes
-------

[`class BottleneckBlock`](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/BottleneckBlock)
: A standard bottleneck block.

[`class BottleneckBlock3D`](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/BottleneckBlock3D)
: Creates a 3D bottleneck block.

[`class BottleneckResidualInner`](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/BottleneckResidualInner)
: Creates a single inner block of a bottleneck.

[`class BoxSampler`](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/BoxSampler)
: Creates a BoxSampler to sample positive and negative boxes.

[`class CausalConvMixin`](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/CausalConvMixin)
: Mixin class to implement CausalConv for `tf_keras.layers.Conv` layers.

[`class Conv2D`](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/Conv2D)
: Conv2D layer supporting CausalConv.

[`class Conv3D`](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/Conv3D)
: Conv3D layer supporting CausalConv.

[`class DepthwiseConv2D`](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/DepthwiseConv2D)
: DepthwiseConv2D layer supporting CausalConv.

[`class DepthwiseSeparableConvBlock`](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/DepthwiseSeparableConvBlock)
: Creates a depthwise separable convolution block with batch normalization.

[`class DetectionGenerator`](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/DetectionGenerator)
: Generates the final detected boxes with scores and classes.

[`class GlobalAveragePool3D`](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/GlobalAveragePool3D)
: Creates a global average pooling layer with causal mode.

[`class InvertedBottleneckBlock`](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/InvertedBottleneckBlock)
: An inverted bottleneck block.

[`class MaskSampler`](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/MaskSampler)
: Samples and creates mask training targets.

[`class MultilevelDetectionGenerator`](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/MultilevelDetectionGenerator)
: Generates detected boxes with scores and classes for one-stage detector.

[`class MultilevelROIAligner`](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/MultilevelROIAligner)
: Performs ROIAlign for the second stage processing.

[`class MultilevelROIGenerator`](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/MultilevelROIGenerator)
: Proposes RoIs for the second stage processing.

[`class PositionalEncoding`](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/PositionalEncoding)
: Creates a network layer that adds a sinusoidal positional encoding.

[`class ROISampler`](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/ROISampler)
: Samples ROIs and assigns targets to the sampled ROIs.

[`class ResidualBlock`](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/ResidualBlock)
: A residual block.

[`class ResidualInner`](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/ResidualInner)
: Creates a single inner block of a residual.

[`class ReversibleLayer`](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/ReversibleLayer)
: Creates a reversible layer.

[`class Scale`](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/Scale)
: Scales the input by a trainable scalar weight.

[`class SelfGating`](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/SelfGating)
: Feature gating as used in S3D-G.

[`class SpatialAveragePool3D`](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/SpatialAveragePool3D)
: Creates a global average pooling layer pooling across spatial dimentions.

[`class SqueezeExcitation`](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/SqueezeExcitation)
: Creates a squeeze and excitation layer.

[`class StochasticDepth`](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/StochasticDepth)
: Creates a stochastic depth layer.

[`class TemporalSoftmaxPool`](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/TemporalSoftmaxPool)
: Creates a network layer corresponding to temporal softmax pooling.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.