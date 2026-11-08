[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/activations/selu#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/activations/selu)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/activations/selu?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/activations/selu#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.activations.selu Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/activations/selu#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/activations/activations.py#L197-L234)

Scaled Exponential Linear Unit (SELU).

tf.keras.activations.selu(
        x
    )

The Scaled Exponential Linear Unit (SELU) activation function is defined as:

*   `scale * x` if `x > 0`
*   `scale * alpha * (exp(x) - 1)` if `x < 0`

where `alpha` and `scale` are pre-defined constants (`alpha=1.67326324` and `scale=1.05070098`).

Basically, the SELU activation function multiplies `scale` (> 1) with the output of the [`keras.activations.elu`](https://www.tensorflow.org/api_docs/python/tf/keras/activations/elu)
 function to ensure a slope larger than one for positive inputs.

The values of `alpha` and `scale` are chosen so that the mean and variance of the inputs are preserved between two consecutive layers as long as the weights are initialized correctly (see [`keras.initializers.LecunNormal`](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/LecunNormal)
 initializer) and the number of input units is "large enough" (see reference paper for more information).

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |

#### Notes:

*   To be used together with the [`keras.initializers.LecunNormal`](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/LecunNormal)
     initializer.
*   To be used together with the dropout variant [`keras.layers.AlphaDropout`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AlphaDropout)
     (rather than regular dropout).

#### Reference:

*   [Klambauer et al., 2017](https://arxiv.org/abs/1706.02515)
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.