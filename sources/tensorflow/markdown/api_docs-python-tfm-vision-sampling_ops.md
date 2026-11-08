[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfm.vision.sampling\_ops Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops#functions)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/sampling_ops.py)

Class to subsample minibatches by balancing positives and negatives.

Subsamples minibatches based on a pre-specified positive fraction in range \[0,1\]. The class presumes there are many more negatives than positive examples: if the desired batch\_size cannot be achieved with the pre-specified positive fraction, it fills the rest with negative examples. If this is not sufficient for obtaining the desired batch\_size, it returns fewer examples.

The main function to call is Subsample(self, indicator, labels). For convenience one can also call SubsampleWeights(self, weights, labels) which is defined in the minibatch\_sampler base class.

When is\_static is True, it implements a method that guarantees static shapes. It also ensures the length of output of the subsample is always batch\_size, even when number of examples set to True in indicator is less than batch\_size.

This is originally implemented in TensorFlow Object Detection API.

Classes
-------

[`class BalancedPositiveNegativeSampler`](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops/BalancedPositiveNegativeSampler)
: Subsamples minibatches to a desired balance of positives and negatives.

Functions
---------

[`combined_static_and_dynamic_shape(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops/combined_static_and_dynamic_shape)
: Returns a list containing static and dynamic values for the dimensions.

[`indices_to_dense_vector(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops/indices_to_dense_vector)
: Creates dense vector with indices set to specific value and rest to zeros.

[`matmul_gather_on_zeroth_axis(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops/matmul_gather_on_zeroth_axis)
: Matrix multiplication based implementation of tf.gather on zeroth axis.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.