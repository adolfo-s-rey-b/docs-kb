[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/utils/get_shape_list#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/utils/get_shape_list)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/utils/get_shape_list?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/utils/get_shape_list#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/utils/get_shape_list#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.utils.get\_shape\_list Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/utils/get_shape_list#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/utils/get_shape_list#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/tf_utils.py#L140-L171)

Returns a list of the shape of tensor, preferring static dimensions.

tfm.utils.get_shape_list(
        tensor, expected_rank=None, name=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `tensor` | A tf.Tensor object to find the shape of. |
| `expected_rank` | (optional) int. The expected rank of `tensor`. If this is specified and the `tensor` has a different rank, and exception will be thrown. |
| `name` | Optional name of the tensor for the error message. |

|     |
| --- |
| Returns<br>------- |     |
| A list of dimensions of the shape of tensor. All static dimensions will be returned as python integers, and dynamic dimensions will be returned as tf.Tensor scalars. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.