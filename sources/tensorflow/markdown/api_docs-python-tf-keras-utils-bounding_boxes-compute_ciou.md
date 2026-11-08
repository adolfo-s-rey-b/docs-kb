[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/compute_ciou#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/compute_ciou)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/compute_ciou?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/compute_ciou#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/compute_ciou#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.utils.bounding\_boxes.compute\_ciou Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/compute_ciou#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/compute_ciou#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/bounding_boxes/iou.py#L176-L281)

Computes the Complete IoU (CIoU) between two bounding boxes or between two batches of bounding boxes.

tf.keras.utils.bounding_boxes.compute_ciou(
        boxes1, boxes2, bounding_box_format, image_shape=None
    )

CIoU loss is an extension of GIoU loss, which further improves the IoU optimization for object detection. CIoU loss not only penalizes the bounding box coordinates but also considers the aspect ratio and center distance of the boxes. The length of the last dimension should be 4 to represent the bounding boxes.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `box1` | `tensor`<br><br>tensor representing the first bounding box with shape (..., 4). |
| `box2` | `tensor`<br><br>tensor representing the second bounding box with shape (..., 4). |
| `bounding_box_format` | a case-insensitive string (for example, "xyxy"). Each bounding box is defined by these 4 values. For detailed information on the supported formats, see the [KerasCV bounding box documentation](https://keras.io/api/keras_cv/bounding_box/formats/)<br>. |
| `image_shape` | `Tuple[int]`. The shape of the image (height, width, 3). When using relative bounding box format for `box_format` the `image_shape` is used for normalization. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `tensor` | The CIoU distance between the two bounding boxes. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.