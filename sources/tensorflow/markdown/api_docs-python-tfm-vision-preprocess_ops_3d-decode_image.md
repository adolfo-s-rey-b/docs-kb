[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d/decode_image#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d/decode_image)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d/decode_image?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d/decode_image#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d/decode_image#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.preprocess\_ops\_3d.decode\_image Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d/decode_image#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d/decode_image#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/preprocess_ops_3d.py#L201-L220)

Decodes PNG or JPEG raw bytes string into a RGB uint8 Tensor.

tfm.vision.preprocess_ops_3d.decode_image(
        image_string: tf.Tensor, channels: int = 0
    ) -> tf.Tensor

|     |     |
| --- | --- |
| Args<br>---- |     |
| `image_string` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of type strings with the raw PNG or JPEG bytes where the first dimension is timesteps. |
| `channels` | Number of channels of the PNG image. Allowed values are 0, 1 and<br><br>1.  If 0, the number of channels will be calculated at runtime and no static shape is set. |

|     |
| --- |
| Returns<br>------- |     |
| A Tensor of shape \[T, H, W, C\] of type uint8 with the decoded images. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.