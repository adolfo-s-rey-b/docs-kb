[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/mask_ops/paste_instance_masks_v2#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/mask_ops/paste_instance_masks_v2)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/mask_ops/paste_instance_masks_v2?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/mask_ops/paste_instance_masks_v2#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/mask_ops/paste_instance_masks_v2#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.mask\_ops.paste\_instance\_masks\_v2 Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/mask_ops/paste_instance_masks_v2#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/mask_ops/paste_instance_masks_v2#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/mask_ops.py#L108-L188)

Paste instance masks to generate the image segmentation (v2).

tfm.vision.mask_ops.paste_instance_masks_v2(
        masks: np.ndarray,
        detected_boxes: np.ndarray,
        image_height: int,
        image_width: int
    ) -> np.ndarray

|     |     |
| --- | --- |
| Args<br>---- |     |
| `masks` | a numpy array of shape \[N, mask\_height, mask\_width\] representing the instance masks w.r.t. the `detected_boxes`. |
| `detected_boxes` | a numpy array of shape \[N, 4\] representing the reference bounding boxes. |
| `image_height` | an integer representing the height of the image. |
| `image_width` | an integer representing the width of the image. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `segms` | a numpy array of shape \[N, image\_height, image\_width\] representing the instance masks _pasted_ on the image canvas. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.