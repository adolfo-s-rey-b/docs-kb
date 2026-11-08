[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/MixupAndCutmix#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/MixupAndCutmix)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/MixupAndCutmix?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/MixupAndCutmix#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/MixupAndCutmix#methods)
    *   [distort](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/MixupAndCutmix#distort)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/MixupAndCutmix#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.augment.MixupAndCutmix Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/MixupAndCutmix#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/MixupAndCutmix#methods)
    *   [distort](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/MixupAndCutmix#distort)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/MixupAndCutmix#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L2618-L2780)

Applies Mixup and/or Cutmix to a batch of images.

tfm.vision.augment.MixupAndCutmix(
        num_classes: int,
        mixup_alpha: float = 0.8,
        cutmix_alpha: float = 1.0,
        prob: float = 1.0,
        switch_prob: float = 0.5,
        label_smoothing: float = 0.1
    )

*   Mixup: [https://arxiv.org/abs/1710.09412](https://arxiv.org/abs/1710.09412)
    
*   Cutmix: [https://arxiv.org/abs/1905.04899](https://arxiv.org/abs/1905.04899)
    

Implementaion is inspired by [https://github.com/rwightman/pytorch-image-models](https://github.com/rwightman/pytorch-image-models)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `num_classes` | `int`<br><br>Number of classes. |
| `mixup_alpha` | `float, optional`<br><br>For drawing a random lambda (`lam`) from a beta distribution (for each image). If zero Mixup is deactivated. Defaults to .8. |
| `cutmix_alpha` | `float, optional`<br><br>For drawing a random lambda (`lam`) from a beta distribution (for each image). If zero Cutmix is deactivated. Defaults to 1.. |
| `prob` | `float, optional`<br><br>Of augmenting the batch. Defaults to 1.0. |
| `switch_prob` | `float, optional`<br><br>Probability of applying Cutmix for the batch. Defaults to 0.5. |
| `label_smoothing` | `float, optional`<br><br>Constant for label smoothing. Defaults to 0.1. |

Methods
-------

### `distort`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L2669-L2696)

distort(
        images: tf.Tensor, labels: tf.Tensor
    ) -> Tuple[tf.Tensor, tf.Tensor]

Applies Mixup and/or Cutmix to batch of images and transforms labels.

|     |     |
| --- | --- |
| Args |     |
| `images` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br><br>Of shape \[batch\_size, height, width, 3\] representing a batch of image, or \[batch\_size, time, height, width, 3\] representing a batch of video. |
| `labels` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br><br>Of shape \[batch\_size, \] representing the class id for each image of the batch. |

|     |
| --- |
| Returns |     |
| Tuple\[tf.Tensor, tf.Tensor\]: The augmented version of `image` and `labels`. |     |

### `__call__`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L2665-L2667)

__call__(
        images: tf.Tensor, labels: tf.Tensor
    ) -> Tuple[tf.Tensor, tf.Tensor]

Call self as a function.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.