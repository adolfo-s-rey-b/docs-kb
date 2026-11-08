[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fmixed_precision&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.compat.v1.mixed\_precision Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision#functions)
    

Public API for tf.\_api.v2.mixed\_precision namespace

Modules
-------

[`experimental`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/experimental)
 module: Public API for tf.\_api.v2.mixed\_precision.experimental namespace

Classes
-------

[`class DynamicLossScale`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/DynamicLossScale)
: Loss scale that dynamically adjusts itself.

[`class FixedLossScale`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/FixedLossScale)
: Loss scale with a fixed value.

[`class LossScale`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/LossScale)
: Base class for all TF1 loss scales.

[`class MixedPrecisionLossScaleOptimizer`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/MixedPrecisionLossScaleOptimizer)
: An optimizer that applies loss scaling.

Functions
---------

[`disable_mixed_precision_graph_rewrite(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/disable_mixed_precision_graph_rewrite)
: Disables the mixed precision graph rewrite.

[`enable_mixed_precision_graph_rewrite(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/enable_mixed_precision_graph_rewrite)
: Enable mixed precision via a graph rewrite.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.