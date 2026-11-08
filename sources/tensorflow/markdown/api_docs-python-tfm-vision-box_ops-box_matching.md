[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/box_matching#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/box_matching)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/box_matching?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/box_matching#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/box_matching#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.box\_ops.box\_matching Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/box_matching#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/box_matching#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/box_ops.py#L798-L864)

Matches boxes to groundtruth boxes.

tfm.vision.box_ops.box_matching(
        boxes, gt_boxes, gt_classes
    )

Given the proposal boxes and the groundtruth boxes and classes, perform the groundtruth matching by taking the argmax of the IoU between boxes and groundtruth boxes.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `boxes` | a tensor of shape of \[batch\_size, N, 4\] representing the box coordiantes to be matched to groundtruth boxes. |
| `gt_boxes` | a tensor of shape of \[batch\_size, MAX\_INSTANCES, 4\] representing the groundtruth box coordinates. It is padded with -1s to indicate the invalid boxes. |
| `gt_classes` | \[batch\_size, MAX\_INSTANCES\] representing the groundtruth box classes. It is padded with -1s to indicate the invalid classes. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `matched_gt_boxes` | a tensor of shape of \[batch\_size, N, 4\], representing the matched groundtruth box coordinates for each input box. If the box does not overlap with any groundtruth boxes, the matched boxes of it will be set to all 0s. |
| `matched_gt_classes` | a tensor of shape of \[batch\_size, N\], representing the matched groundtruth classes for each input box. If the box does not overlap with any groundtruth boxes, the matched box classes of it will be set to 0, which corresponds to the background class. |
| `matched_gt_indices` | a tensor of shape of \[batch\_size, N\], representing the indices of the matched groundtruth boxes in the original gt\_boxes tensor. If the box does not overlap with any groundtruth boxes, the index of the matched groundtruth will be set to -1. |
| `matched_iou` | a tensor of shape of \[batch\_size, N\], representing the IoU between the box and its matched groundtruth box. The matched IoU is the maximum IoU of the box and all the groundtruth boxes. |
| `iou` | a tensor of shape of \[batch\_size, N, K\], representing the IoU matrix between boxes and the groundtruth boxes. The IoU between a box and the invalid groundtruth boxes whose coordinates are \[-1, -1, -1, -1\] is -1. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.