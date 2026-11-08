[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/bbox_generalized_overlap#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/bbox_generalized_overlap)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/bbox_generalized_overlap?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fvision%2Fbox_ops%2Fbbox_generalized_overlap&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/bbox_generalized_overlap#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/bbox_generalized_overlap#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.box\_ops.bbox\_generalized\_overlap Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/bbox_generalized_overlap#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/bbox_generalized_overlap#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/box_ops.py#L673-L740)

Calculates the GIOU between proposal and ground truth boxes.

tfm.vision.box_ops.bbox_generalized_overlap(
        boxes, gt_boxes
    )

The generalized intersection of union is an adjustment of the traditional IOU metric which provides continuous updates even for predictions with no overlap. This metric is defined in [https://giou.stanford.edu/GIoU.pdf](https://giou.stanford.edu/GIoU.pdf)
 Note, some `gt_boxes` may have been padded. The returned `giou` tensor for these boxes will be -1.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `boxes` | a `Tensor` with a shape of \[batch\_size, N, 4\]. N is the number of proposals before groundtruth assignment (e.g., rpn\_post\_nms\_topn). The last dimension is the pixel coordinates in \[ymin, xmin, ymax, xmax\] form. |
| `gt_boxes` | a `Tensor` with a shape of \[batch\_size, max\_num\_instances, 4\]. This tensor may have paddings with a negative value and will also be in the \[ymin, xmin, ymax, xmax\] format. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `giou` | a `Tensor` with as a shape of \[batch\_size, N, max\_num\_instances\]. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.