[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops#other-members)
    
*   [float64(value=0, /)](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops#float64value0)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfm.vision.box\_ops Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops#other-members)
    
*   [float64(value=0, /)](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops#float64value0)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/box_ops.py)

Box related ops.

Functions
---------

[`bbox2mask(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/bbox2mask)
: Converts bounding boxes to bitmasks.

[`bbox_generalized_overlap(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/bbox_generalized_overlap)
: Calculates the GIOU between proposal and ground truth boxes.

[`bbox_intersection_over_area(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/bbox_intersection_over_area)
: Calculates IoAs (intersection over area) between proposal and ground truth boxes.

[`bbox_overlap(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/bbox_overlap)
: Calculates the overlap between proposal and ground truth boxes.

[`box_matching(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/box_matching)
: Matches boxes to groundtruth boxes.

[`clip_boxes(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/clip_boxes)
: Clips boxes to image boundaries.

[`compute_outer_boxes(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/compute_outer_boxes)
: Computes outer box encloses an object with a margin.

[`cycxhw_to_yxyx(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/cycxhw_to_yxyx)
: Converts box center coordinates plus height and width terms to corner.

[`decode_boxes(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/decode_boxes)
: Decodes boxes.

[`denormalize_boxes(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/denormalize_boxes)
: Converts boxes normalized by \[height, width\] to pixel coordinates.

[`encode_boxes(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/encode_boxes)
: Encodes boxes to targets.

[`filter_boxes(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/filter_boxes)
: Filters and remove boxes that are too small or fall outside the image.

[`filter_boxes_by_scores(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/filter_boxes_by_scores)
: Filters and remove boxes whose scores are smaller than the threshold.

[`gather_instances(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/gather_instances)
: Gathers instances by indices.

[`get_non_empty_box_indices(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/get_non_empty_box_indices)
: Gets indices for non-empty boxes.

[`horizontal_flip_boxes(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/horizontal_flip_boxes)
: Flips normalized boxes horizontally.

[`jitter_boxes(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/jitter_boxes)
: Jitters the box coordinates by some noise distribution.

[`normalize_boxes(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/normalize_boxes)
: Converts boxes to the normalized coordinates.

[`top_k_boxes(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/top_k_boxes)
: Sorts and select top k boxes according to the scores.

[`vertical_flip_boxes(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/vertical_flip_boxes)
: Flips normalized boxes vertically.

[`yxyx_to_cycxhw(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/yxyx_to_cycxhw)
: Converts box corner coordinates to center plus height and width terms.

[`yxyx_to_xywh(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/yxyx_to_xywh)
: Converts boxes from ymin, xmin, ymax, xmax to xmin, ymin, width, height.

|     |     |
| --- | --- |
| Other Members<br>------------- |     |
| BBOX\_XFORM\_CLIP | `np.float64(4.135166556742356)`<br><br>float64(value=0, /)<br>-------------------<br><br>Double-precision floating-point number type, compatible with Python :class:`float` and C `double`.<br><br>:Character code: `'d'` :Canonical name: `numpy.double` :Alias on this platform (Linux x86\_64): `numpy.float64`: 64-bit precision floating-point number type: sign bit, 11 bits exponent, 52 bits mantissa. |
| EPSILON | `1e-08` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.