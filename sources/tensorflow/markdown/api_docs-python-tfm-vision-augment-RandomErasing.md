[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/RandomErasing#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/RandomErasing)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/RandomErasing?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/RandomErasing#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/RandomErasing#methods)
    *   [distort](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/RandomErasing#distort)
        
    *   [distort\_with\_boxes](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/RandomErasing#distort_with_boxes)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.augment.RandomErasing Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/RandomErasing#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/RandomErasing#methods)
    *   [distort](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/RandomErasing#distort)
        
    *   [distort\_with\_boxes](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/RandomErasing#distort_with_boxes)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L2498-L2615)

Applies RandomErasing to a single image.

Inherits From: [`ImageAugment`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/ImageAugment)

tfm.vision.augment.RandomErasing(
        probability: float = 0.25,
        min_area: float = 0.02,
        max_area: float = (1 / 3),
        min_aspect: float = 0.3,
        max_aspect: Optional[float] = None,
        min_count=1,
        max_count=1,
        trials=10
    )

Reference: [https://arxiv.org/abs/1708.04896](https://arxiv.org/abs/1708.04896)

Implementation is inspired by [https://github.com/rwightman/pytorch-image-models](https://github.com/rwightman/pytorch-image-models)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `probability` | Probability of augmenting the image. Defaults to `0.25`. |
| `min_area` | Minimum area of the random erasing rectangle. Defaults to `0.02`. |
| `max_area` | Maximum area of the random erasing rectangle. Defaults to `1/3`. |
| `min_aspect` | Minimum aspect rate of the random erasing rectangle. Defaults to `0.3`. |
| `max_aspect` | Maximum aspect rate of the random erasing rectangle. Defaults to `None`. |
| `min_count` | Minimum number of erased rectangles. Defaults to `1`. |
| `max_count` | Maximum number of erased rectangles. Defaults to `1`. |
| `trials` | Maximum number of trials to randomly sample a rectangle that fulfills constraint. Defaults to `10`. |

Methods
-------

### `distort`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L2541-L2553)

distort(
        image: tf.Tensor
    ) -> tf.Tensor

Applies RandomErasing to single `image`.

|     |     |
| --- | --- |
| Args |     |
| `image` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br><br>Of shape \[height, width, 3\] representing an image. |

|     |     |
| --- | --- |
| Returns |     |
| [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor) | The augmented version of `image`. |

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