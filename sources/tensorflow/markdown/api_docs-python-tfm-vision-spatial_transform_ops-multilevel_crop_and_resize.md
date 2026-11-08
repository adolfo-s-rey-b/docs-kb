[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops/multilevel_crop_and_resize#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops/multilevel_crop_and_resize)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops/multilevel_crop_and_resize?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fvision%2Fspatial_transform_ops%2Fmultilevel_crop_and_resize&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops/multilevel_crop_and_resize#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops/multilevel_crop_and_resize#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.spatial\_transform\_ops.multilevel\_crop\_and\_resize Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops/multilevel_crop_and_resize#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops/multilevel_crop_and_resize#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/spatial_transform_ops.py#L148-L292)

Crop and resize on multilevel feature pyramid.

tfm.vision.spatial_transform_ops.multilevel_crop_and_resize(
        features: Dict[str, tf.Tensor],
        boxes: tf.Tensor,
        output_size: int = 7,
        sample_offset: float = 0.5
    ) -> tf.Tensor

Generate the (output\_size, output\_size) set of pixels for each input box by first locating the box into the correct feature level, and then cropping and resizing it using the correspoding feature map of that level.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `features` | A dictionary with key as pyramid level and value as features. The features are in shape of \[batch\_size, height\_l, width\_l, num\_filters\]. |
| `boxes` | A 3-D Tensor of shape \[batch\_size, num\_boxes, 4\]. Each row represents a box with \[y1, x1, y2, x2\] in un-normalized coordinates. |
| `output_size` | A scalar to indicate the output crop size. |
| `sample_offset` | a float number in \[0, 1\] indicates the subpixel sample offset from grid point. |

|     |
| --- |
| Returns<br>------- |     |
| A 5-D tensor representing feature crop of shape \[batch\_size, num\_boxes, output\_size, output\_size, num\_filters\]. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.