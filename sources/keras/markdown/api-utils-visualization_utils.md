None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [Layers API](https://keras.io/api/layers/)
 [Callbacks API](https://keras.io/api/callbacks/)
 [Ops API](https://keras.io/api/ops/)
 [Optimizers](https://keras.io/api/optimizers/)
 [Metrics](https://keras.io/api/metrics/)
 [Losses](https://keras.io/api/losses/)
 [Data loading](https://keras.io/api/data_loading/)
 [Tree API](https://keras.io/api/tree/)
 [Built-in small datasets](https://keras.io/api/datasets/)
 [Keras Applications](https://keras.io/api/applications/)
 [Mixed precision](https://keras.io/api/mixed_precision/)
 [Multi-device distribution](https://keras.io/api/distribution/)
 [RNG API](https://keras.io/api/random/)
 [Quantizers](https://keras.io/api/quantizers/)
 [Scope](https://keras.io/api/scope/)
 [Rematerialization](https://keras.io/api/rematerialization/)
 [Utilities](https://keras.io/api/utils/)
 [Experiment management utilities](https://keras.io/api/utils/experiment_management_utils/)
 [Model plotting utilities](https://keras.io/api/utils/model_plotting_utils/)
 [Structured data preprocessing utilities](https://keras.io/api/utils/feature_space/)
 [Tensor utilities](https://keras.io/api/utils/tensor_utils/)
 [Bounding boxes](https://keras.io/api/utils/bounding_boxes/)
 [Python & NumPy utilities](https://keras.io/api/utils/python_utils/)
 [Bounding boxes utilities](https://keras.io/api/utils/bounding_boxes_utils/)
 [Visualization utilities](https://keras.io/api/utils/visualization_utils/)
 [Preprocessing utilities](https://keras.io/api/utils/preprocessing_utils/)
 [Backend utilities](https://keras.io/api/utils/backend_utils/)
 [Scikit-Learn API wrappers](https://keras.io/api/utils/sklearn_wrappers/)
 [Keras configuration utilities](https://keras.io/api/utils/config_utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

► [Keras 3 API documentation](https://keras.io/api/)
 / [Utilities](https://keras.io/api/utils/)
 / Visualization utilities

Visualization utilities
=======================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/visualization/draw_bounding_boxes.py#L16)

### `draw_bounding_boxes` function

Copied!

`keras.visualization.draw_bounding_boxes(     images,     bounding_boxes,     bounding_box_format,     class_mapping=None,     color=(128, 128, 128),     line_thickness=2,     text_thickness=1,     font_scale=1.0,     data_format=None, )`

Draws bounding boxes on images.

This function draws bounding boxes on a batch of images. It supports different bounding box formats and can optionally display class labels and confidences.

**Arguments**

*   **images**: A batch of images as a 4D tensor or NumPy array. Shape should be `(batch_size, height, width, channels)`.
*   **bounding\_boxes**: A dictionary containing bounding box data. Should have the following keys:
    *   `boxes`: A tensor or array of shape `(batch_size, num_boxes, 4)` containing the bounding box coordinates in the specified format.
    *   `labels`: A tensor or array of shape `(batch_size, num_boxes)` containing the class labels for each bounding box.
    *   `confidences` (Optional): A tensor or array of shape `(batch_size, num_boxes)` containing the confidence scores for each bounding box.
*   **bounding\_box\_format**: A string specifying the format of the bounding boxes. See [`keras.utils.bounding_boxes.convert_format`](https://keras.io/api/utils/bounding_boxes_utils#convertformat-function)
     for supported formats (e.g., "xyxy", "yxyx", "xywh", "center\_xywh", "center\_yxhw", and the "rel\_\*" variants).
*   **class\_mapping**: A dictionary mapping class IDs (integers) to class labels (strings). Used to display class labels next to the bounding boxes. Defaults to None (no labels displayed).
*   **color**: A tuple or list representing the RGB color of the bounding boxes. For example, `(255, 0, 0)` for red. Defaults to `(128, 128, 128)`.
*   **line\_thickness**: An integer specifying the thickness of the bounding box lines. Defaults to `2`.
*   **text\_thickness**: An integer specifying the thickness of the text labels. Defaults to `1`.
*   **font\_scale**: A float specifying the scale of the font used for text labels. Defaults to `1.0`.
*   **data\_format**: A string, either `"channels_last"` or `"channels_first"`, specifying the order of dimensions in the input images. Defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be "channels\_last".

**Returns**

A NumPy array of the annotated images with the bounding boxes drawn. The array will have the same shape as the input `images`.

**Raises**

*   **ValueError**: If `images` is not a 4D tensor/array, if `bounding_boxes` is not a dictionary, or if `bounding_boxes` does not contain `"boxes"` and `"labels"` keys.
*   **TypeError**: If `bounding_boxes` is not a dictionary.
*   **ImportError**: If `cv2` (OpenCV) is not installed.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/visualization/draw_segmentation_masks.py#L8)

### `draw_segmentation_masks` function

Copied!

`keras.visualization.draw_segmentation_masks(     images,     segmentation_masks,     num_classes=None,     color_mapping=None,     alpha=0.8,     blend=True,     ignore_index=-1,     data_format=None, )`

Draws segmentation masks on images.

The function overlays segmentation masks on the input images. The masks are blended with the images using the specified alpha value.

**Arguments**

*   **images**: A batch of images as a 4D tensor or NumPy array. Shape should be (batch\_size, height, width, channels).
*   **segmentation\_masks**: A batch of segmentation masks as a 3D or 4D tensor or NumPy array. Shape should be (batch\_size, height, width) or (batch\_size, height, width, 1). The values represent class indices starting from 1 up to `num_classes`. Class 0 is reserved for the background and will be ignored if `ignore_index` is not 0.
*   **num\_classes**: The number of segmentation classes. If `None`, it is inferred from the maximum value in `segmentation_masks`.
*   **color\_mapping**: A dictionary mapping class indices to RGB colors. If `None`, a default color palette is generated. The keys should be integers starting from 1 up to `num_classes`.
*   **alpha**: The opacity of the segmentation masks. Must be in the range `[0, 1]`.
*   **blend**: Whether to blend the masks with the input image using the `alpha` value. If `False`, the masks are drawn directly on the images without blending. Defaults to `True`.
*   **ignore\_index**: The class index to ignore. Mask pixels with this value will not be drawn. Defaults to -1.
*   **data\_format**: Image data format, either `"channels_last"` or `"channels_first"`. Defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`.

**Returns**

A NumPy array of the images with the segmentation masks overlaid.

**Raises**

*   **ValueError**: If the input `images` is not a 4D tensor or NumPy array.
*   **TypeError**: If the input `segmentation_masks` is not an integer type.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/visualization/plot_bounding_box_gallery.py#L17)

### `plot_bounding_box_gallery` function

Copied!

`keras.visualization.plot_bounding_box_gallery(     images,     bounding_box_format,     y_true=None,     y_pred=None,     value_range=(0, 255),     true_color=(0, 188, 212),     pred_color=(255, 235, 59),     line_thickness=2,     font_scale=1.0,     text_thickness=None,     class_mapping=None,     ground_truth_mapping=None,     prediction_mapping=None,     legend=False,     legend_handles=None,     rows=None,     cols=None,     data_format=None,     **kwargs )`

Plots a gallery of images with bounding boxes.

This function can display both ground truth and predicted bounding boxes on a set of images. It supports various bounding box formats and can include class labels and a legend.

**Arguments**

*   **images**: A 4D tensor or NumPy array of images. Shape should be `(batch_size, height, width, channels)`.
*   **bounding\_box\_format**: The format of the bounding boxes. See [`keras.utils.bounding_boxes.convert_format`](https://keras.io/api/utils/bounding_boxes_utils#convertformat-function)
     for supported formats (e.g., "xyxy", "yxyx", "xywh", "center\_xywh", "center\_yxhw", and the "rel\_\*" variants).
*   **y\_true**: A dictionary containing the ground truth bounding boxes and labels. Should have the same structure as the `bounding_boxes` argument in [`keras.visualization.draw_bounding_boxes`](https://keras.io/api/utils/visualization_utils#drawboundingboxes-function)
    . Defaults to `None`.
*   **y\_pred**: A dictionary containing the predicted bounding boxes and labels. Should have the same structure as `y_true`. Defaults to `None`.
*   **value\_range**: A tuple specifying the value range of the images (e.g., `(0, 255)` or `(0, 1)`). Defaults to `(0, 255)`.
*   **true\_color**: A tuple of three integers representing the RGB color for the ground truth bounding boxes. Defaults to `(0, 188, 212)`.
*   **pred\_color**: A tuple of three integers representing the RGB color for the predicted bounding boxes. Defaults to `(255, 235, 59)`.
*   **line\_thickness**: The thickness of the bounding box lines. Defaults to 2.
*   **font\_scale**: The scale of the font used for labels. Defaults to 1.0.
*   **text\_thickness**: The thickness of the bounding box text. Defaults to `line_thickness`.
*   **class\_mapping**: A dictionary mapping class IDs to class names. Used for both ground truth and predicted boxes if `ground_truth_mapping` and `prediction_mapping` are not provided. Defaults to `None`.
*   **ground\_truth\_mapping**: A dictionary mapping class IDs to class names specifically for ground truth boxes. Overrides `class_mapping` for ground truth. Defaults to `None`.
*   **prediction\_mapping**: A dictionary mapping class IDs to class names specifically for predicted boxes. Overrides `class_mapping` for predictions. Defaults to `None`.
*   **legend**: A boolean indicating whether to show a legend. Defaults to `False`.
*   **legend\_handles**: A list of matplotlib `Patch` objects to use for the legend. If this is provided, the `legend` argument will be ignored. Defaults to `None`.
*   **rows**: The number of rows in the image gallery. Required if the images are not batched. Defaults to `None`.
*   **cols**: The number of columns in the image gallery. Required if the images are not batched. Defaults to `None`.
*   **data\_format**: The image data format `"channels_last"` or `"channels_first"`. Defaults to the Keras backend data format.
*   **kwargs**: Additional keyword arguments to be passed to [`keras.visualization.plot_image_gallery`](https://keras.io/api/utils/visualization_utils#plotimagegallery-function)
    .

**Returns**

The output of [`keras.visualization.plot_image_gallery`](https://keras.io/api/utils/visualization_utils#plotimagegallery-function)
.

**Raises**

*   **ValueError**: If `images` is not a 4D tensor/array or if both `legend` and `legend_handles` are specified.
*   **ImportError**: if matplotlib is not installed

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/visualization/plot_image_gallery.py#L44)

### `plot_image_gallery` function

Copied!

`keras.visualization.plot_image_gallery(     images,     y_true=None,     y_pred=None,     label_map=None,     rows=None,     cols=None,     value_range=(0, 255),     scale=2,     path=None,     show=None,     transparent=True,     dpi=60,     legend_handles=None,     data_format=None, )`

Displays a gallery of images with optional labels and predictions.

**Arguments**

*   **images**: A 4D tensor or NumPy array of images. Shape should be `(batch_size, height, width, channels)`.
*   **y\_true**: A 1D tensor or NumPy array of true labels (class indices). Defaults to `None`.
*   **y\_pred**: A 1D tensor or NumPy array of predicted labels (class indices). Defaults to `None`.
*   **label\_map**: A dictionary mapping class indices to class names. Required if `y_true` or `y_pred` are provided. Defaults to `None`.
*   **value\_range**: A tuple specifying the value range of the images (e.g., `(0, 255)` or `(0, 1)`). Defaults to `(0, 255)`.
*   **rows**: The number of rows in the gallery. If `None`, it's calculated based on the number of images and `cols`. Defaults to `None`.
*   **cols**: The number of columns in the gallery. If `None`, it's calculated based on the number of images and `rows`. Defaults to `None`.
*   **scale**: A float controlling the size of the displayed images. The images are scaled by this factor. Defaults to `2`.
*   **path**: The path to save the generated gallery image. If `None`, the image is displayed using `plt.show()`. Defaults to `None`.
*   **show**: Whether to display the image using `plt.show()`. If `True`, the image is displayed. If `False`, the image is not displayed. Ignored if `path` is not `None`. Defaults to `True` if `path` is `None`, `False` otherwise.
*   **transparent**: A boolean, whether to save the figure with a transparent background. Defaults to `True`.
*   **dpi**: The DPI (dots per inch) for saving the figure. Defaults to 60.
*   **legend\_handles**: A list of matplotlib `Patch` objects to use as legend handles. Defaults to `None`.
*   **data\_format**: The image data format `"channels_last"` or `"channels_first"`. Defaults to the Keras backend data format.

**Raises**

*   **ValueError**: If both `path` and `show` are set to non-`None` values, if `images` is not a 4D tensor or array, or if `y_true` or `y_pred` are provided without a `label_map`.
*   **ImportError**: if matplotlib is not installed.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/visualization/plot_segmentation_mask_gallery.py#L14)

### `plot_segmentation_mask_gallery` function

Copied!

`keras.visualization.plot_segmentation_mask_gallery(     images,     num_classes,     value_range=(0, 255),     y_true=None,     y_pred=None,     color_mapping=None,     blend=True,     alpha=0.8,     ignore_index=-1,     data_format=None,     **kwargs )`

Plots a gallery of images with corresponding segmentation masks.

**Arguments**

*   **images**: A 4D tensor or NumPy array of images. Shape should be `(batch_size, height, width, channels)`.
*   **num\_classes**: The number of segmentation classes. Class indices should start from `1`. Class `0` will be treated as background and ignored if `ignore_index` is not 0.
*   **value\_range**: A tuple specifying the value range of the images (e.g., `(0, 255)` or `(0, 1)`). Defaults to `(0, 255)`.
*   **y\_true**: A 3D/4D tensor or NumPy array representing the ground truth segmentation masks. Shape should be `(batch_size, height, width)` or `(batch_size, height, width, 1)`. Defaults to `None`.
*   **y\_pred**: A 3D/4D tensor or NumPy array representing the predicted segmentation masks. Shape should be the same as `y_true`. Defaults to `None`.
*   **color\_mapping**: A dictionary mapping class indices to RGB colors. If `None`, a default color palette is used. Class indices start from `1`. Defaults to `None`.
*   **blend**: Whether to blend the masks with the input image using the `alpha` value. If `False`, the masks are drawn directly on the images without blending. Defaults to `True`.
*   **alpha**: The opacity of the segmentation masks (a float between 0 and 1). Defaults to `0.8`.
*   **ignore\_index**: The class index to ignore when drawing masks. Defaults to `-1`.
*   **data\_format**: The image data format `"channels_last"` or `"channels_first"`. Defaults to the Keras backend data format.
*   **kwargs**: Additional keyword arguments to be passed to [`keras.visualization.plot_image_gallery`](https://keras.io/api/utils/visualization_utils#plotimagegallery-function)
    .

**Returns**

The output of [`keras.visualization.plot_image_gallery`](https://keras.io/api/utils/visualization_utils#plotimagegallery-function)
.

**Raises**

*   **ValueError**: If `images` is not a 4D tensor/array.

* * *

[Visualization utilities](https://keras.io/api/utils/visualization_utils/#visualization-utilities)

[`draw_bounding_boxes` function](https://keras.io/api/utils/visualization_utils/#drawboundingboxes-function)

[`draw_segmentation_masks` function](https://keras.io/api/utils/visualization_utils/#drawsegmentationmasks-function)

[`plot_bounding_box_gallery` function](https://keras.io/api/utils/visualization_utils/#plotboundingboxgallery-function)

[`plot_image_gallery` function](https://keras.io/api/utils/visualization_utils/#plotimagegallery-function)

[`plot_segmentation_mask_gallery` function](https://keras.io/api/utils/visualization_utils/#plotsegmentationmaskgallery-function)