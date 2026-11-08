[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor/Anchor#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor/Anchor)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor/Anchor?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fvision%2Fanchor%2FAnchor&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor/Anchor#attributes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.anchor.Anchor Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor/Anchor#attributes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/anchor.py#L31-L126)

Anchor class for anchor-based object detectors.

tfm.vision.anchor.Anchor(
        min_level, max_level, num_scales, aspect_ratios, anchor_size, image_size
    )

#### Example:

anchor_boxes = Anchor(
        min_level=3,
        max_level=4,
        num_scales=2,
        aspect_ratios=[0.5, 1., 2.],
        anchor_size=4.,
        image_size=[256, 256],
    ).multilevel_boxes

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `min_level` | integer number of minimum level of the output feature pyramid. |
| `max_level` | integer number of maximum level of the output feature pyramid. |
| `num_scales` | integer number representing intermediate scales added on each level. For instances, num\_scales=2 adds one additional intermediate anchor scales \[2^0, 2^0.5\] on each level. |
| `aspect_ratios` | list of float numbers representing the aspect ratio anchors added on each level. The number indicates the ratio of width to height. For instances, aspect\_ratios=\[1.0, 2.0, 0.5\] adds three anchors on each scale level. |
| `anchor_size` | float number representing the scale of size of the base anchor to the feature stride 2^level. |
| `image_size` | a list of integer numbers or Tensors representing \[height, width\] of the input image size. |
| `multilevel_boxes` | an OrderedDict from level to the generated anchor boxes of shape \[height\_l, width\_l, num\_anchors\_per\_location \* 4\]. |
| `anchors_per_location` | number of anchors per pixel location. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.