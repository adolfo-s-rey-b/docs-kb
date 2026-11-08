[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment#methods)
    *   [deit3\_three\_augment](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment#deit3_three_augment)
        
    *   [detection\_policy\_v0](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment#detection_policy_v0)
        
    *   [distort](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment#distort)
        
    *   [distort\_with\_boxes](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment#distort_with_boxes)
        
    *   [panoptic\_deeplab\_policy](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment#panoptic_deeplab_policy)
        
    *   [policy\_reduced\_cifar10](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment#policy_reduced_cifar10)
        
    *   [policy\_reduced\_imagenet](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment#policy_reduced_imagenet)
        
    *   [policy\_simple](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment#policy_simple)
        
    *   [policy\_svhn](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment#policy_svhn)
        
    *   [policy\_test](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment#policy_test)
        
    *   [policy\_v0](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment#policy_v0)
        
    *   [vit](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment#vit)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.augment.AutoAugment Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment#methods)
    *   [deit3\_three\_augment](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment#deit3_three_augment)
        
    *   [detection\_policy\_v0](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment#detection_policy_v0)
        
    *   [distort](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment#distort)
        
    *   [distort\_with\_boxes](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment#distort_with_boxes)
        
    *   [panoptic\_deeplab\_policy](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment#panoptic_deeplab_policy)
        
    *   [policy\_reduced\_cifar10](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment#policy_reduced_cifar10)
        
    *   [policy\_reduced\_imagenet](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment#policy_reduced_imagenet)
        
    *   [policy\_simple](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment#policy_simple)
        
    *   [policy\_svhn](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment#policy_svhn)
        
    *   [policy\_test](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment#policy_test)
        
    *   [policy\_v0](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment#policy_v0)
        
    *   [vit](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment#vit)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L1922-L2341)

Applies the AutoAugment policy to images.

Inherits From: [`ImageAugment`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/ImageAugment)

tfm.vision.augment.AutoAugment(
        augmentation_name: str = 'v0',
        policies: Optional[Iterable[Iterable[Tuple[str, float, float]]]] = None,
        cutout_const: float = 100,
        translate_const: float = 250
    )

AutoAugment is from the paper: [https://arxiv.org/abs/1805.09501](https://arxiv.org/abs/1805.09501)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `augmentation_name` | The name of the AutoAugment policy to use. The available options are `v0`, `test`, `reduced_cifar10`, `svhn` and `reduced_imagenet`. `v0` is the policy used for all of the results in the paper and was found to achieve the best results on the COCO dataset. [`v1`](https://www.tensorflow.org/api_docs/python/tf/compat/v1)<br>, `v2` and `v3` are additional good policies found on the COCO dataset that have slight variation in what operations were used during the search procedure along with how many operations are applied in parallel to a single image (2 vs 3). Make sure to set `policies` to `None` (the default) if you want to set options using `augmentation_name`. |
| `policies` | list of lists of tuples in the form `(func, prob, level)`, `func` is a string name of the augmentation function, `prob` is the probability of applying the `func` operation, `level` (or magnitude) is the input argument for `func`. For example:<br><br>[[('Equalize', 0.9, 3), ('Color', 0.7, 8)],<br>     [('Invert', 0.6, 5), ('Rotate', 0.2, 9), ('ShearX', 0.1, 2)], ...]<br><br>The outer-most list must be 3-d. The number of operations in a sub-policy can vary from one sub-policy to another. If you provide `policies` as input, any option set with `augmentation_name` will get overriden as they are mutually exclusive. |
| `cutout_const` | multiplier for applying cutout. |
| `translate_const` | multiplier for applying translation. |

|     |
| --- |
| Raises<br>------ |     |
| ValueError if `augmentation_name` is unsupported. |     |

Methods
-------

### `deit3_three_augment`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L2314-L2333)

@staticmethod

Autoaugment policy for three augmentations.

Proposed in paper: [https://arxiv.org/abs/2204.07118](https://arxiv.org/abs/2204.07118)

Each tuple is an augmentation operation of the form (operation, probability, magnitude). Each element in policy is a sub-policy that will be applied on the image. Randomly chooses one of the three augmentation to apply on image.

|     |
| --- |
| Returns |     |
| the policy. |     |

### `detection_policy_v0`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L2078-L2098)

@staticmethod

Autoaugment policy that was used in AutoAugment Paper for Detection.

[https://arxiv.org/pdf/1906.11172](https://arxiv.org/pdf/1906.11172)

Each tuple is an augmentation operation of the form (operation, probability, magnitude). Each element in policy is a sub-policy that will be applied sequentially on the image.

|     |
| --- |
| Returns |     |
| the policy. |     |

### `distort`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L2052-L2062)

distort(
        image: tf.Tensor
    ) -> tf.Tensor

See base class.

### `distort_with_boxes`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L2064-L2076)

distort_with_boxes(
        image: tf.Tensor, bboxes: tf.Tensor
    ) -> Tuple[tf.Tensor, tf.Tensor]

See base class.

### `panoptic_deeplab_policy`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L2288-L2296)

@staticmethod

### `policy_reduced_cifar10`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L2141-L2181)

@staticmethod

Autoaugment policy for reduced CIFAR-10 dataset.

Result is from the AutoAugment paper: [https://arxiv.org/abs/1805.09501](https://arxiv.org/abs/1805.09501)

Each tuple is an augmentation operation of the form (operation, probability, magnitude). Each element in policy is a sub-policy that will be applied sequentially on the image.

|     |
| --- |
| Returns |     |
| the policy. |     |

### `policy_reduced_imagenet`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L2225-L2265)

@staticmethod

Autoaugment policy for reduced ImageNet dataset.

Result is from the AutoAugment paper: [https://arxiv.org/abs/1805.09501](https://arxiv.org/abs/1805.09501)

Each tuple is an augmentation operation of the form (operation, probability, magnitude). Each element in policy is a sub-policy that will be applied sequentially on the image.

|     |
| --- |
| Returns |     |
| the policy. |     |

### `policy_simple`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L2267-L2286)

@staticmethod

Same as `policy_v0`, except with custom ops removed.

### `policy_svhn`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L2183-L2223)

@staticmethod

Autoaugment policy for SVHN dataset.

Result is from the AutoAugment paper: [https://arxiv.org/abs/1805.09501](https://arxiv.org/abs/1805.09501)

Each tuple is an augmentation operation of the form (operation, probability, magnitude). Each element in policy is a sub-policy that will be applied sequentially on the image.

|     |
| --- |
| Returns |     |
| the policy. |     |

### `policy_test`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L2335-L2341)

@staticmethod

Autoaugment test policy for debugging.

### `policy_v0`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L2100-L2139)

@staticmethod

Autoaugment policy that was used in AutoAugment Paper.

Each tuple is an augmentation operation of the form (operation, probability, magnitude). Each element in policy is a sub-policy that will be applied sequentially on the image.

|     |
| --- |
| Returns |     |
| the policy. |     |

### `vit`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L2298-L2312)

@staticmethod

Autoaugment policy for a generic ViT.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.