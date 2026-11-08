[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor/RpnAnchorLabeler#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor/RpnAnchorLabeler)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor/RpnAnchorLabeler?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fvision%2Fanchor%2FRpnAnchorLabeler&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor/RpnAnchorLabeler#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor/RpnAnchorLabeler#methods)
    *   [label\_anchors](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor/RpnAnchorLabeler#label_anchors)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.anchor.RpnAnchorLabeler Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor/RpnAnchorLabeler#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor/RpnAnchorLabeler#methods)
    *   [label\_anchors](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor/RpnAnchorLabeler#label_anchors)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/anchor.py#L275-L408)

Labeler for Region Proposal Network.

Inherits From: [`AnchorLabeler`](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor/AnchorLabeler)

tfm.vision.anchor.RpnAnchorLabeler(
        match_threshold=0.7,
        unmatched_threshold=0.3,
        rpn_batch_size_per_im=256,
        rpn_fg_fraction=0.5
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `match_threshold` | a float number between 0 and 1 representing the lower-bound threshold to assign positive labels for anchors. An anchor with a score over the threshold is labeled positive. |
| `unmatched_threshold` | a float number between 0 and 1 representing the upper-bound threshold to assign negative labels for anchors. An anchor with a score below the threshold is labeled negative. |
| `box_coder_weights` | Optional `list` of 4 positive floats to scale y, x, h, and w when encoding box coordinates. If set to None, does not perform scaling. For Faster RCNN, the open-source implementation recommends using \[10.0, 10.0, 5.0, 5.0\]. |

Methods
-------

### `label_anchors`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/anchor.py#L343-L408)

label_anchors(
        anchor_boxes: Dict[str, tf.Tensor],
        gt_boxes: tf.Tensor,
        gt_labels: tf.Tensor
    ) -> Tuple[Dict[str, tf.Tensor], Dict[str, tf.Tensor]]

Labels anchors with ground truth inputs.

|     |     |
| --- | --- |
| Args |     |
| `anchor_boxes` | An ordered dictionary with keys \[min\_level, min\_level+1, ..., max\_level\]. The values are tensor with shape \[height\_l, width\_l, num\_anchors\_per\_location \* 4\]. The height\_l and width\_l represent the dimension of the feature pyramid at l-th level. For each anchor box, the tensor stores \[y0, x0, y1, x1\] for the four corners. |
| `gt_boxes` | A float tensor with shape \[N, 4\] representing ground-truth boxes. For each row, it stores \[y0, x0, y1, x1\] for four corners of a box. |
| `gt_labels` | A integer tensor with shape \[N, 1\] representing ground-truth classes. |

|     |     |
| --- | --- |
| Returns |     |
| `score_targets_dict` | An ordered dictionary with keys \[min\_level, min\_level+1, ..., max\_level\]. The values are tensor with shape \[height\_l, width\_l, num\_anchors\_per\_location\]. The height\_l and width\_l represent the dimension of class logits at l-th level. |
| `box_targets_dict` | An ordered dictionary with keys \[min\_level, min\_level+1, ..., max\_level\]. The values are tensor with shape \[height\_l, width\_l, num\_anchors\_per\_location \* 4\]. The height\_l and width\_l represent the dimension of bounding box regression output at l-th level. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.