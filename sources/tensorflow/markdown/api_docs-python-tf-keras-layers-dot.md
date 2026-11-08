[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/dot#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/dot)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/dot?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/dot#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/layers/dot#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.dot Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/dot#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/layers/dot#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/merging/dot.py#L360-L378)

Functional interface to the `Dot` layer.

tf.keras.layers.dot(
        inputs, axes=-1, **kwargs
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `inputs` | A list of input tensors (at least 2). |
| `axes` | Integer or tuple of integers, axis or axes along which to take the dot product. Note that axis `0` (the batch axis) cannot be included. |
| `normalize` | Whether to L2-normalize samples along the dot product axis before taking the dot product. If set to `True`, then the output of the dot product is the cosine proximity between the two samples. |
| `**kwargs` | Standard layer keyword arguments. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor, the dot product of the samples from the inputs. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.