[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/decode_deltas_to_boxes#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/decode_deltas_to_boxes)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/decode_deltas_to_boxes?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/decode_deltas_to_boxes#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/decode_deltas_to_boxes#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/decode_deltas_to_boxes#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.utils.bounding\_boxes.decode\_deltas\_to\_boxes Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/decode_deltas_to_boxes#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/decode_deltas_to_boxes#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/decode_deltas_to_boxes#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/bounding_boxes/converters.py#L347-L448)

Converts bounding boxes from delta format to the specified `box_format`.

tf.keras.utils.bounding_boxes.decode_deltas_to_boxes(
        anchors,
        boxes_delta,
        anchor_format,
        box_format,
        encoded_format='center_yxhw',
        variance=None,
        image_shape=None
    )

This function decodes bounding box deltas relative to anchors to obtain the final bounding box coordinates. The boxes are encoded in a specific `encoded_format` (center\_yxhw by default) during the decoding process. This allows flexibility in how the deltas are applied to the anchors.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `anchors` | Can be `Tensors` or `Dict[Tensors]` where keys are level indices and values are corresponding anchor boxes. The shape of the array/tensor should be `(N, 4)` where N is the number of anchors. boxes\_delta Can be `Tensors` or `Dict[Tensors]` Bounding box deltas must have the same type and structure as `anchors`. The shape of the array/tensor can be `(N, 4)` or `(B, N, 4)` where N is the number of boxes. |
| `anchor_format` | str. The format of the input `anchors`. (e.g., `"xyxy"`, `"xywh"`, etc.) |
| `box_format` | str. The desired format for the output boxes. (e.g., `"xyxy"`, `"xywh"`, etc.) |
| `encoded_format` | str. Raw output format from regression head. Defaults to `"center_yxhw"`. |
| `variance` | `List[floats]`. A 4-element array/tensor representing variance factors to scale the box deltas. If provided, the deltas are multiplied by the variance before being applied to the anchors. Defaults to None. |
| `image_shape` | `Tuple[int]`. The shape of the image (height, width, 3). When using relative bounding box format for `box_format` the `image_shape` is used for normalization. |

|     |
| --- |
| Returns<br>------- |     |
| Decoded box coordinates. The return type matches the `box_format`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `variance` is not None and its length is not 4. |
| `ValueError` | If `encoded_format` is not `"center_xywh"` or `"center_yxhw"`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.