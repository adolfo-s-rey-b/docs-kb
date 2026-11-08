[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/TemporalSoftmaxPool#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/TemporalSoftmaxPool)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/TemporalSoftmaxPool?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/TemporalSoftmaxPool#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/TemporalSoftmaxPool#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.layers.TemporalSoftmaxPool Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/TemporalSoftmaxPool#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/TemporalSoftmaxPool#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/layers/nn_layers.py#L459-L479)

Creates a network layer corresponding to temporal softmax pooling.

tfm.vision.layers.TemporalSoftmaxPool(
        trainable=True, name=None, dtype=None, dynamic=False, **kwargs
    )

This is useful for multi-class logits (used in e.g., Charades). Modified from AssembleNet Charades evaluation from:

Michael S. Ryoo, AJ Piergiovanni, Mingxing Tan, Anelia Angelova. AssembleNet: Searching for Multi-Stream Neural Connectivity in Video Architectures. ([https://arxiv.org/pdf/1905.13209.pdf](https://arxiv.org/pdf/1905.13209.pdf)
).

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/layers/nn_layers.py#L472-L479)

call(
        inputs
    )

Calls the layer with the given inputs.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.