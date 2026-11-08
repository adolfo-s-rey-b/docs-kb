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
 / Bounding boxes

Bounding boxes
==============

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/bounding_boxes/converters.py#L116)

### `affine_transform` function

Copied!

`keras.utils.bounding_boxes.affine_transform(     boxes,     angle,     translate_x,     translate_y,     scale,     shear_x,     shear_y,     height,     width,     center_x=None,     center_y=None,     bounding_box_format="xyxy", )`

Applies an affine transformation to the bounding boxes.

The `height` and `width` parameters are used to normalize the translation and scaling factors.

**Arguments**

*   **boxes**: The bounding boxes to transform, a tensor/array of shape `(N, 4)` or `(batch_size, N, 4)`.
*   **angle**: Rotation angle in degrees.
*   **translate\_x**: Horizontal translation fraction.
*   **translate\_y**: Vertical translation fraction.
*   **scale**: Scaling factor.
*   **shear\_x**: Shear angle in x-direction (degrees).
*   **shear\_y**: Shear angle in y-direction (degrees).
*   **height**: Height of the image/data.
*   **width**: Width of the image/data.
*   **center\_x**: x-coordinate of the transformation center (fraction).
*   **center\_y**: y-coordinate of the transformation center (fraction).
*   **bounding\_box\_format**: The format of the input bounding boxes. Defaults to `"xyxy"`.

**Returns**

The transformed bounding boxes, a tensor/array with the same shape as the input `boxes`.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/bounding_boxes/converters.py#L73)

### `clip_to_image_size` function

Copied!

`keras.utils.bounding_boxes.clip_to_image_size(     bounding_boxes, height=None, width=None, bounding_box_format="xyxy" )`

Clips bounding boxes to be within the image dimensions. **Arguments**

*   **bounding\_boxes**: A dictionary with 'boxes' shape `(N, 4)` or `(batch, N, 4)` and 'labels' shape `(N,)` or `(batch, N,)`.
*   **height**: Image height.
*   **width**: Image width.
*   **bounding\_box\_format**: The format of the input bounding boxes. Defaults to `"xyxy"`.

**Returns**

Clipped bounding boxes.

**Example**

Copied!

`boxes = {"boxes": np.array([[-10, -20, 150, 160], [50, 40, 70, 80]]),          "labels": np.array([0, 1])} clipped_boxes = keras.utils.bounding_boxes.clip_to_image_size(     boxes, height=100, width=120, ) # Output will have boxes clipped to the image boundaries, and labels # potentially adjusted if the clipped area becomes zero`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/bounding_boxes/iou.py#L176)

### `compute_ciou` function

Copied!

`keras.utils.bounding_boxes.compute_ciou(     boxes1, boxes2, bounding_box_format, image_shape=None )`

Computes the Complete IoU (CIoU) between two bounding boxes or between two batches of bounding boxes.

CIoU loss is an extension of GIoU loss, which further improves the IoU optimization for object detection. CIoU loss not only penalizes the bounding box coordinates but also considers the aspect ratio and center distance of the boxes. The length of the last dimension should be 4 to represent the bounding boxes.

**Arguments**

*   **box1 (tensor)**: tensor representing the first bounding box with shape (..., 4).
*   **box2 (tensor)**: tensor representing the second bounding box with shape (..., 4).
*   **bounding\_box\_format**: a case-insensitive string (for example, "xyxy"). Each bounding box is defined by these 4 values. For detailed information on the supported formats, see the [KerasCV bounding box documentation](https://keras.io/api/keras_cv/bounding_box/formats/)
    .
*   **image\_shape**: `Tuple[int]`. The shape of the image (height, width, 3). When using relative bounding box format for `box_format` the `image_shape` is used for normalization.

**Returns**

*   **tensor**: The CIoU distance between the two bounding boxes.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/bounding_boxes/iou.py#L55)

### `compute_iou` function

Copied!

`keras.utils.bounding_boxes.compute_iou(     boxes1, boxes2, bounding_box_format, use_masking=False, mask_val=-1, image_shape=None )`

Computes a lookup table vector containing the ious for a given set boxes.

The lookup vector is to be indexed by \[`boxes1_index`,`boxes2_index`\] if boxes are unbatched and by \[`batch`, `boxes1_index`,`boxes2_index`\] if the boxes are batched.

The users can pass `boxes1` and `boxes2` to be different ranks. For example: 1) `boxes1`: \[batch\_size, M, 4\], `boxes2`: \[batch\_size, N, 4\] -> return \[batch\_size, M, N\]. 2) `boxes1`: \[batch\_size, M, 4\], `boxes2`: \[N, 4\] -> return \[batch\_size, M, N\] 3) `boxes1`: \[M, 4\], `boxes2`: \[batch\_size, N, 4\] -> return \[batch\_size, M, N\] 4) `boxes1`: \[M, 4\], `boxes2`: \[N, 4\] -> return \[M, N\]

**Arguments**

*   **boxes1**: a list of bounding boxes in 'corners' format. Can be batched or unbatched.
*   **boxes2**: a list of bounding boxes in 'corners' format. Can be batched or unbatched.
*   **bounding\_box\_format**: a case-insensitive string which is one of `"xyxy"`, `"rel_xyxy"`, `"xyWH"`, `"center_xyWH"`, `"yxyx"`, `"rel_yxyx"`. For detailed information on the supported format, see the
*   **use\_masking**: whether masking will be applied. This will mask all `boxes1` or `boxes2` that have values less than 0 in all its 4 dimensions. Default to `False`.
*   **mask\_val**: int to mask those returned IOUs if the masking is True, defaults to -1.
*   **image\_shape**: `Tuple[int]`. The shape of the image (height, width, 3). When using relative bounding box format for `box_format` the `image_shape` is used for normalization.

**Returns**

*   **iou\_lookup\_table**: a vector containing the pairwise ious of boxes1 and boxes2.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/bounding_boxes/converters.py#L10)

### `convert_format` function

Copied!

`keras.utils.bounding_boxes.convert_format(     boxes, source, target, height=None, width=None, dtype="float32" )`

Converts bounding boxes between formats.

Supported formats (case-insensitive): `"xyxy"`: \[left, top, right, bottom\] `"yxyx"`: \[top, left, bottom, right\] `"xywh"`: \[left, top, width, height\] `"center_xywh"`: \[center\_x, center\_y, width, height\] `"center_yxhw"`: \[center\_y, center\_x, height, width\] `"rel_xyxy"`, `"rel_yxyx"`, `"rel_xywh"`, `"rel_center_xywh"`: Relative versions of the above formats, where coordinates are normalized to the range \[0, 1\] based on the image `height` and `width`.

**Arguments**

*   **boxes**: Bounding boxes tensor/array or dictionary of `boxes` and `labels`.
*   **source**: Source format string.
*   **target**: Target format string.
*   **height**: Image height (required for relative target format).
*   **width**: Image width (required for relative target format).
*   **dtype**: Data type for conversion (optional).

**Returns**

Converted boxes.

**Raises**

*   **ValueError**: For invalid formats, shapes, or missing dimensions.

**Example**

Copied!

`boxes = np.array([[10, 20, 30, 40], [50, 60, 70, 80]]) # Convert from 'xyxy' to 'xywh' format boxes_xywh = keras.utils.bounding_boxes.convert_format(     boxes, source='xyxy', target='xywh' )  # Output: [[10. 20. 20. 20.], [50. 60. 20. 20.]]  # Convert to relative 'rel_xyxy' format boxes_rel_xyxy = keras.utils.bounding_boxes.convert_format(     boxes, source='xyxy', target='rel_xyxy', height=200, width=300 ) # Output: [[0.03333334 0.1        0.1        0.2       ],            #[0.16666667 0.3        0.23333333 0.4       ]]`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/bounding_boxes/converters.py#L180)

### `crop` function

Copied!

`keras.utils.bounding_boxes.crop(     boxes, top, left, height, width, bounding_box_format="xyxy" )`

Crops bounding boxes based on the given offsets and dimensions.

This function crops bounding boxes to a specified region defined by `top`, `left`, `height`, and `width`. The boxes are first converted to `xyxy` format, cropped, and then returned.

**Arguments**

*   **boxes**: The bounding boxes to crop. A NumPy array or tensor of shape `(N, 4)` or `(batch_size, N, 4)`.
*   **top**: The vertical offset of the top-left corner of the cropping region.
*   **left**: The horizontal offset of the top-left corner of the cropping region.
*   **height**: The height of the cropping region. Defaults to `None`.
*   **width**: The width of the cropping region. Defaults to `None`.
*   **bounding\_box\_format**: The format of the input bounding boxes. Defaults to `"xyxy"`.

**Returns**

The cropped bounding boxes.

**Example**

Copied!

``boxes = np.array([[10, 20, 50, 60], [70, 80, 100, 120]])  # xyxy format cropped_boxes = keras.utils.bounding_boxes.crop(     boxes, bounding_box_format="xyxy", top=10, left=20, height=40, width=30 )  # Cropping a 30x40 region starting at (20, 10) print(cropped_boxes) __Expected output__  :  __array([[ 0., 10., 30., 50.]__  ,  __       [50., 70., 80., 110.]])__  ----  <span style="float:right;">[[source]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/bounding_boxes/converters.py#L347)</span>  ### `decode_deltas_to_boxes` function  ```python keras.utils.bounding_boxes.decode_deltas_to_boxes(     anchors,     boxes_delta,     anchor_format,     box_format,     encoded_format="center_yxhw",     variance=None,     image_shape=None, )``

Converts bounding boxes from delta format to the specified `box_format`.

This function decodes bounding box deltas relative to anchors to obtain the final bounding box coordinates. The boxes are encoded in a specific `encoded_format` (center\_yxhw by default) during the decoding process. This allows flexibility in how the deltas are applied to the anchors.

**Arguments**

*   **anchors**: Can be `Tensors` or `Dict[Tensors]` where keys are level indices and values are corresponding anchor boxes. The shape of the array/tensor should be `(N, 4)` where N is the number of anchors. boxes\_delta Can be `Tensors` or `Dict[Tensors]` Bounding box deltas must have the same type and structure as `anchors`. The shape of the array/tensor can be `(N, 4)` or `(B, N, 4)` where N is the number of boxes.
*   **anchor\_format**: str. The format of the input `anchors`. (e.g., `"xyxy"`, `"xywh"`, etc.)
*   **box\_format**: str. The desired format for the output boxes. (e.g., `"xyxy"`, `"xywh"`, etc.)
*   **encoded\_format**: str. Raw output format from regression head. Defaults to `"center_yxhw"`.
*   **variance**: `List[floats]`. A 4-element array/tensor representing variance factors to scale the box deltas. If provided, the deltas are multiplied by the variance before being applied to the anchors. Defaults to None.
*   **image\_shape**: `Tuple[int]`. The shape of the image (height, width, 3). When using relative bounding box format for `box_format` the `image_shape` is used for normalization.

**Returns**

Decoded box coordinates. The return type matches the `box_format`.

**Raises**

*   **ValueError**: If `variance` is not None and its length is not 4.
*   **ValueError**: If `encoded_format` is not `"center_xywh"` or `"center_yxhw"`.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/bounding_boxes/converters.py#L255)

### `encode_box_to_deltas` function

Copied!

`keras.utils.bounding_boxes.encode_box_to_deltas(     anchors,     boxes,     anchor_format,     box_format,     encoding_format="center_yxhw",     variance=None,     image_shape=None, )`

Encodes bounding boxes relative to anchors as deltas.

This function calculates the deltas that represent the difference between bounding boxes and provided anchors. Deltas encode the offsets and scaling factors to apply to anchors to obtain the target boxes.

Boxes and anchors are first converted to the specified `encoding_format` (defaulting to `center_yxhw`) for consistent delta representation.

**Arguments**

*   **anchors**: `Tensors`. Anchor boxes with shape of `(N, 4)` where N is the number of anchors.
*   **boxes**: `Tensors` Bounding boxes to encode. Boxes can be of shape `(B, N, 4)` or `(N, 4)`.
*   **anchor\_format**: str. The format of the input `anchors` (e.g., "xyxy", "xywh", etc.).
*   **box\_format**: str. The format of the input `boxes` (e.g., "xyxy", "xywh", etc.).
*   **encoding\_format**: str. The intermediate format to which boxes and anchors are converted before delta calculation. Defaults to "center\_yxhw".
*   **variance**: `List[float]`. A 4-element array/tensor representing variance factors to scale the box deltas. If provided, the calculated deltas are divided by the variance. Defaults to None.
*   **image\_shape**: `Tuple[int]`. The shape of the image (height, width, 3). When using relative bounding box format for `box_format` the `image_shape` is used for normalization.

**Returns**

Encoded box deltas. The return type matches the `encode_format`.

**Raises**

*   **ValueError**: If `variance` is not None and its length is not 4.
*   **ValueError**: If `encoding_format` is not `"center_xywh"` or `"center_yxhw"`.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/bounding_boxes/converters.py#L224)

### `pad` function

Copied!

`keras.utils.bounding_boxes.pad(     boxes, top, left, height=None, width=None, bounding_box_format="xyxy" )`

Pads bounding boxes by adding top and left offsets.

This function adds padding to the bounding boxes by increasing the 'top' and 'left' coordinates by the specified amounts. The method assume the input bounding\_box\_format is `xyxy`.

**Arguments**

*   **boxes**: Bounding boxes to pad. Shape `(N, 4)` or `(batch, N, 4)`.
*   **top**: Vertical padding to add.
*   **left**: Horizontal padding to add.
*   **height**: Image height. Defaults to None.
*   **width**: Image width. Defaults to None.
*   **bounding\_box\_format**: The format of the input bounding boxes. Defaults to `"xyxy"`.

**Returns**

Padded bounding boxes in the original format.

* * *

[Bounding boxes](https://keras.io/api/utils/bounding_boxes/#bounding-boxes)

[`affine_transform` function](https://keras.io/api/utils/bounding_boxes/#affinetransform-function)

[`clip_to_image_size` function](https://keras.io/api/utils/bounding_boxes/#cliptoimagesize-function)

[`compute_ciou` function](https://keras.io/api/utils/bounding_boxes/#computeciou-function)

[`compute_iou` function](https://keras.io/api/utils/bounding_boxes/#computeiou-function)

[`convert_format` function](https://keras.io/api/utils/bounding_boxes/#convertformat-function)

[`crop` function](https://keras.io/api/utils/bounding_boxes/#crop-function)