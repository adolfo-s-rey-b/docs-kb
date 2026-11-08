[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/unwrap#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/unwrap)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/unwrap?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/unwrap#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/unwrap#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.augment.unwrap Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/unwrap#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/unwrap#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L1043-L1081)

Unwraps an image produced by wrap.

tfm.vision.augment.unwrap(
        image: tf.Tensor, replace: int
    ) -> tf.Tensor

Where there is a 0 in the last channel for every spatial position, the rest of the three channels in that spatial dimension are grayed (set to 128). Operations like translate and shear on a wrapped Tensor will leave 0s in empty locations. Some transformations look at the intensity of values to do preprocessing, and we want these empty pixels to assume the 'average' value, rather than pure black.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `image` | A 3D Image Tensor with 4 channels. |
| `replace` | A one or three value 1D tensor to fill empty pixels. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `image` | A 3D image Tensor with 3 channels. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.