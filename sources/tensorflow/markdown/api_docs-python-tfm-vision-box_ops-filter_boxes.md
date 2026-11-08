[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/filter_boxes#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/filter_boxes)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/filter_boxes?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/filter_boxes#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/filter_boxes#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.box\_ops.filter\_boxes Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/filter_boxes#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/filter_boxes#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/box_ops.py#L447-L504)

Filters and remove boxes that are too small or fall outside the image.

tfm.vision.box_ops.filter_boxes(
        boxes, scores, image_shape, min_size_threshold
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `boxes` | a tensor whose last dimension is 4 representing the coordinates of boxes in ymin, xmin, ymax, xmax order. |
| `scores` | a tensor whose shape is the same as tf.shape(boxes)\[:-1\] representing the original scores of the boxes. |
| `image_shape` | a tensor whose shape is the same as, or `broadcastable` to `boxes` except the last dimension, which is 2, representing \[height, width\] of the scaled image. |
| `min_size_threshold` | a float representing the minimal box size in each side (w.r.t. the scaled image). Boxes whose sides are smaller than it will be filtered out. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `filtered_boxes` | a tensor whose shape is the same as `boxes` but with the position of the filtered boxes are filled with 0. |
| `filtered_scores` | a tensor whose shape is the same as 'scores' but with the positinon of the filtered boxes filled with 0. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.