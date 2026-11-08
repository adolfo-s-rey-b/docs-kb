[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/clip_to_image_size#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/clip_to_image_size)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/clip_to_image_size?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Futils%2Fbounding_boxes%2Fclip_to_image_size&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/clip_to_image_size#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/clip_to_image_size#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.utils.bounding\_boxes.clip\_to\_image\_size Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/clip_to_image_size#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/clip_to_image_size#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/bounding_boxes/converters.py#L73-L113)

Clips bounding boxes to be within the image dimensions.

tf.keras.utils.bounding_boxes.clip_to_image_size(
        bounding_boxes,
        height=None,
        width=None,
        bounding_box_format='xyxy'
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `bounding_boxes` | A dictionary with 'boxes' shape `(N, 4)` or `(batch, N, 4)` and 'labels' shape `(N,)` or `(batch, N,)`. |
| `height` | Image height. |
| `width` | Image width. |
| `bounding_box_format` | The format of the input bounding boxes. Defaults to `"xyxy"`. |

|     |
| --- |
| Returns<br>------- |     |
| Clipped bounding boxes. |     |

#### Example:

boxes = {"boxes": np.array([[-10, -20, 150, 160], [50, 40, 70, 80]]),
             "labels": np.array([0, 1])}
    clipped_boxes = keras.utils.bounding_boxes.clip_to_image_size(
        boxes, height=100, width=120,
    )
    # Output will have boxes clipped to the image boundaries, and labels
    # potentially adjusted if the clipped area becomes zero

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.