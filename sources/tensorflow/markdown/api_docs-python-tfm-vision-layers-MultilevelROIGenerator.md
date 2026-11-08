[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/MultilevelROIGenerator#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/MultilevelROIGenerator)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/MultilevelROIGenerator?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/MultilevelROIGenerator#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/MultilevelROIGenerator#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/MultilevelROIGenerator#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.layers.MultilevelROIGenerator Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/MultilevelROIGenerator#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/MultilevelROIGenerator#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/MultilevelROIGenerator#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/layers/roi_generator.py#L178-L312)

Proposes RoIs for the second stage processing.

tfm.vision.layers.MultilevelROIGenerator(
        pre_nms_top_k: int = 2000,
        pre_nms_score_threshold: float = 0.0,
        pre_nms_min_size_threshold: float = 0.0,
        nms_iou_threshold: float = 0.7,
        num_proposals: int = 1000,
        test_pre_nms_top_k: int = 1000,
        test_pre_nms_score_threshold: float = 0.0,
        test_pre_nms_min_size_threshold: float = 0.0,
        test_nms_iou_threshold: float = 0.7,
        test_num_proposals: int = 1000,
        use_batched_nms: bool = False,
        **kwargs
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `pre_nms_top_k` | An `int` of the number of top scores proposals to be kept before applying NMS. |
| `pre_nms_score_threshold` | A `float` of the score threshold to apply before applying NMS. Proposals whose scores are below this threshold are thrown away. |
| `pre_nms_min_size_threshold` | A `float` of the threshold of each side of the box (w.r.t. the scaled image). Proposals whose sides are below this threshold are thrown away. |
| `nms_iou_threshold` | A `float` in \[0, 1\], the NMS IoU threshold. |
| `num_proposals` | An `int` of the final number of proposals to generate. |
| `test_pre_nms_top_k` | An `int` of the number of top scores proposals to be kept before applying NMS in testing. |
| `test_pre_nms_score_threshold` | A `float` of the score threshold to apply before applying NMS in testing. Proposals whose scores are below this threshold are thrown away. |
| `test_pre_nms_min_size_threshold` | A `float` of the threshold of each side of the box (w.r.t. the scaled image) in testing. Proposals whose sides are below this threshold are thrown away. |
| `test_nms_iou_threshold` | A `float` in \[0, 1\] of the NMS IoU threshold in testing. |
| `test_num_proposals` | An `int` of the final number of proposals to generate in testing. |
| `use_batched_nms` | A `bool` of whether or not use [`tf.image.combined_non_max_suppression`](https://www.tensorflow.org/api_docs/python/tf/image/combined_non_max_suppression)<br>. |
| `**kwargs` | Additional keyword arguments passed to Layer. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/layers/roi_generator.py#L241-L305)

call(
        raw_boxes: Mapping[str, tf.Tensor],
        raw_scores: Mapping[str, tf.Tensor],
        anchor_boxes: Mapping[str, tf.Tensor],
        image_shape: tf.Tensor,
        training: Optional[bool] = None
    )

Proposes RoIs given a group of candidates from different FPN levels.

The following describes the steps:

1.  For each individual level: a. Apply sigmoid transform if specified. b. Decode boxes if specified. c. Clip boxes if specified. d. Filter small boxes and those fall outside image if specified. e. Apply pre-NMS filtering including pre-NMS top k and score thresholding. f. Apply NMS.
2.  Aggregate post-NMS boxes from each level.
3.  Apply an overall top k to generate the final selected RoIs.

|     |     |
| --- | --- |
| Args |     |
| `raw_boxes` | A `dict` with keys representing FPN levels and values representing box tenors of shape \[batch, feature\_h, feature\_w, num\_anchors \* 4\]. |
| `raw_scores` | A `dict` with keys representing FPN levels and values representing logit tensors of shape \[batch, feature\_h, feature\_w, num\_anchors\]. |
| `anchor_boxes` | A `dict` with keys representing FPN levels and values representing anchor box tensors of shape \[batch, feature\_h \* feature\_w \* num\_anchors, 4\]. |
| `image_shape` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of shape \[batch, 2\] where the last dimension are \[height, width\] of the scaled image. |
| `training` | A `bool` that indicates whether it is in training mode. |

|     |     |
| --- | --- |
| Returns |     |
| `roi_boxes` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of shape \[batch, num\_proposals, 4\], the proposed ROIs in the scaled image coordinate. |
| `roi_scores` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of shape \[batch, num\_proposals\], scores of the proposed ROIs. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.