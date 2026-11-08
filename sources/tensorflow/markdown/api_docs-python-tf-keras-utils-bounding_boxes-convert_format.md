[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/convert_format#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/convert_format)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/convert_format?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/convert_format#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/convert_format#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/convert_format#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.utils.bounding\_boxes.convert\_format Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/convert_format#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/convert_format#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/convert_format#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/bounding_boxes/converters.py#L10-L70)

Converts bounding boxes between formats.

tf.keras.utils.bounding_boxes.convert_format(
        boxes, source, target, height=None, width=None, dtype='float32'
    )

Supported formats (case-insensitive): `"xyxy"`: \[left, top, right, bottom\] `"yxyx"`: \[top, left, bottom, right\] `"xywh"`: \[left, top, width, height\] `"center_xywh"`: \[center\_x, center\_y, width, height\] `"center_yxhw"`: \[center\_y, center\_x, height, width\] `"rel_xyxy"`, `"rel_yxyx"`, `"rel_xywh"`, `"rel_center_xywh"`: Relative versions of the above formats, where coordinates are normalized to the range \[0, 1\] based on the image `height` and `width`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `boxes` | Bounding boxes tensor/array or dictionary of `boxes` and `labels`. |
| `source` | Source format string. |
| `target` | Target format string. |
| `height` | Image height (required for relative target format). |
| `width` | Image width (required for relative target format). |
| `dtype` | Data type for conversion (optional). |

|     |
| --- |
| Returns<br>------- |     |
| Converted boxes. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | For invalid formats, shapes, or missing dimensions. |

#### Example:

boxes = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])
    # Convert from 'xyxy' to 'xywh' format
    boxes_xywh = keras.utils.bounding_boxes.convert_format(
        boxes, source='xyxy', target='xywh'
    )  # Output: [[10. 20. 20. 20.], [50. 60. 20. 20.]]
    
    # Convert to relative 'rel_xyxy' format
    boxes_rel_xyxy = keras.utils.bounding_boxes.convert_format(
        boxes, source='xyxy', target='rel_xyxy', height=200, width=300
    ) # Output: [[0.03333334 0.1        0.1        0.2       ],\
               #[0.16666667 0.3        0.23333333 0.4       ]]

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.