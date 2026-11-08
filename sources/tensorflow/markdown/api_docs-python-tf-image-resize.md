[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/resize#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/image/resize)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/image/resize?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/image/resize#used-in-the-notebooks)
    
*   [Note](https://www.tensorflow.org/api_docs/python/tf/image/resize#note)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/resize#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/resize#raises)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/resize#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.resize Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/image/resize#used-in-the-notebooks)
    
*   [Note](https://www.tensorflow.org/api_docs/python/tf/image/resize#note)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/resize#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/resize#raises)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/resize#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L1620-L1802)

Resize `images` to `size` using the specified `method`.

tf.image.resize(
        images,
        size,
        method=ResizeMethod.BILINEAR,
        preserve_aspect_ratio=False,
        antialias=False,
        name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [tf.data: Build TensorFlow input pipelines](https://www.tensorflow.org/guide/data)<br>    <br>*   [Estimators](https://www.tensorflow.org/guide/estimator) | *   [DeepDream](https://www.tensorflow.org/tutorials/generative/deepdream)<br>    <br>*   [pix2pix: Image-to-image translation with a conditional GAN](https://www.tensorflow.org/tutorials/generative/pix2pix)<br>    <br>*   [Neural style transfer](https://www.tensorflow.org/tutorials/generative/style_transfer)<br>    <br>*   [Image segmentation](https://www.tensorflow.org/tutorials/images/segmentation)<br>    <br>*   [Adversarial example using FGSM](https://www.tensorflow.org/tutorials/generative/adversarial_fgsm) |

Resized images will be distorted if their original aspect ratio is not the same as `size`. To avoid distortions see [`tf.image.resize_with_pad`](https://www.tensorflow.org/api_docs/python/tf/image/resize_with_pad)
.

    image = tf.constant([\
\
It works equally well with a single image instead of a batch of images:\
\
    tf.image.resize(image[0], [3,5]).shape.as_list()\
\
When `antialias` is true, the sampling filter will anti-alias the input image as well as interpolate. When downsampling an image with [anti-aliasing](https://en.wikipedia.org/wiki/Spatial_anti-aliasing)\
 the sampling filter kernel is scaled in order to properly anti-alias the input image signal. `antialias` has no effect when upsampling an image:\
\
    a = tf.image.resize(image, [5,10])\
\
The `method` argument expects an item from the [`image.ResizeMethod`](https://www.tensorflow.org/api_docs/python/tf/image/ResizeMethod)\
 enum, or the string equivalent. The options are:\
\
*   **`bilinear`**: [Bilinear interpolation.](https://en.wikipedia.org/wiki/Bilinear_interpolation)\
     If `antialias` is true, becomes a hat/tent filter function with radius 1 when downsampling.\
*   **`lanczos3`**: [Lanczos kernel](https://en.wikipedia.org/wiki/Lanczos_resampling)\
     with radius 3. High-quality practical filter but may have some ringing, especially on synthetic images.\
*   **`lanczos5`**: [Lanczos kernel](https://en.wikipedia.org/wiki/Lanczos_resampling)\
     with radius 5. Very-high-quality filter but may have stronger ringing.\
*   **`bicubic`**: [Cubic interpolant](https://en.wikipedia.org/wiki/Bicubic_interpolation)\
     of Keys. Equivalent to Catmull-Rom kernel. Reasonably good quality and faster than Lanczos3Kernel, particularly when upsampling.\
*   **`gaussian`**: [Gaussian kernel](https://en.wikipedia.org/wiki/Gaussian_filter)\
     with radius 3, sigma = 1.5 / 3.0.\
*   **`nearest`**: [Nearest neighbor interpolation.](https://en.wikipedia.org/wiki/Nearest-neighbor_interpolation)\
     `antialias` has no effect when used with nearest neighbor interpolation.\
*   **`area`**: Anti-aliased resampling with area interpolation. `antialias` has no effect when used with area interpolation; it always anti-aliases.\
*   **`mitchellcubic`**: Mitchell-Netravali Cubic non-interpolating filter. For synthetic images (especially those lacking proper prefiltering), less ringing than Keys cubic kernel but less sharp.\
\
The return value has type `float32`, unless the `method` is [`ResizeMethod.NEAREST_NEIGHBOR`](https://www.tensorflow.org/api_docs/python/tf/image/ResizeMethod#NEAREST_NEIGHBOR)\
, then the return dtype is the dtype of `images`:\
\
    nn = tf.image.resize(image, [5,7], method='nearest')\
\
With `preserve_aspect_ratio=True`, the aspect ratio is preserved, so `size` is the maximum for each dimension:\
\
    max_10_20 = tf.image.resize(image, [10,20], preserve_aspect_ratio=True)\
\
|     |\
| --- |\
| Note<br>---- |     |\
| The `bicubic` interpolation method currently does not have a GPU kernel implementation. As a result, `tf.image.resize(..., method='bicubic')` always executes on the CPU, even when GPU devices are available. |     |\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `images` | 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor of shape `[height, width, channels]`. |\
| `size` | A 1-D int32 Tensor of 2 elements: `new_height, new_width`. The new size for the images. |\
| `method` | An [`image.ResizeMethod`](https://www.tensorflow.org/api_docs/python/tf/image/ResizeMethod)<br>, or string equivalent. Defaults to `bilinear`. |\
| `preserve_aspect_ratio` | Whether to preserve the aspect ratio. If this is set, then `images` will be resized to a size that fits in `size` while preserving the aspect ratio of the original image. Scales up the image if `size` is bigger than the current size of the `image`. Defaults to False. |\
| `antialias` | Whether to use an anti-aliasing filter when downsampling an image. |\
| `name` | A name for this operation (optional). |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `ValueError` | if the shape of `images` is incompatible with the shape arguments to this function |\
| `ValueError` | if `size` has an invalid shape or type. |\
| `ValueError` | if an unsupported resize method is specified. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| If `images` was 4-D, a 4-D float Tensor of shape `[batch, new_height, new_width, channels]`. If `images` was 3-D, a 3-D float Tensor of shape `[new_height, new_width, channels]`. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.