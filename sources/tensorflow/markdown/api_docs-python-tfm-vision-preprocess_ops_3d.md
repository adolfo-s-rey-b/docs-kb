[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfm.vision.preprocess\_ops\_3d Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d#functions)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/preprocess_ops_3d.py)

Utils for processing video dataset features.

Functions
---------

[`crop_image(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d/crop_image)
: Crops the image sequence of images.

[`decode_image(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d/decode_image)
: Decodes PNG or JPEG raw bytes string into a RGB uint8 Tensor.

[`decode_jpeg(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d/decode_jpeg)
: Decodes JPEG raw bytes string into a RGB uint8 Tensor.

[`normalize_image(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d/normalize_image)
: Normalizes images.

[`random_crop_resize(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d/random_crop_resize)
: First crops clip with jittering and then resizes to (output\_h, output\_w).

[`random_flip_left_right(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d/random_flip_left_right)
: Flips all the frames with a probability of 50%.

[`random_rotation(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d/random_rotation)
: Randomly rotate all frames with 0, 90, 180, or 270 degrees.

[`resize_smallest(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d/resize_smallest)
: Resizes frames so that min(`height`, `width`) is equal to `min_resize`.

[`sample_linspace_sequence(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d/sample_linspace_sequence)
: Samples `num_windows` segments from sequence with linearly spaced offsets.

[`sample_segment_sequence(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d/sample_segment_sequence)
: Samples a single segment of size `num_frames` from a given sequence.

[`sample_sequence(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d/sample_sequence)
: Samples a single segment of size `num_steps` from a given sequence.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.