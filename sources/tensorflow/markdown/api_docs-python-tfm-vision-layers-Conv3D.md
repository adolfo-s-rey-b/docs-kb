[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/Conv3D#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/Conv3D)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/Conv3D?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/Conv3D#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/Conv3D#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/Conv3D#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/Conv3D#call)
        
    *   [convolution\_op](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/Conv3D#convolution_op)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.layers.Conv3D Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/Conv3D#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/Conv3D#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/Conv3D#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/Conv3D#call)
        
    *   [convolution\_op](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/Conv3D#convolution_op)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/layers/nn_layers.py#L1015-L1068)

Conv3D layer supporting CausalConv.

Inherits From: [`CausalConvMixin`](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/CausalConvMixin)

tfm.vision.layers.Conv3D(
        *args, use_buffered_input=False, **kwargs
    )

Supports `padding='causal'` option (like in `tf_keras.layers.Conv1D`), which applies causal padding to the temporal dimension, and same padding in the spatial dimensions.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `*args` | Arguments to be passed. |
| `use_buffered_input` | A `bool`. If True, the input is expected to be padded beforehand. In effect, calling this layer will use 'valid' padding on the temporal dimension to simulate 'causal' padding. |
| `**kwargs` | Additional keyword arguments to be passed. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `use_buffered_input` |     |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/layers/nn_layers.py#L1048-L1054)

call(
        inputs
    )

Call the layer with the given inputs.

### `convolution_op`

convolution_op(
        inputs, kernel
    )

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.