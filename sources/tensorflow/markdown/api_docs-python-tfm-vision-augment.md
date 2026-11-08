[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/augment#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfm.vision.augment Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py)

Augmentation policies for enhanced image/video preprocessing.

#### AutoAugment Reference:

*   AutoAugment Reference: [https://arxiv.org/abs/1805.09501](https://arxiv.org/abs/1805.09501)
    
*   AutoAugment for Object Detection Reference: [https://arxiv.org/abs/1906.11172](https://arxiv.org/abs/1906.11172)
    

RandAugment Reference: [https://arxiv.org/abs/1909.13719](https://arxiv.org/abs/1909.13719)
 RandomErasing Reference: [https://arxiv.org/abs/1708.04896](https://arxiv.org/abs/1708.04896)
 MixupAndCutmix:

*   Mixup: [https://arxiv.org/abs/1710.09412](https://arxiv.org/abs/1710.09412)
    
*   Cutmix: [https://arxiv.org/abs/1905.04899](https://arxiv.org/abs/1905.04899)
    

RandomErasing, Mixup and Cutmix are inspired by [https://github.com/rwightman/pytorch-image-models](https://github.com/rwightman/pytorch-image-models)

#### SSDRandCrop Reference:

*   Liu et al., SSD: Single shot multibox detector: [https://arxiv.org/abs/1512.02325](https://arxiv.org/abs/1512.02325)
    
*   Implementation from TF Object Detection API: [https://github.com/tensorflow/models/](https://github.com/tensorflow/models/)
    

Classes
-------

[`class AutoAugment`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/AutoAugment)
: Applies the AutoAugment policy to images.

[`class ImageAugment`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/ImageAugment)
: Image augmentation class for applying image distortions.

[`class MixupAndCutmix`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/MixupAndCutmix)
: Applies Mixup and/or Cutmix to a batch of images.

[`class RandAugment`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/RandAugment)
: Applies the RandAugment policy to images.

[`class RandomErasing`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/RandomErasing)
: Applies RandomErasing to a single image.

[`class SSDRandomCrop`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/SSDRandomCrop)
: Random crop preprocessing as in the SSD paper.

[`class Sequence`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/Sequence)
: All the operations on a read-only sequence.

Functions
---------

[`autocontrast(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/autocontrast)
: Implements Autocontrast function from PIL using TF ops.

[`bbox_wrapper(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/bbox_wrapper)
: Adds a bboxes function argument to func and returns unchanged bboxes.

[`blend(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/blend)
: Blend image1 and image2 using 'factor'.

[`brightness(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/brightness)
: Equivalent of PIL Brightness.

[`color(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/color)
: Equivalent of PIL Color.

[`contrast(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/contrast)
: Equivalent of PIL Contrast.

[`crop_normalized_boxes(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/crop_normalized_boxes)
: Crop normalized boxes.

[`cutout(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/cutout)
: Apply cutout ([https://arxiv.org/abs/1708.04552](https://arxiv.org/abs/1708.04552)
) to image.

[`cutout_video(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/cutout_video)
: Apply cutout ([https://arxiv.org/abs/1708.04552](https://arxiv.org/abs/1708.04552)
) to a video.

[`equalize(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/equalize)
: Implements Equalize function from PIL using TF ops.

[`filter_boxes_by_ioa(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/filter_boxes_by_ioa)
: Filter boxes by intersection over area (IOA).

[`from_4d(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/from_4d)
: Converts a 4D image back to `ndims` rank.

[`gaussian_filter2d(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/gaussian_filter2d)
: Performs Gaussian blur on image(s).

[`gaussian_noise(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/gaussian_noise)
: Add Gaussian noise to image(s).

[`grayscale(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/grayscale)
: Convert image to grayscale.

[`invert(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/invert)
: Inverts the image pixels.

[`level_to_arg(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/level_to_arg)
: Creates a dict mapping image operation names to their arguments.

[`posterize(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/posterize)
: Equivalent of PIL Posterize.

[`rotate(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/rotate)
: Rotates the image by degrees either clockwise or counterclockwise.

[`rotate_with_bboxes(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/rotate_with_bboxes)
: Equivalent of PIL Rotate that rotates the image and bbox.

[`select_and_apply_random_policy(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/select_and_apply_random_policy)
: Select a random policy from `policies` and apply it to `image`.

[`sharpness(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/sharpness)
: Implements Sharpness function from PIL using TF ops.

[`shear_with_bboxes(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/shear_with_bboxes)
: Applies Shear Transformation to the image and shifts the bboxes.

[`shear_x(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/shear_x)
: Equivalent of PIL Shearing in X dimension.

[`shear_y(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/shear_y)
: Equivalent of PIL Shearing in Y dimension.

[`solarize(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/solarize)
: Solarize the input image(s).

[`solarize_add(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/solarize_add)
: Additive solarize the input image(s).

[`to_4d(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/to_4d)
: Converts an input Tensor to 4 dimensions.

[`transform(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/transform)
: Transforms an image.

[`translate(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/translate)
: Translates image(s) by provided vectors.

[`translate_bbox(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/translate_bbox)
: Equivalent of PIL Translate in X/Y dimension that shifts image and bbox.

[`translate_x(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/translate_x)
: Equivalent of PIL Translate in X dimension.

[`translate_y(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/translate_y)
: Equivalent of PIL Translate in Y dimension.

[`translate_y_only_bboxes(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/translate_y_only_bboxes)
: Apply translate\_y to each bbox in the image with probability prob.

[`unwrap(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/unwrap)
: Unwraps an image produced by wrap.

[`wrap(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/wrap)
: Returns 'image' with an extra channel set to all 1s.

[`wrapped_rotate(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/wrapped_rotate)
: Applies rotation with wrap/unwrap.

|     |     |
| --- | --- |
| Other Members<br>------------- |     |
| NAME\_TO\_FUNC | {<br>     'AutoContrast': <function autocontrast>,<br>     'Brightness': <function brightness>,<br>     'Color': <function color>,<br>     'Contrast': <function contrast>,<br>     'Cutout': <function cutout>,<br>     'Equalize': <function equalize>,<br>     'Gaussian_Noise': <function gaussian_noise>,<br>     'Grayscale': <function grayscale>,<br>     'Invert': <function invert>,<br>     'Posterize': <function posterize>,<br>     'Rotate': <function wrapped_rotate>,<br>     'Rotate_BBox': <function rotate_with_bboxes>,<br>     'Sharpness': <function sharpness>,<br>     'ShearX': <function shear_x>,<br>     'ShearX_BBox': <function <lambda>>,<br>     'ShearY': <function shear_y>,<br>     'ShearY_BBox': <function <lambda>>,<br>     'Solarize': <function solarize>,<br>     'SolarizeAdd': <function solarize_add>,<br>     'TranslateX': <function translate_x>,<br>     'TranslateX_BBox': <function <lambda>>,<br>     'TranslateY': <function translate_y>,<br>     'TranslateY_BBox': <function <lambda>>,<br>     'TranslateY_Only_BBoxes': <function translate_y_only_bboxes><br>    } |
| PROB\_FUNCS | {<br>     'TranslateY_Only_BBoxes'<br>    } |
| REPLACE\_FUNCS | {<br>     'Cutout',<br>     'Rotate',<br>     'Rotate_BBox',<br>     'ShearX',<br>     'ShearX_BBox',<br>     'ShearY',<br>     'ShearY_BBox',<br>     'TranslateX',<br>     'TranslateX_BBox',<br>     'TranslateY',<br>     'TranslateY_BBox',<br>     'TranslateY_Only_BBoxes'<br>    } |
| REQUIRE\_BOXES\_FUNCS | {<br>     'Rotate_BBox',<br>     'ShearX_BBox',<br>     'ShearY_BBox',<br>     'TranslateX_BBox',<br>     'TranslateY_BBox',<br>     'TranslateY_Only_BBoxes'<br>    } |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.