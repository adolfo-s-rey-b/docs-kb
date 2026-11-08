[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops/crop_mask_in_target_box#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops/crop_mask_in_target_box)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops/crop_mask_in_target_box?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fvision%2Fspatial_transform_ops%2Fcrop_mask_in_target_box&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops/crop_mask_in_target_box#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops/crop_mask_in_target_box#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.spatial\_transform\_ops.crop\_mask\_in\_target\_box Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops/crop_mask_in_target_box#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops/crop_mask_in_target_box#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/spatial_transform_ops.py#L447-L525)

Crop masks in target boxes.

tfm.vision.spatial_transform_ops.crop_mask_in_target_box(
        masks: tf.Tensor,
        boxes: tf.Tensor,
        target_boxes: tf.Tensor,
        output_size: int,
        sample_offset: float = 0.0,
        use_einsum: bool = True
    ) -> tf.Tensor

|     |     |
| --- | --- |
| Args<br>---- |     |
| `masks` | A tensor with a shape of \[batch\_size, num\_masks, height, width\]. |
| `boxes` | a float tensor representing box cooridnates that tightly enclose masks with a shape of \[batch\_size, num\_masks, 4\] in un-normalized coordinates. A box is represented by \[ymin, xmin, ymax, xmax\]. |
| `target_boxes` | a float tensor representing target box cooridnates for masks with a shape of \[batch\_size, num\_masks, 4\] in un-normalized coordinates. A box is represented by \[ymin, xmin, ymax, xmax\]. |
| `output_size` | A scalar to indicate the output crop size. It currently only supports to output a square shape outputs. |
| `sample_offset` | a float number in \[0, 1\] indicates the subpixel sample offset from grid point. |
| `use_einsum` | Use einsum to replace gather in selective\_crop\_and\_resize. |

|     |
| --- |
| Returns<br>------- |     |
| A 4-D tensor representing feature crop of shape \[batch\_size, num\_boxes, output\_size, output\_size\]. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.