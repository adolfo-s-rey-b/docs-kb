[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/cutout_video#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/cutout_video)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/cutout_video?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/cutout_video#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/cutout_video#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.augment.cutout\_video Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/cutout_video#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/cutout_video#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L698-L801)

Apply cutout ([https://arxiv.org/abs/1708.04552](https://arxiv.org/abs/1708.04552)
) to a video.

tfm.vision.augment.cutout_video(
        video: tf.Tensor, mask_shape: Optional[tf.Tensor] = None, replace: int = 0
    ) -> tf.Tensor

This operation applies a random size 3D mask of zeros to a random location within `video`. The mask is padded The pixel values filled in will be of the value `replace`. The location where the mask will be applied is randomly chosen uniformly over the whole video. If the size of the mask is not set, then, it is randomly sampled uniformly from \[0.25_height, 0.5_height\], \[0.25_width, 0.5_width\], and \[1, 0.25\*depth\], which represent the height, width, and number of frames of the input video tensor respectively.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `video` | A video Tensor of shape \[T, H, W, C\]. |
| `mask_shape` | An optional integer tensor that specifies the depth, height and width of the mask to cut. If it is not set, the shape is randomly sampled as described above. The shape dimensions should be divisible by 2 otherwise they will rounded down. |
| `replace` | What pixel value to fill in the image in the area that has the cutout mask applied to it. |

|     |
| --- |
| Returns<br>------- |     |
| A video Tensor with cutout applied. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.