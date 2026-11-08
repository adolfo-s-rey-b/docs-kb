[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/gather_instances#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/gather_instances)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/gather_instances?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/gather_instances#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/gather_instances#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.box\_ops.gather\_instances Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/gather_instances#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops/gather_instances#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/box_ops.py#L537-L582)

Gathers instances by indices.

tfm.vision.box_ops.gather_instances(
        selected_indices, instances, *aux_instances
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `selected_indices` | a Tensor of shape \[batch, K\] which indicates the selected indices in instance dimension (2nd dimension). |
| `instances` | a Tensor of shape \[batch, N, ...\] where the 2nd dimension is the instance dimension to be selected from. |
| `*aux_instances` | the additional Tensors whose shapes are in \[batch, N, ...\] which are the tensors to be selected from using the `selected_indices`. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `selected_instances` | the tensor of shape \[batch, K, ...\] which corresponds to the selected instances of the `instances` tensor. |
| `selected_aux_instances` | the additional tensors of shape \[batch, K, ...\] which corresponds to the selected instances of the `aus_instances` tensors. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.