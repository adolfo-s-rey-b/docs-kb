[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/visualization/plot_bounding_box_gallery#main-content)

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
    

tf.keras.visualization.plot\_bounding\_box\_gallery Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/visualization/plot_bounding_box_gallery.py#L17-L167)

Plots a gallery of images with bounding boxes.

tf.keras.visualization.plot_bounding_box_gallery(
        images,
        bounding_box_format,
        y_true=None,
        y_pred=None,
        value_range=(0, 255),
        true_color=(0, 188, 212),
        pred_color=(255, 235, 59),
        line_thickness=2,
        font_scale=1.0,
        text_thickness=None,
        class_mapping=None,
        ground_truth_mapping=None,
        prediction_mapping=None,
        legend=False,
        legend_handles=None,
        rows=None,
        cols=None,
        data_format=None,
        **kwargs
    )

This function can display both ground truth and predicted bounding boxes on a set of images. It supports various bounding box formats and can include class labels and a legend.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `images` | A 4D tensor or NumPy array of images. Shape should be `(batch_size, height, width, channels)`. |
| `bounding_box_format` | The format of the bounding boxes. See [`keras.utils.bounding_boxes.convert_format`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/convert_format)<br> for supported formats (e.g., "xyxy", "yxyx", "xywh", "center\_xywh", "center_yxhw", and the "rel_\*" variants). |
| `y_true` | A dictionary containing the ground truth bounding boxes and labels. Should have the same structure as the `bounding_boxes` argument in [`keras.visualization.draw_bounding_boxes`](https://www.tensorflow.org/api_docs/python/tf/keras/visualization/draw_bounding_boxes)<br>. Defaults to `None`. |
| `y_pred` | A dictionary containing the predicted bounding boxes and labels. Should have the same structure as `y_true`. Defaults to `None`. |
| `value_range` | A tuple specifying the value range of the images (e.g., `(0, 255)` or `(0, 1)`). Defaults to `(0, 255)`. |
| `true_color` | A tuple of three integers representing the RGB color for the ground truth bounding boxes. Defaults to `(0, 188, 212)`. |
| `pred_color` | A tuple of three integers representing the RGB color for the predicted bounding boxes. Defaults to `(255, 235, 59)`. |
| `line_thickness` | The thickness of the bounding box lines. Defaults to 2. |
| `font_scale` | The scale of the font used for labels. Defaults to 1.0. |
| `text_thickness` | The thickness of the bounding box text. Defaults to `line_thickness`. |
| `class_mapping` | A dictionary mapping class IDs to class names. Used for both ground truth and predicted boxes if `ground_truth_mapping` and `prediction_mapping` are not provided. Defaults to `None`. |
| `ground_truth_mapping` | A dictionary mapping class IDs to class names specifically for ground truth boxes. Overrides `class_mapping` for ground truth. Defaults to `None`. |
| `prediction_mapping` | A dictionary mapping class IDs to class names specifically for predicted boxes. Overrides `class_mapping` for predictions. Defaults to `None`. |
| `legend` | A boolean indicating whether to show a legend. Defaults to `False`. |
| `legend_handles` | A list of matplotlib `Patch` objects to use for the legend. If this is provided, the `legend` argument will be ignored. Defaults to `None`. |
| `rows` | The number of rows in the image gallery. Required if the images are not batched. Defaults to `None`. |
| `cols` | The number of columns in the image gallery. Required if the images are not batched. Defaults to `None`. |
| `data_format` | The image data format `"channels_last"` or `"channels_first"`. Defaults to the Keras backend data format. |
| `kwargs` | Additional keyword arguments to be passed to [`keras.visualization.plot_image_gallery`](https://www.tensorflow.org/api_docs/python/tf/keras/visualization/plot_image_gallery)<br>. |

|     |
| --- |
| Returns<br>------- |     |
| The output of [`keras.visualization.plot_image_gallery`](https://www.tensorflow.org/api_docs/python/tf/keras/visualization/plot_image_gallery)<br>. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `images` is not a 4D tensor/array or if both `legend` and `legend_handles` are specified. |
| `ImportError` | if matplotlib is not installed |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.