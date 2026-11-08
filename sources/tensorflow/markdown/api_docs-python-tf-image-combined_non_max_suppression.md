[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/combined_non_max_suppression#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/image/combined_non_max_suppression)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/image/combined_non_max_suppression?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/combined_non_max_suppression#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/combined_non_max_suppression#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.combined\_non\_max\_suppression Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/combined_non_max_suppression#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/combined_non_max_suppression#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L5162-L5244)

Greedily selects a subset of bounding boxes in descending order of score.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.combined_non_max_suppression`](https://www.tensorflow.org/api_docs/python/tf/image/combined_non_max_suppression)

tf.image.combined_non_max_suppression(
        boxes,
        scores,
        max_output_size_per_class,
        max_total_size,
        iou_threshold=0.5,
        score_threshold=float('-inf'),
        pad_per_class=False,
        clip_boxes=True,
        name=None
    )

This operation performs non\_max\_suppression on the inputs per batch, across all classes. Prunes away boxes that have high intersection-over-union (IOU) overlap with previously selected boxes. Bounding boxes are supplied as \[y1, x1, y2, x2\], where (y1, x1) and (y2, x2) are the coordinates of any diagonal pair of box corners and the coordinates can be provided as normalized (i.e., lying in the interval \[0, 1\]) or absolute. Note that this algorithm is agnostic to where the origin is in the coordinate system. Also note that this algorithm is invariant to orthogonal transformations and translations of the coordinate system; thus translating or reflections of the coordinate system result in the same boxes being selected by the algorithm. The output of this operation is the final boxes, scores and classes tensor returned after performing non\_max\_suppression.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `boxes` | A 4-D float `Tensor` of shape `[batch_size, num_boxes, q, 4]`. If `q` is 1 then same boxes are used for all classes otherwise, if `q` is equal to number of classes, class-specific boxes are used. |
| `scores` | A 3-D float `Tensor` of shape `[batch_size, num_boxes, num_classes]` representing a single score corresponding to each box (each row of boxes). |
| `max_output_size_per_class` | A scalar integer `Tensor` representing the maximum number of boxes to be selected by non-max suppression per class |
| `max_total_size` | A int32 scalar representing maximum number of boxes retained over all classes. Note that setting this value to a large number may result in OOM error depending on the system workload. |
| `iou_threshold` | A float representing the threshold for deciding whether boxes overlap too much with respect to IOU. |
| `score_threshold` | A float representing the threshold for deciding when to remove boxes based on score. |
| `pad_per_class` | If false, the output nmsed boxes, scores and classes are padded/clipped to `max_total_size`. If true, the output nmsed boxes, scores and classes are padded to be of length `max_size_per_class`\*`num_classes`, unless it exceeds `max_total_size` in which case it is clipped to `max_total_size`. Defaults to false. |
| `clip_boxes` | If true, the coordinates of output nmsed boxes will be clipped to \[0, 1\]. If false, output the box coordinates as it is. Defaults to true. |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `'nmsed_boxes'` | A \[batch\_size, max\_detections, 4\] float32 tensor containing the non-max suppressed boxes. |
| `'nmsed_scores'` | A \[batch\_size, max\_detections\] float32 tensor containing the scores for the boxes. |
| `'nmsed_classes'` | A \[batch\_size, max\_detections\] float32 tensor containing the class for boxes. |
| `'valid_detections'` | A \[batch\_size\] int32 tensor indicating the number of valid detections per batch item. Only the top valid\_detections\[i\] entries in nms\_boxes\[i\], nms\_scores\[i\] and nms\_class\[i\] are valid. The rest of the entries are zero paddings. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.