[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/generate_bounding_box_proposals#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/image/generate_bounding_box_proposals)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/image/generate_bounding_box_proposals?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fimage%2Fgenerate_bounding_box_proposals&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/generate_bounding_box_proposals#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/generate_bounding_box_proposals#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.generate\_bounding\_box\_proposals Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/generate_bounding_box_proposals#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/generate_bounding_box_proposals#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L5928-L5976)

Generate bounding box proposals from encoded bounding boxes.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.generate_bounding_box_proposals`](https://www.tensorflow.org/api_docs/python/tf/image/generate_bounding_box_proposals)

tf.image.generate_bounding_box_proposals(
        scores,
        bbox_deltas,
        image_info,
        anchors,
        nms_threshold=0.7,
        pre_nms_topn=6000,
        min_size=16,
        post_nms_topn=300,
        name=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `scores` | A 4-D float `Tensor` of shape `[num_images, height, width, num_achors]` containing scores of the boxes for given anchors, can be unsorted. |
| `bbox_deltas` | A 4-D float `Tensor` of shape `[num_images, height, width, 4 x num_anchors]` encoding boxes with respect to each anchor. Coordinates are given in the form `[dy, dx, dh, dw]`. |
| `image_info` | A 2-D float `Tensor` of shape `[num_images, 5]` containing image information Height, Width, Scale. |
| `anchors` | A 2-D float `Tensor` of shape `[num_anchors, 4]` describing the anchor boxes. Boxes are formatted in the form `[y1, x1, y2, x2]`. |
| `nms_threshold` | A scalar float `Tensor` for non-maximal-suppression threshold. Defaults to 0.7. |
| `pre_nms_topn` | A scalar int `Tensor` for the number of top scoring boxes to be used as input. Defaults to 6000. |
| `min_size` | A scalar float `Tensor`. Any box that has a smaller size than min\_size will be discarded. Defaults to 16. |
| `post_nms_topn` | An integer. Maximum number of rois in the output. |
| `name` | A name for this operation (optional). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `rois` | Region of interest boxes sorted by their scores. |
| `roi_probabilities` | scores of the ROI boxes in the ROIs' `Tensor`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.