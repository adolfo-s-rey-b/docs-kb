[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/cutout#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/cutout)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/cutout?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/cutout#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/cutout#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.augment.cutout Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/cutout#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/cutout#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L580-L617)

Apply cutout ([https://arxiv.org/abs/1708.04552](https://arxiv.org/abs/1708.04552)
) to image.

tfm.vision.augment.cutout(
        image: tf.Tensor, pad_size: int, replace: int = 0
    ) -> tf.Tensor

This operation applies a (2_pad\_size x 2_pad\_size) mask of zeros to a random location within `image`. The pixel values filled in will be of the value `replace`. The location where the mask will be applied is randomly chosen uniformly over the whole image.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `image` | An image Tensor of type uint8. |
| `pad_size` | Specifies how big the zero mask that will be generated is that is applied to the image. The mask will be of size (2_pad\_size x 2_pad\_size). |
| `replace` | What pixel value to fill in the image in the area that has the cutout mask applied to it. |

|     |
| --- |
| Returns<br>------- |     |
| An image Tensor that is of type uint8. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.