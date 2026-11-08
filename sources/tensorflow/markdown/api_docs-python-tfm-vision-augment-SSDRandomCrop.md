[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/SSDRandomCrop#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/SSDRandomCrop)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/SSDRandomCrop?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/SSDRandomCrop#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/SSDRandomCrop#methods)
    *   [distort](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/SSDRandomCrop#distort)
        
    *   [distort\_with\_boxes](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/SSDRandomCrop#distort_with_boxes)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.augment.SSDRandomCrop Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/SSDRandomCrop#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/SSDRandomCrop#methods)
    *   [distort](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/SSDRandomCrop#distort)
        
    *   [distort\_with\_boxes](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/SSDRandomCrop#distort_with_boxes)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L2835-L2910)

Random crop preprocessing as in the SSD paper.

Inherits From: [`ImageAugment`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/ImageAugment)

tfm.vision.augment.SSDRandomCrop(
        params: (Sequence[configs.SSDRandomCropParam] | None) = None,
        aspect_ratio_range: tuple[float, float] = (0.5, 2.0),
        area_range: tuple[float, float] = (0.1, 1.0)
    )

Liu et al., SSD: Single shot multibox detector [https://arxiv.org/abs/1512.02325](https://arxiv.org/abs/1512.02325)

The implementation originated from TF Object Detection API: [https://github.com/tensorflow/models/blob/f36581036d3346a9496de06c8fd678d23cfe2103/research/object\_detection/core/preprocessor.py#L3529](https://github.com/tensorflow/models/blob/f36581036d3346a9496de06c8fd678d23cfe2103/research/object_detection/core/preprocessor.py#L3529)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `params` | a sequence of SSDRandomCropParam that contains: min\_object\_covered - a float representing minimum the cropped image must cover at least this fraction with at least one of the input bounding boxes. min\_box\_overlap - a float representing minimum overlap of the bounding box with the cropped image to keep the box. prob\_to\_apply - a float representing the probability to crop. |
| `aspect_ratio_range` | allowed range for aspect ratio of the cropped image. |
| `area_range` | allowed range for area ratio between cropped image and the original image. |

Methods
-------

### `distort`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L1884-L1899)

distort(
        image: tf.Tensor
    ) -> tf.Tensor

Given an image tensor, returns a distorted image with the same shape.

Expect the image tensor values are in the range \[0, 255\].

|     |     |
| --- | --- |
| Args |     |
| `image` | `Tensor` of shape \[height, width, 3\] or \[num\_frames, height, width, 3\] representing an image or image sequence. |

|     |
| --- |
| Returns |     |
| The augmented version of `image`. |     |

### `distort_with_boxes`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L2882-L2910)

distort_with_boxes(
        image: tf.Tensor, bboxes: tf.Tensor
    ) -> tuple[tf.Tensor, tf.Tensor]

See base class.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.