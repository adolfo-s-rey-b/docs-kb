[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/non_max_suppression_overlaps#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/image/non_max_suppression_overlaps)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/image/non_max_suppression_overlaps?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/non_max_suppression_overlaps#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/non_max_suppression_overlaps#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.non\_max\_suppression\_overlaps Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/non_max_suppression_overlaps#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/non_max_suppression_overlaps#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L3953-L3999)

Greedily selects a subset of bounding boxes in descending order of score.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.non_max_suppression_overlaps`](https://www.tensorflow.org/api_docs/python/tf/image/non_max_suppression_overlaps)

tf.image.non_max_suppression_overlaps(
        overlaps,
        scores,
        max_output_size,
        overlap_threshold=0.5,
        score_threshold=float('-inf'),
        name=None
    )

Prunes away boxes that have high overlap with previously selected boxes. N-by-n overlap values are supplied as square matrix. The output of this operation is a set of integers indexing into the input collection of bounding boxes representing the selected boxes. The bounding box coordinates corresponding to the selected indices can then be obtained using the [`tf.gather`](https://www.tensorflow.org/api_docs/python/tf/gather)
 operation. For example:

  selected_indices = tf.image.non_max_suppression_overlaps(
          overlaps, scores, max_output_size, iou_threshold)
      selected_boxes = tf.gather(boxes, selected_indices)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `overlaps` | A 2-D float `Tensor` of shape `[num_boxes, num_boxes]` representing the n-by-n box overlap values. |
| `scores` | A 1-D float `Tensor` of shape `[num_boxes]` representing a single score corresponding to each box (each row of boxes). |
| `max_output_size` | A scalar integer `Tensor` representing the maximum number of boxes to be selected by non-max suppression. |
| `overlap_threshold` | A 0-D float tensor representing the threshold for deciding whether boxes overlap too much with respect to the provided overlap values. |
| `score_threshold` | A 0-D float tensor representing the threshold for deciding when to remove boxes based on score. |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `selected_indices` | A 1-D integer `Tensor` of shape `[M]` representing the selected indices from the overlaps tensor, where `M <= max_output_size`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.