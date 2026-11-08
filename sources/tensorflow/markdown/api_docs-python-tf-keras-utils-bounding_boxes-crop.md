[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/crop#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/crop)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/crop?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/crop#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/crop#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.utils.bounding\_boxes.crop Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/crop#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/crop#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/bounding_boxes/converters.py#L180-L221)

Crops bounding boxes based on the given offsets and dimensions.

tf.keras.utils.bounding_boxes.crop(
        boxes, top, left, height, width, bounding_box_format='xyxy'
    )

This function crops bounding boxes to a specified region defined by `top`, `left`, `height`, and `width`. The boxes are first converted to `xyxy` format, cropped, and then returned.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `boxes` | The bounding boxes to crop. A NumPy array or tensor of shape `(N, 4)` or `(batch_size, N, 4)`. |
| `top` | The vertical offset of the top-left corner of the cropping region. |
| `left` | The horizontal offset of the top-left corner of the cropping region. |
| `height` | The height of the cropping region. Defaults to `None`. |
| `width` | The width of the cropping region. Defaults to `None`. |
| `bounding_box_format` | The format of the input bounding boxes. Defaults to `"xyxy"`. |

|     |
| --- |
| Returns<br>------- |     |
| The cropped bounding boxes. |     |

#### Example:

boxes = np.array([[10, 20, 50, 60], [70, 80, 100, 120]])  # xyxy format
    cropped_boxes = keras.utils.bounding_boxes.crop(
        boxes, bounding_box_format="xyxy", top=10, left=20, height=40, width=30
    )  # Cropping a 30x40 region starting at (20, 10)
    print(cropped_boxes)
    # Expected output:
    # array([[ 0., 10., 30., 50.],\
    #        [50., 70., 80., 110.]])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.