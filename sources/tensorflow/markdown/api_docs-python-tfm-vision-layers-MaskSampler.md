[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/MaskSampler#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/MaskSampler)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/MaskSampler?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fvision%2Flayers%2FMaskSampler&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/MaskSampler#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/MaskSampler#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.layers.MaskSampler Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/MaskSampler#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/MaskSampler#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/layers/mask_sampler.py#L102-L165)

Samples and creates mask training targets.

tfm.vision.layers.MaskSampler(
        mask_target_size: int, num_sampled_masks: int, **kwargs
    )

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/layers/mask_sampler.py#L113-L158)

call(
        candidate_rois: tf.Tensor,
        candidate_gt_boxes: tf.Tensor,
        candidate_gt_classes: tf.Tensor,
        candidate_gt_indices: tf.Tensor,
        gt_masks: tf.Tensor
    )

Samples and creates mask targets for training.

|     |     |
| --- | --- |
| Args |     |
| `candidate_rois` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of shape of \[batch\_size, N, 4\], where N is the number of candidate RoIs to be considered for mask sampling. It includes both positive and negative RoIs. The `num_mask_samples_per_image` positive RoIs will be sampled to create mask training targets. |
| `candidate_gt_boxes` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of shape of \[batch\_size, N, 4\], storing the corresponding groundtruth boxes to the `candidate_rois`. |
| `candidate_gt_classes` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of shape of \[batch\_size, N\], storing the corresponding groundtruth classes to the `candidate_rois`. 0 in the tensor corresponds to the background class, i.e. negative RoIs. |
| `candidate_gt_indices` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of shape \[batch\_size, N\], storing the corresponding groundtruth instance indices to the `candidate_gt_boxes`, i.e. gt\_boxes\[candidate\_gt\_indices\[:, i\]\] = candidate\_gt\_boxes\[:, i\], where gt\_boxes which is of shape \[batch\_size, MAX\_INSTANCES, 4\], M >= N, is the superset of candidate\_gt\_boxes. |
| `gt_masks` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of \[batch\_size, MAX\_INSTANCES, mask\_height, mask\_width\] containing all the groundtruth masks which sample masks are drawn from. after sampling. The output masks are resized w.r.t the sampled RoIs. |

|     |     |
| --- | --- |
| Returns |     |
| `foreground_rois` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of shape of \[batch\_size, K, 4\] storing the RoI that corresponds to the sampled foreground masks, where K = num\_mask\_samples\_per\_image. |
| `foreground_classes` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of shape of \[batch\_size, K\] storing the classes corresponding to the sampled foreground masks. |
| `cropoped_foreground_masks` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of shape of \[batch\_size, K, mask\_target\_size, mask\_target\_size\] storing the cropped foreground masks used for training. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.