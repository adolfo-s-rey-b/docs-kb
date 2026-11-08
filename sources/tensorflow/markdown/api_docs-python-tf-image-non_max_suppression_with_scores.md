[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/non_max_suppression_with_scores#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/image/non_max_suppression_with_scores)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/image/non_max_suppression_with_scores?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/non_max_suppression_with_scores#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/non_max_suppression_with_scores#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.non\_max\_suppression\_with\_scores Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/non_max_suppression_with_scores#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/non_max_suppression_with_scores#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L3863-L3950)

Greedily selects a subset of bounding boxes in descending order of score.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.non_max_suppression_with_scores`](https://www.tensorflow.org/api_docs/python/tf/image/non_max_suppression_with_scores)

tf.image.non_max_suppression_with_scores(
        boxes,
        scores,
        max_output_size,
        iou_threshold=0.5,
        score_threshold=float('-inf'),
        soft_nms_sigma=0.0,
        name=None
    )

Prunes away boxes that have high intersection-over-union (IOU) overlap with previously selected boxes. Bounding boxes are supplied as `[y1, x1, y2, x2]`, where `(y1, x1)` and `(y2, x2)` are the coordinates of any diagonal pair of box corners and the coordinates can be provided as normalized (i.e., lying in the interval `[0, 1]`) or absolute. Note that this algorithm is agnostic to where the origin is in the coordinate system. Note that this algorithm is invariant to orthogonal transformations and translations of the coordinate system; thus translating or reflections of the coordinate system result in the same boxes being selected by the algorithm. The output of this operation is a set of integers indexing into the input collection of bounding boxes representing the selected boxes. The bounding box coordinates corresponding to the selected indices can then be obtained using the [`tf.gather`](https://www.tensorflow.org/api_docs/python/tf/gather)
 operation. For example:

  selected_indices, selected_scores = tf.image.non_max_suppression_padded(
          boxes, scores, max_output_size, iou_threshold=1.0, score_threshold=0.1,
          soft_nms_sigma=0.5)
      selected_boxes = tf.gather(boxes, selected_indices)

This function generalizes the [`tf.image.non_max_suppression`](https://www.tensorflow.org/api_docs/python/tf/image/non_max_suppression)
 op by also supporting a Soft-NMS (with Gaussian weighting) mode (c.f. Bodla et al, https://arxiv.org/abs/1704.04503) where boxes reduce the score of other overlapping boxes instead of directly causing them to be pruned. Consequently, in contrast to [`tf.image.non_max_suppression`](https://www.tensorflow.org/api_docs/python/tf/image/non_max_suppression)
, [`tf.image.non_max_suppression_with_scores`](https://www.tensorflow.org/api_docs/python/tf/image/non_max_suppression_with_scores)
 returns the new scores of each input box in the second output, `selected_scores`.

To enable this Soft-NMS mode, set the `soft_nms_sigma` parameter to be larger than 0. When `soft_nms_sigma` equals 0, the behavior of [`tf.image.non_max_suppression_with_scores`](https://www.tensorflow.org/api_docs/python/tf/image/non_max_suppression_with_scores)
 is identical to that of [`tf.image.non_max_suppression`](https://www.tensorflow.org/api_docs/python/tf/image/non_max_suppression)
 (except for the extra output) both in function and in running time.

Note that when `soft_nms_sigma` > 0, Soft-NMS is performed and `iou_threshold` is ignored. `iou_threshold` is only used for standard NMS.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `boxes` | A 2-D float `Tensor` of shape `[num_boxes, 4]`. |
| `scores` | A 1-D float `Tensor` of shape `[num_boxes]` representing a single score corresponding to each box (each row of boxes). |
| `max_output_size` | A scalar integer `Tensor` representing the maximum number of boxes to be selected by non-max suppression. |
| `iou_threshold` | A 0-D float tensor representing the threshold for deciding whether boxes overlap too much with respect to IOU. |
| `score_threshold` | A 0-D float tensor representing the threshold for deciding when to remove boxes based on score. |
| `soft_nms_sigma` | A 0-D float tensor representing the sigma parameter for Soft NMS; see Bodla et al (c.f. https://arxiv.org/abs/1704.04503). When `soft_nms_sigma=0.0` (which is default), we fall back to standard (hard) NMS. |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `selected_indices` | A 1-D integer `Tensor` of shape `[M]` representing the selected indices from the boxes tensor, where `M <= max_output_size`. |
| `selected_scores` | A 1-D float tensor of shape `[M]` representing the corresponding scores for each selected box, where `M <= max_output_size`. Scores only differ from corresponding input scores when using Soft NMS (i.e. when `soft_nms_sigma>0`) |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.