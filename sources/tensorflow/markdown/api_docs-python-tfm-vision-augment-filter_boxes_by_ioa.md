[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/filter_boxes_by_ioa#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/filter_boxes_by_ioa)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/filter_boxes_by_ioa?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fvision%2Faugment%2Ffilter_boxes_by_ioa&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/filter_boxes_by_ioa#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/filter_boxes_by_ioa#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.augment.filter\_boxes\_by\_ioa Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/filter_boxes_by_ioa#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/filter_boxes_by_ioa#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L2783-L2805)

Filter boxes by intersection over area (IOA).

tfm.vision.augment.filter_boxes_by_ioa(
        bboxes: tf.Tensor, crop_box: tf.Tensor, min_box_overlap: float
    ) -> tf.Tensor

The boxes with IOA less than min\_box\_overlap will be replaced by (0, 0, 0, 0) so they can be filtered out later.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `bboxes` | a float tensor of shape \[N, 4\] representing normalized bounding box coordinates. |
| `crop_box` | a float tensor of shape \[1, 1, 4\] representing the normalized crop box. |
| `min_box_overlap` | minimum overlap of the box with the crop box to keep the box. |

|     |
| --- |
| Returns<br>------- |     |
| a tensor of shape \[N, 4\] with filtered box coordinates replaced by 0. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.