[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/RandAugment#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/RandAugment)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/RandAugment?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/RandAugment#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/RandAugment#methods)
    *   [build\_for\_detection](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/RandAugment#build_for_detection)
        
    *   [distort](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/RandAugment#distort)
        
    *   [distort\_with\_boxes](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/RandAugment#distort_with_boxes)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.augment.RandAugment Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/RandAugment#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/RandAugment#methods)
    *   [build\_for\_detection](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/RandAugment#build_for_detection)
        
    *   [distort](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/RandAugment#distort)
        
    *   [distort\_with\_boxes](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/RandAugment#distort_with_boxes)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L2348-L2495)

Applies the RandAugment policy to images.

Inherits From: [`ImageAugment`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/ImageAugment)

tfm.vision.augment.RandAugment(
        num_layers: int = 2,
        magnitude: float = 10.0,
        cutout_const: float = 40.0,
        translate_const: float = 100.0,
        magnitude_std: float = 0.0,
        prob_to_apply: Optional[float] = None,
        exclude_ops: Optional[List[str]] = None
    )

RandAugment is from the paper [https://arxiv.org/abs/1909.13719](https://arxiv.org/abs/1909.13719)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `num_layers` | Integer, the number of augmentation transformations to apply sequentially to an image. Represented as (N) in the paper. Usually best values will be in the range \[1, 3\]. |
| `magnitude` | Integer, shared magnitude across all augmentation operations. Represented as (M) in the paper. Usually best values are in the range \[5, 10\]. |
| `cutout_const` | multiplier for applying cutout. |
| `translate_const` | multiplier for applying translation. |
| `magnitude_std` | randomness of the severity as proposed by the authors of the timm library. |
| `prob_to_apply` | The probability to apply the selected augmentation at each layer. |
| `exclude_ops` | exclude selected operations. |

Methods
-------

### `build_for_detection`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L2398-L2427)

@classmethod

Builds a RandAugment that modifies bboxes for geometric transforms.

### `distort`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L2485-L2488)

distort(
        image: tf.Tensor
    ) -> tf.Tensor

See base class.

### `distort_with_boxes`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L2490-L2495)

distort_with_boxes(
        image: tf.Tensor, bboxes: tf.Tensor
    ) -> Tuple[tf.Tensor, tf.Tensor]

See base class.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.