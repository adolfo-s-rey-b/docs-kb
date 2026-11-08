[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/relu#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/relu)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/relu?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/nn/relu#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/relu#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/relu#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.relu Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/nn/relu#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/relu#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/relu#returns)
    

Computes rectified linear: `max(features, 0)`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.nn.relu`](https://www.tensorflow.org/api_docs/python/tf/nn/relu)

tf.nn.relu(
        features: Annotated[Any, TV_Relu_T], name=None
    ) -> Annotated[Any, TV_Relu_T]

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Introduction to modules, layers, and models](https://www.tensorflow.org/guide/intro_to_modules)<br>    <br>*   [Multilayer perceptrons for digit recognition with Core APIs](https://www.tensorflow.org/guide/core/mlp_core)<br>    <br>*   [Understanding masking & padding](https://www.tensorflow.org/guide/keras/understanding_masking_and_padding) | *   [Custom layers](https://www.tensorflow.org/tutorials/customization/custom_layers)<br>    <br>*   [Generating Images with BigBiGAN](https://www.tensorflow.org/hub/tutorials/bigbigan_with_tf_hub)<br>    <br>*   [Examining the TensorFlow Graph](https://www.tensorflow.org/tensorboard/graphs) |

See: [https://en.wikipedia.org/wiki/Rectifier\_(neural\_networks)](https://en.wikipedia.org/wiki/Rectifier_(neural_networks))
 Example usage:

>>> tf.nn.relu([-2., 0., 3.]).numpy()
    array([0., 0., 3.], dtype=float32)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `features` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`, `qint8`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `features`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.