[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/iou_similarity/IouSimilarity#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.iou\_similarity.IouSimilarity Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/iou_similarity.py#L100-L167)

Class to compute similarity based on Intersection over Union (IOU) metric.

tfm.vision.iou_similarity.IouSimilarity(
        mask_val=-1
    )

Methods
-------

### `__call__`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/iou_similarity.py#L108-L167)

__call__(
        boxes_1, boxes_2, boxes_1_masks=None, boxes_2_masks=None
    )

Compute pairwise IOU similarity between ground truth boxes and anchors.

B: batch\_size N: Number of groundtruth boxes. M: Number of anchor boxes.

|     |     |
| --- | --- |
| Args |     |
| `boxes_1` | a float Tensor with M or B \* M boxes. |
| `boxes_2` | a float Tensor with N or B \* N boxes, the rank must be less than or equal to rank of `boxes_1`. |
| `boxes_1_masks` | a boolean Tensor with M or B \* M boxes. Optional. |
| `boxes_2_masks` | a boolean Tensor with N or B \* N boxes. Optional. |

|     |
| --- |
| Returns |     |
| A Tensor with shape \[M, N\] or \[B, M, N\] representing pairwise iou scores, anchor per row and groundtruth\_box per colulmn. |     |

|     |     |
| --- | --- |
| Input shape |     |
| `boxes_1` | \[N, 4\], or \[B, N, 4\] |
| `boxes_2` | \[M, 4\], or \[B, M, 4\] |
| `boxes_1_masks` | \[N, 1\], or \[B, N, 1\] |
| `boxes_2_masks` | \[M, 1\], or \[B, M, 1\] |

|     |
| --- |
| Output shape |     |
| \[M, N\], or \[B, M, N\] |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.