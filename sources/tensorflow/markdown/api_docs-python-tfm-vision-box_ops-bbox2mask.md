[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/bbox2mask#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/bbox2mask)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/bbox2mask?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fvision%2Fbox_ops%2Fbbox2mask&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/bbox2mask#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/bbox2mask#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.box\_ops.bbox2mask Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/bbox2mask#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/bbox2mask#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/box_ops.py#L867-L927)

Converts bounding boxes to bitmasks.

#### View aliases

**Main aliases**

[`tfm.vision.spatial_transform_ops.bbox2mask`](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/bbox2mask)

tfm.vision.box_ops.bbox2mask(
        bbox: tf.Tensor,
        *,
        image_height: int,
        image_width: int,
        dtype: tf.DType = tf.bool
    ) -> tf.Tensor

|     |     |
| --- | --- |
| Args<br>---- |     |
| `bbox` | A tensor in shape (..., 4) with arbitrary numbers of batch dimensions, representing the absolute coordinates (ymin, xmin, ymax, xmax) for each bounding box. |
| `image_height` | an integer representing the height of the image. |
| `image_width` | an integer representing the width of the image. |
| `dtype` | DType of the output bitmasks. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor in shape (..., height, width) which stores the bitmasks created from the bounding boxes. For example:<br><br>    bbox2mask(tf.constant([[1,2,4,4]]), |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.