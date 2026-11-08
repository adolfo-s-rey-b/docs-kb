[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/compute_outer_boxes#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/compute_outer_boxes)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/compute_outer_boxes?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fvision%2Fbox_ops%2Fcompute_outer_boxes&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/compute_outer_boxes#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/compute_outer_boxes#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.box\_ops.compute\_outer\_boxes Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/compute_outer_boxes#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/compute_outer_boxes#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/box_ops.py#L297-L328)

Computes outer box encloses an object with a margin.

tfm.vision.box_ops.compute_outer_boxes(
        boxes, image_shape, scale=1.0
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `boxes` | a tensor whose last dimension is 4 representing the coordinates of boxes in ymin, xmin, ymax, xmax order. |
| `image_shape` | a list of two integers, a two-element vector or a tensor such that all but the last dimensions are `broadcastable` to `boxes`. The last dimension is 2, which represents \[height, width\]. |
| `scale` | a float number specifying the scale of output outer boxes to input `boxes`. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `outer_boxes` | a tensor whose shape is the same as `boxes` representing the outer boxes. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.