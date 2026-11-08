[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/Scale#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/Scale)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/Scale?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/Scale#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/Scale#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/Scale#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.layers.Scale Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/Scale#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/Scale#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/Scale#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/layers/nn_layers.py#L406-L456)

Scales the input by a trainable scalar weight.

tfm.vision.layers.Scale(
        initializer: tf_keras.initializers.Initializer = 'ones',
        regularizer: Optional[tf_keras.regularizers.Regularizer] = None,
        **kwargs
    )

This is useful for applying ReZero to layers, which improves convergence speed. This implements the paper: ReZero is All You Need: Fast Convergence at Large Depth. ([https://arxiv.org/pdf/2003.04887.pdf](https://arxiv.org/pdf/2003.04887.pdf)
).

|     |     |
| --- | --- |
| Args<br>---- |     |
| `initializer` | A `str` of initializer for the scalar weight. |
| `regularizer` | A `tf_keras.regularizers.Regularizer` for the scalar weight. |
| `**kwargs` | Additional keyword arguments to be passed to this layer. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/layers/nn_layers.py#L453-L456)

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