[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/ImageAugment#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/ImageAugment)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/ImageAugment?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fvision%2Faugment%2FImageAugment&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/ImageAugment#methods)
    *   [distort](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/ImageAugment#distort)
        
    *   [distort\_with\_boxes](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/ImageAugment#distort_with_boxes)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.augment.ImageAugment Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/ImageAugment#methods)
    *   [distort](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/ImageAugment#distort)
        
    *   [distort\_with\_boxes](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/ImageAugment#distort_with_boxes)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L1881-L1919)

Image augmentation class for applying image distortions.

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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L1901-L1919)

distort_with_boxes(
        image: tf.Tensor, bboxes: tf.Tensor
    ) -> Tuple[tf.Tensor, tf.Tensor]

Distorts the image and bounding boxes.

Expect the image tensor values are in the range \[0, 255\].

|     |     |
| --- | --- |
| Args |     |
| `image` | `Tensor` of shape \[height, width, 3\] or \[num\_frames, height, width, 3\] representing an image or image sequence. |
| `bboxes` | `Tensor` of shape \[num\_boxes, 4\] or \[num\_frames, num\_boxes, 4\] representing bounding boxes for an image or image sequence. |

|     |
| --- |
| Returns |     |
| The augmented version of `image` and `bboxes`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.