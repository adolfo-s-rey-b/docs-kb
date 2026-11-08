[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/resize_and_crop_image_v2#main-content)

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
    

tfm.vision.preprocess\_ops.resize\_and\_crop\_image\_v2 Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/preprocess_ops.py#L311-L437)

Resizes the input image to output size (Faster R-CNN style).

tfm.vision.preprocess_ops.resize_and_crop_image_v2(
        image,
        short_side,
        long_side,
        padded_size,
        aug_scale_min=1.0,
        aug_scale_max=1.0,
        seed=1,
        method=tf.image.ResizeMethod.BILINEAR
    )

Resize and pad images given the specified short / long side length and the stride size.

Here are the preprocessing steps.

1.  For a given image, keep its aspect ratio and first try to rescale the short side of the original image to `short_side`.
2.  If the scaled image after 1 has a long side that exceeds `long_side`, keep the aspect ratio and rescale the long side of the image to `long_side`.
3.  (Optional) Apply random jittering according to `aug_scale_min` and `aug_scale_max`. By default this step is skipped.
4.  Pad the rescaled image to the padded\_size.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `image` | a `Tensor` of shape \[height, width, 3\] representing an image. |
| `short_side` | a scalar `Tensor` or `int` representing the desired short side to be rescaled to. |
| `long_side` | a scalar `Tensor` or `int` representing the desired long side to be rescaled to. |
| `padded_size` | a `Tensor` or `int` list/tuple of two elements representing \[height, width\] of the padded output image size. |
| `aug_scale_min` | a `float` with range between \[0, 1.0\] representing minimum random scale applied for training scale jittering. |
| `aug_scale_max` | a `float` with range between \[1.0, inf\] representing maximum random scale applied for training scale jittering. |
| `seed` | seed for random scale jittering. |
| `method` | function to resize input image to scaled image. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `output_image` | `Tensor` of shape \[height, width, 3\] where \[height, width\] equals to `output_size`. |
| `image_info` | a 2D `Tensor` that encodes the information of the image and the applied preprocessing. It is in the format of \[\[original\_height, original\_width\], \[desired\_height, desired\_width\], \[y\_scale, x\_scale\], \[y\_offset, x\_offset\]\], where \[desired\_height, desired\_width\] is the actual scaled image size, and \[y\_scale, x\_scale\] is the scaling factor, which is the ratio of scaled dimension / original dimension. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.