[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/compute_padded_size#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/compute_padded_size)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/compute_padded_size?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/compute_padded_size#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/compute_padded_size#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.preprocess\_ops.compute\_padded\_size Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/compute_padded_size#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/compute_padded_size#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/preprocess_ops.py#L148-L174)

Compute the padded size given the desired size and the stride.

tfm.vision.preprocess_ops.compute_padded_size(
        desired_size, stride
    )

The padded size will be the smallest rectangle, such that each dimension is the smallest multiple of the stride which is larger than the desired dimension. For example, if desired\_size = (100, 200) and stride = 32, the output padded\_size = (128, 224).

|     |     |
| --- | --- |
| Args<br>---- |     |
| `desired_size` | a `Tensor` or `int` list/tuple of two elements representing \[height, width\] of the target output image size. |
| `stride` | an integer, the stride of the backbone network. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `padded_size` | a `Tensor` or `int` list/tuple of two elements representing \[height, width\] of the padded output image size. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.