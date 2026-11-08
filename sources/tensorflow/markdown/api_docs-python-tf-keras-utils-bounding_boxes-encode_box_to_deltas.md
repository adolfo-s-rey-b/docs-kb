[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/encode_box_to_deltas#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/encode_box_to_deltas)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/encode_box_to_deltas?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/encode_box_to_deltas#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/encode_box_to_deltas#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/encode_box_to_deltas#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.utils.bounding\_boxes.encode\_box\_to\_deltas Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/encode_box_to_deltas#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/encode_box_to_deltas#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/encode_box_to_deltas#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/bounding_boxes/converters.py#L255-L344)

Encodes bounding boxes relative to anchors as deltas.

tf.keras.utils.bounding_boxes.encode_box_to_deltas(
        anchors,
        boxes,
        anchor_format,
        box_format,
        encoding_format='center_yxhw',
        variance=None,
        image_shape=None
    )

This function calculates the deltas that represent the difference between bounding boxes and provided anchors. Deltas encode the offsets and scaling factors to apply to anchors to obtain the target boxes.

Boxes and anchors are first converted to the specified `encoding_format` (defaulting to `center_yxhw`) for consistent delta representation.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `anchors` | `Tensors`. Anchor boxes with shape of `(N, 4)` where N is the number of anchors. |
| `boxes` | `Tensors` Bounding boxes to encode. Boxes can be of shape `(B, N, 4)` or `(N, 4)`. |
| `anchor_format` | str. The format of the input `anchors` (e.g., "xyxy", "xywh", etc.). |
| `box_format` | str. The format of the input `boxes` (e.g., "xyxy", "xywh", etc.). |
| `encoding_format` | str. The intermediate format to which boxes and anchors are converted before delta calculation. Defaults to "center\_yxhw". |
| `variance` | `List[float]`. A 4-element array/tensor representing variance factors to scale the box deltas. If provided, the calculated deltas are divided by the variance. Defaults to None. |
| `image_shape` | `Tuple[int]`. The shape of the image (height, width, 3). When using relative bounding box format for `box_format` the `image_shape` is used for normalization. |

|     |
| --- |
| Returns<br>------- |     |
| Encoded box deltas. The return type matches the `encode_format`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `variance` is not None and its length is not 4. |
| `ValueError` | If `encoding_format` is not `"center_xywh"` or `"center_yxhw"`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.