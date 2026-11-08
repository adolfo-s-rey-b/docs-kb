[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fvision%2Fspatial_transform_ops&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfm.vision.spatial\_transform\_ops Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

*   On this page
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops#functions)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/spatial_transform_ops.py)

Spatial transform ops.

Functions
---------

[`bbox2mask(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/bbox2mask)
: Converts bounding boxes to bitmasks.

[`bilinear_resize(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops/bilinear_resize)
: Bilinear resizes the images.

[`bilinear_resize_to_bbox(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops/bilinear_resize_to_bbox)
: Bilinear resizes the images to fit into the bounding boxes in the output.

[`bilinear_resize_with_crop_and_pad(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops/bilinear_resize_with_crop_and_pad)
: Bilinear resizes the images, then crops and finally pads to output size.

[`bilinear_resize_with_pad(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops/bilinear_resize_with_pad)
: Bilinear resizes the images, then pads to output size.

[`crop_mask_in_target_box(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops/crop_mask_in_target_box)
: Crop masks in target boxes.

[`multilevel_crop_and_resize(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops/multilevel_crop_and_resize)
: Crop and resize on multilevel feature pyramid.

[`nearest_upsampling(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops/nearest_upsampling)
: Nearest neighbor upsampling implementation.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.