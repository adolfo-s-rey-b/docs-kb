[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/nms/sorted_non_max_suppression_padded#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/nms/sorted_non_max_suppression_padded)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/nms/sorted_non_max_suppression_padded?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Assumption](https://www.tensorflow.org/api_docs/python/tfm/vision/nms/sorted_non_max_suppression_padded#assumption)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/nms/sorted_non_max_suppression_padded#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/nms/sorted_non_max_suppression_padded#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.nms.sorted\_non\_max\_suppression\_padded Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================================

*   On this page
*   [Assumption](https://www.tensorflow.org/api_docs/python/tfm/vision/nms/sorted_non_max_suppression_padded#assumption)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/nms/sorted_non_max_suppression_padded#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/nms/sorted_non_max_suppression_padded#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/nms.py#L106-L202)

A wrapper that handles non-maximum suppression.

tfm.vision.nms.sorted_non_max_suppression_padded(
        scores, boxes, max_output_size, iou_threshold
    )

|     |
| --- |
| Assumption<br>---------- |     |
| *   The boxes are sorted by scores unless the box is a dot (all coordinates are zero).<br>*   Boxes with higher scores can be used to suppress boxes with lower scores. |     |

The overal design of the algorithm is to handle boxes tile-by-tile:

boxes = boxes.pad\_to\_multiply\_of(tile\_size) num\_tiles = len(boxes) // tile\_size output\_boxes = \[\] for i in range(num\_tiles): box\_tile = boxes\[i_tile\_size : (i+1)_tile\_size\] for j in range(i - 1): suppressing\_tile = boxes\[j_tile\_size : (j+1)_tile\_size\] iou = bbox\_overlap(box\_tile, suppressing\_tile) # if the box is suppressed in iou, clear it to a dot box\_tile \*= \_update\_boxes(iou) # Iteratively handle the diagnal tile. iou = \_box\_overlap(box\_tile, box\_tile) iou\_changed = True while iou\_changed: # boxes that are not suppressed by anything else suppressing\_boxes = \_get\_suppressing\_boxes(iou) # boxes that are suppressed by suppressing\_boxes suppressed\_boxes = \_get\_suppressed\_boxes(iou, suppressing\_boxes) # clear iou to 0 for boxes that are suppressed, as they cannot be used # to suppress other boxes any more new\_iou = \_clear\_iou(iou, suppressed\_boxes) iou\_changed = (new\_iou != iou) iou = new\_iou # remaining boxes that can still suppress others, are selected boxes. output\_boxes.append(\_get\_suppressing\_boxes(iou)) if len(output\_boxes) >= max\_output\_size: break

|     |     |
| --- | --- |
| Args<br>---- |     |
| `scores` | a tensor with a shape of \[batch\_size, anchors\]. |
| `boxes` | a tensor with a shape of \[batch\_size, anchors, 4\]. |
| `max_output_size` | a scalar integer `Tensor` representing the maximum number of boxes to be selected by non max suppression. |
| `iou_threshold` | a float representing the threshold for deciding whether boxes overlap too much with respect to IOU. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `nms_scores` | a tensor with a shape of \[batch\_size, anchors\]. It has same dtype as input scores. |
| `nms_proposals` | a tensor with a shape of \[batch\_size, anchors, 4\]. It has same dtype as input boxes. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.