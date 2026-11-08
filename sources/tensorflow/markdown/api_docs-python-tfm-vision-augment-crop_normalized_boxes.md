[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/crop_normalized_boxes#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/crop_normalized_boxes)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/crop_normalized_boxes?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fvision%2Faugment%2Fcrop_normalized_boxes&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/crop_normalized_boxes#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/crop_normalized_boxes#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.augment.crop\_normalized\_boxes Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/crop_normalized_boxes#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/crop_normalized_boxes#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L2808-L2832)

Crop normalized boxes.

tfm.vision.augment.crop_normalized_boxes(
        bboxes: tf.Tensor,
        ori_image_size: tf.Tensor,
        new_image_size: tf.Tensor,
        offset: tf.Tensor
    ) -> tf.Tensor

|     |     |
| --- | --- |
| Args<br>---- |     |
| `bboxes` | a float tensor of shape \[N, 4\] representing normalized box coordinates. |
| `ori_image_size` | an int tensor of shape \[2\] representing the original image size. |
| `new_image_size` | an int tensor of shape \[2\] representing the cropped image size. |
| `offset` | an int tensor of shape \[2\] representing the offset of the crop. |

|     |
| --- |
| Returns<br>------- |     |
| a tensor of shape \[N, 4\] representing the new normalized bounding box coordinates in the new cropped image. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.