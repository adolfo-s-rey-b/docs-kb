[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/maximum#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/maximum)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/maximum?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/maximum#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/maximum#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/maximum#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.maximum Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/maximum#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/maximum#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/maximum#returns)
    

Returns the max of x and y (i.e. x > y ? x : y) element-wise.

#### View aliases

**Main aliases**

[`tf.maximum`](https://www.tensorflow.org/api_docs/python/tf/math/maximum)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.maximum`](https://www.tensorflow.org/api_docs/python/tf/math/maximum)

tf.math.maximum(
        x: Annotated[Any, tf.raw_ops.Any],
        y: Annotated[Any, tf.raw_ops.Any],
        name=None
    ) -> Annotated[Any, tf.raw_ops.Any]

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Extension types](https://www.tensorflow.org/guide/extension_type)<br>    <br>*   [Introduction to graphs and tf.function](https://www.tensorflow.org/guide/intro_to_graphs) | *   [Generate music with an RNN](https://www.tensorflow.org/tutorials/audio/music_generation)<br>    <br>*   [Instance Segmentation with Model Garden](https://www.tensorflow.org/tfmodels/vision/instance_segmentation)<br>    <br>*   [Graph regularization for sentiment classification using synthesized graphs](https://www.tensorflow.org/neural_structured_learning/tutorials/graph_keras_lstm_imdb)<br>    <br>*   [Substantial Undocumented Infection Facilitates the Rapid Dissemination of Novel Coronavirus (SARS-CoV2)](https://www.tensorflow.org/probability/examples/Undocumented_Infection_and_the_Dissemination_of_SARS-CoV2)<br>    <br>*   [Human Pose Classification with MoveNet and TensorFlow Lite](https://www.tensorflow.org/lite/tutorials/pose_classification) |

#### Example:

    x = tf.constant([0., 0., 0., 0.])

Note that `maximum` supports [broadcast semantics](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)
 for `x` and `y`.

    x = tf.constant([-5., 0., 0., 0.])

The reduction version of this elementwise operation is [`tf.math.reduce_max`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_max)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int8`, `uint8`, `int16`, `uint16`, `int32`, `uint32`, `int64`, `uint64`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `x`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.