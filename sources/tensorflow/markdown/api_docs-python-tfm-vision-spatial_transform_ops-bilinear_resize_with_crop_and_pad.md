[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops/bilinear_resize_with_crop_and_pad#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops/bilinear_resize_with_crop_and_pad)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops/bilinear_resize_with_crop_and_pad?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops/bilinear_resize_with_crop_and_pad#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops/bilinear_resize_with_crop_and_pad#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.spatial\_transform\_ops.bilinear\_resize\_with\_crop\_and\_pad Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops/bilinear_resize_with_crop_and_pad#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops/bilinear_resize_with_crop_and_pad#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/spatial_transform_ops.py#L807-L864)

Bilinear resizes the images, then crops and finally pads to output size.

tfm.vision.spatial_transform_ops.bilinear_resize_with_crop_and_pad(
        images: tf.Tensor,
        rescale_size: tf.Tensor,
        crop_offset: tf.Tensor,
        crop_size: tf.Tensor,
        output_size: tf.Tensor
    ) -> tf.Tensor

|     |     |
| --- | --- |
| Args<br>---- |     |
| `images` | A tensor in shape (batch\_size, input\_h, input\_w, ...) with arbitrary numbers of channel dimensions. |
| `rescale_size` | An int tensor in shape (batch\_size, 2), representing the sizes of the rescaled images. |
| `crop_offset` | An int tensor in shape (batch\_size, 2), representing the left-top offset of the crop box. Applying negative offsets means adding extra margins at the left-top. |
| `crop_size` | An int tensor in shape (batch\_size, 2), representing the sizes of the cropped images. |
| `output_size` | The size of the output image in (output\_h, output\_w). |

|     |
| --- |
| Returns<br>------- |     |
| A tensor in shape (batch\_size, output\_h, output\_w, ...). The result has the same dtype as the input if it's float32, float16, bfloat16, otherwise the result is float32. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.