[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/visualization/draw_bounding_boxes#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.visualization.draw\_bounding\_boxes Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/visualization/draw_bounding_boxes.py#L16-L170)

Draws bounding boxes on images.

tf.keras.visualization.draw_bounding_boxes(
        images,
        bounding_boxes,
        bounding_box_format,
        class_mapping=None,
        color=(128, 128, 128),
        line_thickness=2,
        text_thickness=1,
        font_scale=1.0,
        data_format=None
    )

This function draws bounding boxes on a batch of images. It supports different bounding box formats and can optionally display class labels and confidences.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `images` | A batch of images as a 4D tensor or NumPy array. Shape should be `(batch_size, height, width, channels)`. |
| `bounding_boxes` | A dictionary containing bounding box data. Should have the following keys:<br><br>*   `boxes`: A tensor or array of shape `(batch_size, num_boxes, 4)` containing the bounding box coordinates in the specified format.<br>*   `labels`: A tensor or array of shape `(batch_size, num_boxes)` containing the class labels for each bounding box.<br>*   `confidences` (Optional): A tensor or array of shape `(batch_size, num_boxes)` containing the confidence scores for each bounding box. |
| `bounding_box_format` | A string specifying the format of the bounding boxes. See [`keras.utils.bounding_boxes.convert_format`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/convert_format)<br> for supported formats (e.g., "xyxy", "yxyx", "xywh", "center\_xywh", "center_yxhw", and the "rel_\*" variants). |
| `class_mapping` | A dictionary mapping class IDs (integers) to class labels (strings). Used to display class labels next to the bounding boxes. Defaults to None (no labels displayed). |
| `color` | A tuple or list representing the RGB color of the bounding boxes. For example, `(255, 0, 0)` for red. Defaults to `(128, 128, 128)`. |
| `line_thickness` | An integer specifying the thickness of the bounding box lines. Defaults to `2`. |
| `text_thickness` | An integer specifying the thickness of the text labels. Defaults to `1`. |
| `font_scale` | A float specifying the scale of the font used for text labels. Defaults to `1.0`. |
| `data_format` | A string, either `"channels_last"` or `"channels_first"`, specifying the order of dimensions in the input images. Defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be "channels\_last". |

|     |
| --- |
| Returns<br>------- |     |
| A NumPy array of the annotated images with the bounding boxes drawn. The array will have the same shape as the input `images`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `images` is not a 4D tensor/array, if `bounding_boxes` is not a dictionary, or if `bounding_boxes` does not contain `"boxes"` and `"labels"` keys. |
| `TypeError` | If `bounding_boxes` is not a dictionary. |
| `ImportError` | If `cv2` (OpenCV) is not installed. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.