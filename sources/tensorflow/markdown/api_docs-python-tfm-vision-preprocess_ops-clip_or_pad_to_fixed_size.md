[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/clip_or_pad_to_fixed_size#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/clip_or_pad_to_fixed_size)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/clip_or_pad_to_fixed_size?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/clip_or_pad_to_fixed_size#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/clip_or_pad_to_fixed_size#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.preprocess\_ops.clip\_or\_pad\_to\_fixed\_size Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/clip_or_pad_to_fixed_size#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/clip_or_pad_to_fixed_size#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/preprocess_ops.py#L40-L75)

Pads data to a fixed length at the first dimension.

tfm.vision.preprocess_ops.clip_or_pad_to_fixed_size(
        input_tensor, size, constant_values=0
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input_tensor` | `Tensor` with any dimension. |
| `size` | `int` number for the first dimension of output Tensor. |
| `constant_values` | `int` or `str` value assigned to the paddings. |

|     |
| --- |
| Returns<br>------- |     |
| `Tensor` with the first dimension padded to `size`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.