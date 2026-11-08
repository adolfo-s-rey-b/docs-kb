[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/draw_bounding_boxes#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/draw_bounding_boxes)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/draw_bounding_boxes?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/draw_bounding_boxes#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/draw_bounding_boxes#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.image.draw\_bounding\_boxes Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/draw_bounding_boxes#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/draw_bounding_boxes#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L5875-L5925)

Draw bounding boxes on a batch of images.

tf.compat.v1.image.draw_bounding_boxes(
        images, boxes, name=None, colors=None
    )

Outputs a copy of `images` but draws on top of the pixels zero or more bounding boxes specified by the locations in `boxes`. The coordinates of the each bounding box in `boxes` are encoded as `[y_min, x_min, y_max, x_max]`. The bounding box coordinates are floats in `[0.0, 1.0]` relative to the width and the height of the underlying image.

For example, if an image is 100 x 200 pixels (height x width) and the bounding box is `[0.1, 0.2, 0.5, 0.9]`, the upper-left and bottom-right coordinates of the bounding box will be `(40, 10)` to `(180, 50)` (in (x,y) coordinates).

Parts of the bounding box may fall outside the image.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `images` | A `Tensor`. Must be one of the following types: `float32`, `half`. 4-D with shape `[batch, height, width, depth]`. A batch of images. |
| `boxes` | A `Tensor` of type `float32`. 3-D with shape `[batch, num_bounding_boxes, 4]` containing bounding boxes. |
| `name` | A name for the operation (optional). |
| `colors` | A `Tensor` of type `float32`. 2-D. A list of RGBA colors to cycle through for the boxes. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `images`. |     |

#### Usage Example:

    # create an empty image

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.