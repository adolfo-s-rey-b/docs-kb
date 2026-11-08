[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/ROISampler#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/ROISampler)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/ROISampler?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/ROISampler#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/ROISampler#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/ROISampler#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.layers.ROISampler Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/ROISampler#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/ROISampler#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/ROISampler#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/layers/roi_sampler.py#L30-L206)

Samples ROIs and assigns targets to the sampled ROIs.

tfm.vision.layers.ROISampler(
        mix_gt_boxes: bool = True,
        num_sampled_rois: int = 512,
        foreground_fraction: float = 0.25,
        foreground_iou_threshold: float = 0.5,
        background_iou_high_threshold: float = 0.5,
        background_iou_low_threshold: float = 0,
        skip_subsampling: bool = False,
        **kwargs
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `mix_gt_boxes` | A `bool` of whether to mix the groundtruth boxes with proposed ROIs. |
| `num_sampled_rois` | An `int` of the number of sampled ROIs per image. |
| `foreground_fraction` | A `float` in \[0, 1\], what percentage of proposed ROIs should be sampled from the foreground boxes. |
| `foreground_iou_threshold` | A `float` that represents the IoU threshold for a box to be considered as positive (if >= `foreground_iou_threshold`). |
| `background_iou_high_threshold` | A `float` that represents the IoU threshold for a box to be considered as negative (if overlap in \[`background_iou_low_threshold`, `background_iou_high_threshold`\]). |
| `background_iou_low_threshold` | A `float` that represents the IoU threshold for a box to be considered as negative (if overlap in \[`background_iou_low_threshold`, `background_iou_high_threshold`\]) |
| `skip_subsampling` | a bool that determines if we want to skip the sampling procedure than balances the fg/bg classes. Used for upper frcnn layers in cascade RCNN. |
| `**kwargs` | Additional keyword arguments passed to Layer. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/layers/roi_sampler.py#L87-L199)

call(
        boxes: tf.Tensor,
        gt_boxes: tf.Tensor,
        gt_classes: tf.Tensor,
        gt_outer_boxes: Optional[tf.Tensor] = None
    ) -> ROISamplerReturnType

Assigns the proposals with groundtruth classes and performs subsmpling.

Given `proposed_boxes`, `gt_boxes`, and `gt_classes`, the function uses the following algorithm to generate the final `num_samples_per_image` RoIs.

1.  Calculates the IoU between each proposal box and each gt\_boxes.
2.  Assigns each proposed box with a groundtruth class and box by choosing the largest IoU overlap.
3.  Samples `num_samples_per_image` boxes from all proposed boxes, and returns box\_targets, class\_targets, and RoIs.

|     |     |
| --- | --- |
| Args |     |
| `boxes` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of shape of \[batch\_size, N, 4\]. N is the number of proposals before groundtruth assignment. The last dimension is the box coordinates w.r.t. the scaled images in \[ymin, xmin, ymax, xmax\] format. |
| `gt_boxes` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of shape of \[batch\_size, MAX\_NUM\_INSTANCES, 4\]. The coordinates of gt\_boxes are in the pixel coordinates of the scaled image. This tensor might have padding of values -1 indicating the invalid box coordinates. |
| `gt_classes` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> with a shape of \[batch\_size, MAX\_NUM\_INSTANCES\]. This tensor might have paddings with values of -1 indicating the invalid classes. |
| `gt_outer_boxes` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of shape of \[batch\_size, MAX\_NUM\_INSTANCES, 4\]. The corrdinates of gt\_outer\_boxes are in the pixel coordinates of the scaled image. This tensor might have padding of values -1 indicating the invalid box coordinates. Ignored if not provided. |

|     |     |
| --- | --- |
| Returns |     |
| `sampled_rois` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of shape of \[batch\_size, K, 4\], representing the coordinates of the sampled RoIs, where K is the number of the sampled RoIs, i.e. K = num\_samples\_per\_image. |
| `sampled_gt_boxes` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of shape of \[batch\_size, K, 4\], storing the box coordinates of the matched groundtruth boxes of the samples RoIs. |
| `sampled_gt_outer_boxes` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of shape of \[batch\_size, K, 4\], storing the box coordinates of the matched groundtruth outer boxes of the samples RoIs. This field is missing if gt\_outer\_boxes is None. |
| `sampled_gt_classes` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of shape of \[batch\_size, K\], storing the classes of the matched groundtruth boxes of the sampled RoIs. |
| `sampled_gt_indices` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of shape of \[batch\_size, K\], storing the indices of the sampled groudntruth boxes in the original `gt_boxes` tensor, i.e., gt\_boxes\[sampled\_gt\_indices\[:, i\]\] = sampled\_gt\_boxes\[:, i\]. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.