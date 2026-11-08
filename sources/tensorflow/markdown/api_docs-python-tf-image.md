[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/image)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/image?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/image?version=stable#classes_2)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/image?version=stable#functions_2)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.image Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/image?version=stable#classes_2)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/image?version=stable#functions_2)
    

See Stable See Nightly

Public API for tf.\_api.v2.image namespace

Classes
-------

[`class ResizeMethod`](https://www.tensorflow.org/api_docs/python/tf/image/ResizeMethod)
: See [`tf.image.resize`](https://www.tensorflow.org/api_docs/python/tf/image/resize)
 for details.

Functions
---------

[`adjust_brightness(...)`](https://www.tensorflow.org/api_docs/python/tf/image/adjust_brightness)
: Adjust the brightness of RGB or Grayscale images.

[`adjust_contrast(...)`](https://www.tensorflow.org/api_docs/python/tf/image/adjust_contrast)
: Adjust contrast of RGB or grayscale images.

[`adjust_gamma(...)`](https://www.tensorflow.org/api_docs/python/tf/image/adjust_gamma)
: Performs [Gamma Correction](http://en.wikipedia.org/wiki/Gamma_correction)
.

[`adjust_hue(...)`](https://www.tensorflow.org/api_docs/python/tf/image/adjust_hue)
: Adjust hue of RGB images.

[`adjust_jpeg_quality(...)`](https://www.tensorflow.org/api_docs/python/tf/image/adjust_jpeg_quality)
: Adjust jpeg encoding quality of an image.

[`adjust_saturation(...)`](https://www.tensorflow.org/api_docs/python/tf/image/adjust_saturation)
: Adjust saturation of RGB images.

[`central_crop(...)`](https://www.tensorflow.org/api_docs/python/tf/image/central_crop)
: Crop the central region of the image(s).

[`combined_non_max_suppression(...)`](https://www.tensorflow.org/api_docs/python/tf/image/combined_non_max_suppression)
: Greedily selects a subset of bounding boxes in descending order of score.

[`convert_image_dtype(...)`](https://www.tensorflow.org/api_docs/python/tf/image/convert_image_dtype)
: Convert `image` to `dtype`, scaling its values if needed.

[`crop_and_resize(...)`](https://www.tensorflow.org/api_docs/python/tf/image/crop_and_resize)
: Extracts crops from the input image tensor and resizes them.

[`crop_to_bounding_box(...)`](https://www.tensorflow.org/api_docs/python/tf/image/crop_to_bounding_box)
: Crops an `image` to a specified bounding box.

[`decode_and_crop_jpeg(...)`](https://www.tensorflow.org/api_docs/python/tf/io/decode_and_crop_jpeg)
: Decode and Crop a JPEG-encoded image to a uint8 tensor.

[`decode_bmp(...)`](https://www.tensorflow.org/api_docs/python/tf/io/decode_bmp)
: Decode the first frame of a BMP-encoded image to a uint8 tensor.

[`decode_gif(...)`](https://www.tensorflow.org/api_docs/python/tf/io/decode_gif)
: Decode the frame(s) of a GIF-encoded image to a uint8 tensor.

[`decode_image(...)`](https://www.tensorflow.org/api_docs/python/tf/io/decode_image)
: Function for `decode_bmp`, `decode_gif`, `decode_jpeg`, and `decode_png`.

[`decode_jpeg(...)`](https://www.tensorflow.org/api_docs/python/tf/io/decode_jpeg)
: Decode a JPEG-encoded image to a uint8 tensor.

[`decode_jxl(...)`](https://www.tensorflow.org/api_docs/python/tf/io/decode_jxl)
: Decode a JPEG XL encoded image to a uint8 tensor.

[`decode_png(...)`](https://www.tensorflow.org/api_docs/python/tf/io/decode_png)
: Decode a PNG-encoded image to a uint8 or uint16 tensor.

[`decode_webp(...)`](https://www.tensorflow.org/api_docs/python/tf/io/decode_webp)
: Decode a WebP-encoded image to a uint8 tensor.

[`draw_bounding_boxes(...)`](https://www.tensorflow.org/api_docs/python/tf/image/draw_bounding_boxes)
: Draw bounding boxes on a batch of images.

[`encode_jpeg(...)`](https://www.tensorflow.org/api_docs/python/tf/io/encode_jpeg)
: JPEG-encode an image.

[`encode_png(...)`](https://www.tensorflow.org/api_docs/python/tf/io/encode_png)
: PNG-encode an image.

[`extract_glimpse(...)`](https://www.tensorflow.org/api_docs/python/tf/image/extract_glimpse)
: Extracts a glimpse from the input tensor.

[`extract_jpeg_shape(...)`](https://www.tensorflow.org/api_docs/python/tf/io/extract_jpeg_shape)
: Extract the shape information of a JPEG-encoded image.

[`extract_patches(...)`](https://www.tensorflow.org/api_docs/python/tf/image/extract_patches)
: Extract `patches` from `images`.

[`flip_left_right(...)`](https://www.tensorflow.org/api_docs/python/tf/image/flip_left_right)
: Flip an image horizontally (left to right).

[`flip_up_down(...)`](https://www.tensorflow.org/api_docs/python/tf/image/flip_up_down)
: Flip an image vertically (upside down).

[`generate_bounding_box_proposals(...)`](https://www.tensorflow.org/api_docs/python/tf/image/generate_bounding_box_proposals)
: Generate bounding box proposals from encoded bounding boxes.

[`grayscale_to_rgb(...)`](https://www.tensorflow.org/api_docs/python/tf/image/grayscale_to_rgb)
: Converts one or more images from Grayscale to RGB.

[`hsv_to_rgb(...)`](https://www.tensorflow.org/api_docs/python/tf/image/hsv_to_rgb)
: Convert one or more images from HSV to RGB.

[`image_gradients(...)`](https://www.tensorflow.org/api_docs/python/tf/image/image_gradients)
: Returns image gradients (dy, dx) for each color channel.

[`is_jpeg(...)`](https://www.tensorflow.org/api_docs/python/tf/io/is_jpeg)
: Convenience function to check if the 'contents' encodes a JPEG image.

[`non_max_suppression(...)`](https://www.tensorflow.org/api_docs/python/tf/image/non_max_suppression)
: Greedily selects a subset of bounding boxes in descending order of score.

[`non_max_suppression_overlaps(...)`](https://www.tensorflow.org/api_docs/python/tf/image/non_max_suppression_overlaps)
: Greedily selects a subset of bounding boxes in descending order of score.

[`non_max_suppression_padded(...)`](https://www.tensorflow.org/api_docs/python/tf/image/non_max_suppression_padded)
: Greedily selects a subset of bounding boxes in descending order of score.

[`non_max_suppression_with_scores(...)`](https://www.tensorflow.org/api_docs/python/tf/image/non_max_suppression_with_scores)
: Greedily selects a subset of bounding boxes in descending order of score.

[`pad_to_bounding_box(...)`](https://www.tensorflow.org/api_docs/python/tf/image/pad_to_bounding_box)
: Pad `image` with zeros to the specified `height` and `width`.

[`per_image_standardization(...)`](https://www.tensorflow.org/api_docs/python/tf/image/per_image_standardization)
: Linearly scales each image in `image` to have mean 0 and variance 1.

[`psnr(...)`](https://www.tensorflow.org/api_docs/python/tf/image/psnr)
: Returns the Peak Signal-to-Noise Ratio between a and b.

[`random_brightness(...)`](https://www.tensorflow.org/api_docs/python/tf/image/random_brightness)
: Adjust the brightness of images by a random factor.

[`random_contrast(...)`](https://www.tensorflow.org/api_docs/python/tf/image/random_contrast)
: Adjust the contrast of an image or images by a random factor.

[`random_crop(...)`](https://www.tensorflow.org/api_docs/python/tf/image/random_crop)
: Randomly crops a tensor to a given size.

[`random_flip_left_right(...)`](https://www.tensorflow.org/api_docs/python/tf/image/random_flip_left_right)
: Randomly flip an image horizontally (left to right).

[`random_flip_up_down(...)`](https://www.tensorflow.org/api_docs/python/tf/image/random_flip_up_down)
: Randomly flips an image vertically (upside down).

[`random_hue(...)`](https://www.tensorflow.org/api_docs/python/tf/image/random_hue)
: Adjust the hue of RGB images by a random factor.

[`random_jpeg_quality(...)`](https://www.tensorflow.org/api_docs/python/tf/image/random_jpeg_quality)
: Randomly changes jpeg encoding quality for inducing jpeg noise.

[`random_saturation(...)`](https://www.tensorflow.org/api_docs/python/tf/image/random_saturation)
: Adjust the saturation of RGB images by a random factor.

[`resize(...)`](https://www.tensorflow.org/api_docs/python/tf/image/resize)
: Resize `images` to `size` using the specified `method`.

[`resize_with_crop_or_pad(...)`](https://www.tensorflow.org/api_docs/python/tf/image/resize_with_crop_or_pad)
: Crops and/or pads an image to a target width and height.

[`resize_with_pad(...)`](https://www.tensorflow.org/api_docs/python/tf/image/resize_with_pad)
: Resizes and pads an image to a target width and height.

[`rgb_to_grayscale(...)`](https://www.tensorflow.org/api_docs/python/tf/image/rgb_to_grayscale)
: Converts one or more images from RGB to Grayscale.

[`rgb_to_hsv(...)`](https://www.tensorflow.org/api_docs/python/tf/image/rgb_to_hsv)
: Converts one or more images from RGB to HSV.

[`rgb_to_yiq(...)`](https://www.tensorflow.org/api_docs/python/tf/image/rgb_to_yiq)
: Converts one or more images from RGB to YIQ.

[`rgb_to_yuv(...)`](https://www.tensorflow.org/api_docs/python/tf/image/rgb_to_yuv)
: Converts one or more images from RGB to YUV.

[`rot90(...)`](https://www.tensorflow.org/api_docs/python/tf/image/rot90)
: Rotate image(s) by 90 degrees.

[`sample_distorted_bounding_box(...)`](https://www.tensorflow.org/api_docs/python/tf/image/sample_distorted_bounding_box)
: Generate a single randomly distorted bounding box for an image.

[`sobel_edges(...)`](https://www.tensorflow.org/api_docs/python/tf/image/sobel_edges)
: Returns a tensor holding Sobel edge maps.

[`ssim(...)`](https://www.tensorflow.org/api_docs/python/tf/image/ssim)
: Computes SSIM index between img1 and img2.

[`ssim_multiscale(...)`](https://www.tensorflow.org/api_docs/python/tf/image/ssim_multiscale)
: Computes the MS-SSIM between img1 and img2.

[`stateless_random_brightness(...)`](https://www.tensorflow.org/api_docs/python/tf/image/stateless_random_brightness)
: Adjust the brightness of images by a random factor deterministically.

[`stateless_random_contrast(...)`](https://www.tensorflow.org/api_docs/python/tf/image/stateless_random_contrast)
: Adjust the contrast of images by a random factor deterministically.

[`stateless_random_crop(...)`](https://www.tensorflow.org/api_docs/python/tf/image/stateless_random_crop)
: Randomly crops a tensor to a given size in a deterministic manner.

[`stateless_random_flip_left_right(...)`](https://www.tensorflow.org/api_docs/python/tf/image/stateless_random_flip_left_right)
: Randomly flip an image horizontally (left to right) deterministically.

[`stateless_random_flip_up_down(...)`](https://www.tensorflow.org/api_docs/python/tf/image/stateless_random_flip_up_down)
: Randomly flip an image vertically (upside down) deterministically.

[`stateless_random_hue(...)`](https://www.tensorflow.org/api_docs/python/tf/image/stateless_random_hue)
: Adjust the hue of RGB images by a random factor deterministically.

[`stateless_random_jpeg_quality(...)`](https://www.tensorflow.org/api_docs/python/tf/image/stateless_random_jpeg_quality)
: Deterministically radomize jpeg encoding quality for inducing jpeg noise.

[`stateless_random_saturation(...)`](https://www.tensorflow.org/api_docs/python/tf/image/stateless_random_saturation)
: Adjust the saturation of RGB images by a random factor deterministically.

[`stateless_sample_distorted_bounding_box(...)`](https://www.tensorflow.org/api_docs/python/tf/image/stateless_sample_distorted_bounding_box)
: Generate a randomly distorted bounding box for an image deterministically.

[`total_variation(...)`](https://www.tensorflow.org/api_docs/python/tf/image/total_variation)
: Calculate and return the total variation for one or more images.

[`transpose(...)`](https://www.tensorflow.org/api_docs/python/tf/image/transpose)
: Transpose image(s) by swapping the height and width dimension.

[`yiq_to_rgb(...)`](https://www.tensorflow.org/api_docs/python/tf/image/yiq_to_rgb)
: Converts one or more images from YIQ to RGB.

[`yuv_to_rgb(...)`](https://www.tensorflow.org/api_docs/python/tf/image/yuv_to_rgb)
: Converts one or more images from YUV to RGB.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.