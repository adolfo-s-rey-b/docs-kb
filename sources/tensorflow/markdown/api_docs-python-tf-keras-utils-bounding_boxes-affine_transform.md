[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/affine_transform#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/affine_transform)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/affine_transform?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/affine_transform#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/affine_transform#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.utils.bounding\_boxes.affine\_transform Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/affine_transform#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/affine_transform#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/bounding_boxes/converters.py#L116-L177)

Applies an affine transformation to the bounding boxes.

tf.keras.utils.bounding_boxes.affine_transform(
        boxes,
        angle,
        translate_x,
        translate_y,
        scale,
        shear_x,
        shear_y,
        height,
        width,
        center_x=None,
        center_y=None,
        bounding_box_format='xyxy'
    )

The `height` and `width` parameters are used to normalize the translation and scaling factors.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `boxes` | The bounding boxes to transform, a tensor/array of shape `(N, 4)` or `(batch_size, N, 4)`. |
| `angle` | Rotation angle in degrees. |
| `translate_x` | Horizontal translation fraction. |
| `translate_y` | Vertical translation fraction. |
| `scale` | Scaling factor. |
| `shear_x` | Shear angle in x-direction (degrees). |
| `shear_y` | Shear angle in y-direction (degrees). |
| `height` | Height of the image/data. |
| `width` | Width of the image/data. |
| `center_x` | x-coordinate of the transformation center (fraction). |
| `center_y` | y-coordinate of the transformation center (fraction). |
| `bounding_box_format` | The format of the input bounding boxes. Defaults to `"xyxy"`. |

|     |
| --- |
| Returns<br>------- |     |
| The transformed bounding boxes, a tensor/array with the same shape as the input `boxes`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.