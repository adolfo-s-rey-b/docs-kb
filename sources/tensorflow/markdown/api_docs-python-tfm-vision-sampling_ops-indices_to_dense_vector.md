[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops/indices_to_dense_vector#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops/indices_to_dense_vector)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops/indices_to_dense_vector?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops/indices_to_dense_vector#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops/indices_to_dense_vector#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.sampling\_ops.indices\_to\_dense\_vector Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops/indices_to_dense_vector#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops/indices_to_dense_vector#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/sampling_ops.py#L60-L89)

Creates dense vector with indices set to specific value and rest to zeros.

tfm.vision.sampling_ops.indices_to_dense_vector(
        indices, size, indices_value=1.0, default_value=0, dtype=tf.float32
    )

This function exists because it is unclear if it is safe to use tf.sparse\_to\_dense(indices, \[size\], 1, validate\_indices=False) with indices which are not ordered. This function accepts a dynamic size (e.g. tf.shape(tensor)\[0\])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `indices` | 1d Tensor with integer indices which are to be set to indices\_values. |
| `size` | scalar with size (integer) of output Tensor. |
| `indices_value` | values of elements specified by indices in the output vector |
| `default_value` | values of other elements in the output vector. |
| `dtype` | data type. |

|     |
| --- |
| Returns<br>------- |     |
| dense 1D Tensor of shape \[size\] with indices set to indices\_values and the rest set to default\_value. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.