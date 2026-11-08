[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/mask_ops/instance_masks_overlap#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/mask_ops/instance_masks_overlap)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/mask_ops/instance_masks_overlap?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/mask_ops/instance_masks_overlap#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/mask_ops/instance_masks_overlap#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.mask\_ops.instance\_masks\_overlap Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/mask_ops/instance_masks_overlap#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/mask_ops/instance_masks_overlap#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/mask_ops.py#L191-L267)

Calculates the IoUs and IoAs between the detection masks and the ground truth masks.

tfm.vision.mask_ops.instance_masks_overlap(
        boxes: tf.Tensor,
        masks: tf.Tensor,
        gt_boxes: tf.Tensor,
        gt_masks: tf.Tensor,
        output_size: List[int],
        mask_binarize_threshold: float = 0.5
    ) -> Tuple[tf.Tensor, tf.Tensor]

IoU: intersection over union. IoA: intersection over the area of the detection masks.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `boxes` | a tensor with a shape of \[batch\_size, N, 4\]. The last dimension is the pixel coordinates in \[ymin, xmin, ymax, xmax\] form. |
| `masks` | a float tensor with a shape of \[batch\_size, N, mask\_height, mask\_width\] representing the instance masks w.r.t. the `boxes`. |
| `gt_boxes` | a tensor with a shape of \[batch\_size, M, 4\]. The last dimension is the pixel coordinates in \[ymin, xmin, ymax, xmax\] form. |
| `gt_masks` | a float tensor with a shape of \[batch\_size, M, gt\_mask\_height, gt\_mask\_width\] representing the instance masks w.r.t. the `gt_boxes`. |
| `output_size` | two integers that represent the height and width of the output masks. |
| `mask_binarize_threshold` | a float representing the threshold for binarizing mask values. Default value is 0.5. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `iou` | a tensor with as a shape of \[batch\_size, N, M\]. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.