[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/center_crop_image_v2#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/center_crop_image_v2)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/center_crop_image_v2?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/center_crop_image_v2#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/center_crop_image_v2#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.preprocess\_ops.center\_crop\_image\_v2 Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/center_crop_image_v2#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/center_crop_image_v2#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/preprocess_ops.py#L566-L604)

Center crop a square shape slice from the input image.

tfm.vision.preprocess_ops.center_crop_image_v2(
        image_bytes,
        image_shape,
        center_crop_fraction: float = CENTER_CROP_FRACTION
    )

It crops a square shape slice from the image. The side of the actual crop is 224 / 256 = 0.875 of the short side of the original image. References: \[1\] Very Deep Convolutional Networks for Large-Scale Image Recognition [https://arxiv.org/abs/1409.1556](https://arxiv.org/abs/1409.1556)
 \[2\] Deep Residual Learning for Image Recognition [https://arxiv.org/abs/1512.03385](https://arxiv.org/abs/1512.03385)

This is a faster version of `center_crop_image` which takes the original image bytes and image size as the inputs, and partially decode the JPEG bytes according to the center crop.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `image_bytes` | a Tensor of type string representing the raw image bytes. |
| `image_shape` | a Tensor specifying the shape of the raw image. |
| `center_crop_fraction` | a float of ratio between the side of the cropped image and the short side of the original image |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `cropped_image` | a Tensor representing the center cropped image. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.