[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/SpatialAveragePool3D#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/SpatialAveragePool3D)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/SpatialAveragePool3D?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fvision%2Flayers%2FSpatialAveragePool3D&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/SpatialAveragePool3D#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/SpatialAveragePool3D#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/SpatialAveragePool3D#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.layers.SpatialAveragePool3D Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/SpatialAveragePool3D#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/SpatialAveragePool3D#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/SpatialAveragePool3D#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/layers/nn_layers.py#L784-L823)

Creates a global average pooling layer pooling across spatial dimentions.

tfm.vision.layers.SpatialAveragePool3D(
        keepdims: bool = False, **kwargs
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `keepdims` | A `bool`. If True, keep the averaged dimensions. |
| `**kwargs` | Additional keyword arguments to be passed to this layer. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/layers/nn_layers.py#L816-L823)

call(
        inputs, states=None, output_states: bool = False
    )

Calls the layer with the given inputs.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.