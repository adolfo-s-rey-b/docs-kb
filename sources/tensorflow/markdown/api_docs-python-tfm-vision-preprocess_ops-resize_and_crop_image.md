[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/resize_and_crop_image#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/resize_and_crop_image)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/resize_and_crop_image?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/resize_and_crop_image#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/resize_and_crop_image#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.preprocess\_ops.resize\_and\_crop\_image Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/resize_and_crop_image#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/resize_and_crop_image#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/preprocess_ops.py#L177-L308)

Resizes the input image to output size (RetinaNet style).

tfm.vision.preprocess_ops.resize_and_crop_image(
        image,
        desired_size,
        padded_size,
        aug_scale_min=1.0,
        aug_scale_max=1.0,
        seed=1,
        method=tf.image.ResizeMethod.BILINEAR,
        keep_aspect_ratio=True,
        centered_crop=False
    )

Resize and pad images given the desired output size of the image and stride size.

Here are the preprocessing steps.

1.  For a given image, keep its aspect ratio and rescale the image to make it the largest rectangle to be bounded by the rectangle specified by the `desired_size`.
2.  Pad the rescaled image to the padded\_size.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `image` | a `Tensor` of shape \[height, width, c\] representing an image. |
| `desired_size` | a `Tensor` or `int` list/tuple of two elements representing \[height, width\] of the desired actual output image size. |
| `padded_size` | a `Tensor` or `int` list/tuple of two elements representing \[height, width\] of the padded output image size. Padding will be applied after scaling the image to the desired\_size. Can be None to disable padding. |
| `aug_scale_min` | a `float` with range between \[0, 1.0\] representing minimum random scale applied to desired\_size for training scale jittering. |
| `aug_scale_max` | a `float` with range between \[1.0, inf\] representing maximum random scale applied to desired\_size for training scale jittering. |
| `seed` | seed for random scale jittering. |
| `method` | function to resize input image to scaled image. |
| `keep_aspect_ratio` | whether or not to keep the aspect ratio when resizing. |
| `centered_crop` | If `centered_crop` is set to True, then resized crop (if smaller than padded size) is place in the center of the image. Default behaviour is to place it at left top corner. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `output_image` | `Tensor` of shape \[height, width, c\] where \[height, width\] equals to `output_size`. |
| `image_info` | a 2D `Tensor` that encodes the information of the image and the applied preprocessing. It is in the format of \[\[original\_height, original\_width\], \[desired\_height, desired\_width\], \[y\_scale, x\_scale\], \[y\_offset, x\_offset\]\], where \[desired\_height, desired\_width\] is the actual scaled image size, and \[y\_scale, x\_scale\] is the scaling factor, which is the ratio of scaled dimension / original dimension. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.