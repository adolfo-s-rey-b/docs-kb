[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fvision%2Fpreprocess_ops&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops#other-members)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfm.vision.preprocess\_ops Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops#other-members)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/preprocess_ops.py)

Preprocessing ops.

Classes
-------

[`class range`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range)
: range(stop) -> range object range(start, stop\[, step\]) -> range object

Functions
---------

[`center_crop_image(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/center_crop_image)
: Center crop a square shape slice from the input image.

[`center_crop_image_v2(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/center_crop_image_v2)
: Center crop a square shape slice from the input image.

[`clip_or_pad_to_fixed_size(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/clip_or_pad_to_fixed_size)
: Pads data to a fixed length at the first dimension.

[`color_jitter(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/color_jitter)
: Applies color jitter to an image, similarly to torchvision\`s ColorJitter.

[`compute_padded_size(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/compute_padded_size)
: Compute the padded size given the desired size and the stride.

[`horizontal_flip_boxes(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/horizontal_flip_boxes)
: Flips normalized boxes horizontally.

[`horizontal_flip_image(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/horizontal_flip_image)
: Flips image horizontally.

[`horizontal_flip_masks(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/horizontal_flip_masks)
: Flips masks horizontally. Expects rank-3 input dimensions.

[`normalize_image(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/normalize_image)
: Normalizes the image to zero mean and unit variance.

[`normalize_scaled_float_image(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/normalize_scaled_float_image)
: Normalizes a scaled float image to zero mean and unit variance.

[`random_brightness(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_brightness)
: Jitters brightness of an image.

[`random_contrast(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_contrast)
: Jitters contrast of an image, similarly to torchvision\`s ColorJitter.

[`random_crop(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_crop)
: Randomly crop the image and boxes, filtering labels.

[`random_crop_image(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_crop_image)
: Randomly crop an arbitrary shaped slice from the input image.

[`random_crop_image_v2(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_crop_image_v2)
: Randomly crop an arbitrary shaped slice from the input image.

[`random_crop_image_with_boxes_and_labels(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_crop_image_with_boxes_and_labels)
: Crops a random slice from the input image.

[`random_horizontal_flip(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_horizontal_flip)
: Randomly flips input image and bounding boxes and/or masks horizontally.

[`random_horizontal_flip_with_roi(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_horizontal_flip_with_roi)
: Randomly flips input image and bounding boxes horizontally.

[`random_jpeg_quality(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_jpeg_quality)
: Randomly encode the image as jpeg and decode it.

[`random_saturation(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_saturation)
: Jitters saturation of an image, similarly to torchvision\`s ColorJitter.

[`random_vertical_flip(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_vertical_flip)
: Randomly flips input image and bounding boxes vertically.

[`resize_and_crop_boxes(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/resize_and_crop_boxes)
: Resizes boxes to output size with scale and offset.

[`resize_and_crop_image(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/resize_and_crop_image)
: Resizes the input image to output size (RetinaNet style).

[`resize_and_crop_image_v2(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/resize_and_crop_image_v2)
: Resizes the input image to output size (Faster R-CNN style).

[`resize_and_crop_masks(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/resize_and_crop_masks)
: Resizes boxes to output size with scale and offset.

[`resize_image(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/resize_image)
: Resize image with size and max\_size.

[`vertical_flip_boxes(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/vertical_flip_boxes)
: Flips normalized boxes vertically.

|     |     |
| --- | --- |
| Other Members<br>------------- |     |
| CENTER\_CROP\_FRACTION | `0.875` |
| MEAN\_NORM | `(0.485, 0.456, 0.406)` |
| MEAN\_RGB | `(123.675, 116.28, 103.53)` |
| MEDIAN\_RGB | `(128.0, 128.0, 128.0)` |
| STDDEV\_NORM | `(0.229, 0.224, 0.225)` |
| STDDEV\_RGB | `(58.395, 57.120000000000005, 57.375)` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.